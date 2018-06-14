from spack import *
import os
from subprocess import call

class Dspsr(AutotoolsPackage):
    homepage = "http://dspsr.sourceforge.net/"
    url = "git://git.code.sf.net/p/dspsr/code"

    version('2018-05-22',
            git=url,
            commit='85982f596796dc2c3a9b4da7bbbaa9b28246c7fb')

    depends_on('psrdada')
    depends_on('cuda')
    depends_on('swig')
    depends_on('gsl')

    def autoreconf(self, spec, prefix):
        with open("backends.list", 'w') as f:
            f.write("dada fits sigproc\n")

        # don't know how to call a script the spack way
        call("./bootstrap")
