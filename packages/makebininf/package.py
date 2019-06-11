from spack import *

makefile="""
ROOT_DIR = {root_dir}
CCFLAGS = -O

all: fits2bin

install: fits2bin 
\tmkdir -p $(ROOT_DIR)/bin
\tcp -p fits2bin makebininf.py $(ROOT_DIR)/bin

fits2bin: fits2bin.c
\tgcc $(CCFLAGS) -o fits2bin fits2bin.c -lcfitsio -lm

clean:
\trm -rf *.o *~ core build fits2bin
"""

class Makebininf(MakefilePackage):
    """Codes to convert Fermi LAT event data into a format for use with the PRESTO codes"""
    homepage = "https://fermi.gsfc.nasa.gov/ssc/data/analysis/user/"
    url = "https://fermi.gsfc.nasa.gov/ssc/data/analysis/user/makebininf-1.0.tgz"

    version('1.0', "ed999950b3e749c11ced074d634ddefc")

    depends_on('presto')
    depends_on('cfitsio')

    patch('fix_pyfits.patch', level=0)

    def edit(self, spec, prefix):
        with open('Makefile', 'w') as f:
            f.write(makefile.format(root_dir=prefix))

    def install(self, spec, prefix):
        make()
        make("install")
