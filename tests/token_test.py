import unittest
import time
from tests.default import client
from greensms.client import GreenSMS
from tests.utils import random_phone


token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibWFuYW4yNCIsImlhdCI6MTYwMzU2OTgzMCwiaXNzIjoiYXBpLmdyZWVuc21zLnJ1In0.OKiv5itdirS_PuPJj5kgGcR2_9DsC9ALW9c8FvvHSF4'

class TestTokenMethods(unittest.TestCase):

  def test_balance(self):
    token_client = GreenSMS(token=token)
    response = token_client.account.balance()
    self.assertIn('balance', response)


  def test_without_token(self):
    self.assertRaises(Exception, GreenSMS())

  def test_token_expiry(self):
    token_response = client.account.token(expire=5)
    invalid_token_client = GreenSMS(token=token_response['access_token'])
    time.sleep(5)
    response = invalid_token_client.account.balance()
    self.assertEqual(response.error, 'Authorization declined')


if __name__ == '__main__':
  unittest.main()