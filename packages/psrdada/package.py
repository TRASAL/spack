from spack import *


class Psrdada(AutotoolsPackage):
    """PSRDADA is an Open Source software project to support the development of
    data acquisition and distributed analysis systems. The authors of the code
    use it primarily in the implementation of baseband recording and processing
    instrumentation for pulsar astronomy."""

    homepage = "http://psrdada.sourceforge.net"
    url = 'https://git.code.sf.net/p/psrdada/code'

    version('2024-12-13', git=url, commit='1e48b65e90b279683134f91395668b38e58f7646')

    variant('cuda', default=True, description='Enable CUDA support.')
    variant('hwloc', default=True, description='Enable hwloc support.')
    variant('gsl', default=True, description='Enable gsl support.')
    variant('fftw', default=True, description='Enable FFTW support.')
    variant('shared', default=True, description='Enable generation of shared libs.')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('cuda', when='+cuda')
    depends_on('python', when='+cuda')
    depends_on('hwloc', when='+hwloc')
    depends_on('gsl', when='+gsl')
    depends_on('fftw@3.3', when='+fftw')

#    patch('fix_pragma.patch', level=1)
#    patch('no_cuda_no_mopsr.patch', level=1)
#    patch('missing_cuda_include.patch', level=1)
#    patch('remove_nreader_limit.patch', level=1)
#    patch('fix_dbevent.patch', level=1)
#    patch('fix_dbevent_utcstart.patch', level=1)


    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--force')

    def configure_args(self):
        args = []
        if 'fftw' in self.spec:
            args.append('--with-fftw3-dir=%s' % self.spec['fftw'].prefix)
        if 'gsl' in self.spec:
            args.append('--with-gsl-dir=%s' % self.spec['gsl'].prefix)
        if 'cuda' in self.spec:
            args.append('--with-cuda-dir=%s' % self.spec['cuda'].prefix)
        if 'hwloc' in self.spec:
            args.append('--with-hwloc-dir=%s' % self.spec['hwloc'].prefix)
        if '+shared' in self.spec:
            args.append('--enable-shared')
        return args
