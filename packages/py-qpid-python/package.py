from spack import *
from glob import glob


class PyQpidPython(PythonPackage):
    """Python client implementation and AMQP conformance tests for Apache Qpid"""

    homepage = "https://qpid.apache.org"
    url       = "http://apache.cs.uu.nl/qpid/python/1.37.0/qpid-python-1.37.0.tar.gz"

    version('1.37.0', '0de54715af271cf45fc8e7f8e0065628')

