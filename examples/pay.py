from default import client


def pay_send():
    res = client.pay.send(to='919987409698', amount=10)
    print(res)


def pay_status():
    res = client.pay.status(id='60f231d9-16ec-4313-842e-6e6853063482')
    print(res)


if __name__ == '__main__':
    pay_send()

    pay_status()
