from spack import *
import os


class Dadafilterbank(CMakePackage):
    homepage = "https://github.com/AA-ALERT/dadafilterbank"

    version('2016-12-15', git='https://github.com/gijzelaerr/dadafilterbank', commit='5f79b7b9b3f0eeb5220cf487d81d4e8d1ba35e67')

    depends_on('cuda')
    depends_on('psrdada')

