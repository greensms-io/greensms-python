import unittest
from tests.default import client
from tests.utils import random_phone


class TestPayMethods(unittest.TestCase):

    def test_send(self):
        response = client.pay.send(to=random_phone(), amount=10, tag='PyTest')
        self.assertIn('request_id', response)

    def test_mandatory_to(self):
        self.assertRaises(Exception, client.pay.send())

    def test_status(self):
        response = client.pay.status(id='60f231d9-16ec-4313-842e-6e6853063482')
        self.assertIn('status', response)


if __name__ == '__main__':
    unittest.main()
