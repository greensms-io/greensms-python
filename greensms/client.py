import os
from greensms.utils.version import get_version
from greensms.utils.url import base_url, build_url
from greensms.http.rest import HttpClient

class GreenSMS(object):
  """ Client for accessing the GreenSMS API"""

  def __init__(self, user=None, password=None, token=None, version=None, camel_case_response=False, use_token_for_requests=False):
    """ Initialize the client

    :param str user: Username. Required when AuthToken is not passed
    :param str password: Password. Request when AuthToken is not passed
    :param str token: AuthToken. Required when Username/Password not passed
    :param str version: API version to be used
    :param bool use_token_for_requests: Create Auth Token after login and use for subsequent requests
    :param bool camel_case_response: Convert all response keys to camelCase

    :returns: Twilio Client
    :rtype: greensms.GreenSMS

    """

    environment = os.environ

    self.token = token or environment.get('GREENSMS_TOKEN')
    self.user = user or environment.get('GREENSMS_USER')
    self.password = password or environment.get('GREENSMS_PASS')
    self.version = version
    self.use_camel_case = camel_case_response if type(camel_case_response) == type(True) else False
    self.use_token_for_requests = use_token_for_requests if type(use_token_for_requests) == type(True) else False

    if self.token is not None:
      self.user = None
      self.password = None

    if self.token is not None and (self.user is None or self.password is None):
      raise Exception('Either User/Pass or Auth Token is required!')

    shared_options = {
      'use_token_for_requests': self.use_token_for_requests,
      'version': get_version(version),
      'rest_client': self._http_client(use_camel_case=camel_case_response),
      'base_url': base_url()
    }

    bal_url = build_url(base_url(), 'account', 'balance')

    print(shared_options)

    shared_options['rest_client'].request(method='GET', url=bal_url)

  def test(self, str):
    pass

  def _http_client(self, **kwargs):

    default_params = {}

    if not self.token and self.user:
      default_params['user'] = self.user
      default_params['pass'] = self.password

    http_args = {
      'default_params': default_params,
      'default_data': {},
      'token': self.token
    }

    for key, value in kwargs.items():
      http_args[key] = value

    rest_client = HttpClient(http_args)
    return rest_client