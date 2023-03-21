import requests
import humps
from greensms.http.error import RestError
from greensms.utils.attr_dict import AttrDict
from greensms.constants import SDK_VERSION, SDK_NAME

HEADER_USER_AGENT = 'User-Agent'

class HttpClient:

    def __init__(self, opts):

        self.token = None
        self.default_data = {}
        self.default_params = {}
        self.use_camel_case = False
        self.sdk_version_header = SDK_NAME + " " + SDK_VERSION

        attributes = ['token', 'default_data',
                      'default_params', 'use_camel_case']
        for attribute in attributes:
            if attribute in opts:
                self.__dict__[attribute] = opts[attribute]

    def request(self, **kwargs):  # noqa: C901

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
            for key, value in kwargs['params'].items():
                params[key] = value

        data = {}
        if bool(self.default_data):
            for key, value in self.default_data.items():
                data[key] = value

        if 'data' in kwargs:
            for key, value in kwargs['data'].items():
                data[key] = value

        headers[HEADER_USER_AGENT] = self.sdk_version_header

        response = requests.request(
            method=method, url=url, headers=headers, params=params)

        response = response.json()

        if 'error' in response:
            raise RestError(response)
            # TODO: Decide to raise an Exception or respond with the error json
        else:
            response = AttrDict(response)

        if self.use_camel_case is True:
            response = humps.camelize(response)

        return response
