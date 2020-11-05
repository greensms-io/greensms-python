from greensms.api.modules import MODULES
from greensms.utils.url import build_url
from greensms.utils.validator import validate
from greensms.utils.attr_dict import AttrDict

class ModuleLoader:
  def __init__(self):
    self.module_map = AttrDict({})

  def register_modules(self, shared_options, filters = {}):
    if not filters:
      filters = {}

    current_version = shared_options['version']

    for module_name, module_info in MODULES.items():

      if module_name not in self.module_map:
        self.module_map[module_name] = AttrDict({})

      module_versions = module_info['versions']
      module_schema = module_info['schema'] if 'schema' in module_info else None

      if 'load_static' in filters and 'static' in module_info and filters['load_static'] == True and module_info['static'] == True:
          continue

      for version, version_functions in module_versions.items():
        if version not in self.module_map[module_name]:
          self.module_map[module_name][version] = AttrDict({})

        for function_name, definition in version_functions.items():

          if function_name not in self.module_map[module_name][version]:
            self.module_map[module_name][version][function_name] = AttrDict({})

          url_args = []
          if 'static' not in module_info or module_info['static'] == False:
            url_args.append(module_name)
          url_args.append(function_name)

          api_url = build_url(shared_options['base_url'], url_args)
          self.module_map[module_name][function_name] = lambda shared_options, api_url, definition, module_schema: self.module_api()

          if version == current_version:
            self.module_map[module_name][function_name] = self.module_map[module_name][version][function_name]

    return self.module_map


  def module_api(**kwargs):

    rest_client = kwargs['shared_options']['rest_client']

    request_params = {
      'url': kwargs['api_url'],
      'method': kwargs['definition']['method'],
    }

    if 'module_schema' in kwargs and kwargs['module_schema'] is not None:
      errors = validate(module_schema, kwargs['params'])
      if errors:
        return errors

    request_params['params'] = kwargs['params'] if 'params' in kwargs else {}

    response = rest_client.request(**request_params)
    return response