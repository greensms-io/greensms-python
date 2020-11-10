# try:
#     from builtins import super
# except:
#     pass


class RestError(Exception):
    """ Custom Error Implementation

      Custom Error Class extending Exception with additional fields like error type
    """

    def __init__(self, error):

        error_message = ''
        if type(error) == Exception:
            error_message = error.message
        else:
            error_message = error['error']
            self.name = error['name'] if 'name' in error.keys(
            ) else 'RestError'
            self.code = error['code'] if 'code' in error.keys() else -1

        self.error = error_message
        self.message = error_message

        # super().__init__(self.message)

        error_type = self._get_error_type(self.code)
        self.error_type = error_type

        if 'params' in error.keys():
            self.params = error['params']

    def _get_error_type(self, code):
        if code == 0:
            return 'AUTH_DECLINED'
        elif code == 1:
            return 'MISSING_INPUT_PARAM'
        elif code == 2:
            return 'INVALID_INPUT_PARAM'
        elif code == 404:
            return 'NOT_FOUND'
        else:
            return 'INTERNAL_SERVER_ERROR'
