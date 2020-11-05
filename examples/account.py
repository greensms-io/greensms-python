import settings
from greensms.client import GreenSMS

def get_balance():
  client = GreenSMS()
  res = client.account.balance()
  print(res)


if __name__ == '__main__':
  get_balance()


