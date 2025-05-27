from spack.package import *
from shutil import copytree
import os


class Tempo2(AutotoolsPackage):
    """Tempo2 is a new pulsar timing package."""

    url = "https://bitbucket.org/psrsoft/tempo2/downloads/tempo2-2018.02.1.tar.gz"

    version('2018.02.1', '1c9e881c6f8e3c40e6d79a638a702e8c4c09880b')
    version('2023.05.1', '6748a3a5d8734bedee97dfbe3aab5cd68fd9f7e3')

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

    def configure_args(self):
        args = ['--with-fftw3-dir=' + self.spec['fftw'].prefix,
                '--with-cfitsio-dir=' + self.spec['cfitsio'].prefix]
        if "+x11" in self.spec:
            args.append("--with-x")

        if "+gsl" in self.spec:
            args.append("--with-gsl-prefix=" + self.spec['gsl'].prefix)

        return args

    def setup_build_environment(self, env):
        env.set('TEMPO2', self.prefix)

    def setup_run_environment(self, env):
        env.set('TEMPO2', self.prefix)

    def build(self, spec, prefix):
        make()
        make('plugins')

    def install(self, spec, prefix):
        make('install')
        make('plugins-install')
        for subdir in os.listdir('T2runtime'):
            if os.path.isdir(subdir):
                copytree('T2runtime/'+subdir, self.prefix+'/'+subdir)
