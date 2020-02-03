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
# license.py : ElJef File Creation Base License Plugin
"""ElJef File Creation Base License Plugin

ElJef file creation base license plugin.
"""

import logging

LOGGER = logging.getLogger()


class License:
    """Base License Class that all license plugins must inherit"""
    def __init__(self):
        self.description = ''
        self.name = ''

    @staticmethod
    def header() -> str:
        """Returns a license header with formatters for a file type to replace.

        Returns:
            A formattable string form of a license header.
        """
        raise NotImplementedError
