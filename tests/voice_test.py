import unittest
from tests.default import client
from tests.utils import random_phone
import time

class TestVoiceMethods(unittest.TestCase):

    def test_send(self):
        response = client.voice.send(to=random_phone(), txt='1200', lang='en')
        self.assertIn('request_id', response)
        self.__class__.request_id = response.request_id

    def test_mandatory_to(self):
        try:
            client.voice.send()
        except Exception as e:
            self.assertEqual(e.error, 'Validation Error')

    def test_status(self):
        time.sleep(2)
        request_id = self.__class__.request_id
        response = client.voice.status(
            id=request_id, extended=True)
        self.assertIn('status', response)


if __name__ == '__main__':
    unittest.main()
