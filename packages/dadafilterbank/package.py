from spack import *
import os


class Dadafilterbank(CMakePackage):
    homepage = "https://github.com/TRASAL/dadafilterbank"


    version('2018-06-13',
            git='https://github.com/TRASAL/dadafilterbank',
            commit='fa829f940252772c8363c5e9b5c4057daefd605f')

    version('2019-05-22',
            git='https://github.com/TRASAL/dadafilterbank',
            commit='4959bfeb15481b0d3cc768e265ab48cf9610a189')

    version('2020-02-14',
            git='https://github.com/TRASAL/dadafilterbank',
            commit='88ab35487bc9af84429e18a3a931a9a5c2bd0d39')

    version('2020-04-28',
            git='https://github.com/TRASAL/dadafilterbank',
            commit='3d2f55a0a943513f33311397e45728e18164b928')

    depends_on('cuda')
    depends_on('psrdada')

    depends_on('hwloc')
    depends_on('fftw')
    depends_on('gsl')

