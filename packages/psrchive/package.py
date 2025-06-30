from spack.package import *
import os

class Psrchive(AutotoolsPackage):
    homepage = "http://psrchive.sourceforge.net/"
    url = "https://downloads.sourceforge.net/project/psrchive/psrchive/2025-04-24/psrchive-2025-04-24.tar.gz"

    version('2025-04-24', sha256='20e3ba5dc8979af33498fc0d84a55acf2ac68c8fd854d91cf6e8bab73d65a9e3')

    variant("x11", default=True, description="Enable GUI")
    variant("python", default=True, description="Enable Python interface")

    depends_on('tempo2')
    depends_on('pgplot', when='~x11')
    depends_on('pgplot+X', when='+x11')
    depends_on('fftw')
    depends_on('gsl')
    depends_on('pkg-config', type="build")

    depends_on('libx11', when="+x11")
    depends_on('qt', when="+x11")
    depends_on("python", when="+python")
    depends_on('py-numpy', when="+python")
    depends_on('swig', when="+python")

    @run_before("build")
    def fix_numpy(self):
        # fix compatibility with numpy 2+
        if "+python" in self.spec and self.spec['py-numpy'].satisfies("@2:"):
            new_content = """#include "numpy/ndarrayobject.h"
#define PyArray_DOUBLE NPY_DOUBLE
#define PyArray_FLOAT NPY_FLOAT
"""
            filter_file('#include "numpy/noprefix.h"', new_content, 'More/python/psrchive.i')

    def setup_build_environment(self, env):
        # path to python after following symlinks, such that psrchive can find libpython
        python_path = os.path.abspath(os.path.realpath(f'{self.spec["python"].prefix}/bin'))
        env.set('PYTHON', python_path)

    def setup_run_environment(self, env):
        python_version_major, python_version_minor = self.spec['python'].version.version[0][:2]
        python_version = f'{python_version_major}.{python_version_minor}'
        env.append_path('PYTHONPATH', f'{prefix.lib}/python{python_version}/site-packages')

    def configure_args(self):
        args = ['--enable-shared']
        if "+x11" in self.spec:
            args.append("--with-x") 
        if "+python" not in self.spec:
            args.append("--disable-python")
        return args
