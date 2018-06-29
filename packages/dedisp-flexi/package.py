from spack import *

makefile_inc = """
CUDA_PATH ?= {cuda_path}
CUDA_DIR   ?= $(CUDA_PATH)
THRUST_DIR ?= $(CUDA_DIR)/include
INSTALL_DIR ?= {install_dir}
LIB_ARCH   = lib64
GCC        = gcc
GXX        = g++
AR         = ar
NVCC       = $(CUDA_DIR)/bin/nvcc -Xptxas -abi=no
NVCC = nvcc
DOXYGEN    = doxygen
RM         = rm
ECHO       = echo
MKFLAGS    = 
DEDISP_DEBUG = 0
"""

class DedispFlexi(MakefilePackage):
    homepage = "https://github.com/ewanbarr/dedisp-flexi"
    url = "https://github.com/ewanbarr/dedisp-flexi"

    version('2017-11-27', git=url, commit='19826ae64b0d492bcac352b09b77158365aec5d7')

    depends_on('cuda')

    def edit(self, spec, prefix):
        with open('Makefile.inc', 'w') as f:
            f.write(makefile_inc.format(install_dir=prefix, cuda_path=spec['cuda'].prefix))

    def install(self, spec, prefix):
        mkdir(prefix.include)
        mkdir(prefix.lib)
	make('install')


