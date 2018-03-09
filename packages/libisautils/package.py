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


class Libisautils(CMakePackage):
    """Simple C++ library containing generic utilities."""

    homepage = "https://github.com/isazi/utils"
    url="https://github.com/isazi/utils/archive/0.1.2.tar.gz"

    version("master", git="https://github.com/isazi/utils.git", branch="master")
    version("development", git="https://github.com/isazi/utils.git", branch="development")
    version("0.1.2", "3e5203958bef19e7914c67384c2c6f5c", url="https://github.com/isazi/utils/archive/0.1.2.tar.gz")
    
    depends_on("cmake@3.10:")
    depends_on("googletest")
