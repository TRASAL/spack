from spack import *
import os

class Dspsr(AutotoolsPackage):
    homepage = "http://dspsr.sourceforge.net/"
    url = "https://downloads.sourceforge.net/project/dspsr/dspsr/2025-02-03/dspsr-2025-02-03.tar.gz"

    version('2025-02-03', sha256='e4c54ce91092b42c3cc54cf6046abaa5c7e5595b67ccf469e5111da5cde62c9b')

    depends_on('psrdada')
    depends_on('psrchive')
    depends_on('cuda')
    depends_on('swig')
    depends_on('gsl')
    depends_on('pkg-config', type="build")

    def autoreconf(self, spec, prefix):
        with open("backends.list", 'w') as f:
            f.write("dada fits sigproc\n")
