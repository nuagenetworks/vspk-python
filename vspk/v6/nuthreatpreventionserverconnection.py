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



from bambou import NURESTObject


class NUThreatPreventionServerConnection(NURESTObject):
    """ Represents a ThreatPreventionServerConnection in the VSD

        Notes:
            Represents connection between VSD instance and Threat Prevention Server
    """

    __rest_name__ = "threatpreventionserverconnection"
    __resource_name__ = "threatpreventionserverconnections"

    
    ## Constants
    
    CONST_STATUS_DISCONNECTED = "DISCONNECTED"
    
    CONST_STATUS_CONNECTED = "CONNECTED"
    
    CONST_STATUS_AUTHENTICATION_FAILED = "AUTHENTICATION_FAILED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a ThreatPreventionServerConnection instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> threatpreventionserverconnection = NUThreatPreventionServerConnection(id=u'xxxx-xxx-xxx-xxx', name=u'ThreatPreventionServerConnection')
                >>> threatpreventionserverconnection = NUThreatPreventionServerConnection(data=my_dict)
        """

        super(NUThreatPreventionServerConnection, self).__init__()

        # Read/Write Attributes
        
        self._fqdn = None
        self._vsd_name = None
        self._status = None
        
        self.expose_attribute(local_name="fqdn", remote_name="FQDN", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vsd_name", remote_name="VSDName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'AUTHENTICATION_FAILED', u'CONNECTED', u'DISCONNECTED'])
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def fqdn(self):
        """ Get fqdn value.

            Notes:
                Threat Prevention Server FQDN or IP address

                
                This attribute is named `FQDN` in VSD API.
                
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, value):
        """ Set fqdn value.

            Notes:
                Threat Prevention Server FQDN or IP address

                
                This attribute is named `FQDN` in VSD API.
                
        """
        self._fqdn = value

    
    @property
    def vsd_name(self):
        """ Get vsd_name value.

            Notes:
                VSD instanace Name

                
                This attribute is named `VSDName` in VSD API.
                
        """
        return self._vsd_name

    @vsd_name.setter
    def vsd_name(self, value):
        """ Set vsd_name value.

            Notes:
                VSD instanace Name

                
                This attribute is named `VSDName` in VSD API.
                
        """
        self._vsd_name = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                VSD instance connection status with Threat Prevention Server

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                VSD instance connection status with Threat Prevention Server

                
        """
        self._status = value

    

    