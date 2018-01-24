from spack import *
import os


class Pgplot(Package):
    """The PGPLOT Graphics Subroutine Library is a Fortran- or C-callable, device-independent graphics package for making simple scientific graphs."""

    homepage = "https://www.astro.caltech.edu/~tjp/pgplot"
    url      = "ftp://ftp.astro.caltech.edu/pub/pgplot/pgplot5.2.tar.gz"

    version('5.2', 'e8a6e8d0d5ef9d1709dfb567724525ae')

    parallel = False

    depends_on('zlib')
    depends_on('libpng')
    depends_on('libx11')

    patch('arts.patch')

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PGPLOT_DIR', self.prefix)

    def install(self, spec, prefix):
        env['PGPLOT_LIB'] = "-L"+prefix.lib+" -lpgplot"
        env['CPGPLOT_LIB'] = "-L"+prefix.lib+" -lcpgplot -lpgplot"
        env['XINCL'] = "-I"+spec['libx11'].prefix.include
        env['LIBS'] = "-L"+spec['libx11'].prefix.lib+" -lX11"
        install('drivers.list', prefix)
        src = os.getcwd()
        makemake = which(src + "/makemake")
        os.chdir(prefix)
        makemake(src,"linux","gfortran_gcc")
        make()
        make('cpg')
        os.mkdir('bin', 0755)
        install('pgxwin_server', prefix.bin)
        install('cpgdemo', prefix.bin)
        install('pgbind', prefix.bin)
        install('pgdemo1', prefix.bin)
        install('pgdemo2', prefix.bin)
        install('pgdemo3', prefix.bin)
        install('pgdemo4', prefix.bin)
        install('pgdemo5', prefix.bin)
        install('pgdemo6', prefix.bin)
        install('pgdemo7', prefix.bin)
        install('pgdemo8', prefix.bin)
        install('pgdemo9', prefix.bin)
        install('pgdemo10', prefix.bin)
        install('pgdemo11', prefix.bin)
        install('pgdemo12', prefix.bin)
        install('pgdemo13', prefix.bin)
        install('pgdemo14', prefix.bin)
        install('pgdemo15', prefix.bin)
        install('pgdemo16', prefix.bin)
        install('pgdemo17', prefix.bin)
