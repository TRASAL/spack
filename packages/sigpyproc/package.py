from spack import *
import os


class Sigpyproc(PythonPackage):
    homepage = "https://github.com/ewanbarr/sigpyproc"

    version('2018-05-30',
            git=homepage,
            commit='a18a1e201b69b7babb6dd95f6e994d7317b67dc5')

    depends_on('python')
    depends_on('py-setuptools')
    depends_on('py-numpy')
    depends_on('fftw@3.3:')
