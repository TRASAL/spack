from spack import *
import os
from subprocess import check_call

class Psrchive(AutotoolsPackage):
    homepage = "http://psrchive.sourceforge.net/"
    url = "https://git.code.sf.net/p/psrchive/code"

    version('2018-06-14',
            git=url,
            commit='bcc5729fe92d90d8745d7293d632241ea0ec2b16')

    depends_on('tempo2')
    depends_on('pgplot')
    depends_on('fftw')

    def autoreconf(self, spec, prefix):
        # don't know how to call a script the spack way
        check_call("./bootstrap")
