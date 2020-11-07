try:
  from urllib.parse import urlparse, urljoin
except ImportError:
  from urlparse import urlparse, urljoin
from functools import reduce
from greensms.constants import BASE_URL

def base_url():
  return BASE_URL

def build_url(base_url, args):
  if not base_url:
    raise Exception('Base URL cannot be empty!')

  path = '/'.join(args)

  url = urljoin(base_url, path)
  return url
