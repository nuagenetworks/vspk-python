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


class NUCTranslationMap(NURESTObject):
    """ Represents a CTranslationMap in the VSD

        Notes:
            1:1 mapping of customer private IPs in customer domain to customer alias (public) IPs in provider domain and N:1 mapping to customer alias SPAT IP in the provider domain.
    """

    __rest_name__ = "ctranslationmap"
    __resource_name__ = "ctranslationmaps"

    
    ## Constants
    
    CONST_MAPPING_TYPE_PAT = "PAT"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_MAPPING_TYPE_NAT = "NAT"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a CTranslationMap instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ctranslationmap = NUCTranslationMap(id=u'xxxx-xxx-xxx-xxx', name=u'CTranslationMap')
                >>> ctranslationmap = NUCTranslationMap(data=my_dict)
        """

        super(NUCTranslationMap, self).__init__()

        # Read/Write Attributes
        
        self._mapping_type = None
        self._last_updated_by = None
        self._entity_scope = None
        self._associated_domain_id = None
        self._customer_alias_ip = None
        self._customer_ip = None
        self._external_id = None
        
        self.expose_attribute(local_name="mapping_type", remote_name="mappingType", attribute_type=str, is_required=True, is_unique=False, choices=[u'NAT', u'PAT'])
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_domain_id", remote_name="associatedDomainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="customer_alias_ip", remote_name="customerAliasIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="customer_ip", remote_name="customerIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def mapping_type(self):
        """ Get mapping_type value.

            Notes:
                NAT for 1:1 mapping or PAT for *:1 mappings.

                
                This attribute is named `mappingType` in VSD API.
                
        """
        return self._mapping_type

    @mapping_type.setter
    def mapping_type(self, value):
        """ Set mapping_type value.

            Notes:
                NAT for 1:1 mapping or PAT for *:1 mappings.

                
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
    def associated_domain_id(self):
        """ Get associated_domain_id value.

            Notes:
                Domain associated to this address mapping.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        return self._associated_domain_id

    @associated_domain_id.setter
    def associated_domain_id(self, value):
        """ Set associated_domain_id value.

            Notes:
                Domain associated to this address mapping.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        self._associated_domain_id = value

    
    @property
    def customer_alias_ip(self):
        """ Get customer_alias_ip value.

            Notes:
                Customer public IP in the provider domain.

                
                This attribute is named `customerAliasIP` in VSD API.
                
        """
        return self._customer_alias_ip

    @customer_alias_ip.setter
    def customer_alias_ip(self, value):
        """ Set customer_alias_ip value.

            Notes:
                Customer public IP in the provider domain.

                
                This attribute is named `customerAliasIP` in VSD API.
                
        """
        self._customer_alias_ip = value

    
    @property
    def customer_ip(self):
        """ Get customer_ip value.

            Notes:
                Customer private IP in the customer domain.

                
                This attribute is named `customerIP` in VSD API.
                
        """
        return self._customer_ip

    @customer_ip.setter
    def customer_ip(self, value):
        """ Set customer_ip value.

            Notes:
                Customer private IP in the customer domain.

                
                This attribute is named `customerIP` in VSD API.
                
        """
        self._customer_ip = value

    
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

    

    