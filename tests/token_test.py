import unittest
import time
from tests.default import client
from greensms.client import GreenSMS


class TestTokenMethods(unittest.TestCase):

    def test_balance(self):
        token_response = client.account.token(expire=5)
        token_client = GreenSMS(token=token_response.access_token)
        response = token_client.account.balance()
        self.assertIn('balance', response)

    def test_without_token(self):
        self.assertRaises(Exception, GreenSMS())

    def test_token_expiry(self):
        token_response = client.account.token(expire=5)
        invalid_token_client = GreenSMS(token=token_response['access_token'])
        time.sleep(5)
        try:
            invalid_token_client.account.balance()
        except Exception as e:
            self.assertEqual(e.error, 'Authorization declined')


if __name__ == '__main__':
    unittest.main()
