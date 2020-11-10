try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin
from greensms.constants import BASE_URL


def base_url():
    return BASE_URL


def build_url(base_url, args):
    if not base_url:
        raise Exception('Base URL cannot be empty!')

    path = '/'.join(args)

    url = urljoin(base_url, path)
    return url
