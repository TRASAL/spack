from spack import *


class Psrdada(AutotoolsPackage):
    """PSRDADA is an Open Source software project to support the development of
    data acquisition and distributed analysis systems. The authors of the code
    use it primarily in the implementation of baseband recording and processing
    instrumentation for pulsar astronomy."""

    homepage = "http://psrdada.sourceforge.net"

    version('2018-06-06', git='https://git.code.sf.net/p/psrdada/code',
            commit='754a618b321cf0b328d34c80c995ad0959ddf4e8')


    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('cuda')
    depends_on('fftw@3.3:')
    depends_on('gsl')
    depends_on('hwloc')

    patch('fix_pragma.patch', level=1)
    patch('missing_cuda_include.patch', level=1)

    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--force')

    def configure_args(self):
        args = ['--with-cuda-dir=%s' % self.spec['cuda'].prefix,
                '--with-fftw3-dir=%s' % self.spec['fftw'].prefix,
                '--with-gsl-dir=%s' % self.spec['gsl'].prefix,
                '--with-hwloc-dir=%s' % self.spec['hwloc'].prefix]
        return args
