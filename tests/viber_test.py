import unittest
from tests.default import client
from tests.utils import random_phone


class TestViberMethods(unittest.TestCase):

    def test_send(self):
        dict_params = {
            'to': random_phone(),
            'txt': 'Test Message Hampshire',
            'from': 'PyTest',
            'cascade': 'sms'
        }
        response = client.viber.send(**dict_params)
        self.assertIn('request_id', response)
        self.__class__.request_id = response.request_id

    def test_mandatory_to(self):
        try:
            client.viber.send()
        except Exception as e:
            self.assertEqual(e.error, 'Validation Error')

    def test_status(self):
        request_id = self.__class__.request_id
        response = client.viber.status(
            id=request_id, extended=True)
        self.assertIn('status', response)


if __name__ == '__main__':
    unittest.main()
