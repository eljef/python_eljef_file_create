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
# file.py : ElJef File Creation Base File Plugin
"""ElJef File Creation Base File Plugin

ElJef file creation base file plugin.
"""

import logging
import datetime
import os
import pathlib

from eljef.core import fops

LOGGER = logging.getLogger()


class File:
    """Base File Plugin Class that file type plugins must inherit

    Args:
        data: Data to be used to create the new file
        license: License object
    """
    def __init__(self, data: dict, license_obj: object) -> None:
        self.comment_character = ''
        self.data = data
        self.license_obj = license_obj
        self.name = ''

    def get_dir(self) -> str:
        """Returns that last directory in the provided filename, or the last directory in CWD

        Returns
            Last directory in provided file path or last directory in CWD
        """
        path = pathlib.PurePath(os.path.abspath(self.data.get('name')))
        return path.parent.name

    def header(self) -> str:
        """Returns a string to be added to the header of a file _BEFORE_ the license text

        Returns:
            A formatable string
        """
        raise NotImplementedError

    def metadata(self) -> str:
        """Returns author and comment metadata to be written.

        Returns:
            A formatable string
        """
        raise NotImplementedError

    def write(self) -> None:
        """Writes license to new file"""
        data = self.header()
        data += self.license_obj.header()

        data_add = self.metadata()
        if data_add:
            data += data_add

        data = data.replace('<#>', self.comment_character, -1)
        data = data.replace('<AUTHOR>', self.data.get('author', ''), -1)
        data = data.replace('<COPYRIGHT HOLDER>', self.data.get('copyright_holder'), -1)
        data = data.replace('<FILE NAME>', os.path.basename(self.data.get('name')), -1)
        data = data.replace('<YEAR>', str(datetime.datetime.now().year), -1)
        data = data.replace('<DIR_NAME>', self.get_dir(), -1)
        short_desc = self.data.get('description_short')
        if short_desc:
            data = data.replace('<SHORT DESCRIPTION>', self.data.get('description_short', ''), -1)
        long_desc = self.data.get('description_long')
        if long_desc:
            data = data.replace('<LONG DESCRIPTION>', self.data.get('description_long', ''), -1)

        fops.file_write(self.data.get('name'), data)


class NewFile:
    """Base New File Plugin Class that all new file plugins must inherit"""
    def __init__(self) -> None:
        self.type = ''

    @staticmethod
    def new(data: dict, license_obj: object) -> object:
        """New returns the actual File plugin, initialized

        Args:
            data: Data to be used to create the new file
            license: License object

        Notes:
            Example:
                return File(data, license_obj)
        """
        raise NotImplementedError
