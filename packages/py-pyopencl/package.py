from spack import *


class PyPyopencl(PythonPackage):
    """Python wrapper for OpenCL"""
    homepage = "https://documen.tician.de/pyopencl/"
    url = "https://pypi.io/packages/source/p/pyopencl/pyopencl-2018.2.1.tar.gz"

    version('2018.2.1', "62741a41a3b6d4f46cac57d042bbb6ee")

    depends_on('cuda')
    depends_on('py-pybind11')

