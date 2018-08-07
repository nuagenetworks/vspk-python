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




from .fetchers import NUDemarcationServicesFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUNextHopsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUPolicyStatementsFetcher


from .fetchers import NUCSNATPoolsFetcher


from .fetchers import NUPSNATPoolsFetcher


from .fetchers import NUOverlayAddressPoolsFetcher

from bambou import NURESTObject


class NULink(NURESTObject):
    """ Represents a Link in the VSD

        Notes:
            Border router links provide a way to interconnect VNS domains in the wide-area to datacenter domains. Service chaining links allow domain leaking in order to simplify and enhance capabilities of doing service chaining and traffic steering for NFV and service-provider-grade VPN services.
    """

    __rest_name__ = "link"
    __resource_name__ = "links"

    
    ## Constants
    
    CONST_ASSOCIATED_DESTINATION_TYPE_DOMAIN = "DOMAIN"
    
    CONST_TYPE_BORDER_ROUTER = "BORDER_ROUTER"
    
    CONST_TYPE_SERVICE_CHAINING = "SERVICE_CHAINING"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_TYPE_OVERLAY_ADDRESS_TRANSLATION = "OVERLAY_ADDRESS_TRANSLATION"
    
    CONST_ACCEPTANCE_CRITERIA_SUBNETS_ONLY = "SUBNETS_ONLY"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ACCEPTANCE_CRITERIA_ALL = "ALL"
    
    CONST_TYPE_BIDIR = "BIDIR"
    
    CONST_TYPE_HUB_AND_SPOKE = "HUB_AND_SPOKE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Link instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> link = NULink(id=u'xxxx-xxx-xxx-xxx', name=u'Link')
                >>> link = NULink(data=my_dict)
        """

        super(NULink, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._acceptance_criteria = None
        self._read_only = None
        self._entity_scope = None
        self._associated_destination_id = None
        self._associated_destination_name = None
        self._associated_destination_type = None
        self._associated_source_id = None
        self._associated_source_name = None
        self._associated_source_type = None
        self._external_id = None
        self._type = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="acceptance_criteria", remote_name="acceptanceCriteria", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'SUBNETS_ONLY'])
        self.expose_attribute(local_name="read_only", remote_name="readOnly", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_destination_id", remote_name="associatedDestinationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_destination_name", remote_name="associatedDestinationName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_destination_type", remote_name="associatedDestinationType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DOMAIN'])
        self.expose_attribute(local_name="associated_source_id", remote_name="associatedSourceID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_source_name", remote_name="associatedSourceName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_source_type", remote_name="associatedSourceType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=False, is_unique=False, choices=[u'BIDIR', u'BORDER_ROUTER', u'HUB_AND_SPOKE', u'OVERLAY_ADDRESS_TRANSLATION', u'SERVICE_CHAINING'])
        

        # Fetchers
        
        
        self.demarcation_services = NUDemarcationServicesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.next_hops = NUNextHopsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.policy_statements = NUPolicyStatementsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.csnat_pools = NUCSNATPoolsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.psnat_pools = NUPSNATPoolsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.overlay_address_pools = NUOverlayAddressPoolsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

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
    def acceptance_criteria(self):
        """ Get acceptance_criteria value.

            Notes:
                A route filtering criteria enum. Defaults to ALL.

                
                This attribute is named `acceptanceCriteria` in VSD API.
                
        """
        return self._acceptance_criteria

    @acceptance_criteria.setter
    def acceptance_criteria(self, value):
        """ Set acceptance_criteria value.

            Notes:
                A route filtering criteria enum. Defaults to ALL.

                
                This attribute is named `acceptanceCriteria` in VSD API.
                
        """
        self._acceptance_criteria = value

    
    @property
    def read_only(self):
        """ Get read_only value.

            Notes:
                This is set to true if a link has been created in the opposite direction

                
                This attribute is named `readOnly` in VSD API.
                
        """
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """ Set read_only value.

            Notes:
                This is set to true if a link has been created in the opposite direction

                
                This attribute is named `readOnly` in VSD API.
                
        """
        self._read_only = value

    
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
    def associated_destination_id(self):
        """ Get associated_destination_id value.

            Notes:
                This is the  ID of the domain receiving the routes from the source. This can only be set for links of type OVERLAY_ADDRESS_TRANSLATION.

                
                This attribute is named `associatedDestinationID` in VSD API.
                
        """
        return self._associated_destination_id

    @associated_destination_id.setter
    def associated_destination_id(self, value):
        """ Set associated_destination_id value.

            Notes:
                This is the  ID of the domain receiving the routes from the source. This can only be set for links of type OVERLAY_ADDRESS_TRANSLATION.

                
                This attribute is named `associatedDestinationID` in VSD API.
                
        """
        self._associated_destination_id = value

    
    @property
    def associated_destination_name(self):
        """ Get associated_destination_name value.

            Notes:
                None

                
                This attribute is named `associatedDestinationName` in VSD API.
                
        """
        return self._associated_destination_name

    @associated_destination_name.setter
    def associated_destination_name(self, value):
        """ Set associated_destination_name value.

            Notes:
                None

                
                This attribute is named `associatedDestinationName` in VSD API.
                
        """
        self._associated_destination_name = value

    
    @property
    def associated_destination_type(self):
        """ Get associated_destination_type value.

            Notes:
                Type of the entity type for the source

                
                This attribute is named `associatedDestinationType` in VSD API.
                
        """
        return self._associated_destination_type

    @associated_destination_type.setter
    def associated_destination_type(self, value):
        """ Set associated_destination_type value.

            Notes:
                Type of the entity type for the source

                
                This attribute is named `associatedDestinationType` in VSD API.
                
        """
        self._associated_destination_type = value

    
    @property
    def associated_source_id(self):
        """ Get associated_source_id value.

            Notes:
                The ID of the domain receiving the routes from another domain

                
                This attribute is named `associatedSourceID` in VSD API.
                
        """
        return self._associated_source_id

    @associated_source_id.setter
    def associated_source_id(self, value):
        """ Set associated_source_id value.

            Notes:
                The ID of the domain receiving the routes from another domain

                
                This attribute is named `associatedSourceID` in VSD API.
                
        """
        self._associated_source_id = value

    
    @property
    def associated_source_name(self):
        """ Get associated_source_name value.

            Notes:
                None

                
                This attribute is named `associatedSourceName` in VSD API.
                
        """
        return self._associated_source_name

    @associated_source_name.setter
    def associated_source_name(self, value):
        """ Set associated_source_name value.

            Notes:
                None

                
                This attribute is named `associatedSourceName` in VSD API.
                
        """
        self._associated_source_name = value

    
    @property
    def associated_source_type(self):
        """ Get associated_source_type value.

            Notes:
                This is the source object type for the associatedSourceID

                
                This attribute is named `associatedSourceType` in VSD API.
                
        """
        return self._associated_source_type

    @associated_source_type.setter
    def associated_source_type(self, value):
        """ Set associated_source_type value.

            Notes:
                This is the source object type for the associatedSourceID

                
                This attribute is named `associatedSourceType` in VSD API.
                
        """
        self._associated_source_type = value

    
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

    
    @property
    def type(self):
        """ Get type value.

            Notes:
                This is used to distinguish between different type of links: hub and spoke, ip address, VNS border router links.

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                This is used to distinguish between different type of links: hub and spoke, ip address, VNS border router links.

                
        """
        self._type = value

    

    