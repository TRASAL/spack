from spack import *
import os


class RingbufferSc4(CMakePackage):
    homepage = "https://github.com/AA-ALERT/ringbuffer-sc4"
    url = "https://github.com/AA-ALERT/ringbuffer-sc4"

    version('2018-06-13',
            git='https://github.com/AA-ALERT/ringbuffer-sc4',
            commit='a7e6fcf0d3dd0ef23240789d7203415a58129612')

    depends_on('cuda')
    depends_on('psrdada')

