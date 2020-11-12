import unittest
from tests.default import client
from tests.utils import random_phone


class TestSmsMethods(unittest.TestCase):

    def test_send(self):
        dict_params = {
            'to': random_phone(),
            'txt': 'Test Message Hampshire',
            'from': 'PyTest',
            'tag': 'PyTest',
            'hidden': 'Hampshire'
        }

        response = client.sms.send(**dict_params)
        self.assertIn('request_id', response)

    def test_mandatory_to(self):
        try:
            client.sms.send()
        except Exception as e:
            self.assertEqual(e.error, 'Validation Error')

    def test_status(self):
        response = client.sms.status(id='dc2bac6d-f375-4e19-9a02-ef0148991635')
        self.assertIn('status', response)


if __name__ == '__main__':
    unittest.main()
