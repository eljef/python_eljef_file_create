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
# python.py : ElJef File Creation Python File Plugin
"""ElJef File Creation Python File Plugin.

ElJef file creation python file plugin.
"""

import logging

from eljef.file_create.files.file import (File, NewFile)

LOGGER = logging.getLogger()


class PythonFile(File):
    """Python File Plugin Class.

    Args:
        data: Data to be used to create the new file
        license: License object
    """

    def __init__(self, data: dict, license_obj: object) -> None:
        """Init."""
        super().__init__(data, license_obj)
        self.comment_character = '#'
        self.name = 'python'

    def header(self) -> str:
        """Return a string to be added to the header of a file _BEFORE_ the license text.

        Returns:
            A formatable string
        """
        return '''#!/usr/bin/env python3
<#> -*- coding: UTF-8 -*-
'''

    def metadata(self) -> str:
        """Return author and comment metadata to be written.

        Returns:
            A formatable string
        """
        ret = ''

        if self.data.get('author', ''):
            ret += '''<#>
<#> Authors:
<#> <AUTHOR>
'''

        ret += '''<#>
<#> <FILE NAME> : <SHORT DESCRIPTION>
"""<SHORT DESCRIPTION>

<LONG DESCRIPTION>
"""

import logging

LOGGER = logging.getLogger()

'''

        return ret


class NewPythonFile(NewFile):
    """New PythonFile Plugin Class."""

    def __init__(self) -> None:
        """Init."""
        super().__init__()
        self.name = 'python'

    @staticmethod
    def new(data: dict, license_obj: object) -> object:
        """Return the actual PythonFile plugin, initialized.

        Args:
            data: Data to be used to create the new file
            license: License object
        """
        return PythonFile(data, license_obj)
