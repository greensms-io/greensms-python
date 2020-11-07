from default import client

def whois_lookup():
  res = client.whois.lookup(to='4477743336335')
  print(res)

if __name__ == '__main__':
  whois_lookup()