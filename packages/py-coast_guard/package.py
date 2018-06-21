from spack import *
from glob import glob


class PyCoastGuard(PythonPackage):
    """Python/PSRCHIVE-based timing pipeline for reducing Effelsberg data."""

    homepage = "https://github.com/plazar/coast_guard"
    url      = "https://github.com/plazar/coast_guard"

    version('2015-12-16',
            git=url,
            commit='201031b19994a1e087461b4bfec6fd9f437daf16')
    
    depends_on('py-scipy')
    depends_on('py-numpy')
    depends_on('py-sqlalchemy')

    # disabled since we have this problem: https://github.com/spack/spack/issues/7855
    #depends_on('py-matplotlib')

    def build(self, spec, prefix):
	pass

    def install(self, spec, prefix):
        python_version = self.spec['python'].version.up_to(2)

        module_path = join_path(
            self.prefix.lib,
            'python{0}'.format(python_version),
            'site-packages',
            'coast_guard')

        mkdirp(module_path)
        mkdirp(prefix.bin)

        for i in glob("*.sh"):
            install(i, prefix.bin)

        #for i in glob("*.py"):
        #    install(i, module_path)

        for subdir in ['.', 'cleaners', 'configurations', 'database', 'rcvr_files']:
            target = join_path(module_path, subdir)
            mkdirp(target)
            for i in glob("{}/*.py".format(subdir)):
	        install(i, target)

    
