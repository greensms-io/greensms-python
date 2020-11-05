from greensms.client import GreenSMS

def get_balance():
  client = GreenSMS(user='test', password='test')
  client.account.balance()


get_balance()
