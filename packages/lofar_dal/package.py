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

class LofarDal(CMakePackage):
    homepage = "https://github.com/nextgen-astrodata/DAL"
    url = homepage

    version('2016-06-18', git=url, commit='45c3cbf0cc39f98a0341b3bc734743066a093adf')

    depends_on('hdf5')
    depends_on('python@2.7:')
    depends_on('py-numpy')
    depends_on('swig')


