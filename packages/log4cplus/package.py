##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
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


class Log4cplus(AutotoolsPackage):
    """log4cplus is a simple to use C++ logging API
    providing thread-safe, flexible, and arbitrarily
    granular control over log management and configuration."""

    homepage = "https://sourceforge.net/projects/log4cplus/"
    url      = "http://arts0.apertif/~arts/log4cplus.tar.gz"

    version('61', '1364f62a28600b7616a2971e79f30031', url="http://arts0.apertif/~arts/log4cplus.tar.gz")

    depends_on('m4')
    depends_on('libtool')
    depends_on('automake')
    depends_on('autoconf')
