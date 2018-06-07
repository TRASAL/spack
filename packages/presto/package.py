import os
from spack import *


class Presto(MakefilePackage):
    """Open source pulsar search and analysis toolkit """

    homepage = "http://www.cv.nrao.edu/~sransom/presto/"
    url      = "https://github.com/scottransom/presto/archive/v2.1.tar.gz"

    version('2.1', '36b8007b0e8513371a1e886bf79f309c')

    depends_on('python')
    depends_on('fftw')
    depends_on('cfitsio')
    depends_on('libpng')
    depends_on('glib')
    depends_on('pgplot')

    build_directory = "src"

    def setup_environment(self, spack_env, run_env):
        self.source_path = "{}/{}-{}/".format(self.stage.path, self.name, self.version)
        spack_env.set('PRESTO',  self.source_path)
        spack_env.set('LD_LIBRARY_PATH', self.source_path + "/lib")
        spack_env.set('PGPLOT_DIR', self.spec['pgplot'].prefix)

    def install(self, spec, prefix):
        for i in os.listdir('bin'):
            install('bin/' + i, prefix.bin)

        for i in os.listdir('lib'):
            if i.endswith('.so'):
                install('lib/' + i, prefix.lib)