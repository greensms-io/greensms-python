from greensms.api.modules import MODULES
from greensms.utils.url import build_url
from greensms.utils.validator import validate

class ModuleLoader:
  def __init__(self):
    self.module_map = {}

  def register_modules(self, shared_options, filters = {}):
    if not filters:
      filters = {}

    current_version = shared_options['version']

    for module_name, module_info in MODULES.items():
      module_versions = module_info['versions']
      module_schema = module_info['schema']

      if 'load_static' in filters and 'static' in module_info and filters['load_static'] == True and module_info['static'] == True:
          continue

      for version, version_functions in module_versions.items():
        print(module_name)
        print(version_functions)
