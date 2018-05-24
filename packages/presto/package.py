from spack import *


class Presto(MakefilePackage):
    """Open source pulsar search and analysis toolkit """

    homepage = "http://www.cv.nrao.edu/~sransom/presto/"
    url      = "https://github.com/scottransom/presto/archive/v2.1.tar.gz"

    version('2.1', '36b8007b0e8513371a1e886bf79f309c')

    depends_on('python')

    build_directory = "src"

    def install(self, spec, prefix):
        env['PRESTO'] = "."
        make()
        make('install')
