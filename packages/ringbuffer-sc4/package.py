from spack import *
import os


class RingbufferSc4(CMakePackage):
    homepage = "https://github.com/AA-ALERT/ringbuffer-sc4"
    url = "https://github.com/AA-ALERT/ringbuffer-sc4"

    version('2018-06-13',
            git='https://github.com/AA-ALERT/ringbuffer-sc4',
            commit='a7e6fcf0d3dd0ef23240789d7203415a58129612')

    version('2020-02-12',
            git='https://github.com/AA-ALERT/ringbuffer-sc4',
            commit='f4868da774b76f5558f5f91e852e5eab7698bc28')

    version('2020-04-28',
            git='https://github.com/AA-ALERT/ringbuffer-sc4',
            commit='d5b0299e2c874e352cad7f2bc06149e1f6ab8818')

    depends_on('cuda')
    depends_on('psrdada')
    depends_on('hwloc')
    depends_on('gsl')
    depends_on('fftw')

    patch('temp_fix_iab.patch', level=1)
