from default import client

def account_balance():
  res = client.account.balance()
  print(res)

def account_token():
  res = client.account.token(expire=100)
  print(res)

def account_tariff():
  res = client.account.tariff()
  print(res)

if __name__ == '__main__':
  account_balance()

  account_token()

  account_tariff()