from default import client

def get_balance():
  res = client.account.balance()
  print(res)

def get_token():
  res = client.account.token(expire=100)
  print(res)

if __name__ == '__main__':
  get_balance()

  get_token()