from spack import *


class Pgplot(Package):
    """The PGPLOT Graphics Subroutine Library is a Fortran- or C-callable, device-independent graphics package for making simple scientific graphs."""

    homepage = "https://www.astro.caltech.edu/~tjp/pgplot"
    url      = "ftp://ftp.astro.caltech.edu/pub/pgplot/pgplot5.2.tar.gz"

    version('5.2', 'e8a6e8d0d5ef9d1709dfb567724525ae')

    # depends_on('foo')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
