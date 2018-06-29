from spack import *


class HeimdallAstro(AutotoolsPackage):
    """GPU accelerated transient detection pipeline for radio astronomy"""

    homepage = "https://sourceforge.net/projects/heimdall-astro/"

    version('2018-05-25',
            git='https://git.code.sf.net/p/heimdall-astro/code',
            commit='a3801a37ed53f59557a1ee44cded20bf206c079b')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('cuda')
    depends_on('dedisp-flexi')
    depends_on('psrdada')
    
    def configure_args(self):
        args = []
        args.append('--with-dedisp-dir=%s' % self.spec['dedisp-flexi'].prefix)
        args.append('--with-psrdada-dir=%s' % self.spec['psrdada'].prefix)
	return args
