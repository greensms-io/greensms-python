import unittest
from tests.default import client
from tests.utils import random_phone


class TestPayMethods(unittest.TestCase):

    def test_send(self):
        response = client.pay.send(to=random_phone(), amount=10, tag='PyTest')
        self.assertIn('request_id', response)
        self.__class__.request_id = response.request_id

    def test_mandatory_to(self):
        try:
            client.pay.send()
        except Exception as e:
            self.assertEqual(e.error, 'Validation Error')

    def test_status(self):
        request_id = self.__class__.request_id
        response = client.pay.status(id=request_id, extended=True)
        self.assertIn('status', response)


if __name__ == '__main__':
    unittest.main()
