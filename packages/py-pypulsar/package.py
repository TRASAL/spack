from spack import *
import os
from glob import glob


class PyPypulsar(PythonPackage):
    homepage =  "https://github.com/plazar/pypulsar"

    version('2018-09-25',
            git=homepage,
            commit='5dbc7eb3c13e2800dc68a764d43da219fc8bed17')

    depends_on('python')
    depends_on('py-setuptools')

    def build(self, spec, prefix):
        pass

    def install(self, spec, prefix):
        python_version = self.spec['python'].version.up_to(2)

        module_path = join_path(
            self.prefix.lib,
            'python{0}'.format(python_version),
            'site-packages',
            'pypulsar')

        mkdirp(module_path)
        mkdirp(prefix.bin)

        for i in glob("bin/*"):
            install(i, prefix.bin)

        for i in glob("*.py"):
            install(i, module_path)

        for subdir in ["formats", "lib", "utils"]:
            target = join_path(module_path, subdir)
            mkdirp(target)
            for i in glob("{}/*.py".format(subdir)):
                install(i, target)
