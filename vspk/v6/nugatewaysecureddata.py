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




from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUGatewaySecuredData(NURESTObject):
    """ Represents a GatewaySecuredData in the VSD

        Notes:
            This object represents the secured data object under the gateway
    """

    __rest_name__ = "gatewaysecureddata"
    __resource_name__ = "gatewaysecureddatas"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a GatewaySecuredData instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> gatewaysecureddata = NUGatewaySecuredData(id=u'xxxx-xxx-xxx-xxx', name=u'GatewaySecuredData')
                >>> gatewaysecureddata = NUGatewaySecuredData(data=my_dict)
        """

        super(NUGatewaySecuredData, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._data = None
        self._gateway_cert_serial_number = None
        self._keyserver_cert_serial_number = None
        self._signed_data = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._associated_enterprise_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="data", remote_name="data", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_cert_serial_number", remote_name="gatewayCertSerialNumber", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="keyserver_cert_serial_number", remote_name="keyserverCertSerialNumber", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="signed_data", remote_name="signedData", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_enterprise_id", remote_name="associatedEnterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
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
    def data(self):
        """ Get data value.

            Notes:
                Encrypted data

                
        """
        return self._data

    @data.setter
    def data(self, value):
        """ Set data value.

            Notes:
                Encrypted data

                
        """
        self._data = value

    
    @property
    def gateway_cert_serial_number(self):
        """ Get gateway_cert_serial_number value.

            Notes:
                Serial Number of the certificate of the public key that encrypted this data

                
                This attribute is named `gatewayCertSerialNumber` in VSD API.
                
        """
        return self._gateway_cert_serial_number

    @gateway_cert_serial_number.setter
    def gateway_cert_serial_number(self, value):
        """ Set gateway_cert_serial_number value.

            Notes:
                Serial Number of the certificate of the public key that encrypted this data

                
                This attribute is named `gatewayCertSerialNumber` in VSD API.
                
        """
        self._gateway_cert_serial_number = value

    
    @property
    def keyserver_cert_serial_number(self):
        """ Get keyserver_cert_serial_number value.

            Notes:
                Serial Number of the certificate needed to verify the encrypted data

                
                This attribute is named `keyserverCertSerialNumber` in VSD API.
                
        """
        return self._keyserver_cert_serial_number

    @keyserver_cert_serial_number.setter
    def keyserver_cert_serial_number(self, value):
        """ Set keyserver_cert_serial_number value.

            Notes:
                Serial Number of the certificate needed to verify the encrypted data

                
                This attribute is named `keyserverCertSerialNumber` in VSD API.
                
        """
        self._keyserver_cert_serial_number = value

    
    @property
    def signed_data(self):
        """ Get signed_data value.

            Notes:
                Private key signed data.

                
                This attribute is named `signedData` in VSD API.
                
        """
        return self._signed_data

    @signed_data.setter
    def signed_data(self, value):
        """ Set signed_data value.

            Notes:
                Private key signed data.

                
                This attribute is named `signedData` in VSD API.
                
        """
        self._signed_data = value

    
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
    def associated_enterprise_id(self):
        """ Get associated_enterprise_id value.

            Notes:
                Identification of the Enterprise instance to which the Gateway Secure Data is related.

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        return self._associated_enterprise_id

    @associated_enterprise_id.setter
    def associated_enterprise_id(self, value):
        """ Set associated_enterprise_id value.

            Notes:
                Identification of the Enterprise instance to which the Gateway Secure Data is related.

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        self._associated_enterprise_id = value

    
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

    

    