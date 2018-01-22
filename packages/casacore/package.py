from spack import *


class Casacore(CMakePackage):
    """"""

    homepage = "https://casacore.github.io/casacore"
    url      = "https://github.com/casacore/casacore/archive/v2.4.1.tar.gz"

    version('2.4.1', '88fdbdadbc1320290c36f1605d3bd9e7')
    version('2.4.0', '0f80406b6b2e0a4314866641868184d9')
    version('2.3.0', '8bc047a9fc1d6e28a86a577637000e7a')
    version('2.2.0', '2f89a83171209d0eda7e5433ccd50950')
    version('2.1.0', 'c2a75ed6b664695a3d5f53728e7bd57e')
    version('2.0.3', '32d0a4cd35e8c684e92db1195e8199f7')
    version('2.0.1', '60e36b541dd436b4c1efdb160b11ce96')
    version('2.0.0', '83fb7e779b873ffb312748dd8b1939f4')

    depends_on('flex@2.6.3')
    depends_on('bison')
    depends_on('openblas')
    depends_on('cfitsio')
    depends_on('wcslib')
    depends_on('fftw')
    depends_on('ncurses')
    depends_on('py-numpy')
    depends_on('boost +python')
    depends_on('mpi')
    depends_on('hdf5', when='+hdf5')

    variant('hdf5',values=bool,default=False,description='Enable hdf5 support')

    def cmake_args(self):
        spec = self.spec
        args = ['-DUSE_OPENMP=ON','-DBUILD_PYTHON=ON','-DUSE_THREADS=ON']

        if '+hdf5' in spec:
            args.append('-DUSE_HDF5=ON')
            args.append('-DHDF5_LIBRARIES=%s/lib' % self.spec['hdf5'].prefix)
            args.append('-DHDF5_INCLUDE_DIRS=%s/include' % self.spec['hdf5'].prefix)

        return args
