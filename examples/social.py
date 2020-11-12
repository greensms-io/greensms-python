from default import client


def social_send():
    dict_params = {
      'to': '71231234567',
      'txt': 'Test Message Hampshire',
      'from': 'PyTest',
      'tag': 'PyTest',
      'hidden': 'Hampshire'
    }

    res = client.social.send(**dict_params)
    print(res)


def social_status():
    res = client.social.status(id='caf3efb1-8aca-4387-9ed0-e667d315c5c9')
    print(res)


if __name__ == '__main__':
    social_send()

    social_status()
