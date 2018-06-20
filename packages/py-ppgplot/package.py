from spack import *


class PyPpgplot(PythonPackage):
    """The Python pgplot extension"""

    homepage = "https://github.com/trmrsh/ppgplot"
    url      = "https://github.com/trmrsh/ppgplot"

    version('2018-01-25',
            git='https://github.com/trmrsh/ppgplot',
            commit='6a98736')
    
    depends_on('py-numpy')
    depends_on('pgplot')
