from spack import *


class Castxml(CMakePackage):
    """C-family Abstract Syntax Tree XML Output """

    homepage = "https://github.com/CastXML/CastXML"
    url      = "https://github.com/CastXML/CastXML/archive/v0.2.0.tar.gz"

    version('0.2.0', sha256='626c395d0d3c777b5a1582cdfc4d33d142acfb12204ebe251535209126705ec1')

    depends_on('llvm')
