from spack import *
import os


class Psrcat(Package):
    """PSRCAT is the ATNF pulsar catalogue"""

    homepage = "http://www.atnf.csiro.au/people/pulsar/psrcat/"
    url = "http://www.atnf.csiro.au/people/pulsar/psrcat/downloads/psrcat_pkg.tar.gz"

    version('1.58', '0928ff35f1856655f9da039e35a94820')

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PSRCAT_FILE', self.prefix+"/psrcat.db")

    def install(self, spec, prefix):
        filter_file('MAX_CATLEN 100', 'MAX_CATLEN 255', 'psrcat.h')
        src = os.getcwd()
        makeit = which(src + "/makeit")
        makeit()
        os.mkdir(prefix+'/bin', 0755)
        install('psrcat.db', prefix)
        install('psrcat', prefix.bin)
