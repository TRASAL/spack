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
    url = "https://www.atnf.csiro.au/research/pulsar/psrcat/downloads/psrcat_pkg.v2.6.1.tar.gz"

    version('2.6.1', '6378c1fdb9fac2ba3138cb5b3309de25')

    def setup_run_environment(self, env):
        env.set('PSRCAT_FILE', self.prefix+"/psrcat.db")

    def install(self, spec, prefix):
        filter_file('MAX_CATLEN 100', 'MAX_CATLEN 255', 'psrcat.h')
        make("-B", "psrcat")
        os.mkdir(prefix.bin, 0o755)
        install('psrcat.db', prefix)
        install('psrcat', prefix.bin)
