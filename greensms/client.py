import os
from greensms.utils.version import get_version

class GreenSMS(object):
  """ Client for accessing the GreenSMS API"""

  def __init__(self, user=None, password=None, token=None, version=None, camelCaseResponse=False, useTokenForRequests=False):
    """ Initialize the client

    :param str user: Username. Required when AuthToken is not passed
    :param str password: Password. Request when AuthToken is not passed
    :param str token: AuthToken. Required when Username/Password not passed
    :param str version: API version to be used
    :param bool useTokenForRequests: Create Auth Token after login and use for subsequent requests
    :param bool camelCaseResponse: Convert all response keys to camelCase

    :returns: Twilio Client
    :rtype: greensms.GreenSMS

    """

    environment = os.environ

    self.token = token or environment.get('GREENSMS_TOKEN')
    self.user = user or environment.get('GREENSMS_USER')
    self.password = password or environment.get('GREENSMS_PASS')
    self.version = version
    self.useCamelCase = camelCaseResponse if type(camelCaseResponse) == type(True) else False
    self.useTokenForRequests = useTokenForRequests if type(camelCaseResponse) == type(True) else False

    if self.token is not None:
      self.user = None
      self.password = None

    if self.token is not None and (self.user is None or self.password is None):
      raise Exception('Either User/Pass or Auth Token is required!')

    sharedOptions = {
      'useTokenForRequests': self.useTokenForRequests,
      'version': get_version(version)
    }

  def test(self, str):
    print(self.user, str)