# -*- coding: UTF-8 -*-
# Copyright (c) 22020, Jef Oliver
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
# __vars__.py : Variables used by ElJef File Create CLI
"""ElJef File Create CLI Variables.

Variables used by ElJef File Creation CLI.
"""
import logging
import os
from pathlib import Path

from eljef.file_create.__version__ import VERSION

LOGGER = logging.getLogger(__name__)

CONFIG_DIR_PATH = os.path.join(str(Path.home()), '.config', 'eljef', 'file_create')
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR_PATH, 'config.yaml')

DEFAULTS = {
    'author': '',
    'copyright_holder': '',
}

PROJECT_DESCRIPTION = 'ElJef File Creation Functionality'
PROJECT_NAME = 'eljef_file_create'
PROJECT_VERSION = VERSION
