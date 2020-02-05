# -*- coding: UTF-8 -*-
# pylint: disable=too-few-public-methods
#
# Copyright (c) 2020, Jef Oliver
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU Lesser General Public License,
# version 2.1, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for
# more details.
#
# Authors:
# Jef Oliver <jef@eljef.me>
#
# lgplv21.py : ElJef File Creation LGPLv2.1-only License Plugin
"""ElJef File Creation LGPLv2.1-only License Plugin.

ElJef file creation lgplv2.1-only license plugin.
"""

import logging

from eljef.file_create.licenses.license import License

LOGGER = logging.getLogger()


class LicenseLGPLv21OrNewer(License):
    """LGPLv2.1-only License Class."""

    def __init__(self):
        """Init."""
        super().__init__()
        self.description = 'LGPLv2.1 or newer'
        self.name = 'lgplv21-or-newer'

    @staticmethod
    def header() -> str:
        """Return a license header with formatters for a file type to replace.

        Returns:
            A formattable string form of a license header.
        """
        return '''<#> Copyright (C) <YEAR> <COPYRIGHT HOLDER>
<#>
<#> This library is free software; you can redistribute it and/or modify it
<#> under the terms of the GNU Lesser General Public License as published by
<#> the Free Software Foundation; either version 2.1 of the License, or
<#> (at your option) any later version.
<#>
<#> This library is distributed in the hope that it will be useful, but
<#> WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
<#> or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
<#> License for more details.
<#>
<#> You should have received a copy of the GNU Lesser General Public License
<#> along with this library; if not, write to the
<#> Free Software Foundation, Inc., 59 Temple Place, Suite 330,
<#> Boston, MA 02111-1307 USA
'''
