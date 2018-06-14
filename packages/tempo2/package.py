from spack import *


class Tempo2(AutotoolsPackage):
    """Tempo2 is a new pulsar timing package."""

    homepage = "http://www.atnf.csiro.au/research/pulsar/tempo2/index.php"
    url      = "https://bitbucket.org/psrsoft/tempo2/downloads/tempo2-2018.02.1.tar.gz"

    version('2018.02.1', '1c9e881c6f8e3c40e6d79a638a702e8c4c09880b')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    def setup_environment(self, spack_env, run_env):
	run_env.prepend_path('TEMPO2', self.prefix) 
	spack_env.prepend_path('TEMPO2', self.prefix) 

    def install(self, spec, prefix):
        make()
        make('plugins')
        make('install')
        make('plugins-install')
