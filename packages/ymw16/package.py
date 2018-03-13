from spack import *
import os


class Ymw16(Package):
    """YMW16 is a model for the Galactic distribution of free electrons"""

    homepage = "www.xao.ac.cn/ymw16/"
    url = "http://119.78.162.254/dmodel/ymw16_v1.3.2.tar.gz"

    version('1.3.2', 'bf8584cfbebd1006d561b4a460e93a18')

    patch('arts.patch')

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('YMW16_DIR', self.prefix)

    def install(self, spec, prefix):
        src = os.getcwd()
        make_ymw16 = which(src + "/make_ymw16")
        make_ymw16()
        os.mkdir(prefix+'/bin', 0755)
        install('ymw16', prefix.bin)
        install('ymw16par.txt', prefix)
        install('spiral.txt', prefix)
