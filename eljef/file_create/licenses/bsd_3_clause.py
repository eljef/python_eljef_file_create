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
# bsd_3_clause.py : ElJef File Creation BSD 3-Clause License Plugin
"""ElJef File Creation BSD 3-Clause License Plugin.

ElJef file creation bsd 3-clause license plugin.
"""

import logging

from eljef.file_create.licenses.license import License

LOGGER = logging.getLogger()


class BSD3Clause(License):
    """BSD 3-Clause License Class."""

    def __init__(self):
        """Init."""
        super().__init__()
        self.description = 'BSD 3-Clause'
        self.name = 'bsd-3-clause'

    @staticmethod
    def header() -> str:
        """Return a license header with formatters for a file type to replace.

        Returns:
            A formatable string form of a license header.
        """
        return '''<#> Copyright (C) <YEAR> <COPYRIGHT HOLDER>. All rights reserved.
<#>
<#> Redistribution and use in source and binary forms, with or without
<#> modification, are permitted provided that the following conditions are met:
<#>
<#> 1. Redistributions of source code must retain the above copyright notice,
<#>    this list of conditions and the following disclaimer.
<#> 2. Redistributions in binary form must reproduce the above copyright
<#>    notice, this list of conditions and the following disclaimer in the
<#>    documentation and/or other materials provided with the distribution.
<#> 3. Neither the name of the copyright holder nor the names of its
<#>    contributors may be used to endorse or promote products derived from
<#>    this software without specific prior written permission.
<#>
<#> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
<#> AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
<#> IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
<#> ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
<#> LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
<#> CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
<#> SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
<#> INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
<#> CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
<#> ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
<#> POSSIBILITY OF SUCH DAMAGE.
'''

    @staticmethod
    def text() -> str:
        """Return a license text with formatters for a LICENSE file.

        Returns:
            A formatable string form of a LICENSE text.
        """
        return '''Copyright (C) <YEAR> <COPYRIGHT HOLDER>. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
