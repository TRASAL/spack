from spack import *
import os

cfg = """CLKDIR         {prefix}/clock/
PARDIR         {prefix}/tzpar/
TZDIR          ./
OBS_NIST       time.dat
NIST_UTC       utccorr.tot                     UTC(NIST) to UTC
NIST_BIPM12    bipmnist.12.extrap              UTC(NIST) to TT(BIPM12)
NIST_BIPM14    bipmnist.14                     UTC(NIST) to TT(BIPM14)
NIST_BIPM15    bipmnist.15.extrap              UTC(NIST) to TT(BIPM15)
NIST_BIPM2012  bipmnist.12.extrap              UTC(NIST) to TT(BIPM2012)
NIST_BIPM2014  bipmnist.14                     UTC(NIST) to TT(BIPM2014)
NIST_BIPM2015  bipmnist.15.extrap              UTC(NIST) to TT(BIPM2015)
NIST_BIPM2016  bipmnist.16.extrap              UTC(NIST) to TT(BIPM2016)
NIST_BIPM2017  bipmnist.17.extrap              UTC(NIST) to TT(BIPM2017)
NIST_BIPM      bipmnist.17.extrap              UTC(NIST) to TT(BIPM)
NIST_PTB       ptbnist.90                      UTC(NIST) to UTC(PTB)
NIST_AT1       at1nist.90                      UTC(NIST) to AT1
UT1            ut1.dat                         UT1 - UT
EPHDIR         {prefix}/ephem/
EPHFILE        DE200.1950.2050 --eph=DE200 --endian=big
EPHFILE        DE405.1950.2050 --eph=DE405 --endian=big
EPHFILE        DE418.1950.2050 --eph=DE418 --endian=big
EPHFILE        DE421.1950.2050 --eph=DE421 --endian=little
EPHFILE        DE430.1950.2050 --eph=DE430 --endian=little
EPHFILE        DE435.1950.2050 --eph=DE435 --endian=little
EPHFILE        DE436.1950.2050 --eph=DE436 --endian=little
TDBFILE        TDB.1950.2050
OBSYS          {prefix}/obsys.dat      Observatory list
TZTOT          tztot.dat
TZSITE         1
"""


class Tempo(AutotoolsPackage):
    """Tempo is a pulsar timing data analysis package."""

    homepage = "http://tempo.sourceforge.net/"
    url      = "https://git.code.sf.net/p/tempo/tempo"

    version('2018-04-24', git=url, commit='13e12c')
    version('2025-05-07', git=url, commit='aaf34c')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    patch(f'fix_path_length_2018_04_24.patch', when="@2018-04-24", level=0)
    patch(f'fix_path_length_2025_05_07.patch', when="@2025-05-07")
    patch('fix_wsrt_code_2018_04_24.patch', when="@2028-04-24", level=0)
    patch('fix_wsrt_code_2025_05_07.patch', when="@2025-05-07")

    def setup_build_environment(self, env):
        env.set('TEMPO', self.prefix + '/tempo')

    def setup_run_environment(self, env):
        env.set('TEMPO', self.prefix + '/tempo')

    def install(self, spec, prefix):
        os.mkdir('tempo', 755)
        install_tree('clock', prefix + '/tempo/clock')
        install_tree('ephem', prefix + '/tempo/ephem')
        install('obsys.dat', prefix + '/tempo')
        install('tempo.cfg', prefix + '/tempo')
        install('tempo.hlp', prefix + '/tempo')
        install_tree('tzpar', prefix + '/tempo/tzpar')
        make()
        make('install')
        with open(self.prefix + '/tempo/tempo.cfg', 'w') as f:
            f.write(cfg.format(prefix=self.prefix + '/tempo'))
