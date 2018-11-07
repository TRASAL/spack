from spack import *


class PyPycuda(PythonPackage):
    """Python wrapper for Nvidia CUDA"""
    homepage = "https://documen.tician.de/pycuda/"
    url = "https://pypi.io/packages/source/p/pycuda/pycuda-2018.1.1.tar.gz"

    version('2018.1.1', "d4d925649897ab5a2c805e62ad1dfa14")

    depends_on('cuda')

