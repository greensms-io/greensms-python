from greensms.schema import VALIDATION_SCHEMA

MODULES = {
  'account': {
    'schema': VALIDATION_SCHEMA['account'],
    'versions': {
      'v1': {
        'balance': {
          'args': None,
          'method': 'GET'
        },
        'token': {
          'args': ['params'],
          'method': 'POST'
        },
        'tariff': {
          'args': None,
          'method': 'GET'
        }
      }
    }
  },
  'call': {
    'schema': VALIDATION_SCHEMA['call'],
    'versions': {
      'v1': {
        'send': {
          'args': ['params'],
          'method': 'POST',
        },
        'status: {
          'args': ['params'],
          'method': 'GET',
        },
      }
    }
  }
}