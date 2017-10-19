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



from .fetchers import NUTCAsFetcher


from .fetchers import NURedirectionTargetsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUAggregateMetadatasFetcher


from .fetchers import NUBGPNeighborsFetcher


from .fetchers import NUEgressACLEntryTemplatesFetcher


from .fetchers import NUDHCPOptionsFetcher


from .fetchers import NUVirtualIPsFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVMsFetcher


from .fetchers import NUVMInterfacesFetcher


from .fetchers import NUVNFInterfacesFetcher


from .fetchers import NUIngressACLEntryTemplatesFetcher


from .fetchers import NUIngressAdvFwdEntryTemplatesFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NUPolicyGroupsFetcher


from .fetchers import NUContainersFetcher


from .fetchers import NUContainerInterfacesFetcher


from .fetchers import NUPortMappingsFetcher


from .fetchers import NUQOSsFetcher


from .fetchers import NUHostInterfacesFetcher


from .fetchers import NUVPortMirrorsFetcher


from .fetchers import NUApplicationperformancemanagementsFetcher


from .fetchers import NUBridgeInterfacesFetcher


from .fetchers import NUVRSsFetcher


from .fetchers import NUTrunksFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUStatisticsPoliciesFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUVPort(NURESTObject):
    """ Represents a VPort in the VSD

        Notes:
            VPorts are a new level in the domain hierarchy, intended to provide more granular configuration than at subnet, and also support a split workflow, where the vPort is configured and associated with a VM port (or gateway port) before the port exists.
    """

    __rest_name__ = "vport"
    __resource_name__ = "vports"

    
    ## Constants
    
    CONST_SYSTEM_TYPE_NUAGE_2 = "NUAGE_2"
    
    CONST_SYSTEM_TYPE_NUAGE_1 = "NUAGE_1"
    
    CONST_DPI_ENABLED = "ENABLED"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_TYPE_CONTAINER = "CONTAINER"
    
    CONST_DPI_INHERITED = "INHERITED"
    
    CONST_ADDRESS_SPOOFING_DISABLED = "DISABLED"
    
    CONST_ADDRESS_SPOOFING_INHERITED = "INHERITED"
    
    CONST_ADDRESS_SPOOFING_ENABLED = "ENABLED"
    
    CONST_TYPE_HOST = "HOST"
    
    CONST_GATEWAY_MAC_MOVE_ROLE_TERTIARY = "TERTIARY"
    
    CONST_GATEWAY_MAC_MOVE_ROLE_SECONDARY = "SECONDARY"
    
    CONST_SUB_TYPE_VNF = "VNF"
    
    CONST_OPERATIONAL_STATE_DOWN = "DOWN"
    
    CONST_TRUNK_ROLE_SUB_PORT = "SUB_PORT"
    
    CONST_SEGMENTATION_TYPE_VLAN = "VLAN"
    
    CONST_OPERATIONAL_STATE_UP = "UP"
    
    CONST_MULTICAST_ENABLED = "ENABLED"
    
    CONST_MULTICAST_INHERITED = "INHERITED"
    
    CONST_SYSTEM_TYPE_HARDWARE_VTEP = "HARDWARE_VTEP"
    
    CONST_SYSTEM_TYPE_HARDWARE = "HARDWARE"
    
    CONST_TYPE_BRIDGE = "BRIDGE"
    
    CONST_SUB_TYPE_NONE = "NONE"
    
    CONST_MULTICAST_DISABLED = "DISABLED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_SYSTEM_TYPE_SOFTWARE = "SOFTWARE"
    
    CONST_TRUNK_ROLE_PARENT_PORT = "PARENT_PORT"
    
    CONST_DPI_DISABLED = "DISABLED"
    
    CONST_SYSTEM_TYPE_NUAGE_VRSG = "NUAGE_VRSG"
    
    CONST_OPERATIONAL_STATE_INIT = "INIT"
    
    CONST_TYPE_VM = "VM"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VPort instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vport = NUVPort(id=u'xxxx-xxx-xxx-xxx', name=u'VPort')
                >>> vport = NUVPort(data=my_dict)
        """

        super(NUVPort, self).__init__()

        # Read/Write Attributes
        
        self._vlanid = None
        self._dpi = None
        self._name = None
        self._has_attached_interfaces = None
        self._last_updated_by = None
        self._gateway_mac_move_role = None
        self._active = None
        self._address_spoofing = None
        self._segmentation_id = None
        self._segmentation_type = None
        self._description = None
        self._entity_scope = None
        self._domain_id = None
        self._zone_id = None
        self._operational_state = None
        self._trunk_role = None
        self._associated_floating_ip_id = None
        self._associated_multicast_channel_map_id = None
        self._associated_ssid = None
        self._associated_send_multicast_channel_map_id = None
        self._associated_trunk_id = None
        self._sub_type = None
        self._multi_nic_vport_id = None
        self._multicast = None
        self._external_id = None
        self._type = None
        self._system_type = None
        
        self.expose_attribute(local_name="vlanid", remote_name="VLANID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dpi", remote_name="DPI", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="has_attached_interfaces", remote_name="hasAttachedInterfaces", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_mac_move_role", remote_name="gatewayMACMoveRole", attribute_type=str, is_required=False, is_unique=False, choices=[u'SECONDARY', u'TERTIARY'])
        self.expose_attribute(local_name="active", remote_name="active", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address_spoofing", remote_name="addressSpoofing", attribute_type=str, is_required=True, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="segmentation_id", remote_name="segmentationID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="segmentation_type", remote_name="segmentationType", attribute_type=str, is_required=False, is_unique=False, choices=[u'VLAN'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="domain_id", remote_name="domainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zone_id", remote_name="zoneID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="operational_state", remote_name="operationalState", attribute_type=str, is_required=False, is_unique=False, choices=[u'DOWN', u'INIT', u'UP'])
        self.expose_attribute(local_name="trunk_role", remote_name="trunkRole", attribute_type=str, is_required=False, is_unique=False, choices=[u'PARENT_PORT', u'SUB_PORT'])
        self.expose_attribute(local_name="associated_floating_ip_id", remote_name="associatedFloatingIPID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_multicast_channel_map_id", remote_name="associatedMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ssid", remote_name="associatedSSID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_send_multicast_channel_map_id", remote_name="associatedSendMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_trunk_id", remote_name="associatedTrunkID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sub_type", remote_name="subType", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'VNF'])
        self.expose_attribute(local_name="multi_nic_vport_id", remote_name="multiNICVPortID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast", remote_name="multicast", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=True, is_unique=False, choices=[u'BRIDGE', u'CONTAINER', u'HOST', u'VM'])
        self.expose_attribute(local_name="system_type", remote_name="systemType", attribute_type=str, is_required=False, is_unique=False, choices=[u'HARDWARE', u'HARDWARE_VTEP', u'NUAGE_1', u'NUAGE_2', u'NUAGE_VRSG', u'SOFTWARE'])
        

        # Fetchers
        
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.redirection_targets = NURedirectionTargetsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.aggregate_metadatas = NUAggregateMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bgp_neighbors = NUBGPNeighborsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.egress_acl_entry_templates = NUEgressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.dhcp_options = NUDHCPOptionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.virtual_ips = NUVirtualIPsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vnf_interfaces = NUVNFInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ingress_acl_entry_templates = NUIngressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ingress_adv_fwd_entry_templates = NUIngressAdvFwdEntryTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.policy_groups = NUPolicyGroupsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.containers = NUContainersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.container_interfaces = NUContainerInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.port_mappings = NUPortMappingsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.host_interfaces = NUHostInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vport_mirrors = NUVPortMirrorsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.applicationperformancemanagements = NUApplicationperformancemanagementsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.bridge_interfaces = NUBridgeInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vrss = NUVRSsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.trunks = NUTrunksFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vlanid(self):
        """ Get vlanid value.

            Notes:
                associated Vlan of this vport - applicable for type host/bridge

                
                This attribute is named `VLANID` in VSD API.
                
        """
        return self._vlanid

    @vlanid.setter
    def vlanid(self, value):
        """ Set vlanid value.

            Notes:
                associated Vlan of this vport - applicable for type host/bridge

                
                This attribute is named `VLANID` in VSD API.
                
        """
        self._vlanid = value

    
    @property
    def dpi(self):
        """ Get dpi value.

            Notes:
                determines whether or not Deep packet inspection is enabled

                
                This attribute is named `DPI` in VSD API.
                
        """
        return self._dpi

    @dpi.setter
    def dpi(self, value):
        """ Set dpi value.

            Notes:
                determines whether or not Deep packet inspection is enabled

                
                This attribute is named `DPI` in VSD API.
                
        """
        self._dpi = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the vport. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the vport. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        self._name = value

    
    @property
    def has_attached_interfaces(self):
        """ Get has_attached_interfaces value.

            Notes:
                Indicates that this vport has attached interfaces

                
                This attribute is named `hasAttachedInterfaces` in VSD API.
                
        """
        return self._has_attached_interfaces

    @has_attached_interfaces.setter
    def has_attached_interfaces(self, value):
        """ Set has_attached_interfaces value.

            Notes:
                Indicates that this vport has attached interfaces

                
                This attribute is named `hasAttachedInterfaces` in VSD API.
                
        """
        self._has_attached_interfaces = value

    
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
    def gateway_mac_move_role(self):
        """ Get gateway_mac_move_role value.

            Notes:
                Role of the gateway vport when handling mac move errors

                
                This attribute is named `gatewayMACMoveRole` in VSD API.
                
        """
        return self._gateway_mac_move_role

    @gateway_mac_move_role.setter
    def gateway_mac_move_role(self, value):
        """ Set gateway_mac_move_role value.

            Notes:
                Role of the gateway vport when handling mac move errors

                
                This attribute is named `gatewayMACMoveRole` in VSD API.
                
        """
        self._gateway_mac_move_role = value

    
    @property
    def active(self):
        """ Get active value.

            Notes:
                Indicates if this vport is up or down

                
        """
        return self._active

    @active.setter
    def active(self, value):
        """ Set active value.

            Notes:
                Indicates if this vport is up or down

                
        """
        self._active = value

    
    @property
    def address_spoofing(self):
        """ Get address_spoofing value.

            Notes:
                Indicates if address spoofing is ENABLED/DISABLED/INHERITED for this vport.

                
                This attribute is named `addressSpoofing` in VSD API.
                
        """
        return self._address_spoofing

    @address_spoofing.setter
    def address_spoofing(self, value):
        """ Set address_spoofing value.

            Notes:
                Indicates if address spoofing is ENABLED/DISABLED/INHERITED for this vport.

                
                This attribute is named `addressSpoofing` in VSD API.
                
        """
        self._address_spoofing = value

    
    @property
    def segmentation_id(self):
        """ Get segmentation_id value.

            Notes:
                The VLAN Number (1-4095), valid only if the trunkRole is SUB_PORT

                
                This attribute is named `segmentationID` in VSD API.
                
        """
        return self._segmentation_id

    @segmentation_id.setter
    def segmentation_id(self, value):
        """ Set segmentation_id value.

            Notes:
                The VLAN Number (1-4095), valid only if the trunkRole is SUB_PORT

                
                This attribute is named `segmentationID` in VSD API.
                
        """
        self._segmentation_id = value

    
    @property
    def segmentation_type(self):
        """ Get segmentation_type value.

            Notes:
                The type of segmentation that is used. This must be VLAN for vports with trunkRole set to SUB_PORT. This can not be specified for a parent vport (trunkRole = PARENT_PORT)

                
                This attribute is named `segmentationType` in VSD API.
                
        """
        return self._segmentation_type

    @segmentation_type.setter
    def segmentation_type(self, value):
        """ Set segmentation_type value.

            Notes:
                The type of segmentation that is used. This must be VLAN for vports with trunkRole set to SUB_PORT. This can not be specified for a parent vport (trunkRole = PARENT_PORT)

                
                This attribute is named `segmentationType` in VSD API.
                
        """
        self._segmentation_type = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description for this vport

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description for this vport

                
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
    def domain_id(self):
        """ Get domain_id value.

            Notes:
                ID the Domain associated with the VPort

                
                This attribute is named `domainID` in VSD API.
                
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, value):
        """ Set domain_id value.

            Notes:
                ID the Domain associated with the VPort

                
                This attribute is named `domainID` in VSD API.
                
        """
        self._domain_id = value

    
    @property
    def zone_id(self):
        """ Get zone_id value.

            Notes:
                ID the Zone associated with the VPort

                
                This attribute is named `zoneID` in VSD API.
                
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, value):
        """ Set zone_id value.

            Notes:
                ID the Zone associated with the VPort

                
                This attribute is named `zoneID` in VSD API.
                
        """
        self._zone_id = value

    
    @property
    def operational_state(self):
        """ Get operational_state value.

            Notes:
                Operational State of the VPort. Possible values are INIT, UP, DOWN.

                
                This attribute is named `operationalState` in VSD API.
                
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, value):
        """ Set operational_state value.

            Notes:
                Operational State of the VPort. Possible values are INIT, UP, DOWN.

                
                This attribute is named `operationalState` in VSD API.
                
        """
        self._operational_state = value

    
    @property
    def trunk_role(self):
        """ Get trunk_role value.

            Notes:
                Indicates the role of the vport in trunking operations

                
                This attribute is named `trunkRole` in VSD API.
                
        """
        return self._trunk_role

    @trunk_role.setter
    def trunk_role(self, value):
        """ Set trunk_role value.

            Notes:
                Indicates the role of the vport in trunking operations

                
                This attribute is named `trunkRole` in VSD API.
                
        """
        self._trunk_role = value

    
    @property
    def associated_floating_ip_id(self):
        """ Get associated_floating_ip_id value.

            Notes:
                Id of Floating IP address associated to this vport

                
                This attribute is named `associatedFloatingIPID` in VSD API.
                
        """
        return self._associated_floating_ip_id

    @associated_floating_ip_id.setter
    def associated_floating_ip_id(self, value):
        """ Set associated_floating_ip_id value.

            Notes:
                Id of Floating IP address associated to this vport

                
                This attribute is named `associatedFloatingIPID` in VSD API.
                
        """
        self._associated_floating_ip_id = value

    
    @property
    def associated_multicast_channel_map_id(self):
        """ Get associated_multicast_channel_map_id value.

            Notes:
                The ID of the receive Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_multicast_channel_map_id

    @associated_multicast_channel_map_id.setter
    def associated_multicast_channel_map_id(self, value):
        """ Set associated_multicast_channel_map_id value.

            Notes:
                The ID of the receive Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        self._associated_multicast_channel_map_id = value

    
    @property
    def associated_ssid(self):
        """ Get associated_ssid value.

            Notes:
                The UUID of the SSID Connection tied to this instance of a vPort.

                
                This attribute is named `associatedSSID` in VSD API.
                
        """
        return self._associated_ssid

    @associated_ssid.setter
    def associated_ssid(self, value):
        """ Set associated_ssid value.

            Notes:
                The UUID of the SSID Connection tied to this instance of a vPort.

                
                This attribute is named `associatedSSID` in VSD API.
                
        """
        self._associated_ssid = value

    
    @property
    def associated_send_multicast_channel_map_id(self):
        """ Get associated_send_multicast_channel_map_id value.

            Notes:
                The ID of the send Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedSendMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_send_multicast_channel_map_id

    @associated_send_multicast_channel_map_id.setter
    def associated_send_multicast_channel_map_id(self, value):
        """ Set associated_send_multicast_channel_map_id value.

            Notes:
                The ID of the send Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedSendMulticastChannelMapID` in VSD API.
                
        """
        self._associated_send_multicast_channel_map_id = value

    
    @property
    def associated_trunk_id(self):
        """ Get associated_trunk_id value.

            Notes:
                The trunk uuid associated with another vport of trunkRole PARENT_PORT. Can be specified only if trunkRole of this vport is SUB_PORT.

                
                This attribute is named `associatedTrunkID` in VSD API.
                
        """
        return self._associated_trunk_id

    @associated_trunk_id.setter
    def associated_trunk_id(self, value):
        """ Set associated_trunk_id value.

            Notes:
                The trunk uuid associated with another vport of trunkRole PARENT_PORT. Can be specified only if trunkRole of this vport is SUB_PORT.

                
                This attribute is named `associatedTrunkID` in VSD API.
                
        """
        self._associated_trunk_id = value

    
    @property
    def sub_type(self):
        """ Get sub_type value.

            Notes:
                Sub type of vport - possible values are NONE/VNF

                
                This attribute is named `subType` in VSD API.
                
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        """ Set sub_type value.

            Notes:
                Sub type of vport - possible values are NONE/VNF

                
                This attribute is named `subType` in VSD API.
                
        """
        self._sub_type = value

    
    @property
    def multi_nic_vport_id(self):
        """ Get multi_nic_vport_id value.

            Notes:
                ID of the Multi NIC VPort associated with the VPort

                
                This attribute is named `multiNICVPortID` in VSD API.
                
        """
        return self._multi_nic_vport_id

    @multi_nic_vport_id.setter
    def multi_nic_vport_id(self, value):
        """ Set multi_nic_vport_id value.

            Notes:
                ID of the Multi NIC VPort associated with the VPort

                
                This attribute is named `multiNICVPortID` in VSD API.
                
        """
        self._multi_nic_vport_id = value

    
    @property
    def multicast(self):
        """ Get multicast value.

            Notes:
                Indicates multicast policy on Vport.

                
        """
        return self._multicast

    @multicast.setter
    def multicast(self, value):
        """ Set multicast value.

            Notes:
                Indicates multicast policy on Vport.

                
        """
        self._multicast = value

    
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
                Type of vport. Possible values are VM, HOST, BRIDGE, CONTAINER.

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                Type of vport. Possible values are VM, HOST, BRIDGE, CONTAINER.

                
        """
        self._type = value

    
    @property
    def system_type(self):
        """ Get system_type value.

            Notes:
                Indicates what system it is.

                
                This attribute is named `systemType` in VSD API.
                
        """
        return self._system_type

    @system_type.setter
    def system_type(self, value):
        """ Set system_type value.

            Notes:
                Indicates what system it is.

                
                This attribute is named `systemType` in VSD API.
                
        """
        self._system_type = value

    

    