import requests
from error import RestError

class HttpClient:

  def __init__(self, opts):
    attributes = ['token', 'default_data', 'default_params', 'use_camel_case']
    for attribute in attributes:
      if attribute in opts:
        self.__dict__[attribute] = opts[attribute]

  def request(self, **kwargs):
    print('Request')

    if 'method' not in kwargs:
      raise Exception('Http Method is required')

    if 'uri' not in kwargs:
      raise Exception('URI is required')

    headers = kwargs['headers'] if 'headers' in kwargs else {}
