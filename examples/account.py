from greensms.client import GreenSMS

def get_balance():
  client = GreenSMS(user='test', password='test')
  res = client.account.balance()
  print(res)


get_balance()
