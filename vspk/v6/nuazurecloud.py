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


from .fetchers import NUIKEGatewayProfilesFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUJobsFetcher

from bambou import NURESTObject


class NUAzureCloud(NURESTObject):
    """ Represents a AzureCloud in the VSD

        Notes:
            Represents Azure Cloud account to configure IKE entities. 
    """

    __rest_name__ = "azurecloud"
    __resource_name__ = "azureclouds"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a AzureCloud instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> azurecloud = NUAzureCloud(id=u'xxxx-xxx-xxx-xxx', name=u'AzureCloud')
                >>> azurecloud = NUAzureCloud(data=my_dict)
        """

        super(NUAzureCloud, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._tenant_id = None
        self._client_id = None
        self._client_secret = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._associated_ike_encryption_profile_id = None
        self._associated_ikepskid = None
        self._subscription_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tenant_id", remote_name="tenantID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="client_id", remote_name="clientID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="client_secret", remote_name="clientSecret", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_ike_encryption_profile_id", remote_name="associatedIKEEncryptionProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ikepskid", remote_name="associatedIKEPSKID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="subscription_id", remote_name="subscriptionID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ike_gateway_profiles = NUIKEGatewayProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name given to Azure Cloud instance

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name given to Azure Cloud instance

                
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
    def tenant_id(self):
        """ Get tenant_id value.

            Notes:
                The tenant Id of Azure Cloud account.

                
                This attribute is named `tenantID` in VSD API.
                
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        """ Set tenant_id value.

            Notes:
                The tenant Id of Azure Cloud account.

                
                This attribute is named `tenantID` in VSD API.
                
        """
        self._tenant_id = value

    
    @property
    def client_id(self):
        """ Get client_id value.

            Notes:
                The client Id of Azure Cloud account.

                
                This attribute is named `clientID` in VSD API.
                
        """
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        """ Set client_id value.

            Notes:
                The client Id of Azure Cloud account.

                
                This attribute is named `clientID` in VSD API.
                
        """
        self._client_id = value

    
    @property
    def client_secret(self):
        """ Get client_secret value.

            Notes:
                The client secret of Azure Cloud account.

                
                This attribute is named `clientSecret` in VSD API.
                
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value):
        """ Set client_secret value.

            Notes:
                The client secret of Azure Cloud account.

                
                This attribute is named `clientSecret` in VSD API.
                
        """
        self._client_secret = value

    
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
    def associated_ike_encryption_profile_id(self):
        """ Get associated_ike_encryption_profile_id value.

            Notes:
                Associated IKE Encryption Profile.

                
                This attribute is named `associatedIKEEncryptionProfileID` in VSD API.
                
        """
        return self._associated_ike_encryption_profile_id

    @associated_ike_encryption_profile_id.setter
    def associated_ike_encryption_profile_id(self, value):
        """ Set associated_ike_encryption_profile_id value.

            Notes:
                Associated IKE Encryption Profile.

                
                This attribute is named `associatedIKEEncryptionProfileID` in VSD API.
                
        """
        self._associated_ike_encryption_profile_id = value

    
    @property
    def associated_ikepskid(self):
        """ Get associated_ikepskid value.

            Notes:
                Associated IKE PSK

                
                This attribute is named `associatedIKEPSKID` in VSD API.
                
        """
        return self._associated_ikepskid

    @associated_ikepskid.setter
    def associated_ikepskid(self, value):
        """ Set associated_ikepskid value.

            Notes:
                Associated IKE PSK

                
                This attribute is named `associatedIKEPSKID` in VSD API.
                
        """
        self._associated_ikepskid = value

    
    @property
    def subscription_id(self):
        """ Get subscription_id value.

            Notes:
                The subscription Id of Azure Cloud account.

                
                This attribute is named `subscriptionID` in VSD API.
                
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        """ Set subscription_id value.

            Notes:
                The subscription Id of Azure Cloud account.

                
                This attribute is named `subscriptionID` in VSD API.
                
        """
        self._subscription_id = value

    
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

    

    