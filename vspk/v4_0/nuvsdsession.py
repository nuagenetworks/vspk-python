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

from bambou import NURESTSession
from bambou.exceptions import InternalConsitencyError
from .nume import NUMe


class NUVSDSession(NURESTSession):
    """ VSD User Session

        Session can be started and stopped whenever its needed
    """

    def __init__(self, username, enterprise, api_url, password=None, certificate=None):
        """ Initializes a new sesssion

            Args:
                username (string): the username
                password (string): the password
                enterprise (string): the enterprise
                api_url (string): the url to the api

            Example:
                >>> session =  NUvsdSession(username="csproot", password="csproot", enterprise="csp", api_url="https://VSD:8443")
                >>> session.start()

        """

        if certificate is None and password is None:
            raise InternalConsitencyError('NUvsdSession needs either a password or a certificate')

        super(NUVSDSession, self).__init__(username=username, password=password, enterprise=enterprise, api_url=api_url, api_prefix="nuage/api", version=str(self.version), certificate=certificate)

    @property
    def version(self):
        """ Returns the current VSD version

        """
        return 4.0

    @property
    def me(self):
        """ Returns the root object

        """
        return self.root_object

    @classmethod
    def create_root_object(self):
        """ Returns a new instance

        """
        return NUMe()

    
    ## Custom methods
    @property
    def user(self):
        return self.root_object
    