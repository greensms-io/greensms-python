import unittest
from tests.default import client
from tests.utils import random_phone


class TestVoiceMethods(unittest.TestCase):

    def test_send(self):
        response = client.voice.send(to=random_phone(), txt='1200', lang='en')
        self.assertIn('request_id', response)

    def test_mandatory_to(self):
        self.assertRaises(Exception, client.voice.send())

    def test_status(self):
        response = client.voice.status(
            id='41f23094-deda-4cab-ac9c-3ab4f2fee9e6', extended=True)
        self.assertIn('status', response)


if __name__ == '__main__':
    unittest.main()
