from spack import *


class PyWatchdog(PythonPackage):
    """Python API and shell utilities to monitor file system events."""

    homepage = "https://github.com/gorakhargosh/watchdog"
    url      = "https://pypi.io/packages/source/w/watchdog/watchdog-0.9.0.tar.gz"

    version('0.9.0', '7cdc103f607e72fc32c206301a72d1b2')

    #depends_on('py-pyyaml', type=('build', 'run'))
    
