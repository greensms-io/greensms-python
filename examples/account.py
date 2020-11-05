from default import client

def get_balance():
  res = client.account.balance()
  print(res)


if __name__ == '__main__':
  get_balance()


