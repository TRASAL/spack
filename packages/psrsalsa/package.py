import os
from spack import *


class Psrsalsa(MakefilePackage):
    """
    PSRSALSA - A Suite of ALgorithms for Statistical Analysis of pulsar data
    """

    homepage = "http://www.jb.man.ac.uk/research/pulsar/Resources/psrsalsa.html"
    url      = "https://github.com/weltevrede/psrsalsa"

    version('2022-02-22', git=url, commit='2efbaf4592e08fdb76002bbc9dc25e8e4441813b')

    depends_on('pgplot+X')
    depends_on('cfitsio')
    depends_on('fftw')
    depends_on('gsl')

    @run_before('build')
    def update_gsl_version(self):
        gsl_version = str(self.spec['gsl'].version.joined)
        if len(gsl_version) == 2:
            # major / minor only, psrsalsa expects a zero in the middle
            gsl_version = gsl_version[0] + '0' + gsl_version[1]
        
        filter_file('GSLFLAGS = -DGSL_VERSION_NUMBER=115', f'GSLFLAGS = -DGSL_VERSION_NUMBER={gsl_version}', 'Makefile')

    def install(self, spec, prefix):
        os.remove('bin/README.txt')
        install_tree('bin', prefix.bin)
