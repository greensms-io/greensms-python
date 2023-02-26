from greensms.utils.dict import deep_merge
from greensms.utils.cascade_validator import cascade_validator

to_schema = {
    'type': 'string',
    'minlength': 11,
    'maxlength': 14,
    'required': True,
    'regex': "^[0-9]+"
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
    'call':  deep_merge(common_schema,
                        {
                            'v1': {
                                'send': {
                                    'voice': {
                                        'type': 'string',
                                        'allowed': ['true', 'false']
                                    },
                                    'language': {
                                        'type': 'string',
                                        'allowed': ['ru', 'en']
                                    },
                                    'tag': {
                                        'type': 'string',
                                        'maxLength': 36,
                                    },
                                },
                                'receive': {
                                    'to': to_schema,
                                    'toll_free': {
                                        'type': 'string',
                                        'allowed': ['true', 'false']
                                    },
                                    'tag': {
                                        'type': 'string',
                                        'maxLength': 36,
                                    },
                                }
                            }
                        }),
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
                                        'regex': "^[0-9]+",
                                        'required': True
                                    },
                                    'language': {
                                        'type': 'string',
                                        'allowed': ['ru', 'en']
                                    },
                                    'tag': {
                                        'type': 'string',
                                        'maxLength': 36,
                                    },
                                }
                            }
                        }),
    'pay': deep_merge(common_schema, {
        'v1': {
            'send': {
                'amount': {
                    'type': 'number',
                    'min': 1,
                    'required': True
                },
                'card': {
                    'type': 'string',
                    'minLength': 11,
                    'maxLength': 14
                },
                'tag': {
                    'type': 'string',
                    'maxLength': 36,
                }
            }
        }
    }),
    'sms': deep_merge(common_schema,
                      {
                          'v1': {
                              'send': {
                                  'txt': {
                                      'type': 'string',
                                      'required': True,
                                      'minlength': 1,
                                      'maxLength': 918
                                  },
                                  'from': {
                                      'type': 'string',
                                      'maxLength': 11,
                                  },
                                  'tag': {
                                      'type': 'string',
                                      'maxLength': 36,
                                  },
                                  'hidden': {
                                      'type': 'string',
                                      'maxLength': 918
                                  }
                              }
                          }
                      }),
    'viber': deep_merge(common_schema, {
        'v1': {
            'send': {
                'txt': {
                    'type': 'string',
                    'required': True,
                    'minlength': 1,
                    'maxLength': 14,
                },
                'txt': {
                    'type': 'string',
                },
                'from': {
                    'type': 'string',
                    'maxLength': 11,
                    'minlength': 1
                },
                'cascade': {
                    'type': 'string',
                    'allowed': ['sms', 'voice']
                }
            }
        }
    }),
    'social': deep_merge(common_schema, {
        'v1': {
            'send': {
                'txt': {
                    'type': 'string',
                    'minlength': 1,
                    'required': True
                },
                'from': {
                    'type': 'string',
                },
                'tag': {
                    'type': 'string',
                },
                'hidden': {
                    'type': 'string',
                }
            }
        }
    }),
    'vk': deep_merge(common_schema, {
        'v1': {
            'send': {
                'txt': {
                    'type': 'string',
                    'minlength': 1,
                    'maxLength': 2048,
                    'required': True
                },
                'from': {
                    'type': 'string',
                    'minlength': 1,
                    'maxLength': 11,
                },
                'tag': {
                    'type': 'string',
                    'maxLength': 36
                },
                'cascade': {
                    'validator': cascade_validator
                }
            }
        }
    }),
    'whatsapp': deep_merge(common_schema, {
        'v1': {
            'send': {
                'txt': {
                    'type': 'string',
                    'minlength': 1,
                    'maxLength': 10000,
                    'required': True
                },
                'file': {
                    'type': 'string',
                    'maxLength': 256,
                },
                'tag': {
                    'type': 'string',
                    'maxLength': 36,
                },
            },
            'webhook': {
                'url': {
                    'required': True,
                    'minLength': 11,
                    'maxLength': 256
                }
            }
        }
    }),
}
