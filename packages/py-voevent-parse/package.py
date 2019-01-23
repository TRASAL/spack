from spack import *


class PyVoeventParse(PythonPackage):
    """A lightweight library for parsing, manipulating, and generating VOEvent XML packets"""
    homepage = "https://voevent-parse.readthedocs.io/"
    url = "https://pypi.io/packages/source/v/voevent-parse/voevent-parse-1.0.3.tar.gz"

    version('1.0.3', "2d6cf8397fa874b3125afad387650bac")

    patch('fix_astropy_dependency.patch', level=1)

    depends_on('py-lxml', type='run')
    depends_on('py-orderedmultidict', type='run')

    # only install libs to avoid conflicts with binaries provided by other packages
    phases = ['build', 'install_lib'] 
