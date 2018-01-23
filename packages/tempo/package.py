from spack import *


class Tempo(AutotoolsPackage):
    """Tempo is a pulsar timing data analysis package."""

    homepage = "http://tempo.sourceforge.net/"
    url      = "https://git.code.sf.net/p/tempo/tempo"

    version('2018-01-15', git='https://git.code.sf.net/p/tempo/tempo', commit='ce072d')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    def configure_args(self):
        args = []
        return args
