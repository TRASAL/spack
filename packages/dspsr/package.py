from spack import *
import os

class Dspsr(AutotoolsPackage):
    homepage = "http://dspsr.sourceforge.net/"
    url_sourceforge = "https://downloads.sourceforge.net/project/dspsr/dspsr/2025-02-03/dspsr-2025-02-03.tar.gz"
    url = "https://gitlab.com/pulsar-astronomy/dspsr/"

    version('2025-02-03', url=url_sourceforge, sha256='e4c54ce91092b42c3cc54cf6046abaa5c7e5595b67ccf469e5111da5cde62c9b')
    version('2026-09-01', git=url, commit="2aefdf1b117d49424fee8740b1b4572f92d584d0")

    depends_on('psrdada')
    depends_on('psrchive')
    depends_on('cuda')
    depends_on('swig')
    depends_on('gsl')
    depends_on('pkg-config', type="build")
    depends_on('autoconf', type="build")
    depends_on('automake', type="build")
    depends_on('libtool', type="build")

    def autoreconf(self, spec, prefix):
        # Run bootstrap if downloaded from git
        if not spec.satisfies("2025-02-03"):
            which('bash')('./bootstrap')
        with open("backends.list", 'w') as f:
            f.write("dada fits sigproc\n")
