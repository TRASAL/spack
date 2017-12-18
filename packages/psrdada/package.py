from spack import *


class Psrdada(AutotoolsPackage):
    """PSRDADA is an Open Source software project to support the development of
    data acquisition and distributed analysis systems. The authors of the code
    use it primarily in the implementation of baseband recording and processing
    instrumentation for pulsar astronomy."""

    homepage = "http://psrdada.sourceforge.net"
    url      = "http://arts0.apertif/~sipior/psrdada-1.0.tar.gz"

    version('1.2', '1366ea321f87084bb8e51ceecaed738b')
    version('1.1', '02741557a1181e71ce4fcd132d0d97d5')
    version('1.0', 'a1e4ed800601999679406f21ab9eeed5')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('cuda@8.0.61')
    depends_on('fftw@3.3:')
    depends_on('gsl')
    depends_on('hwloc')

    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--force')

    def configure_args(self):
        args = ['--with-cuda-dir=%s' % self.spec['cuda'].prefix,
                '--with-fftw3-dir=%s' % self.spec['fftw'].prefix,
                '--with-gsl-dir=%s' % self.spec['gsl'].prefix,
                '--with-hwloc-dir=%s' % self.spec['hwloc'].prefix]
        return args
