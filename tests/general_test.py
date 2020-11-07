import unittest
from tests.default import client
from tests.utils import random_phone

class TestGeneralMethods(unittest.TestCase):

  def test_lookup(self):
    response = client.whois.lookup(to='79260000000')
    keys_set = set(response.keys())
    self.assertTrue({'def', 'region'}.issubset(keys_set))

  def test_status(self):
    response = client.status()
    self.assertIn('status', response)


if __name__ == '__main__':
  unittest.main()