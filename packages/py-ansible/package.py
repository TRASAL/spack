from spack import *
from glob import glob


class PyAnsible(PythonPackage):
    """Simple module to parse ISO 8601 dates"""

    homepage = "https://pypi.org/project/ansible/"
    url      = "https://pypi.io/packages/source/a/ansible/ansible-2.8.0.tar.gz"

    version('2.8.0', '9320cd9e26f929568038db49781df245')

