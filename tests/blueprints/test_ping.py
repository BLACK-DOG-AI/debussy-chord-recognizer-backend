from src.main import app

class TestPing():
  def test_health_check_service(self):
    with app.test_client() as test_client:
      response = test_client.get('/offers/ping')
      assert response.status_code == 200
