from spack import *
import shutil


class PyPyplusplus(PythonPackage):
    """A lightweight library for parsing, manipulating, and generating VOEvent XML packets"""
    homepage = "https://pyplusplus.readthedocs.io/"
    url = "https://pypi.io/packages/source/p/pyplusplus/pyplusplus-1.8.1.tar.gz"

    version('1.8.1', "365e9e727acff9ac084b21c1b95b939c")

