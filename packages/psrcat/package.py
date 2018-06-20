from spack import *
import os


class Psrcat(Package):
    """
    PSRCAT is the ATNF pulsar catalogue

    Note that the tarball is updated regularly without version change, so the
    checksum changes also. If the checksum fails it needs to be updated here,
    or the package needs to be installed with --no-checksum
    """

    homepage = "http://www.atnf.csiro.au/people/pulsar/psrcat/"
    url = "http://www.atnf.csiro.au/people/pulsar/psrcat/downloads/psrcat_pkg.tar.gz"

    version('1.58', 'e1b95491e91d708630d15144eae88357')

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
