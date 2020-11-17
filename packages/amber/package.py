##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

from spack import *


class Amber(CMakePackage):
    """A many-core transient searching pipeline, designed mainly to search in real-time for Fast Radio Bursts."""

    homepage = "https://github.com/TRASAL/AMBER"
    url      = "https://github.com/TRASAL/AMBER/archive/2.1.tar.gz"

    version("master", git="https://github.com/TRASAL/AMBER.git", branch="master")
    version("development", git="https://github.com/TRASAL/AMBER.git", branch="development")
    version("2.1", "f67d3d27dd1b946df56f22f7f3fa200b", url="https://github.com/TRASAL/AMBER/archive/2.1.tar.gz")

    variant("lofar", default=False, description="Enable LOFAR HDF5 file format support.")
    variant("psrdada", default=False, description="Enable PSRDADA ringbuffer support.")

    depends_on("cmake@3.10:")
    depends_on("googletest")
    depends_on("cuda@9.0.176")
    depends_on("hwloc")
    depends_on("fftw")
    depends_on("gsl")
    depends_on("libisautils")
    depends_on("libisautils@development", when="@development")
    depends_on("libisaopencl")
    depends_on("libisaopencl@development", when="@development")
    depends_on("astrodata")
    depends_on("astrodata +lofar", when="+lofar")
    depends_on("astrodata +psrdada", when="+psrdada")
    depends_on("astrodata@development", when="@development")
    depends_on("dedispersion")
    depends_on("dedispersion +lofar", when="+lofar")
    depends_on("dedispersion +psrdada", when="+psrdada")
    depends_on("dedispersion@development", when="@development")
    depends_on("integration")
    depends_on("integration +lofar", when="+lofar")
    depends_on("integration +psrdada", when="+psrdada")
    depends_on("integration@development", when="@development")
    depends_on("snr")
    depends_on("snr +lofar", when="+lofar")
    depends_on("snr +psrdada", when="+psrdada")
    depends_on("snr@development", when="@development")
    depends_on("rfim")
    depends_on("rfim +lofar", when="+lofar")
    depends_on("rfim +psrdada", when="+psrdada")
    depends_on("rfim@development", when="@development")
    

    def setup_environment(self, spack_env, run_env):
        if "+lofar" in self.spec:
            spack_env.set("LOFAR", True)
        if "+psrdada" in self.spec:
            spack_env.set("PSRDADA", True)

