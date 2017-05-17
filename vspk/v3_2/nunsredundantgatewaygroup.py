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


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUNSGatewaysFetcher


from .fetchers import NURedundantPortsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUNSRedundantGatewayGroup(NURESTObject):
    """ Represents a NSRedundantGatewayGroup in the VSD

        Notes:
            Represents Redundant Group formed by two VNS Gateways.
    """

    __rest_name__ = "nsgredundancygroup"
    __resource_name__ = "nsgredundancygroups"

    
    ## Constants
    
    CONST_PERSONALITY_HARDWARE_VTEP = "HARDWARE_VTEP"
    
    CONST_PERSONALITY_VSA = "VSA"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_PERSONALITY_VSG = "VSG"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_PERSONALITY_OTHER = "OTHER"
    
    CONST_PERSONALITY_NSG = "NSG"
    
    CONST_REDUNDANT_GATEWAY_STATUS_SUCCESS = "SUCCESS"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_PERSONALITY_VRSG = "VRSG"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_PERSONALITY_DC7X50 = "DC7X50"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_REDUNDANT_GATEWAY_STATUS_FAILED = "FAILED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NSRedundantGatewayGroup instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsredundantgatewaygroup = NUNSRedundantGatewayGroup(id=u'xxxx-xxx-xxx-xxx', name=u'NSRedundantGatewayGroup')
                >>> nsredundantgatewaygroup = NUNSRedundantGatewayGroup(data=my_dict)
        """

        super(NUNSRedundantGatewayGroup, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._gateway_peer1_autodiscovered_gateway_id = None
        self._gateway_peer1_id = None
        self._gateway_peer1_name = None
        self._gateway_peer2_autodiscovered_gateway_id = None
        self._gateway_peer2_name = None
        self._heartbeat_interval = None
        self._heartbeat_vlanid = None
        self._redundancy_port_ids = None
        self._redundant_gateway_status = None
        self._permitted_action = None
        self._personality = None
        self._description = None
        self._enterprise_id = None
        self._entity_scope = None
        self._consecutive_failures_count = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_peer1_autodiscovered_gateway_id", remote_name="gatewayPeer1AutodiscoveredGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_peer1_id", remote_name="gatewayPeer1ID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_peer1_name", remote_name="gatewayPeer1Name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_peer2_autodiscovered_gateway_id", remote_name="gatewayPeer2AutodiscoveredGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_peer2_name", remote_name="gatewayPeer2Name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="heartbeat_interval", remote_name="heartbeatInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="heartbeat_vlanid", remote_name="heartbeatVLANID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redundancy_port_ids", remote_name="redundancyPortIDs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redundant_gateway_status", remote_name="redundantGatewayStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'FAILED', u'SUCCESS'])
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=False, is_unique=False, choices=[u'DC7X50', u'HARDWARE_VTEP', u'NSG', u'OTHER', u'VRSG', u'VSA', u'VSG'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="consecutive_failures_count", remote_name="consecutiveFailuresCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_gateways = NUNSGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.redundant_ports = NURedundantPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Redundancy Group 

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Redundancy Group 

                
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
    def gateway_peer1_autodiscovered_gateway_id(self):
        """ Get gateway_peer1_autodiscovered_gateway_id value.

            Notes:
                The Auto Discovered Gateway configuration owner in this Redundant Group. 

                
                This attribute is named `gatewayPeer1AutodiscoveredGatewayID` in VSD API.
                
        """
        return self._gateway_peer1_autodiscovered_gateway_id

    @gateway_peer1_autodiscovered_gateway_id.setter
    def gateway_peer1_autodiscovered_gateway_id(self, value):
        """ Set gateway_peer1_autodiscovered_gateway_id value.

            Notes:
                The Auto Discovered Gateway configuration owner in this Redundant Group. 

                
                This attribute is named `gatewayPeer1AutodiscoveredGatewayID` in VSD API.
                
        """
        self._gateway_peer1_autodiscovered_gateway_id = value

    
    @property
    def gateway_peer1_id(self):
        """ Get gateway_peer1_id value.

            Notes:
                The gateway configuration owner in this Redundant Group. when Redundant Group is deleted this gateway will recieve vport associations 

                
                This attribute is named `gatewayPeer1ID` in VSD API.
                
        """
        return self._gateway_peer1_id

    @gateway_peer1_id.setter
    def gateway_peer1_id(self, value):
        """ Set gateway_peer1_id value.

            Notes:
                The gateway configuration owner in this Redundant Group. when Redundant Group is deleted this gateway will recieve vport associations 

                
                This attribute is named `gatewayPeer1ID` in VSD API.
                
        """
        self._gateway_peer1_id = value

    
    @property
    def gateway_peer1_name(self):
        """ Get gateway_peer1_name value.

            Notes:
                The gateway   configuration owner name in this Redundant Group

                
                This attribute is named `gatewayPeer1Name` in VSD API.
                
        """
        return self._gateway_peer1_name

    @gateway_peer1_name.setter
    def gateway_peer1_name(self, value):
        """ Set gateway_peer1_name value.

            Notes:
                The gateway   configuration owner name in this Redundant Group

                
                This attribute is named `gatewayPeer1Name` in VSD API.
                
        """
        self._gateway_peer1_name = value

    
    @property
    def gateway_peer2_autodiscovered_gateway_id(self):
        """ Get gateway_peer2_autodiscovered_gateway_id value.

            Notes:
                The Auto Discovered Gateway  peer in this Redundant Group

                
                This attribute is named `gatewayPeer2AutodiscoveredGatewayID` in VSD API.
                
        """
        return self._gateway_peer2_autodiscovered_gateway_id

    @gateway_peer2_autodiscovered_gateway_id.setter
    def gateway_peer2_autodiscovered_gateway_id(self, value):
        """ Set gateway_peer2_autodiscovered_gateway_id value.

            Notes:
                The Auto Discovered Gateway  peer in this Redundant Group

                
                This attribute is named `gatewayPeer2AutodiscoveredGatewayID` in VSD API.
                
        """
        self._gateway_peer2_autodiscovered_gateway_id = value

    
    @property
    def gateway_peer2_name(self):
        """ Get gateway_peer2_name value.

            Notes:
                The gateway peer name in this Redundant Group

                
                This attribute is named `gatewayPeer2Name` in VSD API.
                
        """
        return self._gateway_peer2_name

    @gateway_peer2_name.setter
    def gateway_peer2_name(self, value):
        """ Set gateway_peer2_name value.

            Notes:
                The gateway peer name in this Redundant Group

                
                This attribute is named `gatewayPeer2Name` in VSD API.
                
        """
        self._gateway_peer2_name = value

    
    @property
    def heartbeat_interval(self):
        """ Get heartbeat_interval value.

            Notes:
                Heartbeat interval in milliseconds to declare the neighbor dead.

                
                This attribute is named `heartbeatInterval` in VSD API.
                
        """
        return self._heartbeat_interval

    @heartbeat_interval.setter
    def heartbeat_interval(self, value):
        """ Set heartbeat_interval value.

            Notes:
                Heartbeat interval in milliseconds to declare the neighbor dead.

                
                This attribute is named `heartbeatInterval` in VSD API.
                
        """
        self._heartbeat_interval = value

    
    @property
    def heartbeat_vlanid(self):
        """ Get heartbeat_vlanid value.

            Notes:
                Heartbeat VLAN used for BFD.

                
                This attribute is named `heartbeatVLANID` in VSD API.
                
        """
        return self._heartbeat_vlanid

    @heartbeat_vlanid.setter
    def heartbeat_vlanid(self, value):
        """ Set heartbeat_vlanid value.

            Notes:
                Heartbeat VLAN used for BFD.

                
                This attribute is named `heartbeatVLANID` in VSD API.
                
        """
        self._heartbeat_vlanid = value

    
    @property
    def redundancy_port_ids(self):
        """ Get redundancy_port_ids value.

            Notes:
                Collections resilient port ids associated with this redundant group.

                
                This attribute is named `redundancyPortIDs` in VSD API.
                
        """
        return self._redundancy_port_ids

    @redundancy_port_ids.setter
    def redundancy_port_ids(self, value):
        """ Set redundancy_port_ids value.

            Notes:
                Collections resilient port ids associated with this redundant group.

                
                This attribute is named `redundancyPortIDs` in VSD API.
                
        """
        self._redundancy_port_ids = value

    
    @property
    def redundant_gateway_status(self):
        """ Get redundant_gateway_status value.

            Notes:
                The status of  Redundant Group.

                
                This attribute is named `redundantGatewayStatus` in VSD API.
                
        """
        return self._redundant_gateway_status

    @redundant_gateway_status.setter
    def redundant_gateway_status(self, value):
        """ Set redundant_gateway_status value.

            Notes:
                The status of  Redundant Group.

                
                This attribute is named `redundantGatewayStatus` in VSD API.
                
        """
        self._redundant_gateway_status = value

    
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
                Derived personality of the Redundancy Group.

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                Derived personality of the Redundancy Group.

                
        """
        self._personality = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                 Description of the Redundancy Group

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                 Description of the Redundancy Group

                
        """
        self._description = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                The enterprise associated with this Redundant Group. This is a read only attribute

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                The enterprise associated with this Redundant Group. This is a read only attribute

                
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
    def consecutive_failures_count(self):
        """ Get consecutive_failures_count value.

            Notes:
                Consecutive failure count.

                
                This attribute is named `consecutiveFailuresCount` in VSD API.
                
        """
        return self._consecutive_failures_count

    @consecutive_failures_count.setter
    def consecutive_failures_count(self, value):
        """ Set consecutive_failures_count value.

            Notes:
                Consecutive failure count.

                
                This attribute is named `consecutiveFailuresCount` in VSD API.
                
        """
        self._consecutive_failures_count = value

    
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

    

    