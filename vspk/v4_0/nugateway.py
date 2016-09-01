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



from .fetchers import NUPATNATPoolsFetcher


from .fetchers import NUPermissionsFetcher


from .fetchers import NUWANServicesFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUEnterprisePermissionsFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NUPortsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUGateway(NURESTObject):
    """ Represents a Gateway in the VSD

        Notes:
            Represents Gateway object.
    """

    __rest_name__ = "gateway"
    __resource_name__ = "gateways"

    
    ## Constants
    
    CONST_PERSONALITY_HARDWARE_VTEP = "HARDWARE_VTEP"
    
    CONST_PERSONALITY_VSA = "VSA"
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_PERSONALITY_VSG = "VSG"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_PERSONALITY_OTHER = "OTHER"
    
    CONST_PERSONALITY_NSG = "NSG"
    
    CONST_PERSONALITY_VRSB = "VRSB"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_PERSONALITY_VRSG = "VRSG"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_PERSONALITY_DC7X50 = "DC7X50"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Gateway instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> gateway = NUGateway(id=u'xxxx-xxx-xxx-xxx', name=u'Gateway')
                >>> gateway = NUGateway(data=my_dict)
        """

        super(NUGateway, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._redundancy_group_id = None
        self._peer = None
        self._template_id = None
        self._pending = None
        self._permitted_action = None
        self._personality = None
        self._description = None
        self._enterprise_id = None
        self._entity_scope = None
        self._use_gateway_vlanvnid = None
        self._vtep = None
        self._auto_disc_gateway_id = None
        self._external_id = None
        self._system_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redundancy_group_id", remote_name="redundancyGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer", remote_name="peer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="pending", remote_name="pending", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=True, is_unique=False, choices=[u'DC7X50', u'HARDWARE_VTEP', u'NSG', u'OTHER', u'VRSB', u'VRSG', u'VSA', u'VSG'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="use_gateway_vlanvnid", remote_name="useGatewayVLANVNID", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vtep", remote_name="vtep", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="auto_disc_gateway_id", remote_name="autoDiscGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="system_id", remote_name="systemID", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.patnat_pools = NUPATNATPoolsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.wan_services = NUWANServicesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ports = NUPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Gateway

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Gateway

                
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
    def redundancy_group_id(self):
        """ Get redundancy_group_id value.

            Notes:
                The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute

                
                This attribute is named `redundancyGroupID` in VSD API.
                
        """
        return self._redundancy_group_id

    @redundancy_group_id.setter
    def redundancy_group_id(self, value):
        """ Set redundancy_group_id value.

            Notes:
                The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute

                
                This attribute is named `redundancyGroupID` in VSD API.
                
        """
        self._redundancy_group_id = value

    
    @property
    def peer(self):
        """ Get peer value.

            Notes:
                The System ID of the peer gateway associated with this Gateway instance when it is discovered by the network manager (VSD) as being redundant.

                
        """
        return self._peer

    @peer.setter
    def peer(self, value):
        """ Set peer value.

            Notes:
                The System ID of the peer gateway associated with this Gateway instance when it is discovered by the network manager (VSD) as being redundant.

                
        """
        self._peer = value

    
    @property
    def template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    
    @property
    def pending(self):
        """ Get pending value.

            Notes:
                Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.

                
        """
        return self._pending

    @pending.setter
    def pending(self, value):
        """ Set pending value.

            Notes:
                Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.

                
        """
        self._pending = value

    
    @property
    def permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway.

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    @permitted_action.setter
    def permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway.

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    
    @property
    def personality(self):
        """ Get personality value.

            Notes:
                Personality of the Gateway, cannot be changed after creation.

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                Personality of the Gateway, cannot be changed after creation.

                
        """
        self._personality = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the Gateway

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the Gateway

                
        """
        self._description = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                The enterprise associated with this Gateway. This is a read only attribute

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                The enterprise associated with this Gateway. This is a read only attribute

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
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
    def use_gateway_vlanvnid(self):
        """ Get use_gateway_vlanvnid value.

            Notes:
                When set, VLAN-VNID mapping must be unique for all the vports of the gateway

                
                This attribute is named `useGatewayVLANVNID` in VSD API.
                
        """
        return self._use_gateway_vlanvnid

    @use_gateway_vlanvnid.setter
    def use_gateway_vlanvnid(self, value):
        """ Set use_gateway_vlanvnid value.

            Notes:
                When set, VLAN-VNID mapping must be unique for all the vports of the gateway

                
                This attribute is named `useGatewayVLANVNID` in VSD API.
                
        """
        self._use_gateway_vlanvnid = value

    
    @property
    def vtep(self):
        """ Get vtep value.

            Notes:
                Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.

                
        """
        return self._vtep

    @vtep.setter
    def vtep(self, value):
        """ Set vtep value.

            Notes:
                Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.

                
        """
        self._vtep = value

    
    @property
    def auto_disc_gateway_id(self):
        """ Get auto_disc_gateway_id value.

            Notes:
                The Auto Discovered Gateway associated with this Gateway Instance

                
                This attribute is named `autoDiscGatewayID` in VSD API.
                
        """
        return self._auto_disc_gateway_id

    @auto_disc_gateway_id.setter
    def auto_disc_gateway_id(self, value):
        """ Set auto_disc_gateway_id value.

            Notes:
                The Auto Discovered Gateway associated with this Gateway Instance

                
                This attribute is named `autoDiscGatewayID` in VSD API.
                
        """
        self._auto_disc_gateway_id = value

    
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
    def system_id(self):
        """ Get system_id value.

            Notes:
                Identifier of the Gateway, cannot be modified after creation

                
                This attribute is named `systemID` in VSD API.
                
        """
        return self._system_id

    @system_id.setter
    def system_id(self, value):
        """ Set system_id value.

            Notes:
                Identifier of the Gateway, cannot be modified after creation

                
                This attribute is named `systemID` in VSD API.
                
        """
        self._system_id = value

    

    
    ## Custom methods
    def is_template(self):
        """ Verify that the object is a template
    
            Returns:
                (bool): True if the object is a template
        """
        return False
    
    def is_from_template(self):
        """ Verify if the object has been instantiated from a template
    
            Note:
                The object has to be fetched. Otherwise, it does not
                have information from its parent
    
            Returns:
                (bool): True if the object is a template
        """
        return self.template_id
    