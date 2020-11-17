from spack import *
import os


class Dadafits(CMakePackage):
    homepage = "https://github.com/TRASAL/dadafits"

    version('master',
            git='https://github.com/TRASAL/dadafits',
            branch='master')

    depends_on('cuda')
    depends_on('psrdada')
    depends_on('cfitsio@3.370')
    depends_on('gsl')
    depends_on('hwloc')
    depends_on('fftw')

