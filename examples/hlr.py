from default import client

def hlr_send():
  res = client.hlr.send(to='919987409698')
  print(res)

def hlr_status():
  res = client.hlr.status(id='70d296f5-ac52-403d-a27b-24829c2faebc')
  print(res)

if __name__ == '__main__':
  hlr_send()

  hlr_status()