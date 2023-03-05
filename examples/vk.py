from default import client


def vk_send():
    res = client.viber.send(to='919987409698', txt='Vk Message')
    print(res)


def vk_status():
    res = client.viber.status(id='0b18fab4-0c5d-4a8b-8ee4-057a59596c72')
    print(res)


if __name__ == '__main__':
    vk_send()

    vk_status()
