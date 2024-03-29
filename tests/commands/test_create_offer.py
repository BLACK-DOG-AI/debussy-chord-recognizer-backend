import unittest
from faker import Faker
from unittest.mock import patch, MagicMock
from src.commands.create_offer import CreateOffer
from src.models.model import Offer, db
from flask import jsonify
from src.errors.errors import BadRequest, PreconditionFailed
import json
import random

class TestCreateOffer(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.data_factory = Faker()
    Faker.seed(0)

  @classmethod
  def tearDownClass(self):
    db.session.query(Offer).delete()
    db.session.commit()


  @patch('src.clients.user_client.requests.get')
  def test_create_offer_success(self, mock_get_user):
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
    response = CreateOffer(json_body, token).execute()
    response = jsonify(response)
    response_json = json.loads(response.data)

    assert 'id' in response_json
    assert 'userId' in response_json
    assert 'createdAt' in response_json

  @patch('src.clients.user_client.requests.get')
  def test_create_offer_bad_request(self, mock_get_user):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': self.data_factory.uuid4()}
    mock_get_user.return_value = mock_response

    json_body={
        "postId": "",
        "description": "",
        "size": "",
        "fragile": "",
        "offer": ""
    }

    token = self.data_factory.uuid4()
    with self.assertRaises(BadRequest):
        CreateOffer(json_body, token).execute()

  @patch('src.clients.user_client.requests.get')
  def test_create_offer_size_unknown(self, mock_get_user):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': self.data_factory.uuid4()}
    mock_get_user.return_value = mock_response

    json_body={
        "postId": self.data_factory.uuid4(),
        "description": self.data_factory.paragraph(nb_sentences=1),
        "size": "any-size",
        "fragile": random.choice([True, False]),
        "offer": self.data_factory.random_int(min=0, max=10000)
    }

    token = self.data_factory.uuid4()
    with self.assertRaises(PreconditionFailed):
        CreateOffer(json_body, token).execute()

  @patch('src.clients.user_client.requests.get')
  def test_create_offer_price_error(self, mock_get_user):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': self.data_factory.uuid4()}
    mock_get_user.return_value = mock_response

    json_body={
        "postId": self.data_factory.uuid4(),
        "description": self.data_factory.paragraph(nb_sentences=1),
        "size": "SMALL",
        "fragile": random.choice([True, False]),
        "offer": self.data_factory.random_int(min=-10000, max=-1)
    }

    token = self.data_factory.uuid4()
    with self.assertRaises(PreconditionFailed):
        CreateOffer(json_body, token).execute()


if __name__ == '__main__':
    unittest.main()