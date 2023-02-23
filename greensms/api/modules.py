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
                'receive': {
                    'args': ['params'],
                    'method': 'POST',
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
    'pay': {
        'schema': VALIDATION_SCHEMA['pay'],
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
    'hlr': {
        'schema': VALIDATION_SCHEMA['hlr'],
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
    'sms': {
        'schema': VALIDATION_SCHEMA['sms'],
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
    'viber': {
        'schema': VALIDATION_SCHEMA['viber'],
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
    'social': {
        'schema': VALIDATION_SCHEMA['social'],
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
    'vk': {
        'schema': VALIDATION_SCHEMA['vk'],
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
    'whatsapp': {
        'schema': VALIDATION_SCHEMA['whatsapp'],
        'versions': {
            'v1': {
                'send': {
                    'args': ['params'],
                    'method': 'POST',
                },
                'webhook': {
                    'args': ['params'],
                    'method': 'GET',
                },
                'status': {
                    'args': ['params'],
                    'method': 'GET',
                },
            }
        }
    },
}
