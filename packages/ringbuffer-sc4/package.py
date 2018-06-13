from spack import *
import os


class RingbufferSc4(CMakePackage):
    homepage = "https://github.com/AA-ALERT/ringbuffer-sc4"
    url = "https://github.com/AA-ALERT/ringbuffer-sc4"

    version('2018-06-13',
            git='https://github.com/AA-ALERT/ringbuffer-sc4',
            commit='2a02ac2fb7d944fb81ecb6971fc1cd54811109ea')

    depends_on('cuda')
    depends_on('psrdada')

