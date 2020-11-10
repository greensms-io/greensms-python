from default import client


def voice_send():
    res = client.voice.send(to='919987409698', txt='1234')
    print(res)


def voice_status():
    res = client.voice.status(id='41f23094-deda-4cab-ac9c-3ab4f2fee9e6')
    print(res)


if __name__ == '__main__':
    voice_send()

    voice_status()
