import unittest
from faker import Faker
from src.errors.errors import BadRequest
from src.utils.uuid import UuidUtil

class TestUuid(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.data_factory = Faker()
    Faker.seed(0)

  def test_validate_uuid_success(self):
    id = self.data_factory.uuid4()
    response_uuid = UuidUtil(id).validate_uuid()
    self.assertTrue(response_uuid)

  def test_validate_uuid_error(self):
    id = self.data_factory.random_int(min=0, max=10000)
    with self.assertRaises(BadRequest):
      UuidUtil(id).validate_uuid()

if __name__ == '__main__':
    unittest.main()

