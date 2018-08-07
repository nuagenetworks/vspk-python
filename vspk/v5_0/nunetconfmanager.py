# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc, 2017 Nokia
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




from .fetchers import NUNetconfSessionsFetcher

from bambou import NURESTObject


class NUNetconfManager(NURESTObject):
    """ Represents a NetconfManager in the VSD

        Notes:
            Identifies Netconf Manager communicating with VSD, This can only be created by netconfmgr user
    """

    __rest_name__ = "netconfmanager"
    __resource_name__ = "netconfmanagers"

    
    ## Constants
    
    CONST_STATUS_JMS_DISCONNECTED = "JMS_DISCONNECTED"
    
    CONST_STATUS_DISCONNECTED = "DISCONNECTED"
    
    CONST_STATUS_CONNECTED = "CONNECTED"
    
    CONST_STATUS_INIT = "INIT"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NetconfManager instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> netconfmanager = NUNetconfManager(id=u'xxxx-xxx-xxx-xxx', name=u'NetconfManager')
                >>> netconfmanager = NUNetconfManager(data=my_dict)
        """

        super(NUNetconfManager, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._release = None
        self._status = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="release", remote_name="release", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'CONNECTED', u'DISCONNECTED', u'INIT', u'JMS_DISCONNECTED'])
        

        # Fetchers
        
        
        self.netconf_sessions = NUNetconfSessionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                A unique name of the Netconf Manager entity.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                A unique name of the Netconf Manager entity.

                
        """
        self._name = value

    
    @property
    def release(self):
        """ Get release value.

            Notes:
                Netconf Manager RPM release version

                
        """
        return self._release

    @release.setter
    def release(self, value):
        """ Set release value.

            Notes:
                Netconf Manager RPM release version

                
        """
        self._release = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                VSD connection status with this Netconf Manager

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                VSD connection status with this Netconf Manager

                
        """
        self._status = value

    

    