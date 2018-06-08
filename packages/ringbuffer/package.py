from spack import *
import os


class Ringbuffer(CMakePackage):
    """Tempo is a pulsar timing data analysis package."""

    homepage = "https://github.com/AA-ALERT/ringbuffer"
    url = "https://github.com/AA-ALERT/ringbuffer"

    version('2016-12-15', git='https://github.com/gijzelaerr/ringbuffer', commit='5f79b7b9b3f0eeb5220cf487d81d4e8d1ba35e67')

    depends_on('cuda')
    depends_on('psrdada')

