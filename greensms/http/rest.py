import requests
from error import RestError

class HttpClient:
  def __init__(self, opts):
    print('Hello World')

    if 1 != 2:
      raise RestError({ 'error': 'Hello Error'})


  def request(self, **kwargs):
    print('Request')
