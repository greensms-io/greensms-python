from greensms.http.error import RestError
from cerberus import Validator


def validate(schema, data):
    error_result = None
    validator = Validator(schema, allow_unknown=True)

    if validator.validate(data):
        return error_result
    else:
        error_result = RestError({
            'code': 1,
            'error': 'Validation Error',
            'params': validator.errors
        })

    return error_result
