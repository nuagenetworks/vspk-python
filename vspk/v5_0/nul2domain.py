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




from .fetchers import NUGatewaysFetcher


from .fetchers import NUTCAsFetcher


from .fetchers import NUAddressRangesFetcher


from .fetchers import NURedirectionTargetsFetcher


from .fetchers import NURedundancyGroupsFetcher


from .fetchers import NUDeploymentFailuresFetcher


from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUNetworkPerformanceBindingsFetcher


from .fetchers import NUPGExpressionsFetcher


from .fetchers import NUEgressACLEntryTemplatesFetcher


from .fetchers import NUEgressACLTemplatesFetcher


from .fetchers import NUEgressAdvFwdTemplatesFetcher


from .fetchers import NUDHCPOptionsFetcher


from .fetchers import NUVirtualFirewallPoliciesFetcher


from .fetchers import NUVirtualFirewallRulesFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVMsFetcher


from .fetchers import NUVMInterfacesFetcher


from .fetchers import NUIngressACLEntryTemplatesFetcher


from .fetchers import NUIngressACLTemplatesFetcher


from .fetchers import NUIngressAdvFwdTemplatesFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NUPolicyGroupsFetcher


from .fetchers import NUContainersFetcher


from .fetchers import NUContainerInterfacesFetcher


from .fetchers import NUQOSsFetcher


from .fetchers import NUHostInterfacesFetcher


from .fetchers import NUUplinkRDsFetcher


from .fetchers import NUVPNConnectionsFetcher


from .fetchers import NUVPortsFetcher


from .fetchers import NUApplicationsFetcher


from .fetchers import NUApplicationperformancemanagementbindingsFetcher


from .fetchers import NUBridgeInterfacesFetcher


from .fetchers import NUGroupsFetcher


from .fetchers import NUProxyARPFiltersFetcher


from .fetchers import NUNSGatewaySummariesFetcher


from .fetchers import NUStaticRoutesFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUStatisticsPoliciesFetcher


from .fetchers import NUEventLogsFetcher


from .fetchers import NUOverlayMirrorDestinationsFetcher

from bambou import NURESTObject


class NUL2Domain(NURESTObject):
    """ Represents a L2Domain in the VSD

        Notes:
            This is the definition of a l2 domain associated with a Enterprise.
    """

    __rest_name__ = "l2domain"
    __resource_name__ = "l2domains"

    
    ## Constants
    
    CONST_UPLINK_PREFERENCE_PRIMARY_SECONDARY = "PRIMARY_SECONDARY"
    
    CONST_FLOW_COLLECTION_ENABLED_INHERITED = "INHERITED"
    
    CONST_DPI_ENABLED = "ENABLED"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ENTITY_STATE_MARKED_FOR_DELETION = "MARKED_FOR_DELETION"
    
    CONST_IP_TYPE_IPV4 = "IPV4"
    
    CONST_MAINTENANCE_MODE_DISABLED = "DISABLED"
    
    CONST_USE_GLOBAL_MAC_ENABLED = "ENABLED"
    
    CONST_MAINTENANCE_MODE_ENABLED = "ENABLED"
    
    CONST_UPLINK_PREFERENCE_SYMMETRIC = "SYMMETRIC"
    
    CONST_FLOW_COLLECTION_ENABLED_DISABLED = "DISABLED"
    
    CONST_USE_GLOBAL_MAC_DISABLED = "DISABLED"
    
    CONST_POLICY_CHANGE_STATUS_STARTED = "STARTED"
    
    CONST_UPLINK_PREFERENCE_SECONDARY_PRIMARY = "SECONDARY_PRIMARY"
    
    CONST_ENTITY_STATE_UNDER_CONSTRUCTION = "UNDER_CONSTRUCTION"
    
    CONST_MULTICAST_ENABLED = "ENABLED"
    
    CONST_MULTICAST_INHERITED = "INHERITED"
    
    CONST_POLICY_CHANGE_STATUS_APPLIED = "APPLIED"
    
    CONST_UPLINK_PREFERENCE_SECONDARY = "SECONDARY"
    
    CONST_FLOW_COLLECTION_ENABLED_ENABLED = "ENABLED"
    
    CONST_MULTICAST_DISABLED = "DISABLED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENCRYPTION_DISABLED = "DISABLED"
    
    CONST_UPLINK_PREFERENCE_PRIMARY = "PRIMARY"
    
    CONST_DPI_DISABLED = "DISABLED"
    
    CONST_MAINTENANCE_MODE_ENABLED_INHERITED = "ENABLED_INHERITED"
    
    CONST_ENCRYPTION_ENABLED = "ENABLED"
    
    CONST_IP_TYPE_DUALSTACK = "DUALSTACK"
    
    CONST_POLICY_CHANGE_STATUS_DISCARDED = "DISCARDED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a L2Domain instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> l2domain = NUL2Domain(id=u'xxxx-xxx-xxx-xxx', name=u'L2Domain')
                >>> l2domain = NUL2Domain(data=my_dict)
        """

        super(NUL2Domain, self).__init__()

        # Read/Write Attributes
        
        self._dhcp_managed = None
        self._dpi = None
        self._ip_type = None
        self._ipv6_address = None
        self._ipv6_gateway = None
        self._vxlanecmp_enabled = None
        self._maintenance_mode = None
        self._name = None
        self._last_updated_by = None
        self._gateway = None
        self._gateway_mac_address = None
        self._address = None
        self._template_id = None
        self._service_id = None
        self._description = None
        self._netmask = None
        self._flow_collection_enabled = None
        self._vn_id = None
        self._encryption = None
        self._ingress_replication_enabled = None
        self._entity_scope = None
        self._entity_state = None
        self._policy_change_status = None
        self._route_distinguisher = None
        self._route_target = None
        self._routed_vpls_enabled = None
        self._uplink_preference = None
        self._use_global_mac = None
        self._associated_multicast_channel_map_id = None
        self._associated_shared_network_resource_id = None
        self._associated_underlay_id = None
        self._stretched = None
        self._multicast = None
        self._customer_id = None
        self._external_id = None
        self._dynamic_ipv6_address = None
        
        self.expose_attribute(local_name="dhcp_managed", remote_name="DHCPManaged", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dpi", remote_name="DPI", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED'])
        self.expose_attribute(local_name="ip_type", remote_name="IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DUALSTACK', u'IPV4'])
        self.expose_attribute(local_name="ipv6_address", remote_name="IPv6Address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ipv6_gateway", remote_name="IPv6Gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vxlanecmp_enabled", remote_name="VXLANECMPEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="maintenance_mode", remote_name="maintenanceMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'ENABLED_INHERITED'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway", remote_name="gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_mac_address", remote_name="gatewayMACAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="service_id", remote_name="serviceID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="flow_collection_enabled", remote_name="flowCollectionEnabled", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="vn_id", remote_name="vnId", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="encryption", remote_name="encryption", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED'])
        self.expose_attribute(local_name="ingress_replication_enabled", remote_name="ingressReplicationEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="entity_state", remote_name="entityState", attribute_type=str, is_required=False, is_unique=False, choices=[u'MARKED_FOR_DELETION', u'UNDER_CONSTRUCTION'])
        self.expose_attribute(local_name="policy_change_status", remote_name="policyChangeStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'APPLIED', u'DISCARDED', u'STARTED'])
        self.expose_attribute(local_name="route_distinguisher", remote_name="routeDistinguisher", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="route_target", remote_name="routeTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="routed_vpls_enabled", remote_name="routedVPLSEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="uplink_preference", remote_name="uplinkPreference", attribute_type=str, is_required=False, is_unique=False, choices=[u'PRIMARY', u'PRIMARY_SECONDARY', u'SECONDARY', u'SECONDARY_PRIMARY', u'SYMMETRIC'])
        self.expose_attribute(local_name="use_global_mac", remote_name="useGlobalMAC", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED'])
        self.expose_attribute(local_name="associated_multicast_channel_map_id", remote_name="associatedMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_shared_network_resource_id", remote_name="associatedSharedNetworkResourceID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_underlay_id", remote_name="associatedUnderlayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stretched", remote_name="stretched", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast", remote_name="multicast", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="customer_id", remote_name="customerID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="dynamic_ipv6_address", remote_name="dynamicIpv6Address", attribute_type=bool, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.gateways = NUGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.address_ranges = NUAddressRangesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.redirection_targets = NURedirectionTargetsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.redundancy_groups = NURedundancyGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.deployment_failures = NUDeploymentFailuresFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.network_performance_bindings = NUNetworkPerformanceBindingsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.pg_expressions = NUPGExpressionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.egress_acl_entry_templates = NUEgressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.egress_acl_templates = NUEgressACLTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.egress_adv_fwd_templates = NUEgressAdvFwdTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.dhcp_options = NUDHCPOptionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.virtual_firewall_policies = NUVirtualFirewallPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.virtual_firewall_rules = NUVirtualFirewallRulesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ingress_acl_entry_templates = NUIngressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ingress_acl_templates = NUIngressACLTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ingress_adv_fwd_templates = NUIngressAdvFwdTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.policy_groups = NUPolicyGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.containers = NUContainersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.container_interfaces = NUContainerInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.host_interfaces = NUHostInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.uplink_rds = NUUplinkRDsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vpn_connections = NUVPNConnectionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.applications = NUApplicationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.applicationperformancemanagementbindings = NUApplicationperformancemanagementbindingsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bridge_interfaces = NUBridgeInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.groups = NUGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.proxy_arp_filters = NUProxyARPFiltersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_gateway_summaries = NUNSGatewaySummariesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.static_routes = NUStaticRoutesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.overlay_mirror_destinations = NUOverlayMirrorDestinationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def dhcp_managed(self):
        """ Get dhcp_managed value.

            Notes:
                decides whether L2Domain / L2Domain template DHCP is managed by VSD

                
                This attribute is named `DHCPManaged` in VSD API.
                
        """
        return self._dhcp_managed

    @dhcp_managed.setter
    def dhcp_managed(self, value):
        """ Set dhcp_managed value.

            Notes:
                decides whether L2Domain / L2Domain template DHCP is managed by VSD

                
                This attribute is named `DHCPManaged` in VSD API.
                
        """
        self._dhcp_managed = value

    
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
                IPV6 address of the route - Optional

                
                This attribute is named `IPv6Address` in VSD API.
                
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, value):
        """ Set ipv6_address value.

            Notes:
                IPV6 address of the route - Optional

                
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
    def vxlanecmp_enabled(self):
        """ Get vxlanecmp_enabled value.

            Notes:
                Determines whether VXLAN-ECMP are enabled on this domain.

                
                This attribute is named `VXLANECMPEnabled` in VSD API.
                
        """
        return self._vxlanecmp_enabled

    @vxlanecmp_enabled.setter
    def vxlanecmp_enabled(self, value):
        """ Set vxlanecmp_enabled value.

            Notes:
                Determines whether VXLAN-ECMP are enabled on this domain.

                
                This attribute is named `VXLANECMPEnabled` in VSD API.
                
        """
        self._vxlanecmp_enabled = value

    
    @property
    def maintenance_mode(self):
        """ Get maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the L2Domain is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        return self._maintenance_mode

    @maintenance_mode.setter
    def maintenance_mode(self, value):
        """ Set maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the L2Domain is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        self._maintenance_mode = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

                
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
                The IP address of the gateway of this l2 domain

                
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """ Set gateway value.

            Notes:
                The IP address of the gateway of this l2 domain

                
        """
        self._gateway = value

    
    @property
    def gateway_mac_address(self):
        """ Get gateway_mac_address value.

            Notes:
                The MAC address of the Gateway.

                
                This attribute is named `gatewayMACAddress` in VSD API.
                
        """
        return self._gateway_mac_address

    @gateway_mac_address.setter
    def gateway_mac_address(self, value):
        """ Set gateway_mac_address value.

            Notes:
                The MAC address of the Gateway.

                
                This attribute is named `gatewayMACAddress` in VSD API.
                
        """
        self._gateway_mac_address = value

    
    @property
    def address(self):
        """ Get address value.

            Notes:
                Network address of the L2Domain / L2Domain template defined. 

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                Network address of the L2Domain / L2Domain template defined. 

                
        """
        self._address = value

    
    @property
    def template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the L2 Domain template that this L2 Domain object was derived from

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the L2 Domain template that this L2 Domain object was derived from

                
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
                A description field provided by the user that identifies the L2Domain / L2Domain template.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description field provided by the user that identifies the L2Domain / L2Domain template.

                
        """
        self._description = value

    
    @property
    def netmask(self):
        """ Get netmask value.

            Notes:
                Netmask of the L2Domain / L2Domain template defined

                
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """ Set netmask value.

            Notes:
                Netmask of the L2Domain / L2Domain template defined

                
        """
        self._netmask = value

    
    @property
    def flow_collection_enabled(self):
        """ Get flow_collection_enabled value.

            Notes:
                Determines whether or not flow collection is enabled.

                
                This attribute is named `flowCollectionEnabled` in VSD API.
                
        """
        return self._flow_collection_enabled

    @flow_collection_enabled.setter
    def flow_collection_enabled(self, value):
        """ Set flow_collection_enabled value.

            Notes:
                Determines whether or not flow collection is enabled.

                
                This attribute is named `flowCollectionEnabled` in VSD API.
                
        """
        self._flow_collection_enabled = value

    
    @property
    def vn_id(self):
        """ Get vn_id value.

            Notes:
                Current network's globally unique VXLAN network identifier

                
                This attribute is named `vnId` in VSD API.
                
        """
        return self._vn_id

    @vn_id.setter
    def vn_id(self, value):
        """ Set vn_id value.

            Notes:
                Current network's globally unique VXLAN network identifier

                
                This attribute is named `vnId` in VSD API.
                
        """
        self._vn_id = value

    
    @property
    def encryption(self):
        """ Get encryption value.

            Notes:
                Determines whether IPSEC is enabled Possible values are ENABLED, DISABLED, .

                
        """
        return self._encryption

    @encryption.setter
    def encryption(self, value):
        """ Set encryption value.

            Notes:
                Determines whether IPSEC is enabled Possible values are ENABLED, DISABLED, .

                
        """
        self._encryption = value

    
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
    def policy_change_status(self):
        """ Get policy_change_status value.

            Notes:
                None

                
                This attribute is named `policyChangeStatus` in VSD API.
                
        """
        return self._policy_change_status

    @policy_change_status.setter
    def policy_change_status(self, value):
        """ Set policy_change_status value.

            Notes:
                None

                
                This attribute is named `policyChangeStatus` in VSD API.
                
        """
        self._policy_change_status = value

    
    @property
    def route_distinguisher(self):
        """ Get route_distinguisher value.

            Notes:
                Route distinguisher that is used by the BGP-EVPN protocol in VSC. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        return self._route_distinguisher

    @route_distinguisher.setter
    def route_distinguisher(self, value):
        """ Set route_distinguisher value.

            Notes:
                Route distinguisher that is used by the BGP-EVPN protocol in VSC. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        self._route_distinguisher = value

    
    @property
    def route_target(self):
        """ Get route_target value.

            Notes:
                Route target that is used by the BGP-EVPN protocol in VSC. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        return self._route_target

    @route_target.setter
    def route_target(self, value):
        """ Set route_target value.

            Notes:
                Route target that is used by the BGP-EVPN protocol in VSC. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        self._route_target = value

    
    @property
    def routed_vpls_enabled(self):
        """ Get routed_vpls_enabled value.

            Notes:
                Determines whether routed VPLS services are enabled on this domain.

                
                This attribute is named `routedVPLSEnabled` in VSD API.
                
        """
        return self._routed_vpls_enabled

    @routed_vpls_enabled.setter
    def routed_vpls_enabled(self, value):
        """ Set routed_vpls_enabled value.

            Notes:
                Determines whether routed VPLS services are enabled on this domain.

                
                This attribute is named `routedVPLSEnabled` in VSD API.
                
        """
        self._routed_vpls_enabled = value

    
    @property
    def uplink_preference(self):
        """ Get uplink_preference value.

            Notes:
                Indicates the preferencial path selection for network traffic in this domain - Default is Primary 1 and Secondary 2. Possible values are PRIMARY_SECONDARY, SECONDARY_PRIMARY, PRIMARY, SECONDARY, SYMMETRIC, .

                
                This attribute is named `uplinkPreference` in VSD API.
                
        """
        return self._uplink_preference

    @uplink_preference.setter
    def uplink_preference(self, value):
        """ Set uplink_preference value.

            Notes:
                Indicates the preferencial path selection for network traffic in this domain - Default is Primary 1 and Secondary 2. Possible values are PRIMARY_SECONDARY, SECONDARY_PRIMARY, PRIMARY, SECONDARY, SYMMETRIC, .

                
                This attribute is named `uplinkPreference` in VSD API.
                
        """
        self._uplink_preference = value

    
    @property
    def use_global_mac(self):
        """ Get use_global_mac value.

            Notes:
                Enable this flag to use system configured globalMACAddress as the gateway mac address for managed l2 domains

                
                This attribute is named `useGlobalMAC` in VSD API.
                
        """
        return self._use_global_mac

    @use_global_mac.setter
    def use_global_mac(self, value):
        """ Set use_global_mac value.

            Notes:
                Enable this flag to use system configured globalMACAddress as the gateway mac address for managed l2 domains

                
                This attribute is named `useGlobalMAC` in VSD API.
                
        """
        self._use_global_mac = value

    
    @property
    def associated_multicast_channel_map_id(self):
        """ Get associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_multicast_channel_map_id

    @associated_multicast_channel_map_id.setter
    def associated_multicast_channel_map_id(self, value):
        """ Set associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        self._associated_multicast_channel_map_id = value

    
    @property
    def associated_shared_network_resource_id(self):
        """ Get associated_shared_network_resource_id value.

            Notes:
                The ID of the L2 Domain  that this L2 Domain object is pointing to

                
                This attribute is named `associatedSharedNetworkResourceID` in VSD API.
                
        """
        return self._associated_shared_network_resource_id

    @associated_shared_network_resource_id.setter
    def associated_shared_network_resource_id(self, value):
        """ Set associated_shared_network_resource_id value.

            Notes:
                The ID of the L2 Domain  that this L2 Domain object is pointing to

                
                This attribute is named `associatedSharedNetworkResourceID` in VSD API.
                
        """
        self._associated_shared_network_resource_id = value

    
    @property
    def associated_underlay_id(self):
        """ Get associated_underlay_id value.

            Notes:
                The ID of the Underlay entity to which this L2 Domain is associated.

                
                This attribute is named `associatedUnderlayID` in VSD API.
                
        """
        return self._associated_underlay_id

    @associated_underlay_id.setter
    def associated_underlay_id(self, value):
        """ Set associated_underlay_id value.

            Notes:
                The ID of the Underlay entity to which this L2 Domain is associated.

                
                This attribute is named `associatedUnderlayID` in VSD API.
                
        """
        self._associated_underlay_id = value

    
    @property
    def stretched(self):
        """ Get stretched value.

            Notes:
                Indicates whether this domain is streched,if so remote VM resolutions will be allowed

                
        """
        return self._stretched

    @stretched.setter
    def stretched(self, value):
        """ Set stretched value.

            Notes:
                Indicates whether this domain is streched,if so remote VM resolutions will be allowed

                
        """
        self._stretched = value

    
    @property
    def multicast(self):
        """ Get multicast value.

            Notes:
                Indicates multicast policy on L2Domain.

                
        """
        return self._multicast

    @multicast.setter
    def multicast(self, value):
        """ Set multicast value.

            Notes:
                Indicates multicast policy on L2Domain.

                
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
    