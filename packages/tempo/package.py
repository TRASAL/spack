from spack import *
import os


class Tempo(AutotoolsPackage):
    """Tempo is a pulsar timing data analysis package."""

    homepage = "http://tempo.sourceforge.net/"
    url      = "https://git.code.sf.net/p/tempo/tempo"

    version('2018-04-24', git='https://git.code.sf.net/p/tempo/tempo', commit='13e12c')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    patch('fix_path_length.patch', level=0)
    patch('fix_wsrt_code.patch', level=0)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('TEMPO', self.prefix + '/tempo')

    def install(self, spec, prefix):
        os.mkdir('tempo', 0755)
        install_tree('clock', prefix + '/tempo/clock')
        install_tree('ephem', prefix + '/tempo/ephem')
        install('obsys.dat', prefix + '/tempo')
        install('tempo.cfg', prefix + '/tempo')
        install('tempo.hlp', prefix + '/tempo')
        install_tree('tzpar', prefix + '/tempo/tzpar')
        make()
        make('install')
