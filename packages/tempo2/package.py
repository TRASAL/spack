from spack import *


class Tempo2(AutotoolsPackage):
    """Tempo2 is a new pulsar timing package."""

    homepage = "http://www.atnf.csiro.au/research/pulsar/tempo2/index.php"
    url      = "https://bitbucket.org/psrsoft/tempo2"

    version('2018-01-18', git='https://bitbucket.org/psrsoft/tempo2', commit='b1fe783')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    def install(self, spec, prefix):
        env['TEMPO2'] = prefix
        make()
        make('plugins')
        make('install')
        make('plugins-install')
