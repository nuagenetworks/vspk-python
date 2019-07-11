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


class NUIKEGatewayProfile(NURESTObject):
    """ Represents a IKEGatewayProfile in the VSD

        Notes:
            Define attributes of the remote IKE gateway.
    """

    __rest_name__ = "ikegatewayprofile"
    __resource_name__ = "ikegatewayprofiles"

    
    ## Constants
    
    CONST_IKE_GATEWAY_IDENTIFIER_TYPE_ID_FQDN = "ID_FQDN"
    
    CONST_CONFIGURATION_STATUS_IN_PROGRESS = "IN_PROGRESS"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ASSOCIATED_CLOUD_TYPE_AZURECLOUD = "AZURECLOUD"
    
    CONST_IKE_GATEWAY_IDENTIFIER_TYPE_ID_IPV4_ADDR = "ID_IPV4_ADDR"
    
    CONST_SERVICE_CLASS_H = "H"
    
    CONST_CONFIGURATION_STATUS_WAITING_FOR_RESOURCES = "WAITING_FOR_RESOURCES"
    
    CONST_SERVICE_CLASS_A = "A"
    
    CONST_SERVICE_CLASS_B = "B"
    
    CONST_SERVICE_CLASS_C = "C"
    
    CONST_SERVICE_CLASS_D = "D"
    
    CONST_SERVICE_CLASS_E = "E"
    
    CONST_SERVICE_CLASS_F = "F"
    
    CONST_SERVICE_CLASS_G = "G"
    
    CONST_CONFIGURATION_STATUS_SUCCESS = "SUCCESS"
    
    CONST_IKE_GATEWAY_IDENTIFIER_TYPE_ID_KEY_ID = "ID_KEY_ID"
    
    CONST_CONFIGURATION_STATUS_UNKNOWN = "UNKNOWN"
    
    CONST_ASSOCIATED_IKE_AUTHENTICATION_TYPE_IKE_CERTIFICATE = "IKE_CERTIFICATE"
    
    CONST_CONFIGURATION_STATUS_CANCELLED = "CANCELLED"
    
    CONST_CONFIGURATION_STATUS_WAITING = "WAITING"
    
    CONST_ASSOCIATED_IKE_AUTHENTICATION_TYPE_IKE_PSK = "IKE_PSK"
    
    CONST_CONFIGURATION_STATUS_NOT_APPLICABLE = "NOT_APPLICABLE"
    
    CONST_IKE_GATEWAY_IDENTIFIER_TYPE_ID_RFC822_ADDR = "ID_RFC822_ADDR"
    
    CONST_CONFIGURATION_STATUS_SYNCED_FROM_CLOUD = "SYNCED_FROM_CLOUD"
    
    CONST_CONFIGURATION_STATUS_PAUSING = "PAUSING"
    
    CONST_CONFIGURATION_STATUS_FAILED = "FAILED"
    
    CONST_CONFIGURATION_STATUS_CLOUD_CONFIGURATION_REMOVED = "CLOUD_CONFIGURATION_REMOVED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_CONFIGURATION_STATUS_CANCELING = "CANCELING"
    
    CONST_IKE_GATEWAY_IDENTIFIER_TYPE_ID_DER_ASN1_DN = "ID_DER_ASN1_DN"
    
    CONST_SERVICE_CLASS_NONE = "NONE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a IKEGatewayProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ikegatewayprofile = NUIKEGatewayProfile(id=u'xxxx-xxx-xxx-xxx', name=u'IKEGatewayProfile')
                >>> ikegatewayprofile = NUIKEGatewayProfile(data=my_dict)
        """

        super(NUIKEGatewayProfile, self).__init__()

        # Read/Write Attributes
        
        self._ike_gateway_identifier = None
        self._ike_gateway_identifier_type = None
        self._name = None
        self._last_updated_by = None
        self._service_class = None
        self._description = None
        self._embedded_metadata = None
        self._anti_replay_check = None
        self._entity_scope = None
        self._configuration_status = None
        self._associated_cloud_id = None
        self._associated_cloud_type = None
        self._associated_enterprise_id = None
        self._associated_ike_authentication_id = None
        self._associated_ike_authentication_type = None
        self._associated_ike_encryption_profile_id = None
        self._associated_ike_gateway_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="ike_gateway_identifier", remote_name="IKEGatewayIdentifier", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ike_gateway_identifier_type", remote_name="IKEGatewayIdentifierType", attribute_type=str, is_required=False, is_unique=False, choices=[u'ID_DER_ASN1_DN', u'ID_FQDN', u'ID_IPV4_ADDR', u'ID_KEY_ID', u'ID_RFC822_ADDR'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="service_class", remote_name="serviceClass", attribute_type=str, is_required=False, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'NONE'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="anti_replay_check", remote_name="antiReplayCheck", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="configuration_status", remote_name="configurationStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'CANCELING', u'CANCELLED', u'CLOUD_CONFIGURATION_REMOVED', u'FAILED', u'IN_PROGRESS', u'NOT_APPLICABLE', u'PAUSING', u'SUCCESS', u'SYNCED_FROM_CLOUD', u'UNKNOWN', u'WAITING', u'WAITING_FOR_RESOURCES'])
        self.expose_attribute(local_name="associated_cloud_id", remote_name="associatedCloudID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_cloud_type", remote_name="associatedCloudType", attribute_type=str, is_required=False, is_unique=False, choices=[u'AZURECLOUD'])
        self.expose_attribute(local_name="associated_enterprise_id", remote_name="associatedEnterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ike_authentication_id", remote_name="associatedIKEAuthenticationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ike_authentication_type", remote_name="associatedIKEAuthenticationType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IKE_CERTIFICATE', u'IKE_PSK'])
        self.expose_attribute(local_name="associated_ike_encryption_profile_id", remote_name="associatedIKEEncryptionProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ike_gateway_id", remote_name="associatedIKEGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ike_gateway_identifier(self):
        """ Get ike_gateway_identifier value.

            Notes:
                IKE Gateway Identifier. Null to take on the default 'ipaddress'

                
                This attribute is named `IKEGatewayIdentifier` in VSD API.
                
        """
        return self._ike_gateway_identifier

    @ike_gateway_identifier.setter
    def ike_gateway_identifier(self, value):
        """ Set ike_gateway_identifier value.

            Notes:
                IKE Gateway Identifier. Null to take on the default 'ipaddress'

                
                This attribute is named `IKEGatewayIdentifier` in VSD API.
                
        """
        self._ike_gateway_identifier = value

    
    @property
    def ike_gateway_identifier_type(self):
        """ Get ike_gateway_identifier_type value.

            Notes:
                IKE Gateway Identifier Type.

                
                This attribute is named `IKEGatewayIdentifierType` in VSD API.
                
        """
        return self._ike_gateway_identifier_type

    @ike_gateway_identifier_type.setter
    def ike_gateway_identifier_type(self, value):
        """ Set ike_gateway_identifier_type value.

            Notes:
                IKE Gateway Identifier Type.

                
                This attribute is named `IKEGatewayIdentifierType` in VSD API.
                
        """
        self._ike_gateway_identifier_type = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the IKEv2 Gateway Profile

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the IKEv2 Gateway Profile

                
        """
        self._name = value

    
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
    def service_class(self):
        """ Get service_class value.

            Notes:
                Class of service to be used. Service classes in order of priority are A, B, C, D, E, F, G, and H.

                
                This attribute is named `serviceClass` in VSD API.
                
        """
        return self._service_class

    @service_class.setter
    def service_class(self, value):
        """ Set service_class value.

            Notes:
                Class of service to be used. Service classes in order of priority are A, B, C, D, E, F, G, and H.

                
                This attribute is named `serviceClass` in VSD API.
                
        """
        self._service_class = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the IKEv2 Gateway Profile

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the IKEv2 Gateway Profile

                
        """
        self._description = value

    
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
    def anti_replay_check(self):
        """ Get anti_replay_check value.

            Notes:
                Allow any local subnets to be used

                
                This attribute is named `antiReplayCheck` in VSD API.
                
        """
        return self._anti_replay_check

    @anti_replay_check.setter
    def anti_replay_check(self, value):
        """ Set anti_replay_check value.

            Notes:
                Allow any local subnets to be used

                
                This attribute is named `antiReplayCheck` in VSD API.
                
        """
        self._anti_replay_check = value

    
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
    def configuration_status(self):
        """ Get configuration_status value.

            Notes:
                Status of configuration on third-party cloud instance

                
                This attribute is named `configurationStatus` in VSD API.
                
        """
        return self._configuration_status

    @configuration_status.setter
    def configuration_status(self, value):
        """ Set configuration_status value.

            Notes:
                Status of configuration on third-party cloud instance

                
                This attribute is named `configurationStatus` in VSD API.
                
        """
        self._configuration_status = value

    
    @property
    def associated_cloud_id(self):
        """ Get associated_cloud_id value.

            Notes:
                ID of the associated third-party cloud instance

                
                This attribute is named `associatedCloudID` in VSD API.
                
        """
        return self._associated_cloud_id

    @associated_cloud_id.setter
    def associated_cloud_id(self, value):
        """ Set associated_cloud_id value.

            Notes:
                ID of the associated third-party cloud instance

                
                This attribute is named `associatedCloudID` in VSD API.
                
        """
        self._associated_cloud_id = value

    
    @property
    def associated_cloud_type(self):
        """ Get associated_cloud_type value.

            Notes:
                Type of associated third-party cloud instance, ex. AZURECLOUD

                
                This attribute is named `associatedCloudType` in VSD API.
                
        """
        return self._associated_cloud_type

    @associated_cloud_type.setter
    def associated_cloud_type(self, value):
        """ Set associated_cloud_type value.

            Notes:
                Type of associated third-party cloud instance, ex. AZURECLOUD

                
                This attribute is named `associatedCloudType` in VSD API.
                
        """
        self._associated_cloud_type = value

    
    @property
    def associated_enterprise_id(self):
        """ Get associated_enterprise_id value.

            Notes:
                The ID of the associated Enterprise

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        return self._associated_enterprise_id

    @associated_enterprise_id.setter
    def associated_enterprise_id(self, value):
        """ Set associated_enterprise_id value.

            Notes:
                The ID of the associated Enterprise

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        self._associated_enterprise_id = value

    
    @property
    def associated_ike_authentication_id(self):
        """ Get associated_ike_authentication_id value.

            Notes:
                Associated IKE Authentication ID

                
                This attribute is named `associatedIKEAuthenticationID` in VSD API.
                
        """
        return self._associated_ike_authentication_id

    @associated_ike_authentication_id.setter
    def associated_ike_authentication_id(self, value):
        """ Set associated_ike_authentication_id value.

            Notes:
                Associated IKE Authentication ID

                
                This attribute is named `associatedIKEAuthenticationID` in VSD API.
                
        """
        self._associated_ike_authentication_id = value

    
    @property
    def associated_ike_authentication_type(self):
        """ Get associated_ike_authentication_type value.

            Notes:
                Associated IKE Authentication Type

                
                This attribute is named `associatedIKEAuthenticationType` in VSD API.
                
        """
        return self._associated_ike_authentication_type

    @associated_ike_authentication_type.setter
    def associated_ike_authentication_type(self, value):
        """ Set associated_ike_authentication_type value.

            Notes:
                Associated IKE Authentication Type

                
                This attribute is named `associatedIKEAuthenticationType` in VSD API.
                
        """
        self._associated_ike_authentication_type = value

    
    @property
    def associated_ike_encryption_profile_id(self):
        """ Get associated_ike_encryption_profile_id value.

            Notes:
                The ID of the associated IKE Encryption Profile

                
                This attribute is named `associatedIKEEncryptionProfileID` in VSD API.
                
        """
        return self._associated_ike_encryption_profile_id

    @associated_ike_encryption_profile_id.setter
    def associated_ike_encryption_profile_id(self, value):
        """ Set associated_ike_encryption_profile_id value.

            Notes:
                The ID of the associated IKE Encryption Profile

                
                This attribute is named `associatedIKEEncryptionProfileID` in VSD API.
                
        """
        self._associated_ike_encryption_profile_id = value

    
    @property
    def associated_ike_gateway_id(self):
        """ Get associated_ike_gateway_id value.

            Notes:
                The IKE Gateway associated with this Profile

                
                This attribute is named `associatedIKEGatewayID` in VSD API.
                
        """
        return self._associated_ike_gateway_id

    @associated_ike_gateway_id.setter
    def associated_ike_gateway_id(self, value):
        """ Set associated_ike_gateway_id value.

            Notes:
                The IKE Gateway associated with this Profile

                
                This attribute is named `associatedIKEGatewayID` in VSD API.
                
        """
        self._associated_ike_gateway_id = value

    
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

    

    