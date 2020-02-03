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
"""ElJef File Create CLI Main

ElJef CLI Main file createion functionality.
"""

import logging
import argparse


from eljef.core import fops
from eljef.core.applog import setup_app_logging
from eljef.core.dictobj import DictObj
from eljef.core.merge import merge_dictionaries
from eljef.file_create.cli.__args__ import CMD_LINE_ARGS
from eljef.file_create.cli.__setup__ import setup
from eljef.file_create.cli.__vars__ import (CONFIG_FILE_PATH, DEFAULTS, PROJECT_DESCRIPTION, PROJECT_NAME,
                                            PROJECT_VERSION)
from eljef.file_create.operations import load_files_and_licenses

_DEBUG = False

LOGGER = logging.getLogger()


def do_args() -> argparse.Namespace:
    """Returns command line arguments

    Returns;
        A tuple with the argument parser and parsed namespace
    """
    parser = argparse.ArgumentParser(description=PROJECT_DESCRIPTION)
    for arg_dict in CMD_LINE_ARGS:
        short_arg = arg_dict.get('short')
        if short_arg:
            parser.add_argument(short_arg, arg_dict.get('long'), **arg_dict.get('opts', dict()))
        else:
            parser.add_argument(arg_dict.get('long'), **arg_dict.get('opts', dict()))

    args = parser.parse_args()

    return args


def do_print_file_types(files: DictObj) -> None:
    """Prints the file types supported by file_create

    Args:
        files: The files DictObj returned from load_files_and_licenses
    """
    LOGGER.info('\nSupported File Types:')
    for key in files.keys():
        LOGGER.info("\t%s", key)
    raise SystemExit(0)


def do_print_license_types(licenses: DictObj) -> None:
    """Prints the license types supported by file_create

    Args:
        licenses: The licenses DictOjb returned from load_files_and_licenses
    """
    LOGGER.info('\nSupported License Types:')
    for key, value in licenses.items():
        LOGGER.info('\t%s: %s', key, value().description)
    raise SystemExit(0)


def do_setup() -> None:
    """Runs setup"""
    setup()
    LOGGER.info('defaults saved')
    raise SystemExit(0)


def do_version() -> None:
    """Prints the program version and exists."""
    LOGGER.info("%s - %s", PROJECT_NAME, PROJECT_VERSION)
    raise SystemExit(0)


def verify_config(config: dict, args: argparse.Namespace) -> dict:
    """Verifies needed configuration values are present.

    Args:
        config: dictionary of default configuration values
        args: command line args namespace

    Returns:
        A dictionary of values to be used for operations.
    """
    if args.author:
        config['author'] = args.author
    if args.copyright_holder:
        config['copyright_holder'] = args.copyright_holder

    config['file_type'] = args.file_type
    config['license'] = args.license
    config['name'] = args.name

    for key in config.keys():
        if not config.get(key, ''):
            LOGGER.error("%s not preset. try --help", key.replace('_', '-', -1))
            raise SystemExit(-1)

    config['description_long'] = args.description_long
    config['description_short'] = args.description_short

    return config


def run() -> None:
    """Runs functionality"""
    # pylint: disable=global-statement
    global _DEBUG

    args = do_args()

    if args.version_out:
        do_version()

    _DEBUG = args.debug_log
    setup_app_logging(args.debug_log)

    if args.setup:
        do_setup()

    files, licenses = load_files_and_licenses()

    if args.list_file_types:
        do_print_file_types(files)

    if args.list_licenses:
        do_print_license_types(licenses)

    config = merge_dictionaries(DEFAULTS, fops.file_read_convert(CONFIG_FILE_PATH, fops.YAML, True))
    config = verify_config(config, args)

    if not files.get(config.get('file_type')):
        LOGGER.error("unsupported file type: %s", config.get('file_type'))
        raise SystemExit(-1)

    if not licenses.get(config.get('license')):
        LOGGER.error("unsupported license type: %s", config.get('license)'))
        raise SystemExit(-1)

    license_obj = licenses.get(config.get('license'))
    new_file = files.get(config.get('file_type')).new(config, license_obj)
    new_file.write()


def main() -> None:
    """Main function"""
    try:
        run()
    except KeyboardInterrupt:
        LOGGER.warning("\nkeyboard interrupt")
        raise SystemExit(-1)
    except (IOError, OSError, PermissionError) as exception_object:
        if _DEBUG:
            raise

        LOGGER.Error(exception_object)


if __name__ == '__main__':
    main()
