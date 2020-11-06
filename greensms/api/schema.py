to_schema = {
  'type': 'string',
  'minlength': 11,
  'maxlength': 14,
  'required': True,
  'regex': '^\d+'
}

id_schema = {
  'type': 'string',
  'minlength': 36,
  'maxlength': 36,
  'required': True
}

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
        'to': to_schema
      },
      'status': {
        'id': id_schema,
        'extended': {
          'type': 'boolean',
          'required': False
        }
      }
    }
  },
  'whois': {
    'v1': {
      'lookup': {
        'to': to_schema
      }
    },
  },
  'general': {}
}