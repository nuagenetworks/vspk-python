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




from .fetchers import NUPATIPEntriesFetcher


from .fetchers import NUTCAsFetcher


from .fetchers import NUAddressRangesFetcher


from .fetchers import NUDefaultGatewaysFetcher


from .fetchers import NUDeploymentFailuresFetcher


from .fetchers import NUVMResyncsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUBGPNeighborsFetcher


from .fetchers import NUDHCPOptionsFetcher


from .fetchers import NUVirtualIPsFetcher


from .fetchers import NUIKEGatewayConnectionsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVMsFetcher


from .fetchers import NUVMInterfacesFetcher


from .fetchers import NUEnterprisePermissionsFetcher


from .fetchers import NUContainersFetcher


from .fetchers import NUContainerInterfacesFetcher


from .fetchers import NUContainerResyncsFetcher


from .fetchers import NUQOSsFetcher


from .fetchers import NUVPortsFetcher


from .fetchers import NUIPReservationsFetcher


from .fetchers import NUProxyARPFiltersFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUStatisticsPoliciesFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUSubnet(NURESTObject):
    """ Represents a Subnet in the VSD

        Notes:
            This is the definition of a subnet associated with a Zone.
    """

    __rest_name__ = "subnet"
    __resource_name__ = "subnets"

    
    ## Constants
    
    CONST_PAT_ENABLED_DISABLED = "DISABLED"
    
    CONST_PAT_ENABLED_INHERITED = "INHERITED"
    
    CONST_USE_GLOBAL_MAC_DISABLED = "DISABLED"
    
    CONST_RESOURCE_TYPE_FLOATING = "FLOATING"
    
    CONST_RESOURCE_TYPE_NSG_VNF = "NSG_VNF"
    
    CONST_DPI_ENABLED = "ENABLED"
    
    CONST_DHCP_RELAY_STATUS_DISABLED = "DISABLED"
    
    CONST_DPI_INHERITED = "INHERITED"
    
    CONST_IP_TYPE_IPV4 = "IPV4"
    
    CONST_UNDERLAY_ENABLED_ENABLED = "ENABLED"
    
    CONST_MAINTENANCE_MODE_DISABLED = "DISABLED"
    
    CONST_RESOURCE_TYPE_STANDARD = "STANDARD"
    
    CONST_USE_GLOBAL_MAC_ENABLED = "ENABLED"
    
    CONST_MAINTENANCE_MODE_ENABLED = "ENABLED"
    
    CONST_RESOURCE_TYPE_PUBLIC = "PUBLIC"
    
    CONST_UNDERLAY_ENABLED_INHERITED = "INHERITED"
    
    CONST_USE_GLOBAL_MAC_ENTERPRISE_DEFAULT = "ENTERPRISE_DEFAULT"
    
    CONST_ENCRYPTION_INHERITED = "INHERITED"
    
    CONST_ENTITY_STATE_UNDER_CONSTRUCTION = "UNDER_CONSTRUCTION"
    
    CONST_PAT_ENABLED_ENABLED = "ENABLED"
    
    CONST_MULTICAST_ENABLED = "ENABLED"
    
    CONST_MULTICAST_INHERITED = "INHERITED"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_DHCP_RELAY_STATUS_ENABLED = "ENABLED"
    
    CONST_MULTICAST_DISABLED = "DISABLED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENCRYPTION_DISABLED = "DISABLED"
    
    CONST_DPI_DISABLED = "DISABLED"
    
    CONST_MAINTENANCE_MODE_ENABLED_INHERITED = "ENABLED_INHERITED"
    
    CONST_ENCRYPTION_ENABLED = "ENABLED"
    
    CONST_IP_TYPE_DUALSTACK = "DUALSTACK"
    
    CONST_ENTITY_STATE_MARKED_FOR_DELETION = "MARKED_FOR_DELETION"
    
    CONST_UNDERLAY_ENABLED_DISABLED = "DISABLED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Subnet instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> subnet = NUSubnet(id=u'xxxx-xxx-xxx-xxx', name=u'Subnet')
                >>> subnet = NUSubnet(data=my_dict)
        """

        super(NUSubnet, self).__init__()

        # Read/Write Attributes
        
        self._pat_enabled = None
        self._dhcp_relay_status = None
        self._dpi = None
        self._ip_type = None
        self._ipv6_address = None
        self._ipv6_gateway = None
        self._evpn_enabled = None
        self._maintenance_mode = None
        self._name = None
        self._last_updated_by = None
        self._gateway = None
        self._gateway_mac_address = None
        self._access_restriction_enabled = None
        self._address = None
        self._advertise = None
        self._template_id = None
        self._service_id = None
        self._description = None
        self._resource_type = None
        self._netmask = None
        self._vn_id = None
        self._encryption = None
        self._underlay = None
        self._underlay_enabled = None
        self._ingress_replication_enabled = None
        self._entity_scope = None
        self._entity_state = None
        self._policy_group_id = None
        self._domain_service_label = None
        self._route_distinguisher = None
        self._route_target = None
        self._split_subnet = None
        self._proxy_arp = None
        self._use_global_mac = None
        self._associated_multicast_channel_map_id = None
        self._associated_shared_network_resource_id = None
        self._public = None
        self._subnet_vlanid = None
        self._multi_home_enabled = None
        self._multicast = None
        self._customer_id = None
        self._external_id = None
        self._dynamic_ipv6_address = None
        
        self.expose_attribute(local_name="pat_enabled", remote_name="PATEnabled", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="dhcp_relay_status", remote_name="DHCPRelayStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED'])
        self.expose_attribute(local_name="dpi", remote_name="DPI", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="ip_type", remote_name="IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DUALSTACK', u'IPV4'])
        self.expose_attribute(local_name="ipv6_address", remote_name="IPv6Address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ipv6_gateway", remote_name="IPv6Gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="evpn_enabled", remote_name="EVPNEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="maintenance_mode", remote_name="maintenanceMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'ENABLED_INHERITED'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway", remote_name="gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_mac_address", remote_name="gatewayMACAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="access_restriction_enabled", remote_name="accessRestrictionEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="advertise", remote_name="advertise", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="service_id", remote_name="serviceID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="resource_type", remote_name="resourceType", attribute_type=str, is_required=False, is_unique=False, choices=[u'FLOATING', u'NSG_VNF', u'PUBLIC', u'STANDARD'])
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vn_id", remote_name="vnId", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="encryption", remote_name="encryption", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="underlay", remote_name="underlay", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="underlay_enabled", remote_name="underlayEnabled", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="ingress_replication_enabled", remote_name="ingressReplicationEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="entity_state", remote_name="entityState", attribute_type=str, is_required=False, is_unique=False, choices=[u'MARKED_FOR_DELETION', u'UNDER_CONSTRUCTION'])
        self.expose_attribute(local_name="policy_group_id", remote_name="policyGroupID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="domain_service_label", remote_name="domainServiceLabel", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="route_distinguisher", remote_name="routeDistinguisher", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="route_target", remote_name="routeTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="split_subnet", remote_name="splitSubnet", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="proxy_arp", remote_name="proxyARP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="use_global_mac", remote_name="useGlobalMAC", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'ENTERPRISE_DEFAULT'])
        self.expose_attribute(local_name="associated_multicast_channel_map_id", remote_name="associatedMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_shared_network_resource_id", remote_name="associatedSharedNetworkResourceID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="public", remote_name="public", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="subnet_vlanid", remote_name="subnetVLANID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multi_home_enabled", remote_name="multiHomeEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast", remote_name="multicast", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="customer_id", remote_name="customerID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="dynamic_ipv6_address", remote_name="dynamicIpv6Address", attribute_type=bool, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.patip_entries = NUPATIPEntriesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.address_ranges = NUAddressRangesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.default_gateways = NUDefaultGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.deployment_failures = NUDeploymentFailuresFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vm_resyncs = NUVMResyncsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bgp_neighbors = NUBGPNeighborsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.dhcp_options = NUDHCPOptionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.virtual_ips = NUVirtualIPsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ike_gateway_connections = NUIKEGatewayConnectionsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.containers = NUContainersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.container_interfaces = NUContainerInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.container_resyncs = NUContainerResyncsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ip_reservations = NUIPReservationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.proxy_arp_filters = NUProxyARPFiltersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def pat_enabled(self):
        """ Get pat_enabled value.

            Notes:
                None

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        return self._pat_enabled

    @pat_enabled.setter
    def pat_enabled(self, value):
        """ Set pat_enabled value.

            Notes:
                None

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        self._pat_enabled = value

    
    @property
    def dhcp_relay_status(self):
        """ Get dhcp_relay_status value.

            Notes:
                None

                
                This attribute is named `DHCPRelayStatus` in VSD API.
                
        """
        return self._dhcp_relay_status

    @dhcp_relay_status.setter
    def dhcp_relay_status(self, value):
        """ Set dhcp_relay_status value.

            Notes:
                None

                
                This attribute is named `DHCPRelayStatus` in VSD API.
                
        """
        self._dhcp_relay_status = value

    
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
    def ip_type(self):
        """ Get ip_type value.

            Notes:
                IPv4 or DUALSTACK

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        """ Set ip_type value.

            Notes:
                IPv4 or DUALSTACK

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    
    @property
    def ipv6_address(self):
        """ Get ipv6_address value.

            Notes:
                IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

                
                This attribute is named `IPv6Address` in VSD API.
                
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, value):
        """ Set ipv6_address value.

            Notes:
                IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

                
                This attribute is named `IPv6Address` in VSD API.
                
        """
        self._ipv6_address = value

    
    @property
    def ipv6_gateway(self):
        """ Get ipv6_gateway value.

            Notes:
                The IPv6 address of the gateway of this subnet

                
                This attribute is named `IPv6Gateway` in VSD API.
                
        """
        return self._ipv6_gateway

    @ipv6_gateway.setter
    def ipv6_gateway(self, value):
        """ Set ipv6_gateway value.

            Notes:
                The IPv6 address of the gateway of this subnet

                
                This attribute is named `IPv6Gateway` in VSD API.
                
        """
        self._ipv6_gateway = value

    
    @property
    def evpn_enabled(self):
        """ Get evpn_enabled value.

            Notes:
                Indicates if EVPN capabilities are enabled for this subnet.

                
                This attribute is named `EVPNEnabled` in VSD API.
                
        """
        return self._evpn_enabled

    @evpn_enabled.setter
    def evpn_enabled(self, value):
        """ Set evpn_enabled value.

            Notes:
                Indicates if EVPN capabilities are enabled for this subnet.

                
                This attribute is named `EVPNEnabled` in VSD API.
                
        """
        self._evpn_enabled = value

    
    @property
    def maintenance_mode(self):
        """ Get maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the SubNetwork is accepting VM activation requests.

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        return self._maintenance_mode

    @maintenance_mode.setter
    def maintenance_mode(self, value):
        """ Set maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the SubNetwork is accepting VM activation requests.

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        self._maintenance_mode = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

                
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
    def gateway(self):
        """ Get gateway value.

            Notes:
                The IP address of the gateway of this subnet

                
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """ Set gateway value.

            Notes:
                The IP address of the gateway of this subnet

                
        """
        self._gateway = value

    
    @property
    def gateway_mac_address(self):
        """ Get gateway_mac_address value.

            Notes:
                None

                
                This attribute is named `gatewayMACAddress` in VSD API.
                
        """
        return self._gateway_mac_address

    @gateway_mac_address.setter
    def gateway_mac_address(self, value):
        """ Set gateway_mac_address value.

            Notes:
                None

                
                This attribute is named `gatewayMACAddress` in VSD API.
                
        """
        self._gateway_mac_address = value

    
    @property
    def access_restriction_enabled(self):
        """ Get access_restriction_enabled value.

            Notes:
                This attribute specifies whether subnet is enabled with access restrictions. Note: Applicable to shared infrastructure enterprise subnets.

                
                This attribute is named `accessRestrictionEnabled` in VSD API.
                
        """
        return self._access_restriction_enabled

    @access_restriction_enabled.setter
    def access_restriction_enabled(self, value):
        """ Set access_restriction_enabled value.

            Notes:
                This attribute specifies whether subnet is enabled with access restrictions. Note: Applicable to shared infrastructure enterprise subnets.

                
                This attribute is named `accessRestrictionEnabled` in VSD API.
                
        """
        self._access_restriction_enabled = value

    
    @property
    def address(self):
        """ Get address value.

            Notes:
                IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

                
        """
        self._address = value

    
    @property
    def advertise(self):
        """ Get advertise value.

            Notes:
                Subnet will be advertised in Overlay and WAN BGP

                
        """
        return self._advertise

    @advertise.setter
    def advertise(self, value):
        """ Set advertise value.

            Notes:
                Subnet will be advertised in Overlay and WAN BGP

                
        """
        self._advertise = value

    
    @property
    def template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the subnet template that this subnet object was derived from

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the subnet template that this subnet object was derived from

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    
    @property
    def service_id(self):
        """ Get service_id value.

            Notes:
                The service ID used by the VSCs to identify this subnet

                
                This attribute is named `serviceID` in VSD API.
                
        """
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        """ Set service_id value.

            Notes:
                The service ID used by the VSCs to identify this subnet

                
                This attribute is named `serviceID` in VSD API.
                
        """
        self._service_id = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description field provided by the user that identifies the subnet

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description field provided by the user that identifies the subnet

                
        """
        self._description = value

    
    @property
    def resource_type(self):
        """ Get resource_type value.

            Notes:
                Defines the type of the subnet, PUBLIC,FLOATING,STANDARD OR NSG_VNF

                
                This attribute is named `resourceType` in VSD API.
                
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, value):
        """ Set resource_type value.

            Notes:
                Defines the type of the subnet, PUBLIC,FLOATING,STANDARD OR NSG_VNF

                
                This attribute is named `resourceType` in VSD API.
                
        """
        self._resource_type = value

    
    @property
    def netmask(self):
        """ Get netmask value.

            Notes:
                Netmask of the subnet defined

                
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """ Set netmask value.

            Notes:
                Netmask of the subnet defined

                
        """
        self._netmask = value

    
    @property
    def vn_id(self):
        """ Get vn_id value.

            Notes:
                Current Network's  globally unique  VXLAN network identifier generated by VSD

                
                This attribute is named `vnId` in VSD API.
                
        """
        return self._vn_id

    @vn_id.setter
    def vn_id(self, value):
        """ Set vn_id value.

            Notes:
                Current Network's  globally unique  VXLAN network identifier generated by VSD

                
                This attribute is named `vnId` in VSD API.
                
        """
        self._vn_id = value

    
    @property
    def encryption(self):
        """ Get encryption value.

            Notes:
                Determines whether or not IPSEC is enabled.

                
        """
        return self._encryption

    @encryption.setter
    def encryption(self, value):
        """ Set encryption value.

            Notes:
                Determines whether or not IPSEC is enabled.

                
        """
        self._encryption = value

    
    @property
    def underlay(self):
        """ Get underlay value.

            Notes:
                Read Only Boolean flag to indicate whether underlay is enabled directly or indirectly

                
        """
        return self._underlay

    @underlay.setter
    def underlay(self, value):
        """ Set underlay value.

            Notes:
                Read Only Boolean flag to indicate whether underlay is enabled directly or indirectly

                
        """
        self._underlay = value

    
    @property
    def underlay_enabled(self):
        """ Get underlay_enabled value.

            Notes:
                Indicates whether UNDERLAY is enabled for the subnets in this domain

                
                This attribute is named `underlayEnabled` in VSD API.
                
        """
        return self._underlay_enabled

    @underlay_enabled.setter
    def underlay_enabled(self, value):
        """ Set underlay_enabled value.

            Notes:
                Indicates whether UNDERLAY is enabled for the subnets in this domain

                
                This attribute is named `underlayEnabled` in VSD API.
                
        """
        self._underlay_enabled = value

    
    @property
    def ingress_replication_enabled(self):
        """ Get ingress_replication_enabled value.

            Notes:
                Enables ingress replication for the VNI.

                
                This attribute is named `ingressReplicationEnabled` in VSD API.
                
        """
        return self._ingress_replication_enabled

    @ingress_replication_enabled.setter
    def ingress_replication_enabled(self, value):
        """ Set ingress_replication_enabled value.

            Notes:
                Enables ingress replication for the VNI.

                
                This attribute is named `ingressReplicationEnabled` in VSD API.
                
        """
        self._ingress_replication_enabled = value

    
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
    def entity_state(self):
        """ Get entity_state value.

            Notes:
                Intermediate State of L2 Domain.

                
                This attribute is named `entityState` in VSD API.
                
        """
        return self._entity_state

    @entity_state.setter
    def entity_state(self, value):
        """ Set entity_state value.

            Notes:
                Intermediate State of L2 Domain.

                
                This attribute is named `entityState` in VSD API.
                
        """
        self._entity_state = value

    
    @property
    def policy_group_id(self):
        """ Get policy_group_id value.

            Notes:
                PG ID for the subnet. This is unique per domain and will be in the range 1-4095

                
                This attribute is named `policyGroupID` in VSD API.
                
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, value):
        """ Set policy_group_id value.

            Notes:
                PG ID for the subnet. This is unique per domain and will be in the range 1-4095

                
                This attribute is named `policyGroupID` in VSD API.
                
        """
        self._policy_group_id = value

    
    @property
    def domain_service_label(self):
        """ Get domain_service_label value.

            Notes:
                Service ID or external label given to Domain

                
                This attribute is named `domainServiceLabel` in VSD API.
                
        """
        return self._domain_service_label

    @domain_service_label.setter
    def domain_service_label(self, value):
        """ Set domain_service_label value.

            Notes:
                Service ID or external label given to Domain

                
                This attribute is named `domainServiceLabel` in VSD API.
                
        """
        self._domain_service_label = value

    
    @property
    def route_distinguisher(self):
        """ Get route_distinguisher value.

            Notes:
                Route distinguisher for this subnet that is used by the BGP-EVPN protocol in VSC. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        return self._route_distinguisher

    @route_distinguisher.setter
    def route_distinguisher(self, value):
        """ Set route_distinguisher value.

            Notes:
                Route distinguisher for this subnet that is used by the BGP-EVPN protocol in VSC. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        self._route_distinguisher = value

    
    @property
    def route_target(self):
        """ Get route_target value.

            Notes:
                Route target for this subnet that is used by the BGP-EVPN protocol in VSC. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        return self._route_target

    @route_target.setter
    def route_target(self, value):
        """ Set route_target value.

            Notes:
                Route target for this subnet that is used by the BGP-EVPN protocol in VSC. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        self._route_target = value

    
    @property
    def split_subnet(self):
        """ Get split_subnet value.

            Notes:
                Block subnet routes

                
                This attribute is named `splitSubnet` in VSD API.
                
        """
        return self._split_subnet

    @split_subnet.setter
    def split_subnet(self, value):
        """ Set split_subnet value.

            Notes:
                Block subnet routes

                
                This attribute is named `splitSubnet` in VSD API.
                
        """
        self._split_subnet = value

    
    @property
    def proxy_arp(self):
        """ Get proxy_arp value.

            Notes:
                 When set, VRS will act as  ARP Proxy

                
                This attribute is named `proxyARP` in VSD API.
                
        """
        return self._proxy_arp

    @proxy_arp.setter
    def proxy_arp(self, value):
        """ Set proxy_arp value.

            Notes:
                 When set, VRS will act as  ARP Proxy

                
                This attribute is named `proxyARP` in VSD API.
                
        """
        self._proxy_arp = value

    
    @property
    def use_global_mac(self):
        """ Get use_global_mac value.

            Notes:
                if this flag is enabled, the system configured globalMACAddress will be used as the gateway mac address

                
                This attribute is named `useGlobalMAC` in VSD API.
                
        """
        return self._use_global_mac

    @use_global_mac.setter
    def use_global_mac(self, value):
        """ Set use_global_mac value.

            Notes:
                if this flag is enabled, the system configured globalMACAddress will be used as the gateway mac address

                
                This attribute is named `useGlobalMAC` in VSD API.
                
        """
        self._use_global_mac = value

    
    @property
    def associated_multicast_channel_map_id(self):
        """ Get associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this Subnet/Subnet Template is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_multicast_channel_map_id

    @associated_multicast_channel_map_id.setter
    def associated_multicast_channel_map_id(self, value):
        """ Set associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this Subnet/Subnet Template is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        self._associated_multicast_channel_map_id = value

    
    @property
    def associated_shared_network_resource_id(self):
        """ Get associated_shared_network_resource_id value.

            Notes:
                The ID of public subnet that is associated with this subnet

                
                This attribute is named `associatedSharedNetworkResourceID` in VSD API.
                
        """
        return self._associated_shared_network_resource_id

    @associated_shared_network_resource_id.setter
    def associated_shared_network_resource_id(self, value):
        """ Set associated_shared_network_resource_id value.

            Notes:
                The ID of public subnet that is associated with this subnet

                
                This attribute is named `associatedSharedNetworkResourceID` in VSD API.
                
        """
        self._associated_shared_network_resource_id = value

    
    @property
    def public(self):
        """ Get public value.

            Notes:
                when set to true means public subnet under a public zone

                
        """
        return self._public

    @public.setter
    def public(self, value):
        """ Set public value.

            Notes:
                when set to true means public subnet under a public zone

                
        """
        self._public = value

    
    @property
    def subnet_vlanid(self):
        """ Get subnet_vlanid value.

            Notes:
                Determines the VLANID for this associated Subnet.

                
                This attribute is named `subnetVLANID` in VSD API.
                
        """
        return self._subnet_vlanid

    @subnet_vlanid.setter
    def subnet_vlanid(self, value):
        """ Set subnet_vlanid value.

            Notes:
                Determines the VLANID for this associated Subnet.

                
                This attribute is named `subnetVLANID` in VSD API.
                
        """
        self._subnet_vlanid = value

    
    @property
    def multi_home_enabled(self):
        """ Get multi_home_enabled value.

            Notes:
                Boolean flag to indicate whether this is a Multi-homed subnet or not.

                
                This attribute is named `multiHomeEnabled` in VSD API.
                
        """
        return self._multi_home_enabled

    @multi_home_enabled.setter
    def multi_home_enabled(self, value):
        """ Set multi_home_enabled value.

            Notes:
                Boolean flag to indicate whether this is a Multi-homed subnet or not.

                
                This attribute is named `multiHomeEnabled` in VSD API.
                
        """
        self._multi_home_enabled = value

    
    @property
    def multicast(self):
        """ Get multicast value.

            Notes:
                multicast is enum that indicates multicast policy on Subnet/Subnet Template.

                
        """
        return self._multicast

    @multicast.setter
    def multicast(self, value):
        """ Set multicast value.

            Notes:
                multicast is enum that indicates multicast policy on Subnet/Subnet Template.

                
        """
        self._multicast = value

    
    @property
    def customer_id(self):
        """ Get customer_id value.

            Notes:
                CustomerID that is used by NETCONF MANAGER to identify this enterprise. This can be configured by root user.

                
                This attribute is named `customerID` in VSD API.
                
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        """ Set customer_id value.

            Notes:
                CustomerID that is used by NETCONF MANAGER to identify this enterprise. This can be configured by root user.

                
                This attribute is named `customerID` in VSD API.
                
        """
        self._customer_id = value

    
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
    def dynamic_ipv6_address(self):
        """ Get dynamic_ipv6_address value.

            Notes:
                Turn on or off dynamic allocation of IPV6 address

                
                This attribute is named `dynamicIpv6Address` in VSD API.
                
        """
        return self._dynamic_ipv6_address

    @dynamic_ipv6_address.setter
    def dynamic_ipv6_address(self, value):
        """ Set dynamic_ipv6_address value.

            Notes:
                Turn on or off dynamic allocation of IPV6 address

                
                This attribute is named `dynamicIpv6Address` in VSD API.
                
        """
        self._dynamic_ipv6_address = value

    

    
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
    