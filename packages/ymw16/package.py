from spack import *
import os


class Ymw16(Package):
    """YMW16 is a model for the Galactic distribution of free electrons"""

    homepage = "https://www.atnf.csiro.au/research/pulsar/ymw16/"
    url = "https://www.atnf.csiro.au/research/pulsar/ymw16/ymw16_v1.3.2.tar.gz"

    version('1.3.2', 'bf8584cfbebd1006d561b4a460e93a18')

    patch('arts.patch')

    def setup_run_environment(self, env):
        env.set('YMW16_DIR', self.prefix)

    def install(self, spec, prefix):
        filter_file('gcc -g  ymw16', 'gcc -Wl,--allow-multiple-definition -g ymw16', 'make_ymw16')
        src = os.getcwd()
        make_ymw16 = which(src + "/make_ymw16")
        make_ymw16()
        os.mkdir(prefix+'/bin')
        install('ymw16', prefix.bin)
        install('ymw16par.txt', prefix)
        install('spiral.txt', prefix)
