from spack import *
from shutil import copytree
import os


class Tempo2(AutotoolsPackage):
    """Tempo2 is a new pulsar timing package."""

    homepage = "http://www.atnf.csiro.au/research/pulsar/tempo2/index.php"
    url      = "https://bitbucket.org/psrsoft/tempo2/downloads/tempo2-2018.02.1.tar.gz"

    version('2018.02.1', '1c9e881c6f8e3c40e6d79a638a702e8c4c09880b')

    variant("x11", default=False, description="Enable GUI")
    variant("gsl", default=False, description="Enable GSL")

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('cfitsio')
    depends_on('pgplot')
    depends_on('fftw@3.3:')

    depends_on('libx11', when="+x11")
    depends_on('gsl', when="+gsl")

    patch('fix_gets.patch', level=1)

    def configure_args(self):
        args = ['--with-fftw3-dir=' + self.spec['fftw'].prefix,
                '--with-cfitsio-dir=' + self.spec['cfitsio'].prefix]
        if "+x11" in self.spec:
            args.append("--with-x")

        if "+gsl" in self.spec:
            args.append("--with-gsl-prefix=" + self.spec['gsl'].prefix)

        return args

    def configure(self, spec, prefix):
	if os.access('Makefile', os.R_OK):
		make('distclean')
	configure()

    def setup_environment(self, spack_env, run_env):
	run_env.set('TEMPO2', self.prefix)
	spack_env.set('TEMPO2', self.prefix)

    def install(self, spec, prefix):
        make()
        make('plugins')
        make('install')
        make('plugins-install')
        for subdir in os.listdir('T2runtime'):
            copytree('T2runtime/'+subdir, self.prefix+'/'+subdir)
