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


from .fetchers import NUJobsFetcher


from .fetchers import NUVRSAddressRangesFetcher


from .fetchers import NUVRSMetricsFetcher


from .fetchers import NUVRSRedeploymentpoliciesFetcher

from bambou import NURESTObject


class NUVCenterHypervisor(NURESTObject):
    """ Represents a VCenterHypervisor in the VSD

        Notes:
            Host or Hypervisors.
    """

    __rest_name__ = "vcenterhypervisor"
    __resource_name__ = "vcenterhypervisors"

    
    ## Constants
    
    CONST_REMOTE_SYSLOG_SERVER_TYPE_TCP = "TCP"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_DESTINATION_MIRROR_PORT_NO_MIRROR = "no_mirror"
    
    CONST_PERSONALITY_VRS = "VRS"
    
    CONST_VRS_STATE_UPGRADING = "UPGRADING"
    
    CONST_REMOTE_SYSLOG_SERVER_TYPE_UDP = "UDP"
    
    CONST_VRS_STATE_DEPLOYED = "DEPLOYED"
    
    CONST_AVRS_PROFILE_AVRS_25G = "AVRS_25G"
    
    CONST_CPU_COUNT_LARGE_6 = "LARGE_6"
    
    CONST_DESTINATION_MIRROR_PORT_ENS224 = "ens224"
    
    CONST_CPU_COUNT_DEFAULT_2 = "DEFAULT_2"
    
    CONST_DESTINATION_MIRROR_PORT_ENS160 = "ens160"
    
    CONST_DESTINATION_MIRROR_PORT_ENS161 = "ens161"
    
    CONST_VRS_STATE_TIMEDOUT = "TIMEDOUT"
    
    CONST_DESTINATION_MIRROR_PORT_ENS256 = "ens256"
    
    CONST_CPU_COUNT_XLARGE_8 = "XLARGE_8"
    
    CONST_VRS_STATE_DEPLOYING = "DEPLOYING"
    
    CONST_REMOTE_SYSLOG_SERVER_TYPE_NONE = "NONE"
    
    CONST_MEMORY_SIZE_IN_GB_LARGE_8 = "LARGE_8"
    
    CONST_MEMORY_SIZE_IN_GB_DEFAULT_4 = "DEFAULT_4"
    
    CONST_VRS_STATE_NOT_DEPLOYED = "NOT_DEPLOYED"
    
    CONST_MEMORY_SIZE_IN_GB_MEDIUM_6 = "MEDIUM_6"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_CPU_COUNT_MEDIUM_4 = "MEDIUM_4"
    
    CONST_PERSONALITY_VDF = "VDF"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VCenterHypervisor instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vcenterhypervisor = NUVCenterHypervisor(id=u'xxxx-xxx-xxx-xxx', name=u'VCenterHypervisor')
                >>> vcenterhypervisor = NUVCenterHypervisor(data=my_dict)
        """

        super(NUVCenterHypervisor, self).__init__()

        # Read/Write Attributes
        
        self._vcenter_ip = None
        self._vcenter_password = None
        self._vcenter_user = None
        self._arp_reply = None
        self._vrs_agent_moid = None
        self._vrs_agent_name = None
        self._vrs_configuration_time_limit = None
        self._vrs_metrics_id = None
        self._vrs_mgmt_hostname = None
        self._vrs_state = None
        self._v_require_nuage_metadata = None
        self._name = None
        self._manage_vrs_availability = None
        self._managed_object_id = None
        self._last_updated_by = None
        self._last_vrs_deployed_date = None
        self._data_dns1 = None
        self._data_dns2 = None
        self._data_gateway = None
        self._data_ip_address = None
        self._data_netmask = None
        self._data_network_portgroup = None
        self._datapath_sync_timeout = None
        self._scope = None
        self._secondary_data_uplink_dhcp_enabled = None
        self._secondary_data_uplink_enabled = None
        self._secondary_data_uplink_ip = None
        self._secondary_data_uplink_interface = None
        self._secondary_data_uplink_mtu = None
        self._secondary_data_uplink_netmask = None
        self._secondary_data_uplink_primary_controller = None
        self._secondary_data_uplink_secondary_controller = None
        self._secondary_data_uplink_underlay_id = None
        self._secondary_data_uplink_vdf_control_vlan = None
        self._secondary_nuage_controller = None
        self._memory_size_in_gb = None
        self._remote_syslog_server_ip = None
        self._remote_syslog_server_port = None
        self._remote_syslog_server_type = None
        self._removed_from_vcenter_inventory = None
        self._generic_split_activation = None
        self._separate_data_network = None
        self._deployment_count = None
        self._personality = None
        self._description = None
        self._destination_mirror_port = None
        self._metadata_server_ip = None
        self._metadata_server_listen_port = None
        self._metadata_server_port = None
        self._metadata_service_enabled = None
        self._network_uplink_interface = None
        self._network_uplink_interface_gateway = None
        self._network_uplink_interface_ip = None
        self._network_uplink_interface_netmask = None
        self._revertive_controller_enabled = None
        self._revertive_timer = None
        self._nfs_log_server = None
        self._nfs_mount_path = None
        self._agency_moid = None
        self._mgmt_dns1 = None
        self._mgmt_dns2 = None
        self._mgmt_gateway = None
        self._mgmt_ip_address = None
        self._mgmt_netmask = None
        self._mgmt_network_portgroup = None
        self._dhcp_relay_server = None
        self._mirror_network_portgroup = None
        self._disable_gro_on_datapath = None
        self._disable_lro_on_datapath = None
        self._site_id = None
        self._allow_data_dhcp = None
        self._allow_mgmt_dhcp = None
        self._flow_eviction_threshold = None
        self._vm_network_portgroup = None
        self._enable_vrs_resource_reservation = None
        self._entity_scope = None
        self._configured_metrics_push_interval = None
        self._toolbox_deployment_mode = None
        self._toolbox_group = None
        self._toolbox_ip = None
        self._toolbox_password = None
        self._toolbox_user_name = None
        self._portgroup_metadata = None
        self._nova_client_version = None
        self._nova_identity_url_version = None
        self._nova_metadata_service_auth_url = None
        self._nova_metadata_service_endpoint = None
        self._nova_metadata_service_password = None
        self._nova_metadata_service_tenant = None
        self._nova_metadata_service_username = None
        self._nova_metadata_shared_secret = None
        self._nova_os_keystone_username = None
        self._nova_project_domain_name = None
        self._nova_project_name = None
        self._nova_region_name = None
        self._nova_user_domain_name = None
        self._upgrade_package_password = None
        self._upgrade_package_url = None
        self._upgrade_package_username = None
        self._upgrade_script_time_limit = None
        self._upgrade_status = None
        self._upgrade_timedout = None
        self._cpu_count = None
        self._primary_data_uplink_underlay_id = None
        self._primary_data_uplink_vdf_control_vlan = None
        self._primary_nuage_controller = None
        self._vrs_id = None
        self._vrs_marked_as_available = None
        self._vrs_password = None
        self._vrs_user_name = None
        self._static_route = None
        self._static_route_gateway = None
        self._static_route_netmask = None
        self._ntp_server1 = None
        self._ntp_server2 = None
        self._mtu = None
        self._successfully_applied_upgrade_package_password = None
        self._successfully_applied_upgrade_package_url = None
        self._successfully_applied_upgrade_package_username = None
        self._successfully_applied_version = None
        self._multi_vmssupport = None
        self._multicast_receive_interface = None
        self._multicast_receive_interface_ip = None
        self._multicast_receive_interface_netmask = None
        self._multicast_receive_range = None
        self._multicast_send_interface = None
        self._multicast_send_interface_ip = None
        self._multicast_send_interface_netmask = None
        self._multicast_source_portgroup = None
        self._customized_script_url = None
        self._available_networks = None
        self._ovf_url = None
        self._avrs_enabled = None
        self._avrs_profile = None
        self._external_id = None
        self._hypervisor_ip = None
        self._hypervisor_password = None
        self._hypervisor_user = None
        
        self.expose_attribute(local_name="vcenter_ip", remote_name="vCenterIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vcenter_password", remote_name="vCenterPassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vcenter_user", remote_name="vCenterUser", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="arp_reply", remote_name="ARPReply", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_agent_moid", remote_name="VRSAgentMOID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_agent_name", remote_name="VRSAgentName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_configuration_time_limit", remote_name="VRSConfigurationTimeLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_metrics_id", remote_name="VRSMetricsID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_mgmt_hostname", remote_name="VRSMgmtHostname", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_state", remote_name="VRSState", attribute_type=str, is_required=False, is_unique=False, choices=[u'DEPLOYED', u'DEPLOYING', u'NOT_DEPLOYED', u'TIMEDOUT', u'UPGRADING'])
        self.expose_attribute(local_name="v_require_nuage_metadata", remote_name="vRequireNuageMetadata", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="manage_vrs_availability", remote_name="manageVRSAvailability", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="managed_object_id", remote_name="managedObjectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_vrs_deployed_date", remote_name="lastVRSDeployedDate", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="data_dns1", remote_name="dataDNS1", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="data_dns2", remote_name="dataDNS2", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="data_gateway", remote_name="dataGateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="data_ip_address", remote_name="dataIPAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="data_netmask", remote_name="dataNetmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="data_network_portgroup", remote_name="dataNetworkPortgroup", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="datapath_sync_timeout", remote_name="datapathSyncTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="scope", remote_name="scope", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_data_uplink_dhcp_enabled", remote_name="secondaryDataUplinkDHCPEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_data_uplink_enabled", remote_name="secondaryDataUplinkEnabled", attribute_type=bool, is_required=True, is_unique=False)
        self.expose_attribute(local_name="secondary_data_uplink_ip", remote_name="secondaryDataUplinkIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_data_uplink_interface", remote_name="secondaryDataUplinkInterface", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_data_uplink_mtu", remote_name="secondaryDataUplinkMTU", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_data_uplink_netmask", remote_name="secondaryDataUplinkNetmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_data_uplink_primary_controller", remote_name="secondaryDataUplinkPrimaryController", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_data_uplink_secondary_controller", remote_name="secondaryDataUplinkSecondaryController", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_data_uplink_underlay_id", remote_name="secondaryDataUplinkUnderlayID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_data_uplink_vdf_control_vlan", remote_name="secondaryDataUplinkVDFControlVLAN", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_nuage_controller", remote_name="secondaryNuageController", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="memory_size_in_gb", remote_name="memorySizeInGB", attribute_type=str, is_required=False, is_unique=False, choices=[u'DEFAULT_4', u'LARGE_8', u'MEDIUM_6'])
        self.expose_attribute(local_name="remote_syslog_server_ip", remote_name="remoteSyslogServerIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="remote_syslog_server_port", remote_name="remoteSyslogServerPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="remote_syslog_server_type", remote_name="remoteSyslogServerType", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'TCP', u'UDP'])
        self.expose_attribute(local_name="removed_from_vcenter_inventory", remote_name="removedFromVCenterInventory", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="generic_split_activation", remote_name="genericSplitActivation", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="separate_data_network", remote_name="separateDataNetwork", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="deployment_count", remote_name="deploymentCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=False, is_unique=False, choices=[u'VDF', u'VRS'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="destination_mirror_port", remote_name="destinationMirrorPort", attribute_type=str, is_required=False, is_unique=False, choices=[u'ens160', u'ens161', u'ens224', u'ens256', u'no_mirror'])
        self.expose_attribute(local_name="metadata_server_ip", remote_name="metadataServerIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_server_listen_port", remote_name="metadataServerListenPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_server_port", remote_name="metadataServerPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_service_enabled", remote_name="metadataServiceEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_uplink_interface", remote_name="networkUplinkInterface", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_uplink_interface_gateway", remote_name="networkUplinkInterfaceGateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_uplink_interface_ip", remote_name="networkUplinkInterfaceIp", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_uplink_interface_netmask", remote_name="networkUplinkInterfaceNetmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="revertive_controller_enabled", remote_name="revertiveControllerEnabled", attribute_type=bool, is_required=True, is_unique=False)
        self.expose_attribute(local_name="revertive_timer", remote_name="revertiveTimer", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="nfs_log_server", remote_name="nfsLogServer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nfs_mount_path", remote_name="nfsMountPath", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="agency_moid", remote_name="agencyMoid", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mgmt_dns1", remote_name="mgmtDNS1", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mgmt_dns2", remote_name="mgmtDNS2", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mgmt_gateway", remote_name="mgmtGateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mgmt_ip_address", remote_name="mgmtIPAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mgmt_netmask", remote_name="mgmtNetmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mgmt_network_portgroup", remote_name="mgmtNetworkPortgroup", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="dhcp_relay_server", remote_name="dhcpRelayServer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mirror_network_portgroup", remote_name="mirrorNetworkPortgroup", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="disable_gro_on_datapath", remote_name="disableGROOnDatapath", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="disable_lro_on_datapath", remote_name="disableLROOnDatapath", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="site_id", remote_name="siteId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allow_data_dhcp", remote_name="allowDataDHCP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allow_mgmt_dhcp", remote_name="allowMgmtDHCP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="flow_eviction_threshold", remote_name="flowEvictionThreshold", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vm_network_portgroup", remote_name="vmNetworkPortgroup", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="enable_vrs_resource_reservation", remote_name="enableVRSResourceReservation", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="configured_metrics_push_interval", remote_name="configuredMetricsPushInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="toolbox_deployment_mode", remote_name="toolboxDeploymentMode", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="toolbox_group", remote_name="toolboxGroup", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="toolbox_ip", remote_name="toolboxIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="toolbox_password", remote_name="toolboxPassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="toolbox_user_name", remote_name="toolboxUserName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="portgroup_metadata", remote_name="portgroupMetadata", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_client_version", remote_name="novaClientVersion", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_identity_url_version", remote_name="novaIdentityURLVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_service_auth_url", remote_name="novaMetadataServiceAuthUrl", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_service_endpoint", remote_name="novaMetadataServiceEndpoint", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_service_password", remote_name="novaMetadataServicePassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_service_tenant", remote_name="novaMetadataServiceTenant", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_service_username", remote_name="novaMetadataServiceUsername", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_shared_secret", remote_name="novaMetadataSharedSecret", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_os_keystone_username", remote_name="novaOSKeystoneUsername", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_project_domain_name", remote_name="novaProjectDomainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_project_name", remote_name="novaProjectName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_region_name", remote_name="novaRegionName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_user_domain_name", remote_name="novaUserDomainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="upgrade_package_password", remote_name="upgradePackagePassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="upgrade_package_url", remote_name="upgradePackageURL", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="upgrade_package_username", remote_name="upgradePackageUsername", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="upgrade_script_time_limit", remote_name="upgradeScriptTimeLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="upgrade_status", remote_name="upgradeStatus", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="upgrade_timedout", remote_name="upgradeTimedout", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cpu_count", remote_name="cpuCount", attribute_type=str, is_required=False, is_unique=False, choices=[u'DEFAULT_2', u'LARGE_6', u'MEDIUM_4', u'XLARGE_8'])
        self.expose_attribute(local_name="primary_data_uplink_underlay_id", remote_name="primaryDataUplinkUnderlayID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="primary_data_uplink_vdf_control_vlan", remote_name="primaryDataUplinkVDFControlVLAN", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="primary_nuage_controller", remote_name="primaryNuageController", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_id", remote_name="vrsId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_marked_as_available", remote_name="vrsMarkedAsAvailable", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_password", remote_name="vrsPassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_user_name", remote_name="vrsUserName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="static_route", remote_name="staticRoute", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="static_route_gateway", remote_name="staticRouteGateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="static_route_netmask", remote_name="staticRouteNetmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ntp_server1", remote_name="ntpServer1", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ntp_server2", remote_name="ntpServer2", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mtu", remote_name="mtu", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="successfully_applied_upgrade_package_password", remote_name="successfullyAppliedUpgradePackagePassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="successfully_applied_upgrade_package_url", remote_name="successfullyAppliedUpgradePackageURL", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="successfully_applied_upgrade_package_username", remote_name="successfullyAppliedUpgradePackageUsername", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="successfully_applied_version", remote_name="successfullyAppliedVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multi_vmssupport", remote_name="multiVMSsupport", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_receive_interface", remote_name="multicastReceiveInterface", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_receive_interface_ip", remote_name="multicastReceiveInterfaceIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_receive_interface_netmask", remote_name="multicastReceiveInterfaceNetmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_receive_range", remote_name="multicastReceiveRange", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_send_interface", remote_name="multicastSendInterface", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_send_interface_ip", remote_name="multicastSendInterfaceIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_send_interface_netmask", remote_name="multicastSendInterfaceNetmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_source_portgroup", remote_name="multicastSourcePortgroup", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="customized_script_url", remote_name="customizedScriptURL", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="available_networks", remote_name="availableNetworks", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ovf_url", remote_name="ovfURL", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="avrs_enabled", remote_name="avrsEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="avrs_profile", remote_name="avrsProfile", attribute_type=str, is_required=False, is_unique=False, choices=[u'AVRS_25G'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="hypervisor_ip", remote_name="hypervisorIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="hypervisor_password", remote_name="hypervisorPassword", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="hypervisor_user", remote_name="hypervisorUser", attribute_type=str, is_required=True, is_unique=False)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vrs_address_ranges = NUVRSAddressRangesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vrs_metrics = NUVRSMetricsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vrs_redeploymentpolicies = NUVRSRedeploymentpoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vcenter_ip(self):
        """ Get vcenter_ip value.

            Notes:
                IP Address of the VCenter.

                
                This attribute is named `vCenterIP` in VSD API.
                
        """
        return self._vcenter_ip

    @vcenter_ip.setter
    def vcenter_ip(self, value):
        """ Set vcenter_ip value.

            Notes:
                IP Address of the VCenter.

                
                This attribute is named `vCenterIP` in VSD API.
                
        """
        self._vcenter_ip = value

    
    @property
    def vcenter_password(self):
        """ Get vcenter_password value.

            Notes:
                Password for VCenter.

                
                This attribute is named `vCenterPassword` in VSD API.
                
        """
        return self._vcenter_password

    @vcenter_password.setter
    def vcenter_password(self, value):
        """ Set vcenter_password value.

            Notes:
                Password for VCenter.

                
                This attribute is named `vCenterPassword` in VSD API.
                
        """
        self._vcenter_password = value

    
    @property
    def vcenter_user(self):
        """ Get vcenter_user value.

            Notes:
                Username for VCenter.

                
                This attribute is named `vCenterUser` in VSD API.
                
        """
        return self._vcenter_user

    @vcenter_user.setter
    def vcenter_user(self, value):
        """ Set vcenter_user value.

            Notes:
                Username for VCenter.

                
                This attribute is named `vCenterUser` in VSD API.
                
        """
        self._vcenter_user = value

    
    @property
    def arp_reply(self):
        """ Get arp_reply value.

            Notes:
                Whether ARP Reply is enabled/disabled

                
                This attribute is named `ARPReply` in VSD API.
                
        """
        return self._arp_reply

    @arp_reply.setter
    def arp_reply(self, value):
        """ Set arp_reply value.

            Notes:
                Whether ARP Reply is enabled/disabled

                
                This attribute is named `ARPReply` in VSD API.
                
        """
        self._arp_reply = value

    
    @property
    def vrs_agent_moid(self):
        """ Get vrs_agent_moid value.

            Notes:
                VRS agent MOID to uniquely identify VRS VM on the Vcenter

                
                This attribute is named `VRSAgentMOID` in VSD API.
                
        """
        return self._vrs_agent_moid

    @vrs_agent_moid.setter
    def vrs_agent_moid(self, value):
        """ Set vrs_agent_moid value.

            Notes:
                VRS agent MOID to uniquely identify VRS VM on the Vcenter

                
                This attribute is named `VRSAgentMOID` in VSD API.
                
        """
        self._vrs_agent_moid = value

    
    @property
    def vrs_agent_name(self):
        """ Get vrs_agent_name value.

            Notes:
                VRS agent name on the Vcenter

                
                This attribute is named `VRSAgentName` in VSD API.
                
        """
        return self._vrs_agent_name

    @vrs_agent_name.setter
    def vrs_agent_name(self, value):
        """ Set vrs_agent_name value.

            Notes:
                VRS agent name on the Vcenter

                
                This attribute is named `VRSAgentName` in VSD API.
                
        """
        self._vrs_agent_name = value

    
    @property
    def vrs_configuration_time_limit(self):
        """ Get vrs_configuration_time_limit value.

            Notes:
                The maximum wait time limit in minutes to get VRS configured at cluster level

                
                This attribute is named `VRSConfigurationTimeLimit` in VSD API.
                
        """
        return self._vrs_configuration_time_limit

    @vrs_configuration_time_limit.setter
    def vrs_configuration_time_limit(self, value):
        """ Set vrs_configuration_time_limit value.

            Notes:
                The maximum wait time limit in minutes to get VRS configured at cluster level

                
                This attribute is named `VRSConfigurationTimeLimit` in VSD API.
                
        """
        self._vrs_configuration_time_limit = value

    
    @property
    def vrs_metrics_id(self):
        """ Get vrs_metrics_id value.

            Notes:
                ID of the VRS metrics object.

                
                This attribute is named `VRSMetricsID` in VSD API.
                
        """
        return self._vrs_metrics_id

    @vrs_metrics_id.setter
    def vrs_metrics_id(self, value):
        """ Set vrs_metrics_id value.

            Notes:
                ID of the VRS metrics object.

                
                This attribute is named `VRSMetricsID` in VSD API.
                
        """
        self._vrs_metrics_id = value

    
    @property
    def vrs_mgmt_hostname(self):
        """ Get vrs_mgmt_hostname value.

            Notes:
                The VRS Management Hostname that will be configured on the VRS and in case of vCenter 6.5 and above, will be used to rename the VRS Agent in vCenter

                
                This attribute is named `VRSMgmtHostname` in VSD API.
                
        """
        return self._vrs_mgmt_hostname

    @vrs_mgmt_hostname.setter
    def vrs_mgmt_hostname(self, value):
        """ Set vrs_mgmt_hostname value.

            Notes:
                The VRS Management Hostname that will be configured on the VRS and in case of vCenter 6.5 and above, will be used to rename the VRS Agent in vCenter

                
                This attribute is named `VRSMgmtHostname` in VSD API.
                
        """
        self._vrs_mgmt_hostname = value

    
    @property
    def vrs_state(self):
        """ Get vrs_state value.

            Notes:
                Current state of the VRS VM on the hypervisor

                
                This attribute is named `VRSState` in VSD API.
                
        """
        return self._vrs_state

    @vrs_state.setter
    def vrs_state(self, value):
        """ Set vrs_state value.

            Notes:
                Current state of the VRS VM on the hypervisor

                
                This attribute is named `VRSState` in VSD API.
                
        """
        self._vrs_state = value

    
    @property
    def v_require_nuage_metadata(self):
        """ Get v_require_nuage_metadata value.

            Notes:
                Whether split-activation or not (Openstack/CloudStack)

                
                This attribute is named `vRequireNuageMetadata` in VSD API.
                
        """
        return self._v_require_nuage_metadata

    @v_require_nuage_metadata.setter
    def v_require_nuage_metadata(self, value):
        """ Set v_require_nuage_metadata value.

            Notes:
                Whether split-activation or not (Openstack/CloudStack)

                
                This attribute is named `vRequireNuageMetadata` in VSD API.
                
        """
        self._v_require_nuage_metadata = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Hypervisor

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Hypervisor

                
        """
        self._name = value

    
    @property
    def manage_vrs_availability(self):
        """ Get manage_vrs_availability value.

            Notes:
                When this is set to true, the vCenter Integration Node will be responsible for marking a VRS Agent as available in the EAM framework. Until a VRS Agent has been marked as available, vCenter will not migrate VMs to the host running the VRS Agent and will not allow VMs to be powered on that host.

                
                This attribute is named `manageVRSAvailability` in VSD API.
                
        """
        return self._manage_vrs_availability

    @manage_vrs_availability.setter
    def manage_vrs_availability(self, value):
        """ Set manage_vrs_availability value.

            Notes:
                When this is set to true, the vCenter Integration Node will be responsible for marking a VRS Agent as available in the EAM framework. Until a VRS Agent has been marked as available, vCenter will not migrate VMs to the host running the VRS Agent and will not allow VMs to be powered on that host.

                
                This attribute is named `manageVRSAvailability` in VSD API.
                
        """
        self._manage_vrs_availability = value

    
    @property
    def managed_object_id(self):
        """ Get managed_object_id value.

            Notes:
                managed Object ID of hypervisor

                
                This attribute is named `managedObjectID` in VSD API.
                
        """
        return self._managed_object_id

    @managed_object_id.setter
    def managed_object_id(self, value):
        """ Set managed_object_id value.

            Notes:
                managed Object ID of hypervisor

                
                This attribute is named `managedObjectID` in VSD API.
                
        """
        self._managed_object_id = value

    
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
    def last_vrs_deployed_date(self):
        """ Get last_vrs_deployed_date value.

            Notes:
                Determines the time the vrs vm was last deployed.

                
                This attribute is named `lastVRSDeployedDate` in VSD API.
                
        """
        return self._last_vrs_deployed_date

    @last_vrs_deployed_date.setter
    def last_vrs_deployed_date(self, value):
        """ Set last_vrs_deployed_date value.

            Notes:
                Determines the time the vrs vm was last deployed.

                
                This attribute is named `lastVRSDeployedDate` in VSD API.
                
        """
        self._last_vrs_deployed_date = value

    
    @property
    def data_dns1(self):
        """ Get data_dns1 value.

            Notes:
                Data DNS 1

                
                This attribute is named `dataDNS1` in VSD API.
                
        """
        return self._data_dns1

    @data_dns1.setter
    def data_dns1(self, value):
        """ Set data_dns1 value.

            Notes:
                Data DNS 1

                
                This attribute is named `dataDNS1` in VSD API.
                
        """
        self._data_dns1 = value

    
    @property
    def data_dns2(self):
        """ Get data_dns2 value.

            Notes:
                Data DNS 2

                
                This attribute is named `dataDNS2` in VSD API.
                
        """
        return self._data_dns2

    @data_dns2.setter
    def data_dns2(self, value):
        """ Set data_dns2 value.

            Notes:
                Data DNS 2

                
                This attribute is named `dataDNS2` in VSD API.
                
        """
        self._data_dns2 = value

    
    @property
    def data_gateway(self):
        """ Get data_gateway value.

            Notes:
                Data Gateway

                
                This attribute is named `dataGateway` in VSD API.
                
        """
        return self._data_gateway

    @data_gateway.setter
    def data_gateway(self, value):
        """ Set data_gateway value.

            Notes:
                Data Gateway

                
                This attribute is named `dataGateway` in VSD API.
                
        """
        self._data_gateway = value

    
    @property
    def data_ip_address(self):
        """ Get data_ip_address value.

            Notes:
                Data IP Address

                
                This attribute is named `dataIPAddress` in VSD API.
                
        """
        return self._data_ip_address

    @data_ip_address.setter
    def data_ip_address(self, value):
        """ Set data_ip_address value.

            Notes:
                Data IP Address

                
                This attribute is named `dataIPAddress` in VSD API.
                
        """
        self._data_ip_address = value

    
    @property
    def data_netmask(self):
        """ Get data_netmask value.

            Notes:
                Data NetMask

                
                This attribute is named `dataNetmask` in VSD API.
                
        """
        return self._data_netmask

    @data_netmask.setter
    def data_netmask(self, value):
        """ Set data_netmask value.

            Notes:
                Data NetMask

                
                This attribute is named `dataNetmask` in VSD API.
                
        """
        self._data_netmask = value

    
    @property
    def data_network_portgroup(self):
        """ Get data_network_portgroup value.

            Notes:
                Data Network Port Group

                
                This attribute is named `dataNetworkPortgroup` in VSD API.
                
        """
        return self._data_network_portgroup

    @data_network_portgroup.setter
    def data_network_portgroup(self, value):
        """ Set data_network_portgroup value.

            Notes:
                Data Network Port Group

                
                This attribute is named `dataNetworkPortgroup` in VSD API.
                
        """
        self._data_network_portgroup = value

    
    @property
    def datapath_sync_timeout(self):
        """ Get datapath_sync_timeout value.

            Notes:
                Datapath Sync Timeout

                
                This attribute is named `datapathSyncTimeout` in VSD API.
                
        """
        return self._datapath_sync_timeout

    @datapath_sync_timeout.setter
    def datapath_sync_timeout(self, value):
        """ Set datapath_sync_timeout value.

            Notes:
                Datapath Sync Timeout

                
                This attribute is named `datapathSyncTimeout` in VSD API.
                
        """
        self._datapath_sync_timeout = value

    
    @property
    def scope(self):
        """ Get scope value.

            Notes:
                Specifies if the hypervisor is part of an in scope or out of scope cliuster

                
        """
        return self._scope

    @scope.setter
    def scope(self, value):
        """ Set scope value.

            Notes:
                Specifies if the hypervisor is part of an in scope or out of scope cliuster

                
        """
        self._scope = value

    
    @property
    def secondary_data_uplink_dhcp_enabled(self):
        """ Get secondary_data_uplink_dhcp_enabled value.

            Notes:
                Enable DHCP on the secondary data uplink.

                
                This attribute is named `secondaryDataUplinkDHCPEnabled` in VSD API.
                
        """
        return self._secondary_data_uplink_dhcp_enabled

    @secondary_data_uplink_dhcp_enabled.setter
    def secondary_data_uplink_dhcp_enabled(self, value):
        """ Set secondary_data_uplink_dhcp_enabled value.

            Notes:
                Enable DHCP on the secondary data uplink.

                
                This attribute is named `secondaryDataUplinkDHCPEnabled` in VSD API.
                
        """
        self._secondary_data_uplink_dhcp_enabled = value

    
    @property
    def secondary_data_uplink_enabled(self):
        """ Get secondary_data_uplink_enabled value.

            Notes:
                Enable secondary data uplink

                
                This attribute is named `secondaryDataUplinkEnabled` in VSD API.
                
        """
        return self._secondary_data_uplink_enabled

    @secondary_data_uplink_enabled.setter
    def secondary_data_uplink_enabled(self, value):
        """ Set secondary_data_uplink_enabled value.

            Notes:
                Enable secondary data uplink

                
                This attribute is named `secondaryDataUplinkEnabled` in VSD API.
                
        """
        self._secondary_data_uplink_enabled = value

    
    @property
    def secondary_data_uplink_ip(self):
        """ Get secondary_data_uplink_ip value.

            Notes:
                Secondary data uplink IP

                
                This attribute is named `secondaryDataUplinkIP` in VSD API.
                
        """
        return self._secondary_data_uplink_ip

    @secondary_data_uplink_ip.setter
    def secondary_data_uplink_ip(self, value):
        """ Set secondary_data_uplink_ip value.

            Notes:
                Secondary data uplink IP

                
                This attribute is named `secondaryDataUplinkIP` in VSD API.
                
        """
        self._secondary_data_uplink_ip = value

    
    @property
    def secondary_data_uplink_interface(self):
        """ Get secondary_data_uplink_interface value.

            Notes:
                Interface to use for the secondary data uplink. This interface can be a normal interface or a VLAN on an existing interface. Please read the VMware integration guide for more details.

                
                This attribute is named `secondaryDataUplinkInterface` in VSD API.
                
        """
        return self._secondary_data_uplink_interface

    @secondary_data_uplink_interface.setter
    def secondary_data_uplink_interface(self, value):
        """ Set secondary_data_uplink_interface value.

            Notes:
                Interface to use for the secondary data uplink. This interface can be a normal interface or a VLAN on an existing interface. Please read the VMware integration guide for more details.

                
                This attribute is named `secondaryDataUplinkInterface` in VSD API.
                
        """
        self._secondary_data_uplink_interface = value

    
    @property
    def secondary_data_uplink_mtu(self):
        """ Get secondary_data_uplink_mtu value.

            Notes:
                Secondary data uplink MTU

                
                This attribute is named `secondaryDataUplinkMTU` in VSD API.
                
        """
        return self._secondary_data_uplink_mtu

    @secondary_data_uplink_mtu.setter
    def secondary_data_uplink_mtu(self, value):
        """ Set secondary_data_uplink_mtu value.

            Notes:
                Secondary data uplink MTU

                
                This attribute is named `secondaryDataUplinkMTU` in VSD API.
                
        """
        self._secondary_data_uplink_mtu = value

    
    @property
    def secondary_data_uplink_netmask(self):
        """ Get secondary_data_uplink_netmask value.

            Notes:
                Secondary data uplink Netmask

                
                This attribute is named `secondaryDataUplinkNetmask` in VSD API.
                
        """
        return self._secondary_data_uplink_netmask

    @secondary_data_uplink_netmask.setter
    def secondary_data_uplink_netmask(self, value):
        """ Set secondary_data_uplink_netmask value.

            Notes:
                Secondary data uplink Netmask

                
                This attribute is named `secondaryDataUplinkNetmask` in VSD API.
                
        """
        self._secondary_data_uplink_netmask = value

    
    @property
    def secondary_data_uplink_primary_controller(self):
        """ Get secondary_data_uplink_primary_controller value.

            Notes:
                Secondary data uplink primary controller IP

                
                This attribute is named `secondaryDataUplinkPrimaryController` in VSD API.
                
        """
        return self._secondary_data_uplink_primary_controller

    @secondary_data_uplink_primary_controller.setter
    def secondary_data_uplink_primary_controller(self, value):
        """ Set secondary_data_uplink_primary_controller value.

            Notes:
                Secondary data uplink primary controller IP

                
                This attribute is named `secondaryDataUplinkPrimaryController` in VSD API.
                
        """
        self._secondary_data_uplink_primary_controller = value

    
    @property
    def secondary_data_uplink_secondary_controller(self):
        """ Get secondary_data_uplink_secondary_controller value.

            Notes:
                Secondary data uplink secondary controller IP

                
                This attribute is named `secondaryDataUplinkSecondaryController` in VSD API.
                
        """
        return self._secondary_data_uplink_secondary_controller

    @secondary_data_uplink_secondary_controller.setter
    def secondary_data_uplink_secondary_controller(self, value):
        """ Set secondary_data_uplink_secondary_controller value.

            Notes:
                Secondary data uplink secondary controller IP

                
                This attribute is named `secondaryDataUplinkSecondaryController` in VSD API.
                
        """
        self._secondary_data_uplink_secondary_controller = value

    
    @property
    def secondary_data_uplink_underlay_id(self):
        """ Get secondary_data_uplink_underlay_id value.

            Notes:
                Secondary data uplink underlay ID

                
                This attribute is named `secondaryDataUplinkUnderlayID` in VSD API.
                
        """
        return self._secondary_data_uplink_underlay_id

    @secondary_data_uplink_underlay_id.setter
    def secondary_data_uplink_underlay_id(self, value):
        """ Set secondary_data_uplink_underlay_id value.

            Notes:
                Secondary data uplink underlay ID

                
                This attribute is named `secondaryDataUplinkUnderlayID` in VSD API.
                
        """
        self._secondary_data_uplink_underlay_id = value

    
    @property
    def secondary_data_uplink_vdf_control_vlan(self):
        """ Get secondary_data_uplink_vdf_control_vlan value.

            Notes:
                The VLAN for the control communication with VSC on the secondary datapath interface, when VDF is enabled. This VLAN can not be used as a subnet VLAN in the VSD configuration.

                
                This attribute is named `secondaryDataUplinkVDFControlVLAN` in VSD API.
                
        """
        return self._secondary_data_uplink_vdf_control_vlan

    @secondary_data_uplink_vdf_control_vlan.setter
    def secondary_data_uplink_vdf_control_vlan(self, value):
        """ Set secondary_data_uplink_vdf_control_vlan value.

            Notes:
                The VLAN for the control communication with VSC on the secondary datapath interface, when VDF is enabled. This VLAN can not be used as a subnet VLAN in the VSD configuration.

                
                This attribute is named `secondaryDataUplinkVDFControlVLAN` in VSD API.
                
        """
        self._secondary_data_uplink_vdf_control_vlan = value

    
    @property
    def secondary_nuage_controller(self):
        """ Get secondary_nuage_controller value.

            Notes:
                IP address of the secondary Controller (VSC)

                
                This attribute is named `secondaryNuageController` in VSD API.
                
        """
        return self._secondary_nuage_controller

    @secondary_nuage_controller.setter
    def secondary_nuage_controller(self, value):
        """ Set secondary_nuage_controller value.

            Notes:
                IP address of the secondary Controller (VSC)

                
                This attribute is named `secondaryNuageController` in VSD API.
                
        """
        self._secondary_nuage_controller = value

    
    @property
    def memory_size_in_gb(self):
        """ Get memory_size_in_gb value.

            Notes:
                Memory in Gigabytes

                
                This attribute is named `memorySizeInGB` in VSD API.
                
        """
        return self._memory_size_in_gb

    @memory_size_in_gb.setter
    def memory_size_in_gb(self, value):
        """ Set memory_size_in_gb value.

            Notes:
                Memory in Gigabytes

                
                This attribute is named `memorySizeInGB` in VSD API.
                
        """
        self._memory_size_in_gb = value

    
    @property
    def remote_syslog_server_ip(self):
        """ Get remote_syslog_server_ip value.

            Notes:
                Remote syslog server IP

                
                This attribute is named `remoteSyslogServerIP` in VSD API.
                
        """
        return self._remote_syslog_server_ip

    @remote_syslog_server_ip.setter
    def remote_syslog_server_ip(self, value):
        """ Set remote_syslog_server_ip value.

            Notes:
                Remote syslog server IP

                
                This attribute is named `remoteSyslogServerIP` in VSD API.
                
        """
        self._remote_syslog_server_ip = value

    
    @property
    def remote_syslog_server_port(self):
        """ Get remote_syslog_server_port value.

            Notes:
                Remote syslog server port

                
                This attribute is named `remoteSyslogServerPort` in VSD API.
                
        """
        return self._remote_syslog_server_port

    @remote_syslog_server_port.setter
    def remote_syslog_server_port(self, value):
        """ Set remote_syslog_server_port value.

            Notes:
                Remote syslog server port

                
                This attribute is named `remoteSyslogServerPort` in VSD API.
                
        """
        self._remote_syslog_server_port = value

    
    @property
    def remote_syslog_server_type(self):
        """ Get remote_syslog_server_type value.

            Notes:
                Remote syslog server type (UDP/TCP)

                
                This attribute is named `remoteSyslogServerType` in VSD API.
                
        """
        return self._remote_syslog_server_type

    @remote_syslog_server_type.setter
    def remote_syslog_server_type(self, value):
        """ Set remote_syslog_server_type value.

            Notes:
                Remote syslog server type (UDP/TCP)

                
                This attribute is named `remoteSyslogServerType` in VSD API.
                
        """
        self._remote_syslog_server_type = value

    
    @property
    def removed_from_vcenter_inventory(self):
        """ Get removed_from_vcenter_inventory value.

            Notes:
                Set to true if the hypervisor is removed from Vcenter inventory datacenter or cluster

                
                This attribute is named `removedFromVCenterInventory` in VSD API.
                
        """
        return self._removed_from_vcenter_inventory

    @removed_from_vcenter_inventory.setter
    def removed_from_vcenter_inventory(self, value):
        """ Set removed_from_vcenter_inventory value.

            Notes:
                Set to true if the hypervisor is removed from Vcenter inventory datacenter or cluster

                
                This attribute is named `removedFromVCenterInventory` in VSD API.
                
        """
        self._removed_from_vcenter_inventory = value

    
    @property
    def generic_split_activation(self):
        """ Get generic_split_activation value.

            Notes:
                Whether split-activation is needed from VRO

                
                This attribute is named `genericSplitActivation` in VSD API.
                
        """
        return self._generic_split_activation

    @generic_split_activation.setter
    def generic_split_activation(self, value):
        """ Set generic_split_activation value.

            Notes:
                Whether split-activation is needed from VRO

                
                This attribute is named `genericSplitActivation` in VSD API.
                
        """
        self._generic_split_activation = value

    
    @property
    def separate_data_network(self):
        """ Get separate_data_network value.

            Notes:
                Whether Data will use the management network or not

                
                This attribute is named `separateDataNetwork` in VSD API.
                
        """
        return self._separate_data_network

    @separate_data_network.setter
    def separate_data_network(self, value):
        """ Set separate_data_network value.

            Notes:
                Whether Data will use the management network or not

                
                This attribute is named `separateDataNetwork` in VSD API.
                
        """
        self._separate_data_network = value

    
    @property
    def deployment_count(self):
        """ Get deployment_count value.

            Notes:
                The number of times the vrs was deployed on this hypervisor

                
                This attribute is named `deploymentCount` in VSD API.
                
        """
        return self._deployment_count

    @deployment_count.setter
    def deployment_count(self, value):
        """ Set deployment_count value.

            Notes:
                The number of times the vrs was deployed on this hypervisor

                
                This attribute is named `deploymentCount` in VSD API.
                
        """
        self._deployment_count = value

    
    @property
    def personality(self):
        """ Get personality value.

            Notes:
                The personality of the VRS Agent, supported values when deploying through the vCenter Integration Node: VRS, VDF.

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                The personality of the VRS Agent, supported values when deploying through the vCenter Integration Node: VRS, VDF.

                
        """
        self._personality = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the Hypervisor

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the Hypervisor

                
        """
        self._description = value

    
    @property
    def destination_mirror_port(self):
        """ Get destination_mirror_port value.

            Notes:
                Extra Vnic to mirror access port

                
                This attribute is named `destinationMirrorPort` in VSD API.
                
        """
        return self._destination_mirror_port

    @destination_mirror_port.setter
    def destination_mirror_port(self, value):
        """ Set destination_mirror_port value.

            Notes:
                Extra Vnic to mirror access port

                
                This attribute is named `destinationMirrorPort` in VSD API.
                
        """
        self._destination_mirror_port = value

    
    @property
    def metadata_server_ip(self):
        """ Get metadata_server_ip value.

            Notes:
                Metadata Server IP

                
                This attribute is named `metadataServerIP` in VSD API.
                
        """
        return self._metadata_server_ip

    @metadata_server_ip.setter
    def metadata_server_ip(self, value):
        """ Set metadata_server_ip value.

            Notes:
                Metadata Server IP

                
                This attribute is named `metadataServerIP` in VSD API.
                
        """
        self._metadata_server_ip = value

    
    @property
    def metadata_server_listen_port(self):
        """ Get metadata_server_listen_port value.

            Notes:
                Metadata Server Listen Port

                
                This attribute is named `metadataServerListenPort` in VSD API.
                
        """
        return self._metadata_server_listen_port

    @metadata_server_listen_port.setter
    def metadata_server_listen_port(self, value):
        """ Set metadata_server_listen_port value.

            Notes:
                Metadata Server Listen Port

                
                This attribute is named `metadataServerListenPort` in VSD API.
                
        """
        self._metadata_server_listen_port = value

    
    @property
    def metadata_server_port(self):
        """ Get metadata_server_port value.

            Notes:
                Metadata Server Port

                
                This attribute is named `metadataServerPort` in VSD API.
                
        """
        return self._metadata_server_port

    @metadata_server_port.setter
    def metadata_server_port(self, value):
        """ Set metadata_server_port value.

            Notes:
                Metadata Server Port

                
                This attribute is named `metadataServerPort` in VSD API.
                
        """
        self._metadata_server_port = value

    
    @property
    def metadata_service_enabled(self):
        """ Get metadata_service_enabled value.

            Notes:
                Metadata Service Enabled

                
                This attribute is named `metadataServiceEnabled` in VSD API.
                
        """
        return self._metadata_service_enabled

    @metadata_service_enabled.setter
    def metadata_service_enabled(self, value):
        """ Set metadata_service_enabled value.

            Notes:
                Metadata Service Enabled

                
                This attribute is named `metadataServiceEnabled` in VSD API.
                
        """
        self._metadata_service_enabled = value

    
    @property
    def network_uplink_interface(self):
        """ Get network_uplink_interface value.

            Notes:
                Network Upling Interface to support PAT/NAT with no tunnels on VRS-VM

                
                This attribute is named `networkUplinkInterface` in VSD API.
                
        """
        return self._network_uplink_interface

    @network_uplink_interface.setter
    def network_uplink_interface(self, value):
        """ Set network_uplink_interface value.

            Notes:
                Network Upling Interface to support PAT/NAT with no tunnels on VRS-VM

                
                This attribute is named `networkUplinkInterface` in VSD API.
                
        """
        self._network_uplink_interface = value

    
    @property
    def network_uplink_interface_gateway(self):
        """ Get network_uplink_interface_gateway value.

            Notes:
                Network Uplink Interface Gateway

                
                This attribute is named `networkUplinkInterfaceGateway` in VSD API.
                
        """
        return self._network_uplink_interface_gateway

    @network_uplink_interface_gateway.setter
    def network_uplink_interface_gateway(self, value):
        """ Set network_uplink_interface_gateway value.

            Notes:
                Network Uplink Interface Gateway

                
                This attribute is named `networkUplinkInterfaceGateway` in VSD API.
                
        """
        self._network_uplink_interface_gateway = value

    
    @property
    def network_uplink_interface_ip(self):
        """ Get network_uplink_interface_ip value.

            Notes:
                Ip Address to support PAT/NAT with no tunnels on VRS-VM

                
                This attribute is named `networkUplinkInterfaceIp` in VSD API.
                
        """
        return self._network_uplink_interface_ip

    @network_uplink_interface_ip.setter
    def network_uplink_interface_ip(self, value):
        """ Set network_uplink_interface_ip value.

            Notes:
                Ip Address to support PAT/NAT with no tunnels on VRS-VM

                
                This attribute is named `networkUplinkInterfaceIp` in VSD API.
                
        """
        self._network_uplink_interface_ip = value

    
    @property
    def network_uplink_interface_netmask(self):
        """ Get network_uplink_interface_netmask value.

            Notes:
                Network Uplink Interface Netmask

                
                This attribute is named `networkUplinkInterfaceNetmask` in VSD API.
                
        """
        return self._network_uplink_interface_netmask

    @network_uplink_interface_netmask.setter
    def network_uplink_interface_netmask(self, value):
        """ Set network_uplink_interface_netmask value.

            Notes:
                Network Uplink Interface Netmask

                
                This attribute is named `networkUplinkInterfaceNetmask` in VSD API.
                
        """
        self._network_uplink_interface_netmask = value

    
    @property
    def revertive_controller_enabled(self):
        """ Get revertive_controller_enabled value.

            Notes:
                Enable revertive controller behaviour. If this is enabled, OVS will make its primary VSC as its master VSC once it is back up.

                
                This attribute is named `revertiveControllerEnabled` in VSD API.
                
        """
        return self._revertive_controller_enabled

    @revertive_controller_enabled.setter
    def revertive_controller_enabled(self, value):
        """ Set revertive_controller_enabled value.

            Notes:
                Enable revertive controller behaviour. If this is enabled, OVS will make its primary VSC as its master VSC once it is back up.

                
                This attribute is named `revertiveControllerEnabled` in VSD API.
                
        """
        self._revertive_controller_enabled = value

    
    @property
    def revertive_timer(self):
        """ Get revertive_timer value.

            Notes:
                 A timer in seconds indicating after how long OVS should retry to connect to the primary VSC as its master after a failure.

                
                This attribute is named `revertiveTimer` in VSD API.
                
        """
        return self._revertive_timer

    @revertive_timer.setter
    def revertive_timer(self, value):
        """ Set revertive_timer value.

            Notes:
                 A timer in seconds indicating after how long OVS should retry to connect to the primary VSC as its master after a failure.

                
                This attribute is named `revertiveTimer` in VSD API.
                
        """
        self._revertive_timer = value

    
    @property
    def nfs_log_server(self):
        """ Get nfs_log_server value.

            Notes:
                IP address of NFS server to send the VRS log

                
                This attribute is named `nfsLogServer` in VSD API.
                
        """
        return self._nfs_log_server

    @nfs_log_server.setter
    def nfs_log_server(self, value):
        """ Set nfs_log_server value.

            Notes:
                IP address of NFS server to send the VRS log

                
                This attribute is named `nfsLogServer` in VSD API.
                
        """
        self._nfs_log_server = value

    
    @property
    def nfs_mount_path(self):
        """ Get nfs_mount_path value.

            Notes:
                Location to mount the NFS server

                
                This attribute is named `nfsMountPath` in VSD API.
                
        """
        return self._nfs_mount_path

    @nfs_mount_path.setter
    def nfs_mount_path(self, value):
        """ Set nfs_mount_path value.

            Notes:
                Location to mount the NFS server

                
                This attribute is named `nfsMountPath` in VSD API.
                
        """
        self._nfs_mount_path = value

    
    @property
    def agency_moid(self):
        """ Get agency_moid value.

            Notes:
                cluster in scope or not in scope

                
                This attribute is named `agencyMoid` in VSD API.
                
        """
        return self._agency_moid

    @agency_moid.setter
    def agency_moid(self, value):
        """ Set agency_moid value.

            Notes:
                cluster in scope or not in scope

                
                This attribute is named `agencyMoid` in VSD API.
                
        """
        self._agency_moid = value

    
    @property
    def mgmt_dns1(self):
        """ Get mgmt_dns1 value.

            Notes:
                DNS server 1

                
                This attribute is named `mgmtDNS1` in VSD API.
                
        """
        return self._mgmt_dns1

    @mgmt_dns1.setter
    def mgmt_dns1(self, value):
        """ Set mgmt_dns1 value.

            Notes:
                DNS server 1

                
                This attribute is named `mgmtDNS1` in VSD API.
                
        """
        self._mgmt_dns1 = value

    
    @property
    def mgmt_dns2(self):
        """ Get mgmt_dns2 value.

            Notes:
                DNS server 2

                
                This attribute is named `mgmtDNS2` in VSD API.
                
        """
        return self._mgmt_dns2

    @mgmt_dns2.setter
    def mgmt_dns2(self, value):
        """ Set mgmt_dns2 value.

            Notes:
                DNS server 2

                
                This attribute is named `mgmtDNS2` in VSD API.
                
        """
        self._mgmt_dns2 = value

    
    @property
    def mgmt_gateway(self):
        """ Get mgmt_gateway value.

            Notes:
                Gateway for the IP address

                
                This attribute is named `mgmtGateway` in VSD API.
                
        """
        return self._mgmt_gateway

    @mgmt_gateway.setter
    def mgmt_gateway(self, value):
        """ Set mgmt_gateway value.

            Notes:
                Gateway for the IP address

                
                This attribute is named `mgmtGateway` in VSD API.
                
        """
        self._mgmt_gateway = value

    
    @property
    def mgmt_ip_address(self):
        """ Get mgmt_ip_address value.

            Notes:
                The Mangement IP address for VRS VM if needed to be given statically

                
                This attribute is named `mgmtIPAddress` in VSD API.
                
        """
        return self._mgmt_ip_address

    @mgmt_ip_address.setter
    def mgmt_ip_address(self, value):
        """ Set mgmt_ip_address value.

            Notes:
                The Mangement IP address for VRS VM if needed to be given statically

                
                This attribute is named `mgmtIPAddress` in VSD API.
                
        """
        self._mgmt_ip_address = value

    
    @property
    def mgmt_netmask(self):
        """ Get mgmt_netmask value.

            Notes:
                Netmask of the IP address above

                
                This attribute is named `mgmtNetmask` in VSD API.
                
        """
        return self._mgmt_netmask

    @mgmt_netmask.setter
    def mgmt_netmask(self, value):
        """ Set mgmt_netmask value.

            Notes:
                Netmask of the IP address above

                
                This attribute is named `mgmtNetmask` in VSD API.
                
        """
        self._mgmt_netmask = value

    
    @property
    def mgmt_network_portgroup(self):
        """ Get mgmt_network_portgroup value.

            Notes:
                Management Network Port group

                
                This attribute is named `mgmtNetworkPortgroup` in VSD API.
                
        """
        return self._mgmt_network_portgroup

    @mgmt_network_portgroup.setter
    def mgmt_network_portgroup(self, value):
        """ Set mgmt_network_portgroup value.

            Notes:
                Management Network Port group

                
                This attribute is named `mgmtNetworkPortgroup` in VSD API.
                
        """
        self._mgmt_network_portgroup = value

    
    @property
    def dhcp_relay_server(self):
        """ Get dhcp_relay_server value.

            Notes:
                To provide IP address of the interface from which you will connect to the DHCP relay server

                
                This attribute is named `dhcpRelayServer` in VSD API.
                
        """
        return self._dhcp_relay_server

    @dhcp_relay_server.setter
    def dhcp_relay_server(self, value):
        """ Set dhcp_relay_server value.

            Notes:
                To provide IP address of the interface from which you will connect to the DHCP relay server

                
                This attribute is named `dhcpRelayServer` in VSD API.
                
        """
        self._dhcp_relay_server = value

    
    @property
    def mirror_network_portgroup(self):
        """ Get mirror_network_portgroup value.

            Notes:
                Mirror Port Group Name

                
                This attribute is named `mirrorNetworkPortgroup` in VSD API.
                
        """
        return self._mirror_network_portgroup

    @mirror_network_portgroup.setter
    def mirror_network_portgroup(self, value):
        """ Set mirror_network_portgroup value.

            Notes:
                Mirror Port Group Name

                
                This attribute is named `mirrorNetworkPortgroup` in VSD API.
                
        """
        self._mirror_network_portgroup = value

    
    @property
    def disable_gro_on_datapath(self):
        """ Get disable_gro_on_datapath value.

            Notes:
                Disable GRO on datapath

                
                This attribute is named `disableGROOnDatapath` in VSD API.
                
        """
        return self._disable_gro_on_datapath

    @disable_gro_on_datapath.setter
    def disable_gro_on_datapath(self, value):
        """ Set disable_gro_on_datapath value.

            Notes:
                Disable GRO on datapath

                
                This attribute is named `disableGROOnDatapath` in VSD API.
                
        """
        self._disable_gro_on_datapath = value

    
    @property
    def disable_lro_on_datapath(self):
        """ Get disable_lro_on_datapath value.

            Notes:
                Disable LRO on datapath

                
                This attribute is named `disableLROOnDatapath` in VSD API.
                
        """
        return self._disable_lro_on_datapath

    @disable_lro_on_datapath.setter
    def disable_lro_on_datapath(self, value):
        """ Set disable_lro_on_datapath value.

            Notes:
                Disable LRO on datapath

                
                This attribute is named `disableLROOnDatapath` in VSD API.
                
        """
        self._disable_lro_on_datapath = value

    
    @property
    def site_id(self):
        """ Get site_id value.

            Notes:
                Site ID field for object profiles to support VSD Geo-redundancy

                
                This attribute is named `siteId` in VSD API.
                
        """
        return self._site_id

    @site_id.setter
    def site_id(self, value):
        """ Set site_id value.

            Notes:
                Site ID field for object profiles to support VSD Geo-redundancy

                
                This attribute is named `siteId` in VSD API.
                
        """
        self._site_id = value

    
    @property
    def allow_data_dhcp(self):
        """ Get allow_data_dhcp value.

            Notes:
                Whether to get the Data IP for the VRS VM from DHCP or statically

                
                This attribute is named `allowDataDHCP` in VSD API.
                
        """
        return self._allow_data_dhcp

    @allow_data_dhcp.setter
    def allow_data_dhcp(self, value):
        """ Set allow_data_dhcp value.

            Notes:
                Whether to get the Data IP for the VRS VM from DHCP or statically

                
                This attribute is named `allowDataDHCP` in VSD API.
                
        """
        self._allow_data_dhcp = value

    
    @property
    def allow_mgmt_dhcp(self):
        """ Get allow_mgmt_dhcp value.

            Notes:
                Whether to get the management IP for the VRS VM from DHCP or statically

                
                This attribute is named `allowMgmtDHCP` in VSD API.
                
        """
        return self._allow_mgmt_dhcp

    @allow_mgmt_dhcp.setter
    def allow_mgmt_dhcp(self, value):
        """ Set allow_mgmt_dhcp value.

            Notes:
                Whether to get the management IP for the VRS VM from DHCP or statically

                
                This attribute is named `allowMgmtDHCP` in VSD API.
                
        """
        self._allow_mgmt_dhcp = value

    
    @property
    def flow_eviction_threshold(self):
        """ Get flow_eviction_threshold value.

            Notes:
                Flow Eviction Threshold

                
                This attribute is named `flowEvictionThreshold` in VSD API.
                
        """
        return self._flow_eviction_threshold

    @flow_eviction_threshold.setter
    def flow_eviction_threshold(self, value):
        """ Set flow_eviction_threshold value.

            Notes:
                Flow Eviction Threshold

                
                This attribute is named `flowEvictionThreshold` in VSD API.
                
        """
        self._flow_eviction_threshold = value

    
    @property
    def vm_network_portgroup(self):
        """ Get vm_network_portgroup value.

            Notes:
                VM Network Port Group Name

                
                This attribute is named `vmNetworkPortgroup` in VSD API.
                
        """
        return self._vm_network_portgroup

    @vm_network_portgroup.setter
    def vm_network_portgroup(self, value):
        """ Set vm_network_portgroup value.

            Notes:
                VM Network Port Group Name

                
                This attribute is named `vmNetworkPortgroup` in VSD API.
                
        """
        self._vm_network_portgroup = value

    
    @property
    def enable_vrs_resource_reservation(self):
        """ Get enable_vrs_resource_reservation value.

            Notes:
                Enable resource reservation on the VRS. When this is enabled, all memory and 100% of CPU resources allocated to the VRS will be reserved.

                
                This attribute is named `enableVRSResourceReservation` in VSD API.
                
        """
        return self._enable_vrs_resource_reservation

    @enable_vrs_resource_reservation.setter
    def enable_vrs_resource_reservation(self, value):
        """ Set enable_vrs_resource_reservation value.

            Notes:
                Enable resource reservation on the VRS. When this is enabled, all memory and 100% of CPU resources allocated to the VRS will be reserved.

                
                This attribute is named `enableVRSResourceReservation` in VSD API.
                
        """
        self._enable_vrs_resource_reservation = value

    
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
    def configured_metrics_push_interval(self):
        """ Get configured_metrics_push_interval value.

            Notes:
                Configured VRS metrics push interval on VCIN

                
                This attribute is named `configuredMetricsPushInterval` in VSD API.
                
        """
        return self._configured_metrics_push_interval

    @configured_metrics_push_interval.setter
    def configured_metrics_push_interval(self, value):
        """ Set configured_metrics_push_interval value.

            Notes:
                Configured VRS metrics push interval on VCIN

                
                This attribute is named `configuredMetricsPushInterval` in VSD API.
                
        """
        self._configured_metrics_push_interval = value

    
    @property
    def toolbox_deployment_mode(self):
        """ Get toolbox_deployment_mode value.

            Notes:
                Flag to specify if VRS is deployed using tool box.

                
                This attribute is named `toolboxDeploymentMode` in VSD API.
                
        """
        return self._toolbox_deployment_mode

    @toolbox_deployment_mode.setter
    def toolbox_deployment_mode(self, value):
        """ Set toolbox_deployment_mode value.

            Notes:
                Flag to specify if VRS is deployed using tool box.

                
                This attribute is named `toolboxDeploymentMode` in VSD API.
                
        """
        self._toolbox_deployment_mode = value

    
    @property
    def toolbox_group(self):
        """ Get toolbox_group value.

            Notes:
                Deployment Toolbox Group.

                
                This attribute is named `toolboxGroup` in VSD API.
                
        """
        return self._toolbox_group

    @toolbox_group.setter
    def toolbox_group(self, value):
        """ Set toolbox_group value.

            Notes:
                Deployment Toolbox Group.

                
                This attribute is named `toolboxGroup` in VSD API.
                
        """
        self._toolbox_group = value

    
    @property
    def toolbox_ip(self):
        """ Get toolbox_ip value.

            Notes:
                Deployment Toolbox IP.

                
                This attribute is named `toolboxIP` in VSD API.
                
        """
        return self._toolbox_ip

    @toolbox_ip.setter
    def toolbox_ip(self, value):
        """ Set toolbox_ip value.

            Notes:
                Deployment Toolbox IP.

                
                This attribute is named `toolboxIP` in VSD API.
                
        """
        self._toolbox_ip = value

    
    @property
    def toolbox_password(self):
        """ Get toolbox_password value.

            Notes:
                Deployment Toolbox password.

                
                This attribute is named `toolboxPassword` in VSD API.
                
        """
        return self._toolbox_password

    @toolbox_password.setter
    def toolbox_password(self, value):
        """ Set toolbox_password value.

            Notes:
                Deployment Toolbox password.

                
                This attribute is named `toolboxPassword` in VSD API.
                
        """
        self._toolbox_password = value

    
    @property
    def toolbox_user_name(self):
        """ Get toolbox_user_name value.

            Notes:
                Deployment Toolbox username.

                
                This attribute is named `toolboxUserName` in VSD API.
                
        """
        return self._toolbox_user_name

    @toolbox_user_name.setter
    def toolbox_user_name(self, value):
        """ Set toolbox_user_name value.

            Notes:
                Deployment Toolbox username.

                
                This attribute is named `toolboxUserName` in VSD API.
                
        """
        self._toolbox_user_name = value

    
    @property
    def portgroup_metadata(self):
        """ Get portgroup_metadata value.

            Notes:
                Port Group Meta data

                
                This attribute is named `portgroupMetadata` in VSD API.
                
        """
        return self._portgroup_metadata

    @portgroup_metadata.setter
    def portgroup_metadata(self, value):
        """ Set portgroup_metadata value.

            Notes:
                Port Group Meta data

                
                This attribute is named `portgroupMetadata` in VSD API.
                
        """
        self._portgroup_metadata = value

    
    @property
    def nova_client_version(self):
        """ Get nova_client_version value.

            Notes:
                Nova client Version 

                
                This attribute is named `novaClientVersion` in VSD API.
                
        """
        return self._nova_client_version

    @nova_client_version.setter
    def nova_client_version(self, value):
        """ Set nova_client_version value.

            Notes:
                Nova client Version 

                
                This attribute is named `novaClientVersion` in VSD API.
                
        """
        self._nova_client_version = value

    
    @property
    def nova_identity_url_version(self):
        """ Get nova_identity_url_version value.

            Notes:
                Keystone identity version to use for the Nova metadata configuration on the VRS

                
                This attribute is named `novaIdentityURLVersion` in VSD API.
                
        """
        return self._nova_identity_url_version

    @nova_identity_url_version.setter
    def nova_identity_url_version(self, value):
        """ Set nova_identity_url_version value.

            Notes:
                Keystone identity version to use for the Nova metadata configuration on the VRS

                
                This attribute is named `novaIdentityURLVersion` in VSD API.
                
        """
        self._nova_identity_url_version = value

    
    @property
    def nova_metadata_service_auth_url(self):
        """ Get nova_metadata_service_auth_url value.

            Notes:
                Nova metadata service auth url

                
                This attribute is named `novaMetadataServiceAuthUrl` in VSD API.
                
        """
        return self._nova_metadata_service_auth_url

    @nova_metadata_service_auth_url.setter
    def nova_metadata_service_auth_url(self, value):
        """ Set nova_metadata_service_auth_url value.

            Notes:
                Nova metadata service auth url

                
                This attribute is named `novaMetadataServiceAuthUrl` in VSD API.
                
        """
        self._nova_metadata_service_auth_url = value

    
    @property
    def nova_metadata_service_endpoint(self):
        """ Get nova_metadata_service_endpoint value.

            Notes:
                Nova metadata service endpoint

                
                This attribute is named `novaMetadataServiceEndpoint` in VSD API.
                
        """
        return self._nova_metadata_service_endpoint

    @nova_metadata_service_endpoint.setter
    def nova_metadata_service_endpoint(self, value):
        """ Set nova_metadata_service_endpoint value.

            Notes:
                Nova metadata service endpoint

                
                This attribute is named `novaMetadataServiceEndpoint` in VSD API.
                
        """
        self._nova_metadata_service_endpoint = value

    
    @property
    def nova_metadata_service_password(self):
        """ Get nova_metadata_service_password value.

            Notes:
                Nova metadata service password

                
                This attribute is named `novaMetadataServicePassword` in VSD API.
                
        """
        return self._nova_metadata_service_password

    @nova_metadata_service_password.setter
    def nova_metadata_service_password(self, value):
        """ Set nova_metadata_service_password value.

            Notes:
                Nova metadata service password

                
                This attribute is named `novaMetadataServicePassword` in VSD API.
                
        """
        self._nova_metadata_service_password = value

    
    @property
    def nova_metadata_service_tenant(self):
        """ Get nova_metadata_service_tenant value.

            Notes:
                Nova metadata service tenant

                
                This attribute is named `novaMetadataServiceTenant` in VSD API.
                
        """
        return self._nova_metadata_service_tenant

    @nova_metadata_service_tenant.setter
    def nova_metadata_service_tenant(self, value):
        """ Set nova_metadata_service_tenant value.

            Notes:
                Nova metadata service tenant

                
                This attribute is named `novaMetadataServiceTenant` in VSD API.
                
        """
        self._nova_metadata_service_tenant = value

    
    @property
    def nova_metadata_service_username(self):
        """ Get nova_metadata_service_username value.

            Notes:
                Nova metadata service username

                
                This attribute is named `novaMetadataServiceUsername` in VSD API.
                
        """
        return self._nova_metadata_service_username

    @nova_metadata_service_username.setter
    def nova_metadata_service_username(self, value):
        """ Set nova_metadata_service_username value.

            Notes:
                Nova metadata service username

                
                This attribute is named `novaMetadataServiceUsername` in VSD API.
                
        """
        self._nova_metadata_service_username = value

    
    @property
    def nova_metadata_shared_secret(self):
        """ Get nova_metadata_shared_secret value.

            Notes:
                Nova metadata shared secret

                
                This attribute is named `novaMetadataSharedSecret` in VSD API.
                
        """
        return self._nova_metadata_shared_secret

    @nova_metadata_shared_secret.setter
    def nova_metadata_shared_secret(self, value):
        """ Set nova_metadata_shared_secret value.

            Notes:
                Nova metadata shared secret

                
                This attribute is named `novaMetadataSharedSecret` in VSD API.
                
        """
        self._nova_metadata_shared_secret = value

    
    @property
    def nova_os_keystone_username(self):
        """ Get nova_os_keystone_username value.

            Notes:
                Keystone username used by nova

                
                This attribute is named `novaOSKeystoneUsername` in VSD API.
                
        """
        return self._nova_os_keystone_username

    @nova_os_keystone_username.setter
    def nova_os_keystone_username(self, value):
        """ Set nova_os_keystone_username value.

            Notes:
                Keystone username used by nova

                
                This attribute is named `novaOSKeystoneUsername` in VSD API.
                
        """
        self._nova_os_keystone_username = value

    
    @property
    def nova_project_domain_name(self):
        """ Get nova_project_domain_name value.

            Notes:
                Name of the project that the Nova service uses, can be determined from the nova.conf on the OpenStack controller

                
                This attribute is named `novaProjectDomainName` in VSD API.
                
        """
        return self._nova_project_domain_name

    @nova_project_domain_name.setter
    def nova_project_domain_name(self, value):
        """ Set nova_project_domain_name value.

            Notes:
                Name of the project that the Nova service uses, can be determined from the nova.conf on the OpenStack controller

                
                This attribute is named `novaProjectDomainName` in VSD API.
                
        """
        self._nova_project_domain_name = value

    
    @property
    def nova_project_name(self):
        """ Get nova_project_name value.

            Notes:
                Name of the default Nova project (example: services)

                
                This attribute is named `novaProjectName` in VSD API.
                
        """
        return self._nova_project_name

    @nova_project_name.setter
    def nova_project_name(self, value):
        """ Set nova_project_name value.

            Notes:
                Name of the default Nova project (example: services)

                
                This attribute is named `novaProjectName` in VSD API.
                
        """
        self._nova_project_name = value

    
    @property
    def nova_region_name(self):
        """ Get nova_region_name value.

            Notes:
                Nova region name

                
                This attribute is named `novaRegionName` in VSD API.
                
        """
        return self._nova_region_name

    @nova_region_name.setter
    def nova_region_name(self, value):
        """ Set nova_region_name value.

            Notes:
                Nova region name

                
                This attribute is named `novaRegionName` in VSD API.
                
        """
        self._nova_region_name = value

    
    @property
    def nova_user_domain_name(self):
        """ Get nova_user_domain_name value.

            Notes:
                Name of the user domain used by the Nova service, can be determined from the nova.conf on the OpenStack controller

                
                This attribute is named `novaUserDomainName` in VSD API.
                
        """
        return self._nova_user_domain_name

    @nova_user_domain_name.setter
    def nova_user_domain_name(self, value):
        """ Set nova_user_domain_name value.

            Notes:
                Name of the user domain used by the Nova service, can be determined from the nova.conf on the OpenStack controller

                
                This attribute is named `novaUserDomainName` in VSD API.
                
        """
        self._nova_user_domain_name = value

    
    @property
    def upgrade_package_password(self):
        """ Get upgrade_package_password value.

            Notes:
                Upgrade package password used for script based upgrades

                
                This attribute is named `upgradePackagePassword` in VSD API.
                
        """
        return self._upgrade_package_password

    @upgrade_package_password.setter
    def upgrade_package_password(self, value):
        """ Set upgrade_package_password value.

            Notes:
                Upgrade package password used for script based upgrades

                
                This attribute is named `upgradePackagePassword` in VSD API.
                
        """
        self._upgrade_package_password = value

    
    @property
    def upgrade_package_url(self):
        """ Get upgrade_package_url value.

            Notes:
                Upgrade package URL used for script based upgrades

                
                This attribute is named `upgradePackageURL` in VSD API.
                
        """
        return self._upgrade_package_url

    @upgrade_package_url.setter
    def upgrade_package_url(self, value):
        """ Set upgrade_package_url value.

            Notes:
                Upgrade package URL used for script based upgrades

                
                This attribute is named `upgradePackageURL` in VSD API.
                
        """
        self._upgrade_package_url = value

    
    @property
    def upgrade_package_username(self):
        """ Get upgrade_package_username value.

            Notes:
                Upgrade package username  used for script based upgrades

                
                This attribute is named `upgradePackageUsername` in VSD API.
                
        """
        return self._upgrade_package_username

    @upgrade_package_username.setter
    def upgrade_package_username(self, value):
        """ Set upgrade_package_username value.

            Notes:
                Upgrade package username  used for script based upgrades

                
                This attribute is named `upgradePackageUsername` in VSD API.
                
        """
        self._upgrade_package_username = value

    
    @property
    def upgrade_script_time_limit(self):
        """ Get upgrade_script_time_limit value.

            Notes:
                upgradeScriptTimeLimit

                
                This attribute is named `upgradeScriptTimeLimit` in VSD API.
                
        """
        return self._upgrade_script_time_limit

    @upgrade_script_time_limit.setter
    def upgrade_script_time_limit(self, value):
        """ Set upgrade_script_time_limit value.

            Notes:
                upgradeScriptTimeLimit

                
                This attribute is named `upgradeScriptTimeLimit` in VSD API.
                
        """
        self._upgrade_script_time_limit = value

    
    @property
    def upgrade_status(self):
        """ Get upgrade_status value.

            Notes:
                Script based upgrade Status

                
                This attribute is named `upgradeStatus` in VSD API.
                
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, value):
        """ Set upgrade_status value.

            Notes:
                Script based upgrade Status

                
                This attribute is named `upgradeStatus` in VSD API.
                
        """
        self._upgrade_status = value

    
    @property
    def upgrade_timedout(self):
        """ Get upgrade_timedout value.

            Notes:
                Time limit for the patch based upgrade functionality. If the upgrade process of a VRS has not returned a success or failure status within this time limit, the status will be changed to TIMEOUT. Specified in seconds

                
                This attribute is named `upgradeTimedout` in VSD API.
                
        """
        return self._upgrade_timedout

    @upgrade_timedout.setter
    def upgrade_timedout(self, value):
        """ Set upgrade_timedout value.

            Notes:
                Time limit for the patch based upgrade functionality. If the upgrade process of a VRS has not returned a success or failure status within this time limit, the status will be changed to TIMEOUT. Specified in seconds

                
                This attribute is named `upgradeTimedout` in VSD API.
                
        """
        self._upgrade_timedout = value

    
    @property
    def cpu_count(self):
        """ Get cpu_count value.

            Notes:
                The number of vCPUs that will be assigned to the VRS.

                
                This attribute is named `cpuCount` in VSD API.
                
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, value):
        """ Set cpu_count value.

            Notes:
                The number of vCPUs that will be assigned to the VRS.

                
                This attribute is named `cpuCount` in VSD API.
                
        """
        self._cpu_count = value

    
    @property
    def primary_data_uplink_underlay_id(self):
        """ Get primary_data_uplink_underlay_id value.

            Notes:
                Primary data uplink underlay ID

                
                This attribute is named `primaryDataUplinkUnderlayID` in VSD API.
                
        """
        return self._primary_data_uplink_underlay_id

    @primary_data_uplink_underlay_id.setter
    def primary_data_uplink_underlay_id(self, value):
        """ Set primary_data_uplink_underlay_id value.

            Notes:
                Primary data uplink underlay ID

                
                This attribute is named `primaryDataUplinkUnderlayID` in VSD API.
                
        """
        self._primary_data_uplink_underlay_id = value

    
    @property
    def primary_data_uplink_vdf_control_vlan(self):
        """ Get primary_data_uplink_vdf_control_vlan value.

            Notes:
                The VLAN for the control communication with VSC on the primary datapath interface, when VDF is enabled. This VLAN can not be used as a subnet VLAN in the VSD configuration.

                
                This attribute is named `primaryDataUplinkVDFControlVLAN` in VSD API.
                
        """
        return self._primary_data_uplink_vdf_control_vlan

    @primary_data_uplink_vdf_control_vlan.setter
    def primary_data_uplink_vdf_control_vlan(self, value):
        """ Set primary_data_uplink_vdf_control_vlan value.

            Notes:
                The VLAN for the control communication with VSC on the primary datapath interface, when VDF is enabled. This VLAN can not be used as a subnet VLAN in the VSD configuration.

                
                This attribute is named `primaryDataUplinkVDFControlVLAN` in VSD API.
                
        """
        self._primary_data_uplink_vdf_control_vlan = value

    
    @property
    def primary_nuage_controller(self):
        """ Get primary_nuage_controller value.

            Notes:
                IP address of the primary Controller (VSC)

                
                This attribute is named `primaryNuageController` in VSD API.
                
        """
        return self._primary_nuage_controller

    @primary_nuage_controller.setter
    def primary_nuage_controller(self, value):
        """ Set primary_nuage_controller value.

            Notes:
                IP address of the primary Controller (VSC)

                
                This attribute is named `primaryNuageController` in VSD API.
                
        """
        self._primary_nuage_controller = value

    
    @property
    def vrs_id(self):
        """ Get vrs_id value.

            Notes:
                VCenter Name or Id used by toolbox to identify the VRS virtual machine

                
                This attribute is named `vrsId` in VSD API.
                
        """
        return self._vrs_id

    @vrs_id.setter
    def vrs_id(self, value):
        """ Set vrs_id value.

            Notes:
                VCenter Name or Id used by toolbox to identify the VRS virtual machine

                
                This attribute is named `vrsId` in VSD API.
                
        """
        self._vrs_id = value

    
    @property
    def vrs_marked_as_available(self):
        """ Get vrs_marked_as_available value.

            Notes:
                Indicates whether the VRS Agent has been marked as available by VCIN

                
                This attribute is named `vrsMarkedAsAvailable` in VSD API.
                
        """
        return self._vrs_marked_as_available

    @vrs_marked_as_available.setter
    def vrs_marked_as_available(self, value):
        """ Set vrs_marked_as_available value.

            Notes:
                Indicates whether the VRS Agent has been marked as available by VCIN

                
                This attribute is named `vrsMarkedAsAvailable` in VSD API.
                
        """
        self._vrs_marked_as_available = value

    
    @property
    def vrs_password(self):
        """ Get vrs_password value.

            Notes:
                VRS password to be used by toolbox to communicate with VRS

                
                This attribute is named `vrsPassword` in VSD API.
                
        """
        return self._vrs_password

    @vrs_password.setter
    def vrs_password(self, value):
        """ Set vrs_password value.

            Notes:
                VRS password to be used by toolbox to communicate with VRS

                
                This attribute is named `vrsPassword` in VSD API.
                
        """
        self._vrs_password = value

    
    @property
    def vrs_user_name(self):
        """ Get vrs_user_name value.

            Notes:
                VRS user name to be used by toolbox to communicate with VRS

                
                This attribute is named `vrsUserName` in VSD API.
                
        """
        return self._vrs_user_name

    @vrs_user_name.setter
    def vrs_user_name(self, value):
        """ Set vrs_user_name value.

            Notes:
                VRS user name to be used by toolbox to communicate with VRS

                
                This attribute is named `vrsUserName` in VSD API.
                
        """
        self._vrs_user_name = value

    
    @property
    def static_route(self):
        """ Get static_route value.

            Notes:
                static route to be configured in the VRS

                
                This attribute is named `staticRoute` in VSD API.
                
        """
        return self._static_route

    @static_route.setter
    def static_route(self, value):
        """ Set static_route value.

            Notes:
                static route to be configured in the VRS

                
                This attribute is named `staticRoute` in VSD API.
                
        """
        self._static_route = value

    
    @property
    def static_route_gateway(self):
        """ Get static_route_gateway value.

            Notes:
                Gateway for the static route given above

                
                This attribute is named `staticRouteGateway` in VSD API.
                
        """
        return self._static_route_gateway

    @static_route_gateway.setter
    def static_route_gateway(self, value):
        """ Set static_route_gateway value.

            Notes:
                Gateway for the static route given above

                
                This attribute is named `staticRouteGateway` in VSD API.
                
        """
        self._static_route_gateway = value

    
    @property
    def static_route_netmask(self):
        """ Get static_route_netmask value.

            Notes:
                Nova region name

                
                This attribute is named `staticRouteNetmask` in VSD API.
                
        """
        return self._static_route_netmask

    @static_route_netmask.setter
    def static_route_netmask(self, value):
        """ Set static_route_netmask value.

            Notes:
                Nova region name

                
                This attribute is named `staticRouteNetmask` in VSD API.
                
        """
        self._static_route_netmask = value

    
    @property
    def ntp_server1(self):
        """ Get ntp_server1 value.

            Notes:
                IP of the NTP server 1

                
                This attribute is named `ntpServer1` in VSD API.
                
        """
        return self._ntp_server1

    @ntp_server1.setter
    def ntp_server1(self, value):
        """ Set ntp_server1 value.

            Notes:
                IP of the NTP server 1

                
                This attribute is named `ntpServer1` in VSD API.
                
        """
        self._ntp_server1 = value

    
    @property
    def ntp_server2(self):
        """ Get ntp_server2 value.

            Notes:
                IP of the NTP server 1

                
                This attribute is named `ntpServer2` in VSD API.
                
        """
        return self._ntp_server2

    @ntp_server2.setter
    def ntp_server2(self, value):
        """ Set ntp_server2 value.

            Notes:
                IP of the NTP server 1

                
                This attribute is named `ntpServer2` in VSD API.
                
        """
        self._ntp_server2 = value

    
    @property
    def mtu(self):
        """ Get mtu value.

            Notes:
                Maximum Transmission Unit for eth2 interface

                
        """
        return self._mtu

    @mtu.setter
    def mtu(self, value):
        """ Set mtu value.

            Notes:
                Maximum Transmission Unit for eth2 interface

                
        """
        self._mtu = value

    
    @property
    def successfully_applied_upgrade_package_password(self):
        """ Get successfully_applied_upgrade_package_password value.

            Notes:
                The upgrade package Password that was successfully applied

                
                This attribute is named `successfullyAppliedUpgradePackagePassword` in VSD API.
                
        """
        return self._successfully_applied_upgrade_package_password

    @successfully_applied_upgrade_package_password.setter
    def successfully_applied_upgrade_package_password(self, value):
        """ Set successfully_applied_upgrade_package_password value.

            Notes:
                The upgrade package Password that was successfully applied

                
                This attribute is named `successfullyAppliedUpgradePackagePassword` in VSD API.
                
        """
        self._successfully_applied_upgrade_package_password = value

    
    @property
    def successfully_applied_upgrade_package_url(self):
        """ Get successfully_applied_upgrade_package_url value.

            Notes:
                The upgrade package URL that was successfully applied

                
                This attribute is named `successfullyAppliedUpgradePackageURL` in VSD API.
                
        """
        return self._successfully_applied_upgrade_package_url

    @successfully_applied_upgrade_package_url.setter
    def successfully_applied_upgrade_package_url(self, value):
        """ Set successfully_applied_upgrade_package_url value.

            Notes:
                The upgrade package URL that was successfully applied

                
                This attribute is named `successfullyAppliedUpgradePackageURL` in VSD API.
                
        """
        self._successfully_applied_upgrade_package_url = value

    
    @property
    def successfully_applied_upgrade_package_username(self):
        """ Get successfully_applied_upgrade_package_username value.

            Notes:
                The upgrade package Username that was successfully applied

                
                This attribute is named `successfullyAppliedUpgradePackageUsername` in VSD API.
                
        """
        return self._successfully_applied_upgrade_package_username

    @successfully_applied_upgrade_package_username.setter
    def successfully_applied_upgrade_package_username(self, value):
        """ Set successfully_applied_upgrade_package_username value.

            Notes:
                The upgrade package Username that was successfully applied

                
                This attribute is named `successfullyAppliedUpgradePackageUsername` in VSD API.
                
        """
        self._successfully_applied_upgrade_package_username = value

    
    @property
    def successfully_applied_version(self):
        """ Get successfully_applied_version value.

            Notes:
                successfully Applied Version of the VRS VM

                
                This attribute is named `successfullyAppliedVersion` in VSD API.
                
        """
        return self._successfully_applied_version

    @successfully_applied_version.setter
    def successfully_applied_version(self, value):
        """ Set successfully_applied_version value.

            Notes:
                successfully Applied Version of the VRS VM

                
                This attribute is named `successfullyAppliedVersion` in VSD API.
                
        """
        self._successfully_applied_version = value

    
    @property
    def multi_vmssupport(self):
        """ Get multi_vmssupport value.

            Notes:
                Whether Multi VM is to be used or not

                
                This attribute is named `multiVMSsupport` in VSD API.
                
        """
        return self._multi_vmssupport

    @multi_vmssupport.setter
    def multi_vmssupport(self, value):
        """ Set multi_vmssupport value.

            Notes:
                Whether Multi VM is to be used or not

                
                This attribute is named `multiVMSsupport` in VSD API.
                
        """
        self._multi_vmssupport = value

    
    @property
    def multicast_receive_interface(self):
        """ Get multicast_receive_interface value.

            Notes:
                Multicast Receive Interface

                
                This attribute is named `multicastReceiveInterface` in VSD API.
                
        """
        return self._multicast_receive_interface

    @multicast_receive_interface.setter
    def multicast_receive_interface(self, value):
        """ Set multicast_receive_interface value.

            Notes:
                Multicast Receive Interface

                
                This attribute is named `multicastReceiveInterface` in VSD API.
                
        """
        self._multicast_receive_interface = value

    
    @property
    def multicast_receive_interface_ip(self):
        """ Get multicast_receive_interface_ip value.

            Notes:
                IP address for eth3 interface

                
                This attribute is named `multicastReceiveInterfaceIP` in VSD API.
                
        """
        return self._multicast_receive_interface_ip

    @multicast_receive_interface_ip.setter
    def multicast_receive_interface_ip(self, value):
        """ Set multicast_receive_interface_ip value.

            Notes:
                IP address for eth3 interface

                
                This attribute is named `multicastReceiveInterfaceIP` in VSD API.
                
        """
        self._multicast_receive_interface_ip = value

    
    @property
    def multicast_receive_interface_netmask(self):
        """ Get multicast_receive_interface_netmask value.

            Notes:
                Multicast Interface netmask

                
                This attribute is named `multicastReceiveInterfaceNetmask` in VSD API.
                
        """
        return self._multicast_receive_interface_netmask

    @multicast_receive_interface_netmask.setter
    def multicast_receive_interface_netmask(self, value):
        """ Set multicast_receive_interface_netmask value.

            Notes:
                Multicast Interface netmask

                
                This attribute is named `multicastReceiveInterfaceNetmask` in VSD API.
                
        """
        self._multicast_receive_interface_netmask = value

    
    @property
    def multicast_receive_range(self):
        """ Get multicast_receive_range value.

            Notes:
                Allowed Range to receive the Multicast traffic from

                
                This attribute is named `multicastReceiveRange` in VSD API.
                
        """
        return self._multicast_receive_range

    @multicast_receive_range.setter
    def multicast_receive_range(self, value):
        """ Set multicast_receive_range value.

            Notes:
                Allowed Range to receive the Multicast traffic from

                
                This attribute is named `multicastReceiveRange` in VSD API.
                
        """
        self._multicast_receive_range = value

    
    @property
    def multicast_send_interface(self):
        """ Get multicast_send_interface value.

            Notes:
                Multicast Send Interface

                
                This attribute is named `multicastSendInterface` in VSD API.
                
        """
        return self._multicast_send_interface

    @multicast_send_interface.setter
    def multicast_send_interface(self, value):
        """ Set multicast_send_interface value.

            Notes:
                Multicast Send Interface

                
                This attribute is named `multicastSendInterface` in VSD API.
                
        """
        self._multicast_send_interface = value

    
    @property
    def multicast_send_interface_ip(self):
        """ Get multicast_send_interface_ip value.

            Notes:
                IP address for eth3 interface

                
                This attribute is named `multicastSendInterfaceIP` in VSD API.
                
        """
        return self._multicast_send_interface_ip

    @multicast_send_interface_ip.setter
    def multicast_send_interface_ip(self, value):
        """ Set multicast_send_interface_ip value.

            Notes:
                IP address for eth3 interface

                
                This attribute is named `multicastSendInterfaceIP` in VSD API.
                
        """
        self._multicast_send_interface_ip = value

    
    @property
    def multicast_send_interface_netmask(self):
        """ Get multicast_send_interface_netmask value.

            Notes:
                Multicast Interface netmask

                
                This attribute is named `multicastSendInterfaceNetmask` in VSD API.
                
        """
        return self._multicast_send_interface_netmask

    @multicast_send_interface_netmask.setter
    def multicast_send_interface_netmask(self, value):
        """ Set multicast_send_interface_netmask value.

            Notes:
                Multicast Interface netmask

                
                This attribute is named `multicastSendInterfaceNetmask` in VSD API.
                
        """
        self._multicast_send_interface_netmask = value

    
    @property
    def multicast_source_portgroup(self):
        """ Get multicast_source_portgroup value.

            Notes:
                Multi Cast Source Port Group Name

                
                This attribute is named `multicastSourcePortgroup` in VSD API.
                
        """
        return self._multicast_source_portgroup

    @multicast_source_portgroup.setter
    def multicast_source_portgroup(self, value):
        """ Set multicast_source_portgroup value.

            Notes:
                Multi Cast Source Port Group Name

                
                This attribute is named `multicastSourcePortgroup` in VSD API.
                
        """
        self._multicast_source_portgroup = value

    
    @property
    def customized_script_url(self):
        """ Get customized_script_url value.

            Notes:
                To provide a URL to install a custom app on VRS

                
                This attribute is named `customizedScriptURL` in VSD API.
                
        """
        return self._customized_script_url

    @customized_script_url.setter
    def customized_script_url(self, value):
        """ Set customized_script_url value.

            Notes:
                To provide a URL to install a custom app on VRS

                
                This attribute is named `customizedScriptURL` in VSD API.
                
        """
        self._customized_script_url = value

    
    @property
    def available_networks(self):
        """ Get available_networks value.

            Notes:
                List of the available network list for the hypervisor.

                
                This attribute is named `availableNetworks` in VSD API.
                
        """
        return self._available_networks

    @available_networks.setter
    def available_networks(self, value):
        """ Set available_networks value.

            Notes:
                List of the available network list for the hypervisor.

                
                This attribute is named `availableNetworks` in VSD API.
                
        """
        self._available_networks = value

    
    @property
    def ovf_url(self):
        """ Get ovf_url value.

            Notes:
                ovf url

                
                This attribute is named `ovfURL` in VSD API.
                
        """
        return self._ovf_url

    @ovf_url.setter
    def ovf_url(self, value):
        """ Set ovf_url value.

            Notes:
                ovf url

                
                This attribute is named `ovfURL` in VSD API.
                
        """
        self._ovf_url = value

    
    @property
    def avrs_enabled(self):
        """ Get avrs_enabled value.

            Notes:
                When enabled, the AVRS functionality will be enabled on the VRS during bootstrapping. This feature requires special AVRS licenses and specific configuration which is described in the product documentation.

                
                This attribute is named `avrsEnabled` in VSD API.
                
        """
        return self._avrs_enabled

    @avrs_enabled.setter
    def avrs_enabled(self, value):
        """ Set avrs_enabled value.

            Notes:
                When enabled, the AVRS functionality will be enabled on the VRS during bootstrapping. This feature requires special AVRS licenses and specific configuration which is described in the product documentation.

                
                This attribute is named `avrsEnabled` in VSD API.
                
        """
        self._avrs_enabled = value

    
    @property
    def avrs_profile(self):
        """ Get avrs_profile value.

            Notes:
                The AVRS configuration profile that needs to be set up. This profile will configure the AVRS services so that it can support a certain type of performance.

                
                This attribute is named `avrsProfile` in VSD API.
                
        """
        return self._avrs_profile

    @avrs_profile.setter
    def avrs_profile(self, value):
        """ Set avrs_profile value.

            Notes:
                The AVRS configuration profile that needs to be set up. This profile will configure the AVRS services so that it can support a certain type of performance.

                
                This attribute is named `avrsProfile` in VSD API.
                
        """
        self._avrs_profile = value

    
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
    def hypervisor_ip(self):
        """ Get hypervisor_ip value.

            Notes:
                IP Address of the Hypervisor

                
                This attribute is named `hypervisorIP` in VSD API.
                
        """
        return self._hypervisor_ip

    @hypervisor_ip.setter
    def hypervisor_ip(self, value):
        """ Set hypervisor_ip value.

            Notes:
                IP Address of the Hypervisor

                
                This attribute is named `hypervisorIP` in VSD API.
                
        """
        self._hypervisor_ip = value

    
    @property
    def hypervisor_password(self):
        """ Get hypervisor_password value.

            Notes:
                Hypervisor username

                
                This attribute is named `hypervisorPassword` in VSD API.
                
        """
        return self._hypervisor_password

    @hypervisor_password.setter
    def hypervisor_password(self, value):
        """ Set hypervisor_password value.

            Notes:
                Hypervisor username

                
                This attribute is named `hypervisorPassword` in VSD API.
                
        """
        self._hypervisor_password = value

    
    @property
    def hypervisor_user(self):
        """ Get hypervisor_user value.

            Notes:
                Hypervisor username

                
                This attribute is named `hypervisorUser` in VSD API.
                
        """
        return self._hypervisor_user

    @hypervisor_user.setter
    def hypervisor_user(self, value):
        """ Set hypervisor_user value.

            Notes:
                Hypervisor username

                
                This attribute is named `hypervisorUser` in VSD API.
                
        """
        self._hypervisor_user = value

    

    