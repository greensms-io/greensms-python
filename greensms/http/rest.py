import requests
from greensms.http.error import RestError

class HttpClient:

  def __init__(self, opts):
    attributes = ['token', 'default_data', 'default_params', 'use_camel_case']
    for attribute in attributes:
      if attribute in opts:
        self.__dict__[attribute] = opts[attribute]

  def request(self, **kwargs):

    if 'method' not in kwargs:
      raise Exception('Http Method is required')
    method = kwargs['method']

    if 'url' not in kwargs:
      raise Exception('URL is required')
    url = kwargs['url']

    headers = kwargs['headers'] if 'headers' in kwargs else {}

    if self.token:
      headers['Authorization'] = 'Bearer ' + self.token

    del kwargs['method']
    del kwargs['url']
    if 'headers' in kwargs:
      del kwargs['headers']

    params = {}
    if bool(self.default_params):
      for key, value in self.default_params.items():
        params[key] = value

    if 'params' in kwargs:
      for key, value in kwargs['params']:
        params[key] = value

    data = {}
    if bool(self.default_data):
      for key, value in self.default_data.items():
        data[key] = value

    if 'data' in kwargs:
      for key, value in kwargs['data']:
        data[key] = value

    response = requests.request(method=method, url=url, headers=headers, params=params)

    response = response.json()

    if 'error' in response:
      response = RestError(response)

    return response