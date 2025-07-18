from spack import *


class PyKapteyn(PythonPackage):
    """
    Collection of Python modules and applications developed by the computer
    group of the Kapteyn Astronomical Institute
    """

    homepage = "https://www.astro.rug.nl/software/kapteyn/"
    url      = "https://www.astro.rug.nl/software/kapteyn/kapteyn-3.4.tar.gz"

    version('3.4', 'ad7c1daf5761adc431edf806423d1417')

    depends_on('py-numpy')
    depends_on('py-setuptools')
    depends_on('py-cython', type='build')
