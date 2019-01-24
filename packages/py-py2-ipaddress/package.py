from spack import *

class PyPy2Ipaddress(PythonPackage):
    """This is a Python 2.6 backport of the Python 3.4 ipaddress module."""

    homepage = "https://pypi.org/project/py2-ipaddress/"
    url      = "https://pypi.io/packages/source/p/py2-ipaddress/py2-ipaddress-3.4.1.tar.gz"

    version('3.4.1', '47734313c841068e3d5386d048d01c3d')

    depends_on('py-setuptools', type='build')

