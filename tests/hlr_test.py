import unittest
from tests.default import client
from tests.utils import random_phone

class TestHlrMethods(unittest.TestCase):

  def test_send(self):
    response = client.hlr.send(to=random_phone(79260000111, 79260999999))
    self.assertIn('request_id', response)

  def test_mandatory_to(self):
    self.assertRaises(Exception, client.hlr.send())

  def test_status(self):
    response = client.hlr.status(id='70d296f5-ac52-403d-a27b-24829c2faebc', to=random_phone())
    self.assertIn('status', response)


if __name__ == '__main__':
  unittest.main()