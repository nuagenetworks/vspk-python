# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
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


from .fetchers import NUTiersFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUFlowsFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUApp(NURESTObject):
    """ Represents a App in the VSD

        Notes:
            Represents a real life application like a vendor website, or a social network.
    """

    __rest_name__ = "application"
    __resource_name__ = "applications"

    
    ## Constants
    
    CONST_ASSOCIATED_DOMAIN_TYPE_DOMAIN = "DOMAIN"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ZONE = "ZONE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DOMAIN = "DOMAIN"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ASSOCIATED_DOMAIN_TYPE_L2DOMAIN = "L2DOMAIN"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a App instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> app = NUApp(id=u'xxxx-xxx-xxx-xxx', name=u'App')
                >>> app = NUApp(data=my_dict)
        """

        super(NUApp, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._description = None
        self._entity_scope = None
        self._assoc_egress_acl_template_id = None
        self._assoc_ingress_acl_template_id = None
        self._associated_domain_id = None
        self._associated_domain_type = None
        self._associated_network_object_id = None
        self._associated_network_object_type = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="assoc_egress_acl_template_id", remote_name="assocEgressACLTemplateId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="assoc_ingress_acl_template_id", remote_name="assocIngressACLTemplateId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_domain_id", remote_name="associatedDomainID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="associated_domain_type", remote_name="associatedDomainType", attribute_type=str, is_required=True, is_unique=False, choices=[u'DOMAIN', u'L2DOMAIN'])
        self.expose_attribute(local_name="associated_network_object_id", remote_name="associatedNetworkObjectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_network_object_type", remote_name="associatedNetworkObjectType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DOMAIN', u'ENTERPRISE', u'ZONE'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.tiers = NUTiersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.flows = NUFlowsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the application.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the application.

                
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
    def description(self):
        """ Get description value.

            Notes:
                Description of the application.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the application.

                
        """
        self._description = value

    
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
    def assoc_egress_acl_template_id(self):
        """ Get assoc_egress_acl_template_id value.

            Notes:
                The ID of the ACL template that this application is pointing to.

                
                This attribute is named `assocEgressACLTemplateId` in VSD API.
                
        """
        return self._assoc_egress_acl_template_id

    @assoc_egress_acl_template_id.setter
    def assoc_egress_acl_template_id(self, value):
        """ Set assoc_egress_acl_template_id value.

            Notes:
                The ID of the ACL template that this application is pointing to.

                
                This attribute is named `assocEgressACLTemplateId` in VSD API.
                
        """
        self._assoc_egress_acl_template_id = value

    
    @property
    def assoc_ingress_acl_template_id(self):
        """ Get assoc_ingress_acl_template_id value.

            Notes:
                The ID of the ACL template that this application is pointing to

                
                This attribute is named `assocIngressACLTemplateId` in VSD API.
                
        """
        return self._assoc_ingress_acl_template_id

    @assoc_ingress_acl_template_id.setter
    def assoc_ingress_acl_template_id(self, value):
        """ Set assoc_ingress_acl_template_id value.

            Notes:
                The ID of the ACL template that this application is pointing to

                
                This attribute is named `assocIngressACLTemplateId` in VSD API.
                
        """
        self._assoc_ingress_acl_template_id = value

    
    @property
    def associated_domain_id(self):
        """ Get associated_domain_id value.

            Notes:
                Domain id where the application is running.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        return self._associated_domain_id

    @associated_domain_id.setter
    def associated_domain_id(self, value):
        """ Set associated_domain_id value.

            Notes:
                Domain id where the application is running.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        self._associated_domain_id = value

    
    @property
    def associated_domain_type(self):
        """ Get associated_domain_type value.

            Notes:
                Type of domain (DOMAIN, L2DOMAIN). Refer to API section for supported types.

                
                This attribute is named `associatedDomainType` in VSD API.
                
        """
        return self._associated_domain_type

    @associated_domain_type.setter
    def associated_domain_type(self, value):
        """ Set associated_domain_type value.

            Notes:
                Type of domain (DOMAIN, L2DOMAIN). Refer to API section for supported types.

                
                This attribute is named `associatedDomainType` in VSD API.
                
        """
        self._associated_domain_type = value

    
    @property
    def associated_network_object_id(self):
        """ Get associated_network_object_id value.

            Notes:
                ID of the network object that this App is associated with.

                
                This attribute is named `associatedNetworkObjectID` in VSD API.
                
        """
        return self._associated_network_object_id

    @associated_network_object_id.setter
    def associated_network_object_id(self, value):
        """ Set associated_network_object_id value.

            Notes:
                ID of the network object that this App is associated with.

                
                This attribute is named `associatedNetworkObjectID` in VSD API.
                
        """
        self._associated_network_object_id = value

    
    @property
    def associated_network_object_type(self):
        """ Get associated_network_object_type value.

            Notes:
                Type of network object this App is associated with (ENTERPRISE, DOMAIN) Refer to API section for supported types.

                
                This attribute is named `associatedNetworkObjectType` in VSD API.
                
        """
        return self._associated_network_object_type

    @associated_network_object_type.setter
    def associated_network_object_type(self, value):
        """ Set associated_network_object_type value.

            Notes:
                Type of network object this App is associated with (ENTERPRISE, DOMAIN) Refer to API section for supported types.

                
                This attribute is named `associatedNetworkObjectType` in VSD API.
                
        """
        self._associated_network_object_type = value

    
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

    

    