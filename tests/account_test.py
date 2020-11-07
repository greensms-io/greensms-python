import unittest
from tests.default import client
from greensms.client import GreenSMS
from tests.utils import random_phone

class TestAccountMethods(unittest.TestCase):

  def test_balance(self):
    response = client.account.balance()
    self.assertIn('balance', response)

  def test_token(self):
    response = client.account.token()
    self.assertIn('access_token', response)

  def test_tarrif(self):
    response = client.account.tariff()
    self.assertGreater(len(response), 0)

  def test_without_credentials(self):
    self.assertRaises(Exception, GreenSMS())

  def test_unauthorized_access(self):
    test_client = GreenSMS(user='username', password='password')
    response = test_client.account.balance()
    self.assertEqual(response.error, 'Authorization declined')

  def test_insufficient_funds(self):
    test_client = GreenSMS(user='test_block_user', password='183456')
    response = test_client.sms.send(to=random_phone(), txt='Test Message')
    self.assertEqual(response.error, 'Insufficient funds')


if __name__ == '__main__':
  unittest.main()