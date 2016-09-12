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


from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUEgressACLEntryTemplatesFetcher


from .fetchers import NUEgressACLTemplatesFetcher


from .fetchers import NUDomainFIPAclTemplatesFetcher


from .fetchers import NUFloatingIPACLTemplatesFetcher


from .fetchers import NUDHCPOptionsFetcher


from .fetchers import NULinksFetcher


from .fetchers import NUFloatingIpsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVMsFetcher


from .fetchers import NUVMInterfacesFetcher


from .fetchers import NUIngressACLEntryTemplatesFetcher


from .fetchers import NUIngressACLTemplatesFetcher


from .fetchers import NUIngressAdvFwdTemplatesFetcher


from .fetchers import NUIngressExternalServiceTemplatesFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NUPolicyGroupsFetcher


from .fetchers import NUDomainsFetcher


from .fetchers import NUDomainTemplatesFetcher


from .fetchers import NUZonesFetcher


from .fetchers import NUContainersFetcher


from .fetchers import NUContainerInterfacesFetcher


from .fetchers import NUQOSsFetcher


from .fetchers import NUHostInterfacesFetcher


from .fetchers import NURoutingPoliciesFetcher


from .fetchers import NUUplinkRDsFetcher


from .fetchers import NUVPNConnectionsFetcher


from .fetchers import NUVPortsFetcher


from .fetchers import NUApplicationperformancemanagementbindingsFetcher


from .fetchers import NUBridgeInterfacesFetcher


from .fetchers import NUGroupsFetcher


from .fetchers import NUStaticRoutesFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUStatisticsPoliciesFetcher


from .fetchers import NUSubnetsFetcher


from .fetchers import NUEventLogsFetcher


from .fetchers import NUExternalAppServicesFetcher

from bambou import NURESTObject


class NUDomain(NURESTObject):
    """ Represents a Domain in the VSD

        Notes:
            This object is used to manipulate domain state. A domain corresponds to a distributed Virtual Router and Switch.
    """

    __rest_name__ = "domain"
    __resource_name__ = "domains"

    
    ## Constants
    
    CONST_PAT_ENABLED_DISABLED = "DISABLED"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_PAT_ENABLED_INHERITED = "INHERITED"
    
    CONST_UPLINK_PREFERENCE_SECONDARY_PRIMARY = "SECONDARY_PRIMARY"
    
    CONST_UPLINK_PREFERENCE_PRIMARY_SECONDARY = "PRIMARY_SECONDARY"
    
    CONST_DHCP_BEHAVIOR_CONSUME = "CONSUME"
    
    CONST_DPI_ENABLED = "ENABLED"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_POLICY_CHANGE_STATUS_DISCARDED = "DISCARDED"
    
    CONST_UNDERLAY_ENABLED_ENABLED = "ENABLED"
    
    CONST_MAINTENANCE_MODE_DISABLED = "DISABLED"
    
    CONST_TUNNEL_TYPE_DC_DEFAULT = "DC_DEFAULT"
    
    CONST_MAINTENANCE_MODE_ENABLED = "ENABLED"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_UPLINK_PREFERENCE_SYMMETRIC = "SYMMETRIC"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_UNDERLAY_ENABLED_INHERITED = "INHERITED"
    
    CONST_POLICY_CHANGE_STATUS_STARTED = "STARTED"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_DHCP_BEHAVIOR_RELAY = "RELAY"
    
    CONST_APPLICATION_DEPLOYMENT_POLICY_ZONE = "ZONE"
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_PAT_ENABLED_ENABLED = "ENABLED"
    
    CONST_MULTICAST_ENABLED = "ENABLED"
    
    CONST_MULTICAST_INHERITED = "INHERITED"
    
    CONST_APPLICATION_DEPLOYMENT_POLICY_NONE = "NONE"
    
    CONST_UPLINK_PREFERENCE_SECONDARY = "SECONDARY"
    
    CONST_DHCP_BEHAVIOR_FLOOD = "FLOOD"
    
    CONST_MULTICAST_DISABLED = "DISABLED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_TUNNEL_TYPE_VXLAN = "VXLAN"
    
    CONST_ENCRYPTION_DISABLED = "DISABLED"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_UPLINK_PREFERENCE_PRIMARY = "PRIMARY"
    
    CONST_DPI_DISABLED = "DISABLED"
    
    CONST_MAINTENANCE_MODE_ENABLED_INHERITED = "ENABLED_INHERITED"
    
    CONST_ENCRYPTION_ENABLED = "ENABLED"
    
    CONST_TUNNEL_TYPE_GRE = "GRE"
    
    CONST_POLICY_CHANGE_STATUS_APPLIED = "APPLIED"
    
    CONST_UNDERLAY_ENABLED_DISABLED = "DISABLED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Domain instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> domain = NUDomain(id=u'xxxx-xxx-xxx-xxx', name=u'Domain')
                >>> domain = NUDomain(data=my_dict)
        """

        super(NUDomain, self).__init__()

        # Read/Write Attributes
        
        self._pat_enabled = None
        self._ecmp_count = None
        self._bgp_enabled = None
        self._dhcp_behavior = None
        self._dhcp_server_address = None
        self._dpi = None
        self._label_id = None
        self._back_haul_route_distinguisher = None
        self._back_haul_route_target = None
        self._back_haul_subnet_ip_address = None
        self._back_haul_subnet_mask = None
        self._back_haul_vnid = None
        self._maintenance_mode = None
        self._name = None
        self._last_updated_by = None
        self._leaking_enabled = None
        self._secondary_dhcp_server_address = None
        self._template_id = None
        self._permitted_action = None
        self._service_id = None
        self._description = None
        self._dhcp_server_addresses = None
        self._global_routing_enabled = None
        self._import_route_target = None
        self._encryption = None
        self._underlay_enabled = None
        self._entity_scope = None
        self._policy_change_status = None
        self._domain_id = None
        self._route_distinguisher = None
        self._route_target = None
        self._uplink_preference = None
        self._application_deployment_policy = None
        self._associated_bgp_profile_id = None
        self._associated_multicast_channel_map_id = None
        self._associated_pat_mapper_id = None
        self._stretched = None
        self._multicast = None
        self._tunnel_type = None
        self._customer_id = None
        self._export_route_target = None
        self._external_id = None
        
        self.expose_attribute(local_name="pat_enabled", remote_name="PATEnabled", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="ecmp_count", remote_name="ECMPCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bgp_enabled", remote_name="BGPEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dhcp_behavior", remote_name="DHCPBehavior", attribute_type=str, is_required=False, is_unique=False, choices=[u'CONSUME', u'FLOOD', u'RELAY'])
        self.expose_attribute(local_name="dhcp_server_address", remote_name="DHCPServerAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dpi", remote_name="DPI", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED'])
        self.expose_attribute(local_name="label_id", remote_name="labelID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="back_haul_route_distinguisher", remote_name="backHaulRouteDistinguisher", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="back_haul_route_target", remote_name="backHaulRouteTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="back_haul_subnet_ip_address", remote_name="backHaulSubnetIPAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="back_haul_subnet_mask", remote_name="backHaulSubnetMask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="back_haul_vnid", remote_name="backHaulVNID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="maintenance_mode", remote_name="maintenanceMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'ENABLED_INHERITED'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="leaking_enabled", remote_name="leakingEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_dhcp_server_address", remote_name="secondaryDHCPServerAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="service_id", remote_name="serviceID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dhcp_server_addresses", remote_name="dhcpServerAddresses", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="global_routing_enabled", remote_name="globalRoutingEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="import_route_target", remote_name="importRouteTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="encryption", remote_name="encryption", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED'])
        self.expose_attribute(local_name="underlay_enabled", remote_name="underlayEnabled", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="policy_change_status", remote_name="policyChangeStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'APPLIED', u'DISCARDED', u'STARTED'])
        self.expose_attribute(local_name="domain_id", remote_name="domainID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="route_distinguisher", remote_name="routeDistinguisher", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="route_target", remote_name="routeTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="uplink_preference", remote_name="uplinkPreference", attribute_type=str, is_required=False, is_unique=False, choices=[u'PRIMARY', u'PRIMARY_SECONDARY', u'SECONDARY', u'SECONDARY_PRIMARY', u'SYMMETRIC'])
        self.expose_attribute(local_name="application_deployment_policy", remote_name="applicationDeploymentPolicy", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'ZONE'])
        self.expose_attribute(local_name="associated_bgp_profile_id", remote_name="associatedBGPProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_multicast_channel_map_id", remote_name="associatedMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_pat_mapper_id", remote_name="associatedPATMapperID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stretched", remote_name="stretched", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast", remote_name="multicast", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="tunnel_type", remote_name="tunnelType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DC_DEFAULT', u'GRE', u'VXLAN'])
        self.expose_attribute(local_name="customer_id", remote_name="customerID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="export_route_target", remote_name="exportRouteTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.redirection_targets = NURedirectionTargetsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.egress_acl_entry_templates = NUEgressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.egress_acl_templates = NUEgressACLTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.domain_fip_acl_templates = NUDomainFIPAclTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.floating_ipacl_templates = NUFloatingIPACLTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.dhcp_options = NUDHCPOptionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.links = NULinksFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.floating_ips = NUFloatingIpsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ingress_acl_entry_templates = NUIngressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ingress_acl_templates = NUIngressACLTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ingress_adv_fwd_templates = NUIngressAdvFwdTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ingress_external_service_templates = NUIngressExternalServiceTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.policy_groups = NUPolicyGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.domains = NUDomainsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.domain_templates = NUDomainTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.zones = NUZonesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.containers = NUContainersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.container_interfaces = NUContainerInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.host_interfaces = NUHostInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.routing_policies = NURoutingPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.uplink_rds = NUUplinkRDsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vpn_connections = NUVPNConnectionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.applicationperformancemanagementbindings = NUApplicationperformancemanagementbindingsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bridge_interfaces = NUBridgeInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.groups = NUGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.static_routes = NUStaticRoutesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.subnets = NUSubnetsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.external_app_services = NUExternalAppServicesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def pat_enabled(self):
        """ Get pat_enabled value.

            Notes:
                Indicates whether PAT is enabled for the subnets in this domain - ENABLED/DISABLED Possible values are INHERITED, ENABLED, DISABLED, .

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        return self._pat_enabled

    @pat_enabled.setter
    def pat_enabled(self, value):
        """ Set pat_enabled value.

            Notes:
                Indicates whether PAT is enabled for the subnets in this domain - ENABLED/DISABLED Possible values are INHERITED, ENABLED, DISABLED, .

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        self._pat_enabled = value

    
    @property
    def ecmp_count(self):
        """ Get ecmp_count value.

            Notes:
                Domain specific Equal-cost multi-path routing count, ECMPCount = 1 means no ECMP

                
                This attribute is named `ECMPCount` in VSD API.
                
        """
        return self._ecmp_count

    @ecmp_count.setter
    def ecmp_count(self, value):
        """ Set ecmp_count value.

            Notes:
                Domain specific Equal-cost multi-path routing count, ECMPCount = 1 means no ECMP

                
                This attribute is named `ECMPCount` in VSD API.
                
        """
        self._ecmp_count = value

    
    @property
    def bgp_enabled(self):
        """ Get bgp_enabled value.

            Notes:
                Read only flag to display if BGP is enabled for this domain

                
                This attribute is named `BGPEnabled` in VSD API.
                
        """
        return self._bgp_enabled

    @bgp_enabled.setter
    def bgp_enabled(self, value):
        """ Set bgp_enabled value.

            Notes:
                Read only flag to display if BGP is enabled for this domain

                
                This attribute is named `BGPEnabled` in VSD API.
                
        """
        self._bgp_enabled = value

    
    @property
    def dhcp_behavior(self):
        """ Get dhcp_behavior value.

            Notes:
                DHCPBehaviorType is an enum that indicates DHCP Behavior of VRS having VM's under this domain. Possible values are FLOOD, CONSUME ,RELAY Possible values are CONSUME, FLOOD, RELAY, .

                
                This attribute is named `DHCPBehavior` in VSD API.
                
        """
        return self._dhcp_behavior

    @dhcp_behavior.setter
    def dhcp_behavior(self, value):
        """ Set dhcp_behavior value.

            Notes:
                DHCPBehaviorType is an enum that indicates DHCP Behavior of VRS having VM's under this domain. Possible values are FLOOD, CONSUME ,RELAY Possible values are CONSUME, FLOOD, RELAY, .

                
                This attribute is named `DHCPBehavior` in VSD API.
                
        """
        self._dhcp_behavior = value

    
    @property
    def dhcp_server_address(self):
        """ Get dhcp_server_address value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `DHCPServerAddress` in VSD API.
                
        """
        return self._dhcp_server_address

    @dhcp_server_address.setter
    def dhcp_server_address(self, value):
        """ Set dhcp_server_address value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `DHCPServerAddress` in VSD API.
                
        """
        self._dhcp_server_address = value

    
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
    def label_id(self):
        """ Get label_id value.

            Notes:
                The label associated with the dVRS. This is a read only attribute

                
                This attribute is named `labelID` in VSD API.
                
        """
        return self._label_id

    @label_id.setter
    def label_id(self, value):
        """ Set label_id value.

            Notes:
                The label associated with the dVRS. This is a read only attribute

                
                This attribute is named `labelID` in VSD API.
                
        """
        self._label_id = value

    
    @property
    def back_haul_route_distinguisher(self):
        """ Get back_haul_route_distinguisher value.

            Notes:
                Route distinguisher associated with the BackHaul Service in dVRS. If not provided during creation, System generates this identifier automatically

                
                This attribute is named `backHaulRouteDistinguisher` in VSD API.
                
        """
        return self._back_haul_route_distinguisher

    @back_haul_route_distinguisher.setter
    def back_haul_route_distinguisher(self, value):
        """ Set back_haul_route_distinguisher value.

            Notes:
                Route distinguisher associated with the BackHaul Service in dVRS. If not provided during creation, System generates this identifier automatically

                
                This attribute is named `backHaulRouteDistinguisher` in VSD API.
                
        """
        self._back_haul_route_distinguisher = value

    
    @property
    def back_haul_route_target(self):
        """ Get back_haul_route_target value.

            Notes:
                Route target associated with the BackHaul Service in dVRS. If not provided during creation, System generates this identifier automatically

                
                This attribute is named `backHaulRouteTarget` in VSD API.
                
        """
        return self._back_haul_route_target

    @back_haul_route_target.setter
    def back_haul_route_target(self, value):
        """ Set back_haul_route_target value.

            Notes:
                Route target associated with the BackHaul Service in dVRS. If not provided during creation, System generates this identifier automatically

                
                This attribute is named `backHaulRouteTarget` in VSD API.
                
        """
        self._back_haul_route_target = value

    
    @property
    def back_haul_subnet_ip_address(self):
        """ Get back_haul_subnet_ip_address value.

            Notes:
                IP Address of the backhaul subnet 

                
                This attribute is named `backHaulSubnetIPAddress` in VSD API.
                
        """
        return self._back_haul_subnet_ip_address

    @back_haul_subnet_ip_address.setter
    def back_haul_subnet_ip_address(self, value):
        """ Set back_haul_subnet_ip_address value.

            Notes:
                IP Address of the backhaul subnet 

                
                This attribute is named `backHaulSubnetIPAddress` in VSD API.
                
        """
        self._back_haul_subnet_ip_address = value

    
    @property
    def back_haul_subnet_mask(self):
        """ Get back_haul_subnet_mask value.

            Notes:
                Network mask of the backhaul subnet

                
                This attribute is named `backHaulSubnetMask` in VSD API.
                
        """
        return self._back_haul_subnet_mask

    @back_haul_subnet_mask.setter
    def back_haul_subnet_mask(self, value):
        """ Set back_haul_subnet_mask value.

            Notes:
                Network mask of the backhaul subnet

                
                This attribute is named `backHaulSubnetMask` in VSD API.
                
        """
        self._back_haul_subnet_mask = value

    
    @property
    def back_haul_vnid(self):
        """ Get back_haul_vnid value.

            Notes:
                Current BackHaul Network's globally unique  VXLAN network identifier generated by VSD

                
                This attribute is named `backHaulVNID` in VSD API.
                
        """
        return self._back_haul_vnid

    @back_haul_vnid.setter
    def back_haul_vnid(self, value):
        """ Set back_haul_vnid value.

            Notes:
                Current BackHaul Network's globally unique  VXLAN network identifier generated by VSD

                
                This attribute is named `backHaulVNID` in VSD API.
                
        """
        self._back_haul_vnid = value

    
    @property
    def maintenance_mode(self):
        """ Get maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the Domain is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        return self._maintenance_mode

    @maintenance_mode.setter
    def maintenance_mode(self, value):
        """ Set maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the Domain is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        self._maintenance_mode = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name of the domain. Valid characters are  alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name of the domain. Valid characters are  alphabets, numbers, space and hyphen( - ).

                
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
    def leaking_enabled(self):
        """ Get leaking_enabled value.

            Notes:
                Indicates if this domain is a leakable domain or not - boolean true/false

                
                This attribute is named `leakingEnabled` in VSD API.
                
        """
        return self._leaking_enabled

    @leaking_enabled.setter
    def leaking_enabled(self, value):
        """ Set leaking_enabled value.

            Notes:
                Indicates if this domain is a leakable domain or not - boolean true/false

                
                This attribute is named `leakingEnabled` in VSD API.
                
        """
        self._leaking_enabled = value

    
    @property
    def secondary_dhcp_server_address(self):
        """ Get secondary_dhcp_server_address value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `secondaryDHCPServerAddress` in VSD API.
                
        """
        return self._secondary_dhcp_server_address

    @secondary_dhcp_server_address.setter
    def secondary_dhcp_server_address(self, value):
        """ Set secondary_dhcp_server_address value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `secondaryDHCPServerAddress` in VSD API.
                
        """
        self._secondary_dhcp_server_address = value

    
    @property
    def template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the template that this domain was created from. This should be set when instantiating a domain

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the template that this domain was created from. This should be set when instantiating a domain

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    
    @property
    def permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted  action to USE/DEPLOY for the Domain Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    @permitted_action.setter
    def permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted  action to USE/DEPLOY for the Domain Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    
    @property
    def service_id(self):
        """ Get service_id value.

            Notes:
                The serviceID of the Virtual Router created in VSC and is associated with this object. This is auto-generated by VSD

                
                This attribute is named `serviceID` in VSD API.
                
        """
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        """ Set service_id value.

            Notes:
                The serviceID of the Virtual Router created in VSC and is associated with this object. This is auto-generated by VSD

                
                This attribute is named `serviceID` in VSD API.
                
        """
        self._service_id = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description string of the domain that is provided by the user

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description string of the domain that is provided by the user

                
        """
        self._description = value

    
    @property
    def dhcp_server_addresses(self):
        """ Get dhcp_server_addresses value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `dhcpServerAddresses` in VSD API.
                
        """
        return self._dhcp_server_addresses

    @dhcp_server_addresses.setter
    def dhcp_server_addresses(self, value):
        """ Set dhcp_server_addresses value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `dhcpServerAddresses` in VSD API.
                
        """
        self._dhcp_server_addresses = value

    
    @property
    def global_routing_enabled(self):
        """ Get global_routing_enabled value.

            Notes:
                Indicates if this domain is a globally routable domain or not - boolean true/false

                
                This attribute is named `globalRoutingEnabled` in VSD API.
                
        """
        return self._global_routing_enabled

    @global_routing_enabled.setter
    def global_routing_enabled(self, value):
        """ Set global_routing_enabled value.

            Notes:
                Indicates if this domain is a globally routable domain or not - boolean true/false

                
                This attribute is named `globalRoutingEnabled` in VSD API.
                
        """
        self._global_routing_enabled = value

    
    @property
    def import_route_target(self):
        """ Get import_route_target value.

            Notes:
                Route distinguisher associated with the dVRS. It is an optional parameter that can be provided by the user or auto-managed by VSD. System generates this identifier automatically, if not provided

                
                This attribute is named `importRouteTarget` in VSD API.
                
        """
        return self._import_route_target

    @import_route_target.setter
    def import_route_target(self, value):
        """ Set import_route_target value.

            Notes:
                Route distinguisher associated with the dVRS. It is an optional parameter that can be provided by the user or auto-managed by VSD. System generates this identifier automatically, if not provided

                
                This attribute is named `importRouteTarget` in VSD API.
                
        """
        self._import_route_target = value

    
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
    def domain_id(self):
        """ Get domain_id value.

            Notes:
                A unique 20-bitID editable however could be auto-generated by VSD.

                
                This attribute is named `domainID` in VSD API.
                
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, value):
        """ Set domain_id value.

            Notes:
                A unique 20-bitID editable however could be auto-generated by VSD.

                
                This attribute is named `domainID` in VSD API.
                
        """
        self._domain_id = value

    
    @property
    def route_distinguisher(self):
        """ Get route_distinguisher value.

            Notes:
                Route distinguisher associated with the dVRS. It is an optional parameter that can be provided by the user or auto-managed by VSD. System generates this identifier automatically, if not provided

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        return self._route_distinguisher

    @route_distinguisher.setter
    def route_distinguisher(self, value):
        """ Set route_distinguisher value.

            Notes:
                Route distinguisher associated with the dVRS. It is an optional parameter that can be provided by the user or auto-managed by VSD. System generates this identifier automatically, if not provided

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        self._route_distinguisher = value

    
    @property
    def route_target(self):
        """ Get route_target value.

            Notes:
                Route target associated with the dVRS. It is an optional parameterthat can be provided by the user or auto-managed by VSDSystem generates this identifier automatically, if not provided

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        return self._route_target

    @route_target.setter
    def route_target(self, value):
        """ Set route_target value.

            Notes:
                Route target associated with the dVRS. It is an optional parameterthat can be provided by the user or auto-managed by VSDSystem generates this identifier automatically, if not provided

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        self._route_target = value

    
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
    def application_deployment_policy(self):
        """ Get application_deployment_policy value.

            Notes:
                Application deployment policy.

                
                This attribute is named `applicationDeploymentPolicy` in VSD API.
                
        """
        return self._application_deployment_policy

    @application_deployment_policy.setter
    def application_deployment_policy(self, value):
        """ Set application_deployment_policy value.

            Notes:
                Application deployment policy.

                
                This attribute is named `applicationDeploymentPolicy` in VSD API.
                
        """
        self._application_deployment_policy = value

    
    @property
    def associated_bgp_profile_id(self):
        """ Get associated_bgp_profile_id value.

            Notes:
                None

                
                This attribute is named `associatedBGPProfileID` in VSD API.
                
        """
        return self._associated_bgp_profile_id

    @associated_bgp_profile_id.setter
    def associated_bgp_profile_id(self, value):
        """ Set associated_bgp_profile_id value.

            Notes:
                None

                
                This attribute is named `associatedBGPProfileID` in VSD API.
                
        """
        self._associated_bgp_profile_id = value

    
    @property
    def associated_multicast_channel_map_id(self):
        """ Get associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this domain is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_multicast_channel_map_id

    @associated_multicast_channel_map_id.setter
    def associated_multicast_channel_map_id(self, value):
        """ Set associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this domain is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        self._associated_multicast_channel_map_id = value

    
    @property
    def associated_pat_mapper_id(self):
        """ Get associated_pat_mapper_id value.

            Notes:
                The ID of the PatMapper entity to which this l3-domain is associated to.

                
                This attribute is named `associatedPATMapperID` in VSD API.
                
        """
        return self._associated_pat_mapper_id

    @associated_pat_mapper_id.setter
    def associated_pat_mapper_id(self, value):
        """ Set associated_pat_mapper_id value.

            Notes:
                The ID of the PatMapper entity to which this l3-domain is associated to.

                
                This attribute is named `associatedPATMapperID` in VSD API.
                
        """
        self._associated_pat_mapper_id = value

    
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
                multicast is enum that indicates multicast policy on domain. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        return self._multicast

    @multicast.setter
    def multicast(self, value):
        """ Set multicast value.

            Notes:
                multicast is enum that indicates multicast policy on domain. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        self._multicast = value

    
    @property
    def tunnel_type(self):
        """ Get tunnel_type value.

            Notes:
                Default Domain Tunnel Type

                
                This attribute is named `tunnelType` in VSD API.
                
        """
        return self._tunnel_type

    @tunnel_type.setter
    def tunnel_type(self, value):
        """ Set tunnel_type value.

            Notes:
                Default Domain Tunnel Type

                
                This attribute is named `tunnelType` in VSD API.
                
        """
        self._tunnel_type = value

    
    @property
    def customer_id(self):
        """ Get customer_id value.

            Notes:
                The customerID that is created in the VSC and identifies this dVRS. This is auto-generated by VSD

                
                This attribute is named `customerID` in VSD API.
                
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        """ Set customer_id value.

            Notes:
                The customerID that is created in the VSC and identifies this dVRS. This is auto-generated by VSD

                
                This attribute is named `customerID` in VSD API.
                
        """
        self._customer_id = value

    
    @property
    def export_route_target(self):
        """ Get export_route_target value.

            Notes:
                Route target associated with the dVRS. It is an optional parameterthat can be provided by the user or auto-managed by VSDSystem generates this identifier automatically, if not provided

                
                This attribute is named `exportRouteTarget` in VSD API.
                
        """
        return self._export_route_target

    @export_route_target.setter
    def export_route_target(self, value):
        """ Set export_route_target value.

            Notes:
                Route target associated with the dVRS. It is an optional parameterthat can be provided by the user or auto-managed by VSDSystem generates this identifier automatically, if not provided

                
                This attribute is named `exportRouteTarget` in VSD API.
                
        """
        self._export_route_target = value

    
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
    