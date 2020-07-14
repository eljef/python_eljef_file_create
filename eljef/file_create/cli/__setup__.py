# -*- coding: UTF-8 -*-
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
# __main__.py : ElJef File Create CLI Main
"""ElJef File Create CLI Main.

ElJef CLI Main file creation functionality.
"""

import logging
import os
from copy import deepcopy

from eljef.core import fops
from eljef.file_create.cli.__vars__ import CONFIG_DIR_PATH, CONFIG_FILE_PATH, DEFAULTS

LOGGER = logging.getLogger()


def setup() -> None:
    """Run the setup routine for file_create."""
    new_defaults = deepcopy(DEFAULTS)
    new_defaults['copyright_holder'] = input("What is the name of the default copyright holder? : ")

    done = False
    while not done:
        new_author = input("What is the name of the author? : ")
        new_email = input("What is the email address for this author? : ")
        if not new_author or not new_email:
            LOGGER.error("you must provide both a name and an email address for the author.")
            continue
        new_defaults['author'] = "{0!s} <{1!s}>".format(new_author, new_email)
        done = True

    os.makedirs(CONFIG_DIR_PATH, 0o700, exist_ok=True)
    fops.file_write_convert(CONFIG_FILE_PATH, fops.YAML, new_defaults)
