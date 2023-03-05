import unittest
from tests.default import client
from tests.utils import random_phone
import time


class TestCallMethods(unittest.TestCase):

    def test_send(self):
        response = client.call.send(to=random_phone())
        keys_set = set(response.keys())
        self.assertTrue({'request_id', 'code'}.issubset(keys_set))
        self.__class__.request_id = response.request_id

    def test_receive(self):
        response = client.call.receive(to=random_phone(), tag="aaeb96d6-cb0e-46f2-8d09-2cd5c9ea421c")
        keys_set = set(response.keys())
        self.assertTrue({'request_id', 'number'}.issubset(keys_set))
        self.__class__.request_id = response.request_id

    def test_mandatory_to(self):
        try:
            client.call.send()
        except Exception as e:
            self.assertEqual(e.error, 'Validation Error')

    def test_status(self):
        time.sleep(2)
        request_id = self.__class__.request_id
        response = client.call.status(
            id=request_id, extended=True)
        self.assertIn('status', response)


if __name__ == '__main__':
    unittest.main()
