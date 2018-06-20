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
DOXYGEN    = doxygen
RM         = rm
ECHO       = echo
MKFLAGS    = 
DEDISP_DEBUG = 0
INSTALL_DIR = {install_dir}
GCC = gcc
GXX = g++
AR = ar
NVCC = nvcc
SHELL = bash
UVCFLAGS = "-DUSE_NVTX"
"""

class Dedisp(MakefilePackage):
    homepage = "https://github.com/ewanbarr/dedisp"
    url = "https://github.com/ewanbarr/dedisp"
    # there are multiple version floating around
    #url = "https://github.com/ajameson/dedisp"

    version('2017-11-27', git=url, commit='7aa2a81d77401767e37d1084ce692e5288433f66')

    depends_on('cuda')

    def edit(self, spec, prefix):
        with open('Makefile.inc', 'w') as f:
            f.write(makefile_inc.format(install_dir=prefix, cuda_path=spec['cuda'].prefix))

    def install(self, spec, prefix):
        mkdir(prefix.include)
        mkdir(prefix.lib)
	make('install')


