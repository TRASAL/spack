from spack import *
from glob import glob


class PyIso8601(PythonPackage):
    """Simple module to parse ISO 8601 dates"""

    homepage = "https://pypi.org/project/iso8601/"
    url      = "https://pypi.io/packages/source/i/iso8601/iso8601-0.1.12.tar.gz"

    version('0.1.12', '4de940f691c5ea759fb254384c8ddcf6')

