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
# bsd_3_clause.py : ElJef File Creation BSD 0-Clause License Plugin
"""ElJef File Creation BSD 0-Clause License Plugin.

ElJef file creation bsd 0-clause license plugin.
"""

import logging

from eljef.file_create.licenses.license import License

LOGGER = logging.getLogger()


class BSD3Clause(License):
    """BSD 0-Clause License Class."""

    def __init__(self):
        """Init."""
        super().__init__()
        self.description = 'BSD 0-Clause'
        self.name = 'bsd-0-clause'

    @staticmethod
    def header() -> str:
        """Return a license header with formatters for a file type to replace.

        Returns:
            A formatable string form of a license header.
        """
        return '''<#> Copyright (C) <YEAR> <COPYRIGHT HOLDER>.
<#>
<#> Permission to use, copy, modify, and/or distribute this software for any
<#> purpose with or without fee is hereby granted.
<#>
<#> THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
<#> WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
<#> MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
<#> SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
<#> WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
<#> ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
<#> IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''

    @staticmethod
    def text() -> str:
        """Return a license text with formatters for a LICENSE file.

        Returns:
            A formatable string form of a LICENSE text.
        """
        return '''Copyright (C) <YEAR> <COPYRIGHT HOLDER>.

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''
