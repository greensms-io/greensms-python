from default import client


def status():
    res = client.status()
    print(res)


if __name__ == '__main__':
    status()
