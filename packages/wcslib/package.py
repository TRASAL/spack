from spack import *


class Wcslib(AutotoolsPackage):
    """A C library that implements the FITS World Coordinate System (WCS) standard"""

    homepage = "http://www.atnf.csiro.au/people/mcalabre/WCS/wcslib/"
    #url      = "ftp://ftp.atnf.csiro.au/pub/software/wcslib/wcslib-5.18.tar.bz2"
    #version('5.18', '67a78354be74eca4f17d3e0853d5685f')

    # lets use a ubuntu mirror since we don't have access to FTP
    url = "http://archive.ubuntu.com/ubuntu/pool/universe/w/wcslib/wcslib_5.18.orig.tar.bz2"
    version('5.18', 'c011a1b1370b2f16d5ac9c3fe702870e')


    depends_on('cfitsio')

    def configure_args(self):
        args = []
        return args
