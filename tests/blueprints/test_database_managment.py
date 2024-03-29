from src.main import app
from faker import Faker

class TestDatabaseManagment():
  def setup_method(self):
    self.data_factory = Faker()
    Faker.seed(0)

  def test_reset_db(self):
    with app.test_client() as test_client:
      response = test_client.post('/offers/reset', 
        headers={'Authorization': self.data_factory.uuid4()}
      )
      assert response.status_code == 200