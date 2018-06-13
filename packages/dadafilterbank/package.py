from spack import *
import os


class Dadafilterbank(CMakePackage):
    homepage = "https://github.com/AA-ALERT/dadafilterbank"

    version('2018-06-11',
            git='https://github.com/gijzelaerr/dadafilterbank',
            commit='5acbe65159ca6dd8d3525fa31d8714815f79af6d')

    depends_on('cuda')
    depends_on('psrdada')

