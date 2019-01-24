from spack import *


class PyComet(PythonPackage):
    """Comet is an implementation of the VOEvent Transport Protocol, which provides a mechanism for fast and reliable distribution of VOEvents to the community."""
    homepage = "https://comet.readthedocs.io/"
    url = "https://pypi.io/packages/source/c/comet/Comet-3.1.0.tar.gz"

    version('3.1.0', "4e85ded8908a08244f44dd3cfd87d66e")

    depends_on('py-twisted', type='run')
    depends_on('py-zope-interface', type='run')
    depends_on('py-py2-ipaddress', type='run')
    depends_on('py-lxml', type='run')
