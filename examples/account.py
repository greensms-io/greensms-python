from greensms.client import GreenSMS

def get_balance():
  client = GreenSMS(user='test', password='test')

  client.test('E')

get_balance()