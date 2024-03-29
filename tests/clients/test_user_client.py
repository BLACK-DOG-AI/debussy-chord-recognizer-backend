import unittest
from faker import Faker
from unittest.mock import patch, MagicMock
from src.clients.user_client import UserClient
from src.errors.errors import Unauthorized, Forbidden, BadRequest, PreconditionFailed

class TestUserClient(unittest.TestCase):
    def setUp(self):
        self.data_factory = Faker()
        Faker.seed(0)


    @patch('src.clients.user_client.requests.get')
    def test_validate_user_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'id': self.data_factory.uuid4()}
        mock_get.return_value = mock_response

        token = self.data_factory.uuid4()
        response = UserClient(token).validate_user()

        self.assertTrue(response)

    @patch('src.clients.user_client.requests.get')
    def test_validate_user_unauthorized(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response

        token = self.data_factory.uuid4()
        with self.assertRaises(Unauthorized):
           UserClient(token).validate_user()

    @patch('src.clients.user_client.requests.get')
    def test_validate_user_forbidden(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_get.return_value = mock_response

        token = self.data_factory.uuid4()
        with self.assertRaises(Forbidden):
           UserClient(token).validate_user()

    @patch('src.clients.user_client.requests.get')
    def test_validate_user_forbidden(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_get.return_value = mock_response

        token = self.data_factory.uuid4()
        with self.assertRaises(Forbidden):
           UserClient(token).validate_user()

    @patch('src.clients.user_client.requests.get')
    def test_validate_user_bad_request(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        token = self.data_factory.uuid4()
        with self.assertRaises(BadRequest):
           UserClient(token).validate_user()

    @patch('src.clients.user_client.requests.get')
    def test_validate_user_precondition_failed(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 412
        mock_get.return_value = mock_response

        token = self.data_factory.uuid4()
        with self.assertRaises(PreconditionFailed):
           UserClient(token).validate_user()

if __name__ == '__main__':
    unittest.main()