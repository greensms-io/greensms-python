import unittest
from tests.default import client
from tests.utils import random_phone
import time


class TestHlrMethods(unittest.TestCase):

    def test_send(self):
        response = client.hlr.send(to=random_phone(79150000000, 79150999999))
        self.assertIn('request_id', response)
        self.__class__.request_id = response.request_id

    def test_mandatory_to(self):
        try:
            client.hlr.send()
        except Exception as e:
            self.assertEqual(e.error, 'Validation Error')

    def test_status(self):
        time.sleep(2)
        request_id = self.__class__.request_id
        response = client.hlr.status(
            id=request_id, to=random_phone())
        self.assertIn('status', response)


if __name__ == '__main__':
    unittest.main()
