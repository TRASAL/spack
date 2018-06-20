from spack import *


class PyKapteyn(PythonPackage):
    """
    Collection of Python modules and applications developed by the computer
    group of the Kapteyn Astronomical Institute
    """

    homepage = "https://www.astro.rug.nl/software/kapteyn/"
    url      = "https://www.astro.rug.nl/software/kapteyn/kapteyn-2.3.tar.gz"

    version('2.3', '43b26064b0af78b1cc906c5fa90fcc63')

    depends_on('py-numpy')
