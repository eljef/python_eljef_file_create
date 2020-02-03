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
# golang.py : ElJef File Creation Golang File Plugin
"""ElJef File Creation Golang File Plugin

ElJef file creation golang file plugin.
"""

import logging

from eljef.file_create.files.file import (File, NewFile)

LOGGER = logging.getLogger()


class GolangFile(File):
    """Golang File Plugin Class

    Args:
        data: Data to be used to create the new file
        license: License object
    """
    def __init__(self, data: dict, license_obj: object) -> None:
        super().__init__(data, license_obj)
        self.comment_character = '//'
        self.name = 'golang'

    def header(self) -> str:
        """Returns a string to be added to the header of a file _BEFORE_ the license text

        Returns:
            A formatable string
        """
        return ''

    def metadata(self) -> str:
        """Returns author and comment metadata to be written.

        Returns:
            A formatable string
        """
        return '''
package <DIR_NAME>

'''


class NewGolangFile(NewFile):
    """New GolangFile Plugin Class"""
    def __init__(self) -> None:
        super().__init__()
        self.name = 'golang'

    @staticmethod
    def new(data: dict, license_obj: object) -> object:
        """New returns the actual GolangFile plugin, initialized

        Args:
            data: Data to be used to create the new file
            license: License object
        """
        return GolangFile(data, license_obj)
