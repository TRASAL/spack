from spack import *


class Sigproc(AutotoolsPackage):
    """
    package designed to standardize the initial analysis of the many types of
    fast-sampled pulsar data
    """

    homepage = "http://sigproc.sourceforge.net/"
    url = "https://github.com/SixByNine/sigproc"

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')
    depends_on('zlib', type='build')

    depends_on('fftw@3.3:')
    depends_on('pgplot')
    depends_on('tempo2')
    
    version('2017-11-13',
            git=url,
            commit='2dbe77cf14a0ea28c95e5d8ef19fed37d6c5be42')
    version('2025-03-29',
            git=url,
            commit='22b75695a120dc2c32136003240c93cb638fd94c')

    patch('include_csh.patch', level=0)

    def autoreconf(self, spec, prefix):
        autoreconf('-f', '-i', '-I', 'autoconf.boot')
        # ugly hack to avoid rank mismatch errors in calls to pgplot
        filter_file('AM_FFLAGS = -fno-second-underscore', 'AM_FFLAGS = -fno-second-underscore -fallow-argument-mismatch', 'src/Makefile.in')

    

