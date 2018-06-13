from spack import *
import os


class Dadafits(CMakePackage):
    homepage = "https://github.com/AA-ALERT/dadafits"

    # todo: switch to upstream when PR gets merged
    # https://github.com/AA-ALERT/dadafits/pull/3

    version('2018-06-13',
            git='https://github.com/gijzelaerr/dadafits',
            commit='4026498a721f691597b9198942088d8085622feb')

    depends_on('cuda')
    depends_on('psrdada')
    depends_on('cfitsio')

