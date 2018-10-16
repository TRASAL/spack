from spack import *
from glob import glob


class PyQpidTools(PythonPackage):
    """Python libraries for the Apache Qpid C++ broker"""

    homepage = "https://qpid.apache.org"
    url       = "https://pypi.io/packages/source/q/qpid-tools/qpid-tools-1.36.0_1.tar.gz"

    version('1.36.0-1', 'd0208471a086b98ba9d3aae9e6066af7')

