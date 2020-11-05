from greensms.utils.validator import validate

class Module:

  def __init__(self, rest_client, module_schema, **kwargs):
    self.rest_client = rest_client
    self.module_schema = module_schema
    self.params = {}

    for key, value in kwargs.items():
      self.params[key] = value

  def api_func(self, **kwargs):

    if self.module_schema is not None:
      errors = validate(self.module_schema, kwargs)
      if errors:
        return errors

    api_params={}
    for key, value in kwargs.items():
      self.api_params[key] = value

    request_params = {**self.params, **api_params}
    response = self.rest_client.request(**request_params)

    return response

