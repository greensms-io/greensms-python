from default import client


def call_send():
    res = client.call.send(to='919987409698')
    print(res)

def call_receive():
    res = client.call.receive(to='919987409698')
    print(res)


def call_status():
    res = client.call.status(id='1fd4ac4d-6e4f-4e32-b6e4-8087d3466f55')
    print(res)


if __name__ == '__main__':
    call_send()

    call_receive
    
    call_status()
