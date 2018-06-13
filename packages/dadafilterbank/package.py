from spack import *
import os


class Dadafilterbank(CMakePackage):
    homepage = "https://github.com/AA-ALERT/dadafilterbank"


    version('2018-06-13',
            git='https://github.com/AA-ALERT/dadafilterbank',
            commit='fa829f940252772c8363c5e9b5c4057daefd605f')

    depends_on('cuda')
    depends_on('psrdada')

