import unittest
import time
from tests.default import client
from greensms.client import GreenSMS

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdCIsImlhdCI6MTYwNTc5NjEwOCwiaXNzIjoiYXBpLmdyZWVuc21zLnJ1In0.St8-5fJqQnHx1MFybJ5o4D5VZ-RK3HxcL0DScJsOYec'  # noqa: E501


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
        try:
            invalid_token_client.account.balance()
        except Exception as e:
            self.assertEqual(e.error, 'Authorization declined')


if __name__ == '__main__':
    unittest.main()
