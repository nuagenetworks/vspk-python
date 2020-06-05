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


class NUThreatPreventionInfo(NURESTObject):
    """ Represents a ThreatPreventionInfo in the VSD

        Notes:
            Represents information about Threat Prevention service/instance on NSG. This is read only entity.
    """

    __rest_name__ = "threatpreventioninfo"
    __resource_name__ = "threatpreventioninfos"

    
    ## Constants
    
    CONST_CONFIGURATION_STATUS_REGISTRATION_FAILED = "REGISTRATION_FAILED"
    
    CONST_SERVICE_STATUS_SHUTOFF = "SHUTOFF"
    
    CONST_CONFIGURATION_STATUS_CONFIG_FAILED = "CONFIG_FAILED"
    
    CONST_SERVICE_STATUS_RUNNING = "RUNNING"
    
    CONST_SERVICE_STATUS_IDLE = "IDLE"
    
    CONST_MANAGEMENT_SERVER_CONNECTION_STATUS_NOT_APPLICABLE = "NOT_APPLICABLE"
    
    CONST_SERVICE_STATUS_DYING = "DYING"
    
    CONST_SERVICE_STATUS_CRASHED = "CRASHED"
    
    CONST_CONFIGURATION_STATUS_ACTIVATION_FAILED = "ACTIVATION_FAILED"
    
    CONST_CONFIGURATION_STATUS_SYNCED = "SYNCED"
    
    CONST_SERVICE_STATUS_PAUSED = "PAUSED"
    
    CONST_MANAGEMENT_SERVER_CONNECTION_STATUS_CONNECTED = "CONNECTED"
    
    CONST_SERVICE_STATUS_BLOCKED = "BLOCKED"
    
    CONST_CONFIGURATION_STATUS_NOT_APPLICABLE = "NOT_APPLICABLE"
    
    CONST_SERVICE_STATUS_SHUTDOWN = "SHUTDOWN"
    
    CONST_MANAGEMENT_SERVER_CONNECTION_STATUS_DISCONNECTED = "DISCONNECTED"
    
    CONST_SERVICE_STATUS_LAST = "LAST"
    
    CONST_SERVICE_STATUS_INIT = "INIT"
    
    CONST_SERVICE_STATUS_PMSUSPENDED = "PMSUSPENDED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a ThreatPreventionInfo instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> threatpreventioninfo = NUThreatPreventionInfo(id=u'xxxx-xxx-xxx-xxx', name=u'ThreatPreventionInfo')
                >>> threatpreventioninfo = NUThreatPreventionInfo(data=my_dict)
        """

        super(NUThreatPreventionInfo, self).__init__()

        # Read/Write Attributes
        
        self._management_server_connection_status = None
        self._service_status = None
        self._configuration_status = None
        
        self.expose_attribute(local_name="management_server_connection_status", remote_name="managementServerConnectionStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'CONNECTED', u'DISCONNECTED', u'NOT_APPLICABLE'])
        self.expose_attribute(local_name="service_status", remote_name="serviceStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'BLOCKED', u'CRASHED', u'DYING', u'IDLE', u'INIT', u'LAST', u'PAUSED', u'PMSUSPENDED', u'RUNNING', u'SHUTDOWN', u'SHUTOFF'])
        self.expose_attribute(local_name="configuration_status", remote_name="configurationStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'ACTIVATION_FAILED', u'CONFIG_FAILED', u'NOT_APPLICABLE', u'REGISTRATION_FAILED', u'SYNCED'])
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def management_server_connection_status(self):
        """ Get management_server_connection_status value.

            Notes:
                Connection status between Threat Prevention manaement Server and NSG.

                
                This attribute is named `managementServerConnectionStatus` in VSD API.
                
        """
        return self._management_server_connection_status

    @management_server_connection_status.setter
    def management_server_connection_status(self, value):
        """ Set management_server_connection_status value.

            Notes:
                Connection status between Threat Prevention manaement Server and NSG.

                
                This attribute is named `managementServerConnectionStatus` in VSD API.
                
        """
        self._management_server_connection_status = value

    
    @property
    def service_status(self):
        """ Get service_status value.

            Notes:
                Status of Threat prevention service/instance on NSG.

                
                This attribute is named `serviceStatus` in VSD API.
                
        """
        return self._service_status

    @service_status.setter
    def service_status(self, value):
        """ Set service_status value.

            Notes:
                Status of Threat prevention service/instance on NSG.

                
                This attribute is named `serviceStatus` in VSD API.
                
        """
        self._service_status = value

    
    @property
    def configuration_status(self):
        """ Get configuration_status value.

            Notes:
                VSD Configuration status for Threat Prevention service on NSG.

                
                This attribute is named `configurationStatus` in VSD API.
                
        """
        return self._configuration_status

    @configuration_status.setter
    def configuration_status(self, value):
        """ Set configuration_status value.

            Notes:
                VSD Configuration status for Threat Prevention service on NSG.

                
                This attribute is named `configurationStatus` in VSD API.
                
        """
        self._configuration_status = value

    

    