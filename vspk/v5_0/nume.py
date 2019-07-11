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




from .fetchers import NUL2DomainsFetcher


from .fetchers import NUL4ServicesFetcher


from .fetchers import NUL7applicationsignaturesFetcher


from .fetchers import NUSaaSApplicationTypesFetcher


from .fetchers import NUVCenterEAMConfigsFetcher


from .fetchers import NURateLimitersFetcher


from .fetchers import NUGatewaysFetcher


from .fetchers import NUGatewayTemplatesFetcher


from .fetchers import NUPATMappersFetcher


from .fetchers import NUPATNATPoolsFetcher


from .fetchers import NUTCAsFetcher


from .fetchers import NUVCentersFetcher


from .fetchers import NUVCenterHypervisorsFetcher


from .fetchers import NURedirectionTargetsFetcher


from .fetchers import NURedundancyGroupsFetcher


from .fetchers import NUPerformanceMonitorsFetcher


from .fetchers import NUCertificatesFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUNetconfProfilesFetcher


from .fetchers import NUNetworkLayoutsFetcher


from .fetchers import NUNetworkPerformanceMeasurementsFetcher


from .fetchers import NUKeyServerMembersFetcher


from .fetchers import NUZFBAutoAssignmentsFetcher


from .fetchers import NUZFBRequestsFetcher


from .fetchers import NUBGPNeighborsFetcher


from .fetchers import NUBGPProfilesFetcher


from .fetchers import NUEgressACLEntryTemplatesFetcher


from .fetchers import NUEgressACLTemplatesFetcher


from .fetchers import NUEgressAdvFwdEntryTemplatesFetcher


from .fetchers import NUDomainFIPAclTemplatesFetcher


from .fetchers import NUEgressQOSPoliciesFetcher


from .fetchers import NUSharedNetworkResourcesFetcher


from .fetchers import NULicensesFetcher


from .fetchers import NULicenseStatusFetcher


from .fetchers import NUMirrorDestinationsFetcher


from .fetchers import NUVirtualFirewallPoliciesFetcher


from .fetchers import NUVirtualFirewallRulesFetcher


from .fetchers import NUSiteInfosFetcher


from .fetchers import NUAllGatewaysFetcher


from .fetchers import NUAllRedundancyGroupsFetcher


from .fetchers import NUFloatingIpsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVMsFetcher


from .fetchers import NUVMInterfacesFetcher


from .fetchers import NUCloudMgmtSystemsFetcher


from .fetchers import NUUnderlaysFetcher


from .fetchers import NUVNFCatalogsFetcher


from .fetchers import NUVNFMetadatasFetcher


from .fetchers import NUInfrastructureAccessProfilesFetcher


from .fetchers import NUInfrastructureEVDFProfilesFetcher


from .fetchers import NUInfrastructureGatewayProfilesFetcher


from .fetchers import NUInfrastructureVscProfilesFetcher


from .fetchers import NUVNFThresholdPoliciesFetcher


from .fetchers import NUIngressACLEntryTemplatesFetcher


from .fetchers import NUIngressACLTemplatesFetcher


from .fetchers import NUIngressAdvFwdEntryTemplatesFetcher


from .fetchers import NUIngressQOSPoliciesFetcher


from .fetchers import NUEnterprisesFetcher


from .fetchers import NUEnterpriseProfilesFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NUPolicyGroupsFetcher


from .fetchers import NUPolicyObjectGroupsFetcher


from .fetchers import NUDomainsFetcher


from .fetchers import NUCommandsFetcher


from .fetchers import NUZonesFetcher


from .fetchers import NUContainersFetcher


from .fetchers import NUContainerInterfacesFetcher


from .fetchers import NUQosPolicersFetcher


from .fetchers import NUCOSRemarkingPolicyTablesFetcher


from .fetchers import NUHostInterfacesFetcher


from .fetchers import NURoutingPoliciesFetcher


from .fetchers import NUUplinkRDsFetcher


from .fetchers import NUApplicationsFetcher


from .fetchers import NUApplicationperformancemanagementsFetcher


from .fetchers import NUVRSsFetcher


from .fetchers import NUVCenterVRSConfigsFetcher


from .fetchers import NUDSCPRemarkingPolicyTablesFetcher


from .fetchers import NUUsersFetcher


from .fetchers import NUUserContextsFetcher


from .fetchers import NUNSGatewaysFetcher


from .fetchers import NUNSGatewayTemplatesFetcher


from .fetchers import NUNSGGroupsFetcher


from .fetchers import NUNSGInfosFetcher


from .fetchers import NUNSGPatchProfilesFetcher


from .fetchers import NUNSRedundantGatewayGroupsFetcher


from .fetchers import NUNSGUpgradeProfilesFetcher


from .fetchers import NUVSPsFetcher


from .fetchers import NUStaticRoutesFetcher


from .fetchers import NUStatsCollectorInfosFetcher


from .fetchers import NUSubnetsFetcher


from .fetchers import NUDUCGroupsFetcher


from .fetchers import NUMultiCastChannelMapsFetcher


from .fetchers import NUAutoDiscoveredGatewaysFetcher


from .fetchers import NUOverlayMirrorDestinationsFetcher


from .fetchers import NUSystemConfigsFetcher

from bambou import NURESTRootObject


class NUMe(NURESTRootObject):
    """ Represents a Me in the VSD

        Notes:
            Object that identifies the user functions
    """

    __rest_name__ = "me"
    __resource_name__ = "me"

    
    ## Constants
    
    CONST_AVATAR_TYPE_URL = "URL"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_AVATAR_TYPE_BASE64 = "BASE64"
    
    CONST_AVATAR_TYPE_COMPUTEDURL = "COMPUTEDURL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Me instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> me = NUMe(id=u'xxxx-xxx-xxx-xxx', name=u'Me')
                >>> me = NUMe(data=my_dict)
        """

        super(NUMe, self).__init__()

        # Read/Write Attributes
        
        self._aar_flow_stats_interval = None
        self._aar_probe_stats_interval = None
        self._vss_stats_interval = None
        self._password = None
        self._last_name = None
        self._last_updated_by = None
        self._first_name = None
        self._disabled = None
        self._elastic_search_address = None
        self._flow_collection_enabled = None
        self._email = None
        self._enterprise_id = None
        self._enterprise_name = None
        self._entity_scope = None
        self._mobile_number = None
        self._role = None
        self._user_name = None
        self._statistics_enabled = None
        self._avatar_data = None
        self._avatar_type = None
        self._external_id = None
        
        self.expose_attribute(local_name="aar_flow_stats_interval", remote_name="AARFlowStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aar_probe_stats_interval", remote_name="AARProbeStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vss_stats_interval", remote_name="VSSStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="password", remote_name="password", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_name", remote_name="lastName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="first_name", remote_name="firstName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="disabled", remote_name="disabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="elastic_search_address", remote_name="elasticSearchAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="flow_collection_enabled", remote_name="flowCollectionEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="email", remote_name="email", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_name", remote_name="enterpriseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="mobile_number", remote_name="mobileNumber", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="role", remote_name="role", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="user_name", remote_name="userName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="statistics_enabled", remote_name="statisticsEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="avatar_data", remote_name="avatarData", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="avatar_type", remote_name="avatarType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BASE64', u'COMPUTEDURL', u'URL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.l2_domains = NUL2DomainsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.l4_services = NUL4ServicesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.l7applicationsignatures = NUL7applicationsignaturesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.saa_s_application_types = NUSaaSApplicationTypesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.vcenter_eam_configs = NUVCenterEAMConfigsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.rate_limiters = NURateLimitersFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.gateways = NUGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.gateway_templates = NUGatewayTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.pat_mappers = NUPATMappersFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.patnat_pools = NUPATNATPoolsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.vcenters = NUVCentersFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.vcenter_hypervisors = NUVCenterHypervisorsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.redirection_targets = NURedirectionTargetsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.redundancy_groups = NURedundancyGroupsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.performance_monitors = NUPerformanceMonitorsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.certificates = NUCertificatesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.netconf_profiles = NUNetconfProfilesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.network_layouts = NUNetworkLayoutsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.network_performance_measurements = NUNetworkPerformanceMeasurementsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.key_server_members = NUKeyServerMembersFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.zfb_auto_assignments = NUZFBAutoAssignmentsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.zfb_requests = NUZFBRequestsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.bgp_neighbors = NUBGPNeighborsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.bgp_profiles = NUBGPProfilesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.egress_acl_entry_templates = NUEgressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.egress_acl_templates = NUEgressACLTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.egress_adv_fwd_entry_templates = NUEgressAdvFwdEntryTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.domain_fip_acl_templates = NUDomainFIPAclTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.egress_qos_policies = NUEgressQOSPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.shared_network_resources = NUSharedNetworkResourcesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.licenses = NULicensesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.license_status = NULicenseStatusFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.mirror_destinations = NUMirrorDestinationsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.virtual_firewall_policies = NUVirtualFirewallPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.virtual_firewall_rules = NUVirtualFirewallRulesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.site_infos = NUSiteInfosFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.all_gateways = NUAllGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.all_redundancy_groups = NUAllRedundancyGroupsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.floating_ips = NUFloatingIpsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.cloud_mgmt_systems = NUCloudMgmtSystemsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.underlays = NUUnderlaysFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.vnf_catalogs = NUVNFCatalogsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.vnf_metadatas = NUVNFMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.infrastructure_access_profiles = NUInfrastructureAccessProfilesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.infrastructure_evdf_profiles = NUInfrastructureEVDFProfilesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.infrastructure_gateway_profiles = NUInfrastructureGatewayProfilesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.infrastructure_vsc_profiles = NUInfrastructureVscProfilesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.vnf_threshold_policies = NUVNFThresholdPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.ingress_acl_entry_templates = NUIngressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.ingress_acl_templates = NUIngressACLTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.ingress_adv_fwd_entry_templates = NUIngressAdvFwdEntryTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.ingress_qos_policies = NUIngressQOSPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.enterprises = NUEnterprisesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.enterprise_profiles = NUEnterpriseProfilesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.policy_groups = NUPolicyGroupsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.policy_object_groups = NUPolicyObjectGroupsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.domains = NUDomainsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.commands = NUCommandsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.zones = NUZonesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.containers = NUContainersFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.container_interfaces = NUContainerInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.qos_policers = NUQosPolicersFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.cos_remarking_policy_tables = NUCOSRemarkingPolicyTablesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.host_interfaces = NUHostInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.routing_policies = NURoutingPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.uplink_rds = NUUplinkRDsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.applications = NUApplicationsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.applicationperformancemanagements = NUApplicationperformancemanagementsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.vrss = NUVRSsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.vcenter_vrs_configs = NUVCenterVRSConfigsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.dscp_remarking_policy_tables = NUDSCPRemarkingPolicyTablesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.users = NUUsersFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.user_contexts = NUUserContextsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.ns_gateways = NUNSGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.ns_gateway_templates = NUNSGatewayTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.nsg_groups = NUNSGGroupsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.nsg_infos = NUNSGInfosFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.nsg_patch_profiles = NUNSGPatchProfilesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.ns_redundant_gateway_groups = NUNSRedundantGatewayGroupsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.nsg_upgrade_profiles = NUNSGUpgradeProfilesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.vsps = NUVSPsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.static_routes = NUStaticRoutesFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.stats_collector_infos = NUStatsCollectorInfosFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.subnets = NUSubnetsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.duc_groups = NUDUCGroupsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.multi_cast_channel_maps = NUMultiCastChannelMapsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.auto_discovered_gateways = NUAutoDiscoveredGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.overlay_mirror_destinations = NUOverlayMirrorDestinationsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.system_configs = NUSystemConfigsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def aar_flow_stats_interval(self):
        """ Get aar_flow_stats_interval value.

            Notes:
                AAR flow stats frequency

                
                This attribute is named `AARFlowStatsInterval` in VSD API.
                
        """
        return self._aar_flow_stats_interval

    @aar_flow_stats_interval.setter
    def aar_flow_stats_interval(self, value):
        """ Set aar_flow_stats_interval value.

            Notes:
                AAR flow stats frequency

                
                This attribute is named `AARFlowStatsInterval` in VSD API.
                
        """
        self._aar_flow_stats_interval = value

    
    @property
    def aar_probe_stats_interval(self):
        """ Get aar_probe_stats_interval value.

            Notes:
                AAR Probe stats frequency

                
                This attribute is named `AARProbeStatsInterval` in VSD API.
                
        """
        return self._aar_probe_stats_interval

    @aar_probe_stats_interval.setter
    def aar_probe_stats_interval(self, value):
        """ Set aar_probe_stats_interval value.

            Notes:
                AAR Probe stats frequency

                
                This attribute is named `AARProbeStatsInterval` in VSD API.
                
        """
        self._aar_probe_stats_interval = value

    
    @property
    def vss_stats_interval(self):
        """ Get vss_stats_interval value.

            Notes:
                VSS flow stats frequency

                
                This attribute is named `VSSStatsInterval` in VSD API.
                
        """
        return self._vss_stats_interval

    @vss_stats_interval.setter
    def vss_stats_interval(self, value):
        """ Set vss_stats_interval value.

            Notes:
                VSS flow stats frequency

                
                This attribute is named `VSSStatsInterval` in VSD API.
                
        """
        self._vss_stats_interval = value

    
    @property
    def password(self):
        """ Get password value.

            Notes:
                User password in clear text. Password cannot be a single character asterisk (*)

                
        """
        return self._password

    @password.setter
    def password(self, value):
        """ Set password value.

            Notes:
                User password in clear text. Password cannot be a single character asterisk (*)

                
        """
        self._password = value

    
    @property
    def last_name(self):
        """ Get last_name value.

            Notes:
                Last name of the user

                
                This attribute is named `lastName` in VSD API.
                
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """ Set last_name value.

            Notes:
                Last name of the user

                
                This attribute is named `lastName` in VSD API.
                
        """
        self._last_name = value

    
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
    def first_name(self):
        """ Get first_name value.

            Notes:
                First name of the user

                
                This attribute is named `firstName` in VSD API.
                
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """ Set first_name value.

            Notes:
                First name of the user

                
                This attribute is named `firstName` in VSD API.
                
        """
        self._first_name = value

    
    @property
    def disabled(self):
        """ Get disabled value.

            Notes:
                Status of the user account; true=disabled, false=not disabled; default value = false

                
        """
        return self._disabled

    @disabled.setter
    def disabled(self, value):
        """ Set disabled value.

            Notes:
                Status of the user account; true=disabled, false=not disabled; default value = false

                
        """
        self._disabled = value

    
    @property
    def elastic_search_address(self):
        """ Get elastic_search_address value.

            Notes:
                elastic search address

                
                This attribute is named `elasticSearchAddress` in VSD API.
                
        """
        return self._elastic_search_address

    @elastic_search_address.setter
    def elastic_search_address(self, value):
        """ Set elastic_search_address value.

            Notes:
                elastic search address

                
                This attribute is named `elasticSearchAddress` in VSD API.
                
        """
        self._elastic_search_address = value

    
    @property
    def flow_collection_enabled(self):
        """ Get flow_collection_enabled value.

            Notes:
                Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires 'statisticsEnabled'.

                
                This attribute is named `flowCollectionEnabled` in VSD API.
                
        """
        return self._flow_collection_enabled

    @flow_collection_enabled.setter
    def flow_collection_enabled(self, value):
        """ Set flow_collection_enabled value.

            Notes:
                Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires 'statisticsEnabled'.

                
                This attribute is named `flowCollectionEnabled` in VSD API.
                
        """
        self._flow_collection_enabled = value

    
    @property
    def email(self):
        """ Get email value.

            Notes:
                Email address of the user

                
        """
        return self._email

    @email.setter
    def email(self, value):
        """ Set email value.

            Notes:
                Email address of the user

                
        """
        self._email = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                Identifier of the enterprise.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                Identifier of the enterprise.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
    @property
    def enterprise_name(self):
        """ Get enterprise_name value.

            Notes:
                Name of the enterprise.

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        """ Set enterprise_name value.

            Notes:
                Name of the enterprise.

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        self._enterprise_name = value

    
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
    def mobile_number(self):
        """ Get mobile_number value.

            Notes:
                Mobile Number of the user

                
                This attribute is named `mobileNumber` in VSD API.
                
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        """ Set mobile_number value.

            Notes:
                Mobile Number of the user

                
                This attribute is named `mobileNumber` in VSD API.
                
        """
        self._mobile_number = value

    
    @property
    def role(self):
        """ Get role value.

            Notes:
                Role of the user.

                
        """
        return self._role

    @role.setter
    def role(self, value):
        """ Set role value.

            Notes:
                Role of the user.

                
        """
        self._role = value

    
    @property
    def user_name(self):
        """ Get user_name value.

            Notes:
                Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).

                
                This attribute is named `userName` in VSD API.
                
        """
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        """ Set user_name value.

            Notes:
                Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).

                
                This attribute is named `userName` in VSD API.
                
        """
        self._user_name = value

    
    @property
    def statistics_enabled(self):
        """ Get statistics_enabled value.

            Notes:
                This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

                
                This attribute is named `statisticsEnabled` in VSD API.
                
        """
        return self._statistics_enabled

    @statistics_enabled.setter
    def statistics_enabled(self, value):
        """ Set statistics_enabled value.

            Notes:
                This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

                
                This attribute is named `statisticsEnabled` in VSD API.
                
        """
        self._statistics_enabled = value

    
    @property
    def avatar_data(self):
        """ Get avatar_data value.

            Notes:
                URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

                
                This attribute is named `avatarData` in VSD API.
                
        """
        return self._avatar_data

    @avatar_data.setter
    def avatar_data(self, value):
        """ Set avatar_data value.

            Notes:
                URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

                
                This attribute is named `avatarData` in VSD API.
                
        """
        self._avatar_data = value

    
    @property
    def avatar_type(self):
        """ Get avatar_type value.

            Notes:
                Avatar type.

                
                This attribute is named `avatarType` in VSD API.
                
        """
        return self._avatar_type

    @avatar_type.setter
    def avatar_type(self, value):
        """ Set avatar_type value.

            Notes:
                Avatar type.

                
                This attribute is named `avatarType` in VSD API.
                
        """
        self._avatar_type = value

    
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
    def save(self, as_async=False, callback=None, **kwargs):
        """ """
        if 'async' in kwargs.keys() and not as_async:
            as_async = kwargs['async']
        super(NUMe, self).save(as_async=as_async, callback=callback, encrypted=False)
    
    