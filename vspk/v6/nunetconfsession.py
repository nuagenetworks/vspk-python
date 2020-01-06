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




from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUNetconfSession(NURESTObject):
    """ Represents a NetconfSession in the VSD

        Notes:
            Represents session between gateway and Netconf Manager, This can only be created by netconfmgr user
    """

    __rest_name__ = "netconfsession"
    __resource_name__ = "netconfsessions"

    
    ## Constants
    
    CONST_STATUS_CONNECTED = "CONNECTED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_GATEWAY_VENDOR_NOKIA = "NOKIA"
    
    CONST_GATEWAY_VENDOR_CISCO = "CISCO"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_STATUS_DISCONNECTED = "DISCONNECTED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NetconfSession instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> netconfsession = NUNetconfSession(id=u'xxxx-xxx-xxx-xxx', name=u'NetconfSession')
                >>> netconfsession = NUNetconfSession(data=my_dict)
        """

        super(NUNetconfSession, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._gateway_model = None
        self._gateway_vendor = None
        self._gateway_version = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._associated_gateway_id = None
        self._associated_gateway_name = None
        self._status = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_model", remote_name="gatewayModel", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_vendor", remote_name="gatewayVendor", attribute_type=str, is_required=False, is_unique=False, choices=[u'CISCO', u'NOKIA'])
        self.expose_attribute(local_name="gateway_version", remote_name="gatewayVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_gateway_id", remote_name="associatedGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_gateway_name", remote_name="associatedGatewayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'CONNECTED', u'DISCONNECTED'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def gateway_model(self):
        """ Get gateway_model value.

            Notes:
                The model string of the gateway to which this session connected from Netconf Manager

                
                This attribute is named `gatewayModel` in VSD API.
                
        """
        return self._gateway_model

    @gateway_model.setter
    def gateway_model(self, value):
        """ Set gateway_model value.

            Notes:
                The model string of the gateway to which this session connected from Netconf Manager

                
                This attribute is named `gatewayModel` in VSD API.
                
        """
        self._gateway_model = value

    
    @property
    def gateway_vendor(self):
        """ Get gateway_vendor value.

            Notes:
                Vendor of the gateway to which this session connected from Netconf Manager

                
                This attribute is named `gatewayVendor` in VSD API.
                
        """
        return self._gateway_vendor

    @gateway_vendor.setter
    def gateway_vendor(self, value):
        """ Set gateway_vendor value.

            Notes:
                Vendor of the gateway to which this session connected from Netconf Manager

                
                This attribute is named `gatewayVendor` in VSD API.
                
        """
        self._gateway_vendor = value

    
    @property
    def gateway_version(self):
        """ Get gateway_version value.

            Notes:
                Boot image version of gateway to which this session connected from Netconf Manager

                
                This attribute is named `gatewayVersion` in VSD API.
                
        """
        return self._gateway_version

    @gateway_version.setter
    def gateway_version(self, value):
        """ Set gateway_version value.

            Notes:
                Boot image version of gateway to which this session connected from Netconf Manager

                
                This attribute is named `gatewayVersion` in VSD API.
                
        """
        self._gateway_version = value

    
    @property
    def embedded_metadata(self):
        """ Get embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        return self._embedded_metadata

    @embedded_metadata.setter
    def embedded_metadata(self, value):
        """ Set embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        self._embedded_metadata = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def associated_gateway_id(self):
        """ Get associated_gateway_id value.

            Notes:
                UUID of the gateway associated to this Netconf session.

                
                This attribute is named `associatedGatewayID` in VSD API.
                
        """
        return self._associated_gateway_id

    @associated_gateway_id.setter
    def associated_gateway_id(self, value):
        """ Set associated_gateway_id value.

            Notes:
                UUID of the gateway associated to this Netconf session.

                
                This attribute is named `associatedGatewayID` in VSD API.
                
        """
        self._associated_gateway_id = value

    
    @property
    def associated_gateway_name(self):
        """ Get associated_gateway_name value.

            Notes:
                Name of the gateway associated to this Netconf session.

                
                This attribute is named `associatedGatewayName` in VSD API.
                
        """
        return self._associated_gateway_name

    @associated_gateway_name.setter
    def associated_gateway_name(self, value):
        """ Set associated_gateway_name value.

            Notes:
                Name of the gateway associated to this Netconf session.

                
                This attribute is named `associatedGatewayName` in VSD API.
                
        """
        self._associated_gateway_name = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                The status of the NetConf session to a gateway.

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                The status of the NetConf session to a gateway.

                
        """
        self._status = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    

    