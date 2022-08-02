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




from .fetchers import NUDdnsconfigbindingsFetcher

from bambou import NURESTObject


class NUDdnsconfig(NURESTObject):
    """ Represents a Ddnsconfig in the VSD

        Notes:
            The Dynamic DNS (DDNS) Configuration holds the information used to establish the connection with the provider
    """

    __rest_name__ = "ddnsconfig"
    __resource_name__ = "ddnsconfigs"

    
    ## Constants
    
    CONST_PROVIDER_NAME_DYN_DNS = "DYN_DNS"
    
    CONST_PROVIDER_NAME_NO_IP = "NO_IP"
    
    CONST_CONNECTION_STATUS_SUCCESS = "SUCCESS"
    
    CONST_CONNECTION_STATUS_FAILED = "FAILED"
    
    CONST_CONNECTION_STATUS_UNKNOWN = "UNKNOWN"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Ddnsconfig instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ddnsconfig = NUDdnsconfig(id=u'xxxx-xxx-xxx-xxx', name=u'Ddnsconfig')
                >>> ddnsconfig = NUDdnsconfig(data=my_dict)
        """

        super(NUDdnsconfig, self).__init__()

        # Read/Write Attributes
        
        self._password = None
        self._enable_ddns_config = None
        self._connection_status = None
        self._hostname = None
        self._provider_name = None
        self._username = None
        self._assoc_gateway_id = None
        
        self.expose_attribute(local_name="password", remote_name="password", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="enable_ddns_config", remote_name="enableDDNSConfig", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="connection_status", remote_name="connectionStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'FAILED', u'SUCCESS', u'UNKNOWN'])
        self.expose_attribute(local_name="hostname", remote_name="hostname", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="provider_name", remote_name="providerName", attribute_type=str, is_required=True, is_unique=False, choices=[u'DYN_DNS', u'NO_IP'])
        self.expose_attribute(local_name="username", remote_name="username", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="assoc_gateway_id", remote_name="assocGatewayId", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.ddnsconfigbindings = NUDdnsconfigbindingsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def password(self):
        """ Get password value.

            Notes:
                Dynamic DNS provider password

                
        """
        return self._password

    @password.setter
    def password(self, value):
        """ Set password value.

            Notes:
                Dynamic DNS provider password

                
        """
        self._password = value

    
    @property
    def enable_ddns_config(self):
        """ Get enable_ddns_config value.

            Notes:
                User can enable/disable the DDNS config using this flag

                
                This attribute is named `enableDDNSConfig` in VSD API.
                
        """
        return self._enable_ddns_config

    @enable_ddns_config.setter
    def enable_ddns_config(self, value):
        """ Set enable_ddns_config value.

            Notes:
                User can enable/disable the DDNS config using this flag

                
                This attribute is named `enableDDNSConfig` in VSD API.
                
        """
        self._enable_ddns_config = value

    
    @property
    def connection_status(self):
        """ Get connection_status value.

            Notes:
                Dynamic DNS connection status represents the status of the provider connection.

                
                This attribute is named `connectionStatus` in VSD API.
                
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, value):
        """ Set connection_status value.

            Notes:
                Dynamic DNS connection status represents the status of the provider connection.

                
                This attribute is named `connectionStatus` in VSD API.
                
        """
        self._connection_status = value

    
    @property
    def hostname(self):
        """ Get hostname value.

            Notes:
                Fully Qualified Domain Name to be used for NSG Uplink

                
        """
        return self._hostname

    @hostname.setter
    def hostname(self, value):
        """ Set hostname value.

            Notes:
                Fully Qualified Domain Name to be used for NSG Uplink

                
        """
        self._hostname = value

    
    @property
    def provider_name(self):
        """ Get provider_name value.

            Notes:
                Dynamic DNS Provider Name

                
                This attribute is named `providerName` in VSD API.
                
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, value):
        """ Set provider_name value.

            Notes:
                Dynamic DNS Provider Name

                
                This attribute is named `providerName` in VSD API.
                
        """
        self._provider_name = value

    
    @property
    def username(self):
        """ Get username value.

            Notes:
                Dynamic DNS provider username

                
        """
        return self._username

    @username.setter
    def username(self, value):
        """ Set username value.

            Notes:
                Dynamic DNS provider username

                
        """
        self._username = value

    
    @property
    def assoc_gateway_id(self):
        """ Get assoc_gateway_id value.

            Notes:
                The associated parent NSGateway UUID to the Dynamic DNS Config

                
                This attribute is named `assocGatewayId` in VSD API.
                
        """
        return self._assoc_gateway_id

    @assoc_gateway_id.setter
    def assoc_gateway_id(self, value):
        """ Set assoc_gateway_id value.

            Notes:
                The associated parent NSGateway UUID to the Dynamic DNS Config

                
                This attribute is named `assocGatewayId` in VSD API.
                
        """
        self._assoc_gateway_id = value

    

    