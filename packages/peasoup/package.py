from spack import *

makefile_inc = """
INSTALL_DIR = {install_dir}
CUDA_DIR   = {cuda_dir}
THRUST_DIR = {cuda_dir}
DEDISP_DIR = {dedisp_dir}

GCC       = gcc
GXX       = g++
AR        = ar
NVCC      = $(CUDA_DIR)/bin/nvcc
SHELL     = /bin/bash
UCFLAGS   = -DUSE_NVTX
"""

class Peasoup(MakefilePackage):
    homepage = "https://github.com/ewanbarr/peasoup"
    url = "https://github.com/ewanbarr/peasoup"
    version('2017-11-27',
            git=url,
            commit='213cc60819ed55e314a90afda0a61b84850f6b77')

    depends_on('cuda')
    depends_on('dedisp')

    def edit(self, spec, prefix):
        with open('Makefile.inc', 'w') as f:
            f.write(makefile_inc.format(install_dir=prefix,
                                         cuda_dir=spec['cuda'].prefix,
                                         dedisp_dir=spec['dedisp'].prefix))
