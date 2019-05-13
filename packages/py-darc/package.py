from spack import *


class PyDarc(PythonPackage):
    """Data Analysis of Real-time Candidates from ARTS"""
    homepage = "https://github.com/loostrum/darc"

    version('master',
            git=homepage,
            branch='master')

    version('test_trigger',
            git=homepage,
            branch='test_trigger')

    version('dev'
            git=homepage,
            branch='dev')

    depends_on('python')
    depends_on('py-setuptools')
    depends_on('py-numpy')
    depends_on('py-astropy')
    depends_on('py-pyyaml')
    depends_on('py-voevent-parse')

