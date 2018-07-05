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

    version('2018-07-05-a', git=url, commit='503808ce361abac206622c7b67d6b49b26461540')

    depends_on('hdf5 -mpi')
    depends_on('python@2.7:')
    depends_on('py-numpy')
    depends_on('swig')


