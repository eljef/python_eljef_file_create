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
# operations.py : ElJef File Create Common Operations
"""ElJef File Create Common Operations.

Operations common to all file creation functionality.
"""

import inspect
import logging
import pkgutil
from typing import Tuple

from eljef.core.dictobj import DictObj
from eljef.file_create.files.file import NewFile
from eljef.file_create.licenses.license import License

LOGGER = logging.getLogger(__name__)


def load_plugins(plugin_path: str, from_list: list, base_class: object) -> DictObj:
    """Load plugins.

    Args:
        plugin_path: Python path to the plugins directory
        from_list: same as __import__ fromlist
        base_class: Base class that plugins are inheriting from, to be used for discovery

    Returns:
        DictObj: plugin name => plugin
    """
    plugins = dict()
    imported_package = __import__(plugin_path, fromlist=from_list)
    for i in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + '.'):
        if not i.ispkg:
            plugin_module = __import__(i.name, fromlist=from_list)
            class_members = inspect.getmembers(plugin_module, inspect.isclass)
            for (_, class_member) in class_members:
                if issubclass(class_member, base_class) & (class_member is not base_class):
                    plugins[class_member().name] = class_member

    return DictObj(plugins)


def load_files_and_licenses() -> Tuple[DictObj, DictObj]:
    """Load file and license plugins.

    Returns:
        Tuple of Dictobj: plugin name -> plugins
        Order is files, licenses
    """
    files = load_plugins('eljef.file_create.files', ['plugin'], NewFile)
    licenses = load_plugins('eljef.file_create.licenses', ['plugin'], License)

    return files, licenses
