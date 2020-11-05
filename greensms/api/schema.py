VALIDATION_SCHEMA = {
  'account': {
    'v1': {
      'token': {
        'expire': {
          'type': 'integer',
          'min': 0
        }
      }
    }
  },
  'call': {
    'v1': {
      'send': {
        'to': {
          'type': 'string',
          'minlength': 11,
          'maxlength': 14,
          'required': True
        }
      },
      'status': {
        'id': {
          'type': 'string',
          'length': 36,
          'required': True
        },
        'extended': {
          'type': 'bool'
        }
      }
    }
  }
}