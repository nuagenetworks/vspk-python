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


class NUPTranslationMap(NURESTObject):
    """ Represents a PTranslationMap in the VSD

        Notes:
            1:1 mappings of private IPs in provider domain to the provider  alias (public) IPs in customer domain and N:1 mappings of a collection of provider private IPs to a provider alias IP into the customer domain.
    """

    __rest_name__ = "ptranslationmap"
    __resource_name__ = "ptranslationmaps"

    
    ## Constants
    
    CONST_MAPPING_TYPE_PAT = "PAT"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_MAPPING_TYPE_NAT = "NAT"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a PTranslationMap instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ptranslationmap = NUPTranslationMap(id=u'xxxx-xxx-xxx-xxx', name=u'PTranslationMap')
                >>> ptranslationmap = NUPTranslationMap(data=my_dict)
        """

        super(NUPTranslationMap, self).__init__()

        # Read/Write Attributes
        
        self._spat_source_list = None
        self._mapping_type = None
        self._last_updated_by = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._provider_alias_ip = None
        self._provider_ip = None
        self._associated_domain_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="spat_source_list", remote_name="SPATSourceList", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mapping_type", remote_name="mappingType", attribute_type=str, is_required=False, is_unique=False, choices=[u'NAT', u'PAT'])
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="provider_alias_ip", remote_name="providerAliasIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="provider_ip", remote_name="providerIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="associated_domain_id", remote_name="associatedDomainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def spat_source_list(self):
        """ Get spat_source_list value.

            Notes:
                The list of provider source IPs to be SPAT'd.

                
                This attribute is named `SPATSourceList` in VSD API.
                
        """
        return self._spat_source_list

    @spat_source_list.setter
    def spat_source_list(self, value):
        """ Set spat_source_list value.

            Notes:
                The list of provider source IPs to be SPAT'd.

                
                This attribute is named `SPATSourceList` in VSD API.
                
        """
        self._spat_source_list = value

    
    @property
    def mapping_type(self):
        """ Get mapping_type value.

            Notes:
                1:1 NATmapping, or *:1 PAT mappings

                
                This attribute is named `mappingType` in VSD API.
                
        """
        return self._mapping_type

    @mapping_type.setter
    def mapping_type(self, value):
        """ Set mapping_type value.

            Notes:
                1:1 NATmapping, or *:1 PAT mappings

                
                This attribute is named `mappingType` in VSD API.
                
        """
        self._mapping_type = value

    
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
    def provider_alias_ip(self):
        """ Get provider_alias_ip value.

            Notes:
                Provider public IP in Customer Domain

                
                This attribute is named `providerAliasIP` in VSD API.
                
        """
        return self._provider_alias_ip

    @provider_alias_ip.setter
    def provider_alias_ip(self, value):
        """ Set provider_alias_ip value.

            Notes:
                Provider public IP in Customer Domain

                
                This attribute is named `providerAliasIP` in VSD API.
                
        """
        self._provider_alias_ip = value

    
    @property
    def provider_ip(self):
        """ Get provider_ip value.

            Notes:
                Provider private IP in Provider Domain.

                
                This attribute is named `providerIP` in VSD API.
                
        """
        return self._provider_ip

    @provider_ip.setter
    def provider_ip(self, value):
        """ Set provider_ip value.

            Notes:
                Provider private IP in Provider Domain.

                
                This attribute is named `providerIP` in VSD API.
                
        """
        self._provider_ip = value

    
    @property
    def associated_domain_id(self):
        """ Get associated_domain_id value.

            Notes:
                associated domain for this

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        return self._associated_domain_id

    @associated_domain_id.setter
    def associated_domain_id(self, value):
        """ Set associated_domain_id value.

            Notes:
                associated domain for this

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        self._associated_domain_id = value

    
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

    

    