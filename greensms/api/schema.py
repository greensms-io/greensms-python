from greensms.utils.dict import deep_merge

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

common_schema = {
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
  'call': common_schema ,
  'hlr': common_schema,
  'whois': {
    'v1': {
      'lookup': {
        'to': to_schema
      }
    },
  },
  'general': {},
  'voice': deep_merge(common_schema,
    {
      'v1': {
        'send': {
          'txt': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 5,
            'regex': '^\d+',
            'required': True
          },
          'lang': {
            'type': 'string',
            'allowed': ['ru', 'en']
          }
        }
      }
    })

}