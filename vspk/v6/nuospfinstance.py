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


from .fetchers import NUOSPFAreasFetcher

from bambou import NURESTObject


class NUOSPFInstance(NURESTObject):
    """ Represents a OSPFInstance in the VSD

        Notes:
            The OSPF instance is the highest hierarchical OSPF configuration object in a domain. The OSPF instance allows you to assign global import and export routing policies for OSPF traffic in the domain. 
    """

    __rest_name__ = "ospfinstance"
    __resource_name__ = "ospfinstances"

    
    ## Constants
    
    CONST_IP_TYPE_IPV4 = "IPV4"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_OSPF_TYPE_OSPFV2 = "OSPFv2"
    
    CONST_OSPF_TYPE_OSPFV3 = "OSPFv3"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a OSPFInstance instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ospfinstance = NUOSPFInstance(id=u'xxxx-xxx-xxx-xxx', name=u'OSPFInstance')
                >>> ospfinstance = NUOSPFInstance(data=my_dict)
        """

        super(NUOSPFInstance, self).__init__()

        # Read/Write Attributes
        
        self._ip_type = None
        self._ospf_type = None
        self._name = None
        self._last_updated_by = None
        self._last_updated_date = None
        self._description = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._creation_date = None
        self._preference = None
        self._associated_export_routing_policy_id = None
        self._associated_import_routing_policy_id = None
        self._super_backbone_enabled = None
        self._owner = None
        self._export_limit = None
        self._export_to_overlay = None
        self._external_id = None
        self._external_preference = None
        
        self.expose_attribute(local_name="ip_type", remote_name="IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4'])
        self.expose_attribute(local_name="ospf_type", remote_name="OSPFType", attribute_type=str, is_required=False, is_unique=True, choices=[u'OSPFv2', u'OSPFv3'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="preference", remote_name="preference", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_export_routing_policy_id", remote_name="associatedExportRoutingPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_import_routing_policy_id", remote_name="associatedImportRoutingPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="super_backbone_enabled", remote_name="superBackboneEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="export_limit", remote_name="exportLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="export_to_overlay", remote_name="exportToOverlay", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="external_preference", remote_name="externalPreference", attribute_type=int, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ospf_areas = NUOSPFAreasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ip_type(self):
        """ Get ip_type value.

            Notes:
                The IP Type of the OSPF Instance, currently only IPv4 is supported.

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        """ Set ip_type value.

            Notes:
                The IP Type of the OSPF Instance, currently only IPv4 is supported.

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    
    @property
    def ospf_type(self):
        """ Get ospf_type value.

            Notes:
                Type of the OSPF protocol, possible values are OSPFv2 and OSPFv3.

                
                This attribute is named `OSPFType` in VSD API.
                
        """
        return self._ospf_type

    @ospf_type.setter
    def ospf_type(self, value):
        """ Set ospf_type value.

            Notes:
                Type of the OSPF protocol, possible values are OSPFv2 and OSPFv3.

                
                This attribute is named `OSPFType` in VSD API.
                
        """
        self._ospf_type = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of OSPF Instance

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of OSPF Instance

                
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
    def last_updated_date(self):
        """ Get last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, value):
        """ Set last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        self._last_updated_date = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of OSPF Instance

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of OSPF Instance

                
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
    def creation_date(self):
        """ Get creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """ Set creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        self._creation_date = value

    
    @property
    def preference(self):
        """ Get preference value.

            Notes:
                Preference for OSPF Internal Routes.

                
        """
        return self._preference

    @preference.setter
    def preference(self, value):
        """ Set preference value.

            Notes:
                Preference for OSPF Internal Routes.

                
        """
        self._preference = value

    
    @property
    def associated_export_routing_policy_id(self):
        """ Get associated_export_routing_policy_id value.

            Notes:
                Export OSPF Routing Policy ID 

                
                This attribute is named `associatedExportRoutingPolicyID` in VSD API.
                
        """
        return self._associated_export_routing_policy_id

    @associated_export_routing_policy_id.setter
    def associated_export_routing_policy_id(self, value):
        """ Set associated_export_routing_policy_id value.

            Notes:
                Export OSPF Routing Policy ID 

                
                This attribute is named `associatedExportRoutingPolicyID` in VSD API.
                
        """
        self._associated_export_routing_policy_id = value

    
    @property
    def associated_import_routing_policy_id(self):
        """ Get associated_import_routing_policy_id value.

            Notes:
                Import OSPF Routing Policy ID

                
                This attribute is named `associatedImportRoutingPolicyID` in VSD API.
                
        """
        return self._associated_import_routing_policy_id

    @associated_import_routing_policy_id.setter
    def associated_import_routing_policy_id(self, value):
        """ Set associated_import_routing_policy_id value.

            Notes:
                Import OSPF Routing Policy ID

                
                This attribute is named `associatedImportRoutingPolicyID` in VSD API.
                
        """
        self._associated_import_routing_policy_id = value

    
    @property
    def super_backbone_enabled(self):
        """ Get super_backbone_enabled value.

            Notes:
                Flag to determine whether SuperBackbone is enabled or not.

                
                This attribute is named `superBackboneEnabled` in VSD API.
                
        """
        return self._super_backbone_enabled

    @super_backbone_enabled.setter
    def super_backbone_enabled(self, value):
        """ Set super_backbone_enabled value.

            Notes:
                Flag to determine whether SuperBackbone is enabled or not.

                
                This attribute is named `superBackboneEnabled` in VSD API.
                
        """
        self._super_backbone_enabled = value

    
    @property
    def owner(self):
        """ Get owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """ Set owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        self._owner = value

    
    @property
    def export_limit(self):
        """ Get export_limit value.

            Notes:
                This command configures the maximum number of routes (prefixes) that can be exported into OSPF from the route table.

                
                This attribute is named `exportLimit` in VSD API.
                
        """
        return self._export_limit

    @export_limit.setter
    def export_limit(self, value):
        """ Set export_limit value.

            Notes:
                This command configures the maximum number of routes (prefixes) that can be exported into OSPF from the route table.

                
                This attribute is named `exportLimit` in VSD API.
                
        """
        self._export_limit = value

    
    @property
    def export_to_overlay(self):
        """ Get export_to_overlay value.

            Notes:
                Flag which determines whether the routes learnt through BGP and OSPF will be exported to VSC or not. This flag also exists in the NSGRoutingPolicyBinding entity. The NSGRoutingPolicyBinding flag takes precedence over this one.

                
                This attribute is named `exportToOverlay` in VSD API.
                
        """
        return self._export_to_overlay

    @export_to_overlay.setter
    def export_to_overlay(self, value):
        """ Set export_to_overlay value.

            Notes:
                Flag which determines whether the routes learnt through BGP and OSPF will be exported to VSC or not. This flag also exists in the NSGRoutingPolicyBinding entity. The NSGRoutingPolicyBinding flag takes precedence over this one.

                
                This attribute is named `exportToOverlay` in VSD API.
                
        """
        self._export_to_overlay = value

    
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
    def external_preference(self):
        """ Get external_preference value.

            Notes:
                Preference for OSPF External Routes.

                
                This attribute is named `externalPreference` in VSD API.
                
        """
        return self._external_preference

    @external_preference.setter
    def external_preference(self, value):
        """ Set external_preference value.

            Notes:
                Preference for OSPF External Routes.

                
                This attribute is named `externalPreference` in VSD API.
                
        """
        self._external_preference = value

    

    