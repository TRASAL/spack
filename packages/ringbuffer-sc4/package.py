from spack import *
import os


class RingbufferSC4(CMakePackage):
    homepage = "https://github.com/AA-ALERT/ringbuffer-sc4"
    url = "https://github.com/AA-ALERT/ringbuffer-sc4"

    version('2016-12-15', git='https://github.com/gijzelaerr/ringbuffer-sc4',
            commit='e77ee0671ef319665f98cd2659f91e2d1da0d363')

    depends_on('cuda')
    depends_on('psrdada')

