from default import client

def viber_send():
  res = client.viber.send(to='919987409698',txt='Viber Message')
  print(res)

def viber_status():
  res = client.viber.status(id='0b18fab4-0c5d-4a8b-8ee4-057a59596c7d')
  print(res)

if __name__ == '__main__':
  viber_send()

  viber_status()