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
# __args__.py : ElJef File Create CLI Arguments
"""ElJef File Create CLI Arguments.

ElJef CLI File Create command line arguments.
"""

CMD_LINE_ARGS = [
    {
        'short': '-a',
        'long': '--author',
        'opts': {
            'dest': 'author',
            'metavar': 'author-name-and-email',
            'help': 'Author name and email formatted as "author name <name@email.com>"'
        }
    },
    {
        'short': '-c',
        'long': '--copyright-holder',
        'opts': {
            'dest': 'copyright_holder',
            'metavar': 'copyright-holder-name',
            'help': 'Name of the copyright holder to use.'
        }
    },
    {
        'short': '-d',
        'long': '--debug',
        'opts': {
            'dest': 'debug_log',
            'action': 'store_true',
            'help': 'Enable debug output.'
        }
    },
    {
        'short': '-f',
        'long': '--file-name',
        'opts': {
            'dest': 'name',
            'metavar': 'file_name',
            'help': 'Name of file to create.'
        }
    },
    {
        'short': '',
        'long': '--description-long',
        'opts': {
            'dest': 'description_long',
            'metavar': 'long-description',
            'help': 'Long description of source code if needed.'
        }
    },
    {
        'short': '',
        'long': '--description-short',
        'opts': {
            'dest': 'description_short',
            'metavar': 'short-description',
            'help': 'Short description of source code if needed.'
        }
    },
    {
        'short': '-l',
        'long': '--license',
        'opts': {
            'dest': 'license',
            'metavar': 'license_name',
            'help': 'License to use.'
        }
    },
    {
        'short': '',
        'long': '--list-file-types',
        'opts': {
            'dest': 'list_file_types',
            'action': 'store_true',
            'help': 'Lists supported file types.'
        }
    },
    {
        'short': '',
        'long': '--list-licenses',
        'opts': {
            'dest': 'list_licenses',
            'action': 'store_true',
            'help': 'Lists supported licenes.'
        }
    },
    {
        'short': '-s',
        'long': '--setup',
        'opts': {
            'dest': 'setup',
            'action': 'store_true',
            'help': 'Set defaults to be used by file create.'
        }
    },
    {
        'short': '-t',
        'long': '--file-type',
        'opts': {
            'dest': 'file_type',
            'metavar': 'file-type',
            'help': 'Type of file to create.'
        }
    },
    {
        'short': '-v',
        'long': '--version',
        'opts': {
            'dest': 'version_out',
            'action': 'store_true',
            'help': 'Print version and exit.'
        }
    }
]
