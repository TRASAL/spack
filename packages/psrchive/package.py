from spack.package import *
import os

class Psrchive(AutotoolsPackage):
    homepage = "http://psrchive.sourceforge.net/"
    url = "https://downloads.sourceforge.net/project/psrchive/psrchive/2025-04-24/psrchive-2025-04-24.tar.gz"

    version('2025-04-24', sha256='20e3ba5dc8979af33498fc0d84a55acf2ac68c8fd854d91cf6e8bab73d65a9e3')

    variant("x11", default=False, description="Enable GUI")
    variant("python", default=False, description="Enable Python interface")

    depends_on('tempo2')
    depends_on('pgplot', when='~x11')
    depends_on('pgplot+X', when='+x11')
    depends_on('fftw')

    depends_on('libx11', when="+x11")
    depends_on('qt', when="+x11")
    depends_on("python", when="+python")
    depends_on('py-numpy', when="+python")

    def configure_args(self):
        args = ['--enable-shared']
        if "+x11" in self.spec:
            args.append("--with-x") 
        return args

    def setup_run_environment(self, env):
        env.set('PGPLOT_FONT', self.spec['pgplot'].prefix+'/include/grfont.dat')
