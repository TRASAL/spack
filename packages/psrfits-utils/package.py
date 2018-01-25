from spack import *


class PsrfitsUtils(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/demorest/psrfits_utils"
    url      = "https://github.com/demorest/psrfits_utils.git"

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    version('2018-01-25', git='https://github.com/demorest/psrfits_utils', commit='1fbf51b')

    depends_on('cfitsio')

    patch('conf.patch')
    
    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--force')
