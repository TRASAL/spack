from spack import *


class Wcslib(AutotoolsPackage):
    """A C library that implements the FITS World Coordinate System (WCS) standard"""

    homepage = "http://www.atnf.csiro.au/people/mcalabre/WCS/wcslib/"
    url      = "ftp://ftp.atnf.csiro.au/pub/software/wcslib/wcslib-5.18.tar.bz2"

    version('5.18', '67a78354be74eca4f17d3e0853d5685f')

    depends_on('cfitsio')

    def configure_args(self):
        args = []
        return args
