from spack import *


class PyOrderedmultidict(PythonPackage):
    """omdict is an ordered multivalue dictionary that retains method parity with Python's dict and helps power furl."""
    homepage = "https://github.com/gruns/orderedmultidict"
    url = "https://pypi.io/packages/source/o/orderedmultidict/orderedmultidict-1.0.tar.gz"

    version('1.0', "fbfe9bad0b5a90f14e8b3838012be2e5")

