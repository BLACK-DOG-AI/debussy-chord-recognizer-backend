import unittest
from src.main import app
from faker import Faker
from unittest.mock import patch, MagicMock
from src.models.model import Offer, db
import json
import random

class TestOffer(unittest.TestCase):
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

    with app.test_client() as test_client:
      response = test_client.post('/offers', 
        headers={'Authorization': self.data_factory.uuid4()},
        json={
          "postId": self.data_factory.uuid4(),
          "description": self.data_factory.paragraph(nb_sentences=1),
          "size": "MEDIUM",
          "fragile": random.choice([True, False]),
          "offer": self.data_factory.random_int(min=0, max=10000)
        }
      )
      response_json = json.loads(response.data)

      assert response.status_code == 201
      assert 'id' in response_json
      assert 'userId' in response_json
      assert 'createdAt' in response_json

  @patch('src.clients.user_client.requests.get')
  def test_get_offer_not_found(self, mock_get_user):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': self.data_factory.uuid4()}
    mock_get_user.return_value = mock_response

    with app.test_client() as test_client:
      response = test_client.get('/offers/' + self.data_factory.uuid4(), 
        headers={'Authorization': self.data_factory.uuid4()}
      )

    assert response.status_code == 404

  @patch('src.clients.user_client.requests.get')
  def test_get_offer_list(self, mock_get_user):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': self.data_factory.uuid4()}
    mock_get_user.return_value = mock_response

    with app.test_client() as test_client:
      response = test_client.get('/offers', 
        headers={'Authorization': self.data_factory.uuid4()}
      )

      assert response.status_code == 200

  @patch('src.clients.user_client.requests.get')
  def test_get_offer_list_filter(self, mock_get_user):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': self.data_factory.uuid4()}
    mock_get_user.return_value = mock_response

    with app.test_client() as test_client:
      response = test_client.get('/offers?owner=me', 
        headers={'Authorization': self.data_factory.uuid4()}
      )

      assert response.status_code == 200

  @patch('src.clients.user_client.requests.get')
  def test_delete_offer_not_found(self, mock_get_user):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': self.data_factory.uuid4()}
    mock_get_user.return_value = mock_response

    with app.test_client() as test_client:
      response = test_client.delete('/offers/' + self.data_factory.uuid4(), 
        headers={'Authorization': self.data_factory.uuid4()}
      )

      assert response.status_code == 404


if __name__ == '__main__':
    unittest.main()