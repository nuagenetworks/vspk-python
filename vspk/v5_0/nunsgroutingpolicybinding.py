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


class NUNSGRoutingPolicyBinding(NURESTObject):
    """ Represents a NSGRoutingPolicyBinding in the VSD

        Notes:
            The NSG routing policy binding is used to assign routing policies to an NSG or group of NSGs as defined by the routing policy group. The local routing policies assigned to an NSG in a policy binding are preferred over global routing policies defined at the OSPF instance level.
    """

    __rest_name__ = "nsgroutingpolicybinding"
    __resource_name__ = "nsgroutingpolicybindings"

    
    ## Constants
    
    CONST_EXPORT_TO_OVERLAY_DISABLED = "DISABLED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_EXPORT_TO_OVERLAY_INHERITED = "INHERITED"
    
    CONST_EXPORT_TO_OVERLAY_ENABLED = "ENABLED"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NSGRoutingPolicyBinding instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsgroutingpolicybinding = NUNSGRoutingPolicyBinding(id=u'xxxx-xxx-xxx-xxx', name=u'NSGRoutingPolicyBinding')
                >>> nsgroutingpolicybinding = NUNSGRoutingPolicyBinding(data=my_dict)
        """

        super(NUNSGRoutingPolicyBinding, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._description = None
        self._entity_scope = None
        self._associated_export_routing_policy_id = None
        self._associated_import_routing_policy_id = None
        self._associated_policy_object_group_id = None
        self._export_to_overlay = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_export_routing_policy_id", remote_name="associatedExportRoutingPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_import_routing_policy_id", remote_name="associatedImportRoutingPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_policy_object_group_id", remote_name="associatedPolicyObjectGroupID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="export_to_overlay", remote_name="exportToOverlay", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the RoutingPolicyBinding is unique within the Domain

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the RoutingPolicyBinding is unique within the Domain

                
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
                Description for this Routing Policy Binding Object.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description for this Routing Policy Binding Object.

                
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
    def associated_export_routing_policy_id(self):
        """ Get associated_export_routing_policy_id value.

            Notes:
                ID of the Export Routing Policy which is associated to the current NSGRoutingPolicyBinding object.

                
                This attribute is named `associatedExportRoutingPolicyID` in VSD API.
                
        """
        return self._associated_export_routing_policy_id

    @associated_export_routing_policy_id.setter
    def associated_export_routing_policy_id(self, value):
        """ Set associated_export_routing_policy_id value.

            Notes:
                ID of the Export Routing Policy which is associated to the current NSGRoutingPolicyBinding object.

                
                This attribute is named `associatedExportRoutingPolicyID` in VSD API.
                
        """
        self._associated_export_routing_policy_id = value

    
    @property
    def associated_import_routing_policy_id(self):
        """ Get associated_import_routing_policy_id value.

            Notes:
                ID of the Import Routing Policy which is associated to the current NSGRoutingPolicyBinding object.

                
                This attribute is named `associatedImportRoutingPolicyID` in VSD API.
                
        """
        return self._associated_import_routing_policy_id

    @associated_import_routing_policy_id.setter
    def associated_import_routing_policy_id(self, value):
        """ Set associated_import_routing_policy_id value.

            Notes:
                ID of the Import Routing Policy which is associated to the current NSGRoutingPolicyBinding object.

                
                This attribute is named `associatedImportRoutingPolicyID` in VSD API.
                
        """
        self._associated_import_routing_policy_id = value

    
    @property
    def associated_policy_object_group_id(self):
        """ Get associated_policy_object_group_id value.

            Notes:
                ID of the Policy Object Group which is associated to the current NSGRoutingPolicyBinding object.

                
                This attribute is named `associatedPolicyObjectGroupID` in VSD API.
                
        """
        return self._associated_policy_object_group_id

    @associated_policy_object_group_id.setter
    def associated_policy_object_group_id(self, value):
        """ Set associated_policy_object_group_id value.

            Notes:
                ID of the Policy Object Group which is associated to the current NSGRoutingPolicyBinding object.

                
                This attribute is named `associatedPolicyObjectGroupID` in VSD API.
                
        """
        self._associated_policy_object_group_id = value

    
    @property
    def export_to_overlay(self):
        """ Get export_to_overlay value.

            Notes:
                Flag to determine whether the BGP and OSPF learnt routes will be exported to VSC or not. This flags also exists at the domain level. If this attribute is set to 'INHERITED' (the default), the behavior is whatever is set at the domain level. Otherwise, this attribute takes precedence over the domain level one.

                
                This attribute is named `exportToOverlay` in VSD API.
                
        """
        return self._export_to_overlay

    @export_to_overlay.setter
    def export_to_overlay(self, value):
        """ Set export_to_overlay value.

            Notes:
                Flag to determine whether the BGP and OSPF learnt routes will be exported to VSC or not. This flags also exists at the domain level. If this attribute is set to 'INHERITED' (the default), the behavior is whatever is set at the domain level. Otherwise, this attribute takes precedence over the domain level one.

                
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

    

    