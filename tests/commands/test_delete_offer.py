import unittest
from faker import Faker
from unittest.mock import patch, MagicMock
from src.commands.create_offer import CreateOffer
from src.commands.delete_offer import DeleteOffer
from src.models.model import Offer, db
from flask import jsonify
import json
import random

class TestDeleteOffer(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.data_factory = Faker()
    Faker.seed(0)

  @classmethod
  def tearDownClass(self):
    db.session.query(Offer).delete()
    db.session.commit()


  @patch('src.clients.user_client.requests.get')
  def test_delete_offer_success(self, mock_get_user):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': self.data_factory.uuid4()}
    mock_get_user.return_value = mock_response

    json_body={
        "postId": self.data_factory.uuid4(),
        "description": self.data_factory.paragraph(nb_sentences=1),
        "size": "MEDIUM",
        "fragile": random.choice([True, False]),
        "offer": self.data_factory.random_int(min=0, max=10000)
    }

    token = self.data_factory.uuid4()
    response_create = CreateOffer(json_body, token).execute()

    id = response_create["id"]

    response_delete = DeleteOffer(id, token).execute()
    response_delete = jsonify(response_delete)
    response_json_delete = json.loads(response_delete.data)

    assert 'msg' in response_json_delete    