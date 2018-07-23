from spack import *
import os


class RingbufferSc4(CMakePackage):
    homepage = "https://github.com/AA-ALERT/ringbuffer-sc4"
    url = "https://github.com/AA-ALERT/ringbuffer-sc4"

    version('2018-06-13',
            git='https://github.com/AA-ALERT/ringbuffer-sc4',
            commit='603814db9767a663b6b6b38bcdbbb91c1f70da3a')

    depends_on('cuda')
    depends_on('psrdada')

