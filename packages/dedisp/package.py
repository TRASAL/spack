from spack import *

makefile_inc = """
GPU_ARCH = sm_61  # this is for geforce 1080 and higher
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
    homepage = "https://github.com/ajameson/dedisp"
    url = homepage

    version('2018-04-26', git=url, commit='8a3d017cdb97e3d4ea2a423604602e04cde03b0e')
    version('2023-01-18', git=url, commit='0f763a3bd1c726d9363c63cae855c844e9549d88')

    depends_on('cuda')

    def edit(self, spec, prefix):
        with open('Makefile.inc', 'w') as f:
            f.write(makefile_inc.format(install_dir=prefix, cuda_path=spec['cuda'].prefix))

    def install(self, spec, prefix):
        mkdir(prefix.include)
        mkdir(prefix.lib)
        make('install')


