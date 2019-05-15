from spack import *


class PyPygccxml(PythonPackage):
    """Python package for easy C++ declarations navigation."""
    homepage = "https://pypi.org/project/pygccxml/"
    url = "https://github.com/gccxml/pygccxml/archive/v1.9.1.tar.gz"

    version('1.9.1', "149959b6c339991049824af6b42616cf")
    version('1.8.6', "8f6769d957199cf349e17773288d5826")
    version('1.8.0', "8bc7ec72d41e349d9d3001ad82dbe9b4", preferred=True)

