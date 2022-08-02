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


class NUDdnsconfigbinding(NURESTObject):
    """ Represents a Ddnsconfigbinding in the VSD

        Notes:
            Dynamic DNS Uplink Binding will allow the user to bridge or bind the NSG or an uplink on the NSG and the DDNSConfiguration object.
    """

    __rest_name__ = "ddnsconfigbinding"
    __resource_name__ = "ddnsconfigbindings"

    

    def __init__(self, **kwargs):
        """ Initializes a Ddnsconfigbinding instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ddnsconfigbinding = NUDdnsconfigbinding(id=u'xxxx-xxx-xxx-xxx', name=u'Ddnsconfigbinding')
                >>> ddnsconfigbinding = NUDdnsconfigbinding(data=my_dict)
        """

        super(NUDdnsconfigbinding, self).__init__()

        # Read/Write Attributes
        
        self._uplink_name = None
        self._uplink_priority = None
        self._assoc_ddns_config_id = None
        self._associated_uplink_id = None
        
        self.expose_attribute(local_name="uplink_name", remote_name="uplinkName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="uplink_priority", remote_name="uplinkPriority", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="assoc_ddns_config_id", remote_name="assocDDNSConfigId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_uplink_id", remote_name="associatedUplinkID", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def uplink_name(self):
        """ Get uplink_name value.

            Notes:
                The name of the associated NSG Uplink to the parent DDNS Configuration

                
                This attribute is named `uplinkName` in VSD API.
                
        """
        return self._uplink_name

    @uplink_name.setter
    def uplink_name(self, value):
        """ Set uplink_name value.

            Notes:
                The name of the associated NSG Uplink to the parent DDNS Configuration

                
                This attribute is named `uplinkName` in VSD API.
                
        """
        self._uplink_name = value

    
    @property
    def uplink_priority(self):
        """ Get uplink_priority value.

            Notes:
                The priority of the associated uplink to the DDNS config

                
                This attribute is named `uplinkPriority` in VSD API.
                
        """
        return self._uplink_priority

    @uplink_priority.setter
    def uplink_priority(self, value):
        """ Set uplink_priority value.

            Notes:
                The priority of the associated uplink to the DDNS config

                
                This attribute is named `uplinkPriority` in VSD API.
                
        """
        self._uplink_priority = value

    
    @property
    def assoc_ddns_config_id(self):
        """ Get assoc_ddns_config_id value.

            Notes:
                The associated DDNS Configuration UUID to the Dynamic DNS Config Binding

                
                This attribute is named `assocDDNSConfigId` in VSD API.
                
        """
        return self._assoc_ddns_config_id

    @assoc_ddns_config_id.setter
    def assoc_ddns_config_id(self, value):
        """ Set assoc_ddns_config_id value.

            Notes:
                The associated DDNS Configuration UUID to the Dynamic DNS Config Binding

                
                This attribute is named `assocDDNSConfigId` in VSD API.
                
        """
        self._assoc_ddns_config_id = value

    
    @property
    def associated_uplink_id(self):
        """ Get associated_uplink_id value.

            Notes:
                UUID of the associated NSG Uplink to the parent DDNS Configuration 

                
                This attribute is named `associatedUplinkID` in VSD API.
                
        """
        return self._associated_uplink_id

    @associated_uplink_id.setter
    def associated_uplink_id(self, value):
        """ Set associated_uplink_id value.

            Notes:
                UUID of the associated NSG Uplink to the parent DDNS Configuration 

                
                This attribute is named `associatedUplinkID` in VSD API.
                
        """
        self._associated_uplink_id = value

    

    