from default import client


def sms_send():
    res = client.sms.send(
        to='919987409698', txt='Here is your message for delivery')
    print(res)


def sms_status():
    res = client.sms.status(id='dc2bac6d-f375-4e19-9a02-ef0148991635')
    print(res)


if __name__ == '__main__':
    sms_send()

    sms_status()
