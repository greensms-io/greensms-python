import unittest
from tests.default import client
from tests.utils import random_phone


class TestSocialMethods(unittest.TestCase):

    def test_send(self):
        dict_params = {
            'to': random_phone(),
            'txt': 'Test Message Hampshire',
            'from': 'PyTest',
            'tag': 'PyTest',
            'hidden': 'Hampshire'
        }

        response = client.social.send(**dict_params)
        self.assertIn('request_id', response)

    def test_mandatory_to(self):
        try:
            client.social.send()
        except Exception as e:
            self.assertEqual(e.error, 'Validation Error')

    def test_status(self):
        response = client.social.status(
            id='caf3efb1-8aca-4387-9ed0-e667d315c5c9')
        self.assertIn('status', response)


if __name__ == '__main__':
    unittest.main()
