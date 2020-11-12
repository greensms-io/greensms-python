import unittest
from tests.default import client
from tests.utils import random_phone


class TestCallMethods(unittest.TestCase):

    def test_send(self):
        response = client.call.send(to=random_phone())
        keys_set = set(response.keys())
        self.assertTrue({'request_id', 'code'}.issubset(keys_set))

    def test_mandatory_to(self):
        try:
            client.call.send()
        except Exception as e:
            self.assertEqual(e.error, 'Validation Error')

    def test_status(self):
        response = client.call.status(
            id='1fd4ac4d-6e4f-4e32-b6e4-8087d3466f55', extended=True)
        self.assertIn('status', response)


if __name__ == '__main__':
    unittest.main()
