from spack import *


class PsrfitsUtils(AutotoolsPackage):
    """Utility library for working with search- and fold-mode PSRFITS pulsar data files"""

    homepage = "https://github.com/demorest/psrfits_utils"
    url = homepage

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    version('2017-01-20', git=url, commit='1fbf51b')
    version('2021-03-24', git=url, commit='c2a60b0')

    depends_on('cfitsio')

    patch('conf.patch')
    
    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--force')
