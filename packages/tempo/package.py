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

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('TEMPO', self.prefix)

    def install(self, spec, prefix):
        install_tree('clock', prefix + '/clock')
        install_tree('ephem', prefix + '/ephem')
        install('obsys.dat', prefix)
        install('tempo.cfg', prefix)
        install('tempo.hlp', prefix)
        install_tree('tzpar', prefix + '/tzpar')
        make()
        make('install')
