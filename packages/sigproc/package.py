from spack import *


class Sigproc(AutotoolsPackage):
    """
    package designed to standardize the initial analysis of the many types of
    fast-sampled pulsar data
    """

    homepage = "http://sigproc.sourceforge.net/"
    #url      = "http://prdownloads.sourceforge.net/sigproc/sigproc-4.3.tar.gz?download"
    
    # this fork is more up-to-dateish
    url = "https://github.com/SixByNine/sigproc"

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')
    depends_on('zlib', type='build')

    depends_on('fftw@3.3:')
    depends_on('tempo2')
    
    version('2017-11-13',
            git=url,
            commit='2dbe77cf14a0ea28c95e5d8ef19fed37d6c5be42')

    def autoreconf(self, spec, prefix):
        autoreconf('-f', '-i', '-I', 'autoconf.boot')



