from greensms.constants import VERSIONS


def get_version(version):
    version = version or VERSIONS['v1']
    version = version.lower()
    if version in VERSIONS.keys():
        return VERSIONS[version]
    raise Exception('Invalid Version')
