import os
from spack import *

class Presto(MesonPackage):
    """Open source pulsar search and analysis toolkit """

    homepage = "http://www.cv.nrao.edu/~sransom/presto/"
    url      = "https://github.com/scottransom/presto/archive/v2.1.tar.gz"

    version('5.0.3', '3e9ce6df9098a8b1086b0892538d0554')

    variant("python", default=True, description="Build python bindings.")

    depends_on('cmake', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('cfitsio')
    depends_on('glib')
    depends_on('fftw')
    depends_on('libpng')
    depends_on('pgplot+X')
    depends_on('tempo')

    depends_on('python', when="+python")
    depends_on('py-pip', when="+python")

    patch('add_wsrt.patch', level=1)

    def setup_build_environment(self, env):
        source_path = f'{self.stage.path}/{self.name}-{self.version}'
        env.set('PRESTO', source_path)
        # to ensure python bindings can find libpresto
        env.append_path('LIBRARY_PATH', f'{self.prefix}/lib')

    def setup_run_environment(self, env):
        env.set('PRESTO', self.prefix)
        env.append_path('PYTHONPATH', f'{self.prefix}/python')

    @run_after('install')
    def post_install(self):
        # FFTW wisdom file is optimized for ARTS
        package_path = os.path.dirname(os.path.abspath(__file__))
        install(f'{package_path}/fftw_wisdom.txt', f'{prefix}/lib')
        install_tree('examplescripts', f'{prefix}/examplescripts')
        install_tree('lib', f'{prefix}/lib')

        if "+python" in self.spec:
            os.chdir('python')
            pip = which('pip')
            pip('install', '.', f'--target={prefix}/python')
