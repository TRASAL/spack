from spack import *


class PySupervisor(PythonPackage):
    """Supervisor is a client/server system that allows its users to control a number of processes on UNIX-like operating systems."""
    homepage = """http://supervisord.org/"""
    url = "https://pypi.io/packages/source/s/supervisor/supervisor-3.1.4.tar.gz"

    version('3.1.4', "cb64f92409ebabf17aa0884fc407fec6")

