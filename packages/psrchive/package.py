from spack import *
import os
from subprocess import check_call

class Psrchive(AutotoolsPackage):
    homepage = "http://psrchive.sourceforge.net/"
    url = "https://git.code.sf.net/p/psrchive/code"

    version('2018-06-14',
            git=url,
            commit='bcc5729fe92d90d8745d7293d632241ea0ec2b16')

    variant("x11", default=False, description="Enable GUI")
    variant("python", default=False, description="Enable Python interface")

    depends_on('tempo2')
    depends_on('pgplot')
    depends_on('fftw')

    depends_on('libx11', when="+x11")
    depends_on('qt', when="+x11")
    depends_on("python")
    depends_on('py-numpy')

    def configure_args(self):
        args = ['--enable-shared']
        if "+x11" in self.spec:
            args.append("--with-x") 
        return args

    def setup_environment(self, spack_env, run_env):
        run_env.set('PGPLOT_FONT', self.spec['pgplot'].prefix)

    def autoreconf(self, spec, prefix):
        bootstrap = which(os.getcwd() + '/bootstrap')
        bootstrap()
