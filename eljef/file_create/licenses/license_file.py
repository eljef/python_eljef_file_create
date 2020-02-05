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
# liceense_file.py : ElJef File Creation License File License Plugin
"""ElJef File Creation License File License Plugin.

ElJef file creation license file license plugin.
"""

import logging

from eljef.file_create.licenses.license import License

LOGGER = logging.getLogger()


class LicenseFile(License):
    """License File License Class."""

    def __init__(self):
        """Init."""
        super().__init__()
        self.description = 'License header prompting reader to view LICENSE file for license.'
        self.name = 'license-file'

    @staticmethod
    def header() -> str:
        """Return a license header with formatters for a file type to replace.

        Returns:
            A formattable string form of a license header.
        """
        return '''<#> Copyright (C) <YEAR> <COPYRIGHT HOLDER>. All rights reserved.
<#> Use of this source code is governed by a license
<#> that can be found in the LICENSE file.
'''
