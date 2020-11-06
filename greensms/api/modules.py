from greensms.api.schema import VALIDATION_SCHEMA

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
        'status': {
          'args': ['params'],
          'method': 'GET',
        },
      }
    }
  },
  'whois': {
    'schema': VALIDATION_SCHEMA['whois'],
    'versions': {
      'v1': {
        'lookup': {
          'args': ['params'],
          'method': 'GET'
        }
      }
    }
  },
  'general': {
    'schema': VALIDATION_SCHEMA['general'],
    'static': True,
    'versions': {
      'v1': {
        'status': {
          'args': None,
          'method': 'GET',
        },
      },
    },
  },
  'voice': {
    'schema': VALIDATION_SCHEMA['voice'],
    'versions': {
      'v1': {
        'send': {
          'args': ['params'],
          'method': 'POST',
        },
        'status': {
          'args': ['params'],
          'method': 'GET',
        },
      }
    }
  },
}