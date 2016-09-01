# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from .nuvsdsession import NUVSDSession
from .nume import NUMe

class SDKInfo (object):

    @classmethod
    def api_version(cls):
        """
            Returns the api version
        """
        return 4.0

    @classmethod
    def api_prefix(cls):
        """
            Returns the api prefix
        """
        return "nuage/api"

    @classmethod
    def product_accronym(cls):
        """
            Returns the product accronym
        """
        return "VSD"

    @classmethod
    def product_name(cls):
        """
            Returns the product name
        """
        return "VSD"

    @classmethod
    def class_prefix(cls):
        """
            Returns the api prefix
        """
        return "NU"

    @classmethod
    def name(cls):
        """
            Returns the sdk name
        """
        return "vspk"

    @classmethod
    def root_object_class(cls):
        """
            Returns the root object class
        """
        return NUMe

    @classmethod
    def session_class(cls):
        """
            Returns the session object class
        """
        return NUVSDSession