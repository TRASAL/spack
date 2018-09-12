from spack import *
import os


class Sigpyproc(PythonPackage):
    homepage = "https://github.com/ewanbarr/sigpyproc"

    version('2018-05-30',
            git=homepage,
            commit='e003fdf37f2ded9d549a386d993547eca479a43e')

    depends_on('python')
    depends_on('py-setuptools')
    depends_on('py-numpy')
    depends_on('fftw@3.3:')
