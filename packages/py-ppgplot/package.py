from spack import *


class PyPpgplot(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/trmrsh/ppgplot"
    url      = "https://github.com/trmrsh/ppgplot"

    version('2018-01-25', git='https://github.com/trmrsh/ppgplot', commit='6a98736')
    
    extends('python')

    depends_on('py-numpy', type=('build', 'run'))
    depends_on('pgplot', type=('build','run', 'link'))

    def build_args(self, spec, prefix):
        args = []
        return args
