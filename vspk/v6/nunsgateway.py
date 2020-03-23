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




from .fetchers import NUPatchsFetcher


from .fetchers import NUGatewaySecuritiesFetcher


from .fetchers import NUPATNATPoolsFetcher


from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUWirelessPortsFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVNFsFetcher


from .fetchers import NUInfrastructureConfigsFetcher


from .fetchers import NUEnterprisePermissionsFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NULocationsFetcher


from .fetchers import NUCommandsFetcher


from .fetchers import NUBootstrapsFetcher


from .fetchers import NUBootstrapActivationsFetcher


from .fetchers import NUNSPortInfosFetcher


from .fetchers import NUUplinkConnectionsFetcher


from .fetchers import NUNSGatewayMonitorsFetcher


from .fetchers import NUNSGatewaySummariesFetcher


from .fetchers import NUNSGInfosFetcher


from .fetchers import NUNSPortsFetcher


from .fetchers import NUSubnetsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUNSGateway(NURESTObject):
    """ Represents a NSGateway in the VSD

        Notes:
            Network Services Gateways are a policy enforcement end-points responsible for the delivery of networking services. NSG access ports/VLANs may be attached to existing host or bridge VPorts.
    """

    __rest_name__ = "nsgateway"
    __resource_name__ = "nsgateways"

    
    ## Constants
    
    CONST_FAMILY_NSG_C = "NSG_C"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_NETWORK_ACCELERATION_NONE = "NONE"
    
    CONST_FAMILY_NSG_E = "NSG_E"
    
    CONST_INHERITED_SSH_SERVICE_STATE_ENABLED = "ENABLED"
    
    CONST_CONFIGURATION_RELOAD_STATE_FAILED_TO_APPLY = "FAILED_TO_APPLY"
    
    CONST_FUNCTIONS_HUB = "HUB"
    
    CONST_BOOTSTRAP_STATUS_REVOKED = "REVOKED"
    
    CONST_CONFIGURATION_STATUS_FAILURE = "FAILURE"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ZFB_MATCH_ATTRIBUTE_MAC_ADDRESS = "MAC_ADDRESS"
    
    CONST_PERSONALITY_NSGDUC = "NSGDUC"
    
    CONST_FAMILY_NSG_V = "NSG_V"
    
    CONST_DERIVED_SSH_SERVICE_STATE_INSTANCE_DISABLED = "INSTANCE_DISABLED"
    
    CONST_BOOTSTRAP_STATUS_ACTIVE = "ACTIVE"
    
    CONST_ZFB_MATCH_ATTRIBUTE_IP_ADDRESS = "IP_ADDRESS"
    
    CONST_FAMILY_NSG_X = "NSG_X"
    
    CONST_SYSLOG_LEVEL_NOTICE = "NOTICE"
    
    CONST_FAMILY_NSG_E200 = "NSG_E200"
    
    CONST_SYSLOG_LEVEL_INFO = "INFO"
    
    CONST_BOOTSTRAP_STATUS_NOTIFICATION_APP_REQ_SENT = "NOTIFICATION_APP_REQ_SENT"
    
    CONST_SSH_SERVICE_DISABLED = "DISABLED"
    
    CONST_ZFB_MATCH_ATTRIBUTE_NSGATEWAY_ID = "NSGATEWAY_ID"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_NETWORK_ACCELERATION_PERFORMANCE = "PERFORMANCE"
    
    CONST_SSH_SERVICE_ENABLED = "ENABLED"
    
    CONST_BOOTSTRAP_STATUS_NOTIFICATION_APP_REQ_ACK = "NOTIFICATION_APP_REQ_ACK"
    
    CONST_PERSONALITY_NSG = "NSG"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_DERIVED_SSH_SERVICE_STATE_INHERITED_ENABLED = "INHERITED_ENABLED"
    
    CONST_SYSLOG_LEVEL_EMERGENCY = "EMERGENCY"
    
    CONST_BOOTSTRAP_STATUS_QUARANTINED = "QUARANTINED"
    
    CONST_CONFIGURATION_STATUS_SUCCESS = "SUCCESS"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_CONFIGURATION_RELOAD_STATE_UNKNOWN = "UNKNOWN"
    
    CONST_SYSLOG_LEVEL_ALERT = "ALERT"
    
    CONST_BOOTSTRAP_STATUS_CERTIFICATE_SIGNED = "CERTIFICATE_SIGNED"
    
    CONST_FAMILY_NSG_AZ = "NSG_AZ"
    
    CONST_FAMILY_ANY = "ANY"
    
    CONST_TPM_STATUS_DISABLED = "DISABLED"
    
    CONST_CONFIGURATION_RELOAD_STATE_APPLIED = "APPLIED"
    
    CONST_ZFB_MATCH_ATTRIBUTE_NONE = "NONE"
    
    CONST_CONFIGURE_LOAD_BALANCING_DISABLED = "DISABLED"
    
    CONST_CONFIGURATION_RELOAD_STATE_PENDING = "PENDING"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_SYSLOG_LEVEL_WARNING = "WARNING"
    
    CONST_NETWORK_ACCELERATION_VNF_AWARE = "VNF_AWARE"
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_DERIVED_SSH_SERVICE_STATE_INHERITED_DISABLED = "INHERITED_DISABLED"
    
    CONST_TPM_STATUS_ENABLED_NOT_OPERATIONAL = "ENABLED_NOT_OPERATIONAL"
    
    CONST_FUNCTIONS_UBR = "UBR"
    
    CONST_SYSLOG_LEVEL_ERROR = "ERROR"
    
    CONST_TPM_STATUS_UNKNOWN = "UNKNOWN"
    
    CONST_FAMILY_NSG_E300 = "NSG_E300"
    
    CONST_FAMILY_NSG_X200 = "NSG_X200"
    
    CONST_DERIVED_SSH_SERVICE_STATE_INSTANCE_ENABLED = "INSTANCE_ENABLED"
    
    CONST_CONFIGURE_LOAD_BALANCING_INHERITED = "INHERITED"
    
    CONST_TUNNEL_SHAPING_DISABLED = "DISABLED"
    
    CONST_ZFB_MATCH_ATTRIBUTE_SERIAL_NUMBER = "SERIAL_NUMBER"
    
    CONST_NETWORK_ACCELERATION_SESSION_OPTIMIZED = "SESSION_OPTIMIZED"
    
    CONST_ZFB_MATCH_ATTRIBUTE_UUID = "UUID"
    
    CONST_FAMILY_NSG_AMI = "NSG_AMI"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_DERIVED_SSH_SERVICE_STATE_UNKNOWN = "UNKNOWN"
    
    CONST_FUNCTIONS_GATEWAY = "GATEWAY"
    
    CONST_INHERITED_SSH_SERVICE_STATE_DISABLED = "DISABLED"
    
    CONST_TPM_STATUS_ENABLED_OPERATIONAL = "ENABLED_OPERATIONAL"
    
    CONST_SSH_SERVICE_INHERITED = "INHERITED"
    
    CONST_SYSLOG_LEVEL_CRITICAL = "CRITICAL"
    
    CONST_CONFIGURATION_STATUS_UNKNOWN = "UNKNOWN"
    
    CONST_ZFB_MATCH_ATTRIBUTE_HOSTNAME = "HOSTNAME"
    
    CONST_CONFIGURATION_RELOAD_STATE_SENT = "SENT"
    
    CONST_BOOTSTRAP_STATUS_INACTIVE = "INACTIVE"
    
    CONST_TUNNEL_SHAPING_ENABLED = "ENABLED"
    
    CONST_PERSONALITY_NSGBR = "NSGBR"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NSGateway instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsgateway = NUNSGateway(id=u'xxxx-xxx-xxx-xxx', name=u'NSGateway')
                >>> nsgateway = NUNSGateway(data=my_dict)
        """

        super(NUNSGateway, self).__init__()

        # Read/Write Attributes
        
        self._mac_address = None
        self._aar_application_release_date = None
        self._aar_application_version = None
        self._nat_traversal_enabled = None
        self._tcpmss_enabled = None
        self._tcp_maximum_segment_size = None
        self._zfb_match_attribute = None
        self._zfb_match_value = None
        self._bios_release_date = None
        self._bios_version = None
        self._sku = None
        self._tpm_status = None
        self._tpm_version = None
        self._cpu_type = None
        self._vsdaar_application_version = None
        self._nsg_version = None
        self._ssh_service = None
        self._uuid = None
        self._name = None
        self._family = None
        self._last_configuration_reload_timestamp = None
        self._last_updated_by = None
        self._datapath_id = None
        self._gateway_config_raw_version = None
        self._gateway_config_version = None
        self._gateway_connected = None
        self._redundancy_group_id = None
        self._template_id = None
        self._pending = None
        self._serial_number = None
        self._derived_ssh_service_state = None
        self._permitted_action = None
        self._personality = None
        self._description = None
        self._network_acceleration = None
        self._libraries = None
        self._embedded_metadata = None
        self._inherited_ssh_service_state = None
        self._enterprise_id = None
        self._entity_scope = None
        self._location_id = None
        self._configuration_reload_state = None
        self._configuration_status = None
        self._configure_load_balancing = None
        self._control_traffic_cos_value = None
        self._control_traffic_dscp_value = None
        self._bootstrap_id = None
        self._bootstrap_status = None
        self._operation_mode = None
        self._operation_status = None
        self._product_name = None
        self._associated_gateway_security_id = None
        self._associated_gateway_security_profile_id = None
        self._associated_nsg_info_id = None
        self._associated_nsg_upgrade_profile_id = None
        self._associated_overlay_management_profile_id = None
        self._functions = None
        self._tunnel_shaping = None
        self._auto_disc_gateway_id = None
        self._external_id = None
        self._syslog_level = None
        self._system_id = None
        
        self.expose_attribute(local_name="mac_address", remote_name="MACAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aar_application_release_date", remote_name="AARApplicationReleaseDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aar_application_version", remote_name="AARApplicationVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nat_traversal_enabled", remote_name="NATTraversalEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tcpmss_enabled", remote_name="TCPMSSEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tcp_maximum_segment_size", remote_name="TCPMaximumSegmentSize", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zfb_match_attribute", remote_name="ZFBMatchAttribute", attribute_type=str, is_required=False, is_unique=False, choices=[u'HOSTNAME', u'IP_ADDRESS', u'MAC_ADDRESS', u'NONE', u'NSGATEWAY_ID', u'SERIAL_NUMBER', u'UUID'])
        self.expose_attribute(local_name="zfb_match_value", remote_name="ZFBMatchValue", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bios_release_date", remote_name="BIOSReleaseDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bios_version", remote_name="BIOSVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sku", remote_name="SKU", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tpm_status", remote_name="TPMStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED_NOT_OPERATIONAL', u'ENABLED_OPERATIONAL', u'UNKNOWN'])
        self.expose_attribute(local_name="tpm_version", remote_name="TPMVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cpu_type", remote_name="CPUType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vsdaar_application_version", remote_name="VSDAARApplicationVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_version", remote_name="NSGVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ssh_service", remote_name="SSHService", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="uuid", remote_name="UUID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="family", remote_name="family", attribute_type=str, is_required=False, is_unique=False, choices=[u'ANY', u'NSG_AMI', u'NSG_AZ', u'NSG_C', u'NSG_E', u'NSG_E200', u'NSG_E300', u'NSG_V', u'NSG_X', u'NSG_X200'])
        self.expose_attribute(local_name="last_configuration_reload_timestamp", remote_name="lastConfigurationReloadTimestamp", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="datapath_id", remote_name="datapathID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_config_raw_version", remote_name="gatewayConfigRawVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_config_version", remote_name="gatewayConfigVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_connected", remote_name="gatewayConnected", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redundancy_group_id", remote_name="redundancyGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="pending", remote_name="pending", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="serial_number", remote_name="serialNumber", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="derived_ssh_service_state", remote_name="derivedSSHServiceState", attribute_type=str, is_required=False, is_unique=False, choices=[u'INHERITED_DISABLED', u'INHERITED_ENABLED', u'INSTANCE_DISABLED', u'INSTANCE_ENABLED', u'UNKNOWN'])
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=False, is_unique=False, choices=[u'NSG', u'NSGBR', u'NSGDUC'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_acceleration", remote_name="networkAcceleration", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'PERFORMANCE', u'SESSION_OPTIMIZED', u'VNF_AWARE'])
        self.expose_attribute(local_name="libraries", remote_name="libraries", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="inherited_ssh_service_state", remote_name="inheritedSSHServiceState", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED'])
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="location_id", remote_name="locationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="configuration_reload_state", remote_name="configurationReloadState", attribute_type=str, is_required=False, is_unique=False, choices=[u'APPLIED', u'FAILED_TO_APPLY', u'PENDING', u'SENT', u'UNKNOWN'])
        self.expose_attribute(local_name="configuration_status", remote_name="configurationStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'FAILURE', u'SUCCESS', u'UNKNOWN'])
        self.expose_attribute(local_name="configure_load_balancing", remote_name="configureLoadBalancing", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'INHERITED'])
        self.expose_attribute(local_name="control_traffic_cos_value", remote_name="controlTrafficCOSValue", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="control_traffic_dscp_value", remote_name="controlTrafficDSCPValue", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bootstrap_id", remote_name="bootstrapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bootstrap_status", remote_name="bootstrapStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'ACTIVE', u'CERTIFICATE_SIGNED', u'INACTIVE', u'NOTIFICATION_APP_REQ_ACK', u'NOTIFICATION_APP_REQ_SENT', u'QUARANTINED', u'REVOKED'])
        self.expose_attribute(local_name="operation_mode", remote_name="operationMode", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="operation_status", remote_name="operationStatus", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="product_name", remote_name="productName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_gateway_security_id", remote_name="associatedGatewaySecurityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_gateway_security_profile_id", remote_name="associatedGatewaySecurityProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_nsg_info_id", remote_name="associatedNSGInfoID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_nsg_upgrade_profile_id", remote_name="associatedNSGUpgradeProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_overlay_management_profile_id", remote_name="associatedOverlayManagementProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="functions", remote_name="functions", attribute_type=list, is_required=False, is_unique=False, choices=[u'GATEWAY', u'HUB', u'UBR'])
        self.expose_attribute(local_name="tunnel_shaping", remote_name="tunnelShaping", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED'])
        self.expose_attribute(local_name="auto_disc_gateway_id", remote_name="autoDiscGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="syslog_level", remote_name="syslogLevel", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALERT', u'CRITICAL', u'EMERGENCY', u'ERROR', u'INFO', u'NOTICE', u'WARNING'])
        self.expose_attribute(local_name="system_id", remote_name="systemID", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.patchs = NUPatchsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.gateway_securities = NUGatewaySecuritiesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.patnat_pools = NUPATNATPoolsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.wireless_ports = NUWirelessPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vnfs = NUVNFsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.infrastructure_configs = NUInfrastructureConfigsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.locations = NULocationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.commands = NUCommandsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bootstraps = NUBootstrapsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bootstrap_activations = NUBootstrapActivationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_port_infos = NUNSPortInfosFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.uplink_connections = NUUplinkConnectionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_gateway_monitors = NUNSGatewayMonitorsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_gateway_summaries = NUNSGatewaySummariesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.nsg_infos = NUNSGInfosFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_ports = NUNSPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.subnets = NUSubnetsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def mac_address(self):
        """ Get mac_address value.

            Notes:
                MAC Address of the NSG

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        """ Set mac_address value.

            Notes:
                MAC Address of the NSG

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        self._mac_address = value

    
    @property
    def aar_application_release_date(self):
        """ Get aar_application_release_date value.

            Notes:
                Release Date of the AAR Application

                
                This attribute is named `AARApplicationReleaseDate` in VSD API.
                
        """
        return self._aar_application_release_date

    @aar_application_release_date.setter
    def aar_application_release_date(self, value):
        """ Set aar_application_release_date value.

            Notes:
                Release Date of the AAR Application

                
                This attribute is named `AARApplicationReleaseDate` in VSD API.
                
        """
        self._aar_application_release_date = value

    
    @property
    def aar_application_version(self):
        """ Get aar_application_version value.

            Notes:
                The AAR Application Version

                
                This attribute is named `AARApplicationVersion` in VSD API.
                
        """
        return self._aar_application_version

    @aar_application_version.setter
    def aar_application_version(self, value):
        """ Set aar_application_version value.

            Notes:
                The AAR Application Version

                
                This attribute is named `AARApplicationVersion` in VSD API.
                
        """
        self._aar_application_version = value

    
    @property
    def nat_traversal_enabled(self):
        """ Get nat_traversal_enabled value.

            Notes:
                This attribute is deprecated in version 4.0.

                
                This attribute is named `NATTraversalEnabled` in VSD API.
                
        """
        return self._nat_traversal_enabled

    @nat_traversal_enabled.setter
    def nat_traversal_enabled(self, value):
        """ Set nat_traversal_enabled value.

            Notes:
                This attribute is deprecated in version 4.0.

                
                This attribute is named `NATTraversalEnabled` in VSD API.
                
        """
        self._nat_traversal_enabled = value

    
    @property
    def tcpmss_enabled(self):
        """ Get tcpmss_enabled value.

            Notes:
                Boolean flag to indicate whether MSS on TCP is enabled or not

                
                This attribute is named `TCPMSSEnabled` in VSD API.
                
        """
        return self._tcpmss_enabled

    @tcpmss_enabled.setter
    def tcpmss_enabled(self, value):
        """ Set tcpmss_enabled value.

            Notes:
                Boolean flag to indicate whether MSS on TCP is enabled or not

                
                This attribute is named `TCPMSSEnabled` in VSD API.
                
        """
        self._tcpmss_enabled = value

    
    @property
    def tcp_maximum_segment_size(self):
        """ Get tcp_maximum_segment_size value.

            Notes:
                Maximum Segment Size for TCP(min = 576, max = 7812).

                
                This attribute is named `TCPMaximumSegmentSize` in VSD API.
                
        """
        return self._tcp_maximum_segment_size

    @tcp_maximum_segment_size.setter
    def tcp_maximum_segment_size(self, value):
        """ Set tcp_maximum_segment_size value.

            Notes:
                Maximum Segment Size for TCP(min = 576, max = 7812).

                
                This attribute is named `TCPMaximumSegmentSize` in VSD API.
                
        """
        self._tcp_maximum_segment_size = value

    
    @property
    def zfb_match_attribute(self):
        """ Get zfb_match_attribute value.

            Notes:
                The Zero Factor Bootstrapping (ZFB) Attribute that should be used to match the gateway on when it tries to bootstrap.

                
                This attribute is named `ZFBMatchAttribute` in VSD API.
                
        """
        return self._zfb_match_attribute

    @zfb_match_attribute.setter
    def zfb_match_attribute(self, value):
        """ Set zfb_match_attribute value.

            Notes:
                The Zero Factor Bootstrapping (ZFB) Attribute that should be used to match the gateway on when it tries to bootstrap.

                
                This attribute is named `ZFBMatchAttribute` in VSD API.
                
        """
        self._zfb_match_attribute = value

    
    @property
    def zfb_match_value(self):
        """ Get zfb_match_value value.

            Notes:
                The Zero Factor Bootstrapping (ZFB) value that needs to match with the gateway during the bootstrap attempt. This value needs to match with the ZFB Match Attribute.

                
                This attribute is named `ZFBMatchValue` in VSD API.
                
        """
        return self._zfb_match_value

    @zfb_match_value.setter
    def zfb_match_value(self, value):
        """ Set zfb_match_value value.

            Notes:
                The Zero Factor Bootstrapping (ZFB) value that needs to match with the gateway during the bootstrap attempt. This value needs to match with the ZFB Match Attribute.

                
                This attribute is named `ZFBMatchValue` in VSD API.
                
        """
        self._zfb_match_value = value

    
    @property
    def bios_release_date(self):
        """ Get bios_release_date value.

            Notes:
                Release Date of the NSG BiOS

                
                This attribute is named `BIOSReleaseDate` in VSD API.
                
        """
        return self._bios_release_date

    @bios_release_date.setter
    def bios_release_date(self, value):
        """ Set bios_release_date value.

            Notes:
                Release Date of the NSG BiOS

                
                This attribute is named `BIOSReleaseDate` in VSD API.
                
        """
        self._bios_release_date = value

    
    @property
    def bios_version(self):
        """ Get bios_version value.

            Notes:
                NSG BIOS Version

                
                This attribute is named `BIOSVersion` in VSD API.
                
        """
        return self._bios_version

    @bios_version.setter
    def bios_version(self, value):
        """ Set bios_version value.

            Notes:
                NSG BIOS Version

                
                This attribute is named `BIOSVersion` in VSD API.
                
        """
        self._bios_version = value

    
    @property
    def sku(self):
        """ Get sku value.

            Notes:
                The part number of the NSG

                
                This attribute is named `SKU` in VSD API.
                
        """
        return self._sku

    @sku.setter
    def sku(self, value):
        """ Set sku value.

            Notes:
                The part number of the NSG

                
                This attribute is named `SKU` in VSD API.
                
        """
        self._sku = value

    
    @property
    def tpm_status(self):
        """ Get tpm_status value.

            Notes:
                TPM Status of the NSG based on the information received by the device during bootstrapping or upgrade.

                
                This attribute is named `TPMStatus` in VSD API.
                
        """
        return self._tpm_status

    @tpm_status.setter
    def tpm_status(self, value):
        """ Set tpm_status value.

            Notes:
                TPM Status of the NSG based on the information received by the device during bootstrapping or upgrade.

                
                This attribute is named `TPMStatus` in VSD API.
                
        """
        self._tpm_status = value

    
    @property
    def tpm_version(self):
        """ Get tpm_version value.

            Notes:
                TPM (Trusted Platform Module) version as reported by the NSG.

                
                This attribute is named `TPMVersion` in VSD API.
                
        """
        return self._tpm_version

    @tpm_version.setter
    def tpm_version(self, value):
        """ Set tpm_version value.

            Notes:
                TPM (Trusted Platform Module) version as reported by the NSG.

                
                This attribute is named `TPMVersion` in VSD API.
                
        """
        self._tpm_version = value

    
    @property
    def cpu_type(self):
        """ Get cpu_type value.

            Notes:
                The NSG Processor Type as reported during bootstrapping.

                
                This attribute is named `CPUType` in VSD API.
                
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, value):
        """ Set cpu_type value.

            Notes:
                The NSG Processor Type as reported during bootstrapping.

                
                This attribute is named `CPUType` in VSD API.
                
        """
        self._cpu_type = value

    
    @property
    def vsdaar_application_version(self):
        """ Get vsdaar_application_version value.

            Notes:
                Version of the latest imported Application Signatures.

                
                This attribute is named `VSDAARApplicationVersion` in VSD API.
                
        """
        return self._vsdaar_application_version

    @vsdaar_application_version.setter
    def vsdaar_application_version(self, value):
        """ Set vsdaar_application_version value.

            Notes:
                Version of the latest imported Application Signatures.

                
                This attribute is named `VSDAARApplicationVersion` in VSD API.
                
        """
        self._vsdaar_application_version = value

    
    @property
    def nsg_version(self):
        """ Get nsg_version value.

            Notes:
                The NSG Version (software) as reported during bootstrapping or following an upgrade.

                
                This attribute is named `NSGVersion` in VSD API.
                
        """
        return self._nsg_version

    @nsg_version.setter
    def nsg_version(self, value):
        """ Set nsg_version value.

            Notes:
                The NSG Version (software) as reported during bootstrapping or following an upgrade.

                
                This attribute is named `NSGVersion` in VSD API.
                
        """
        self._nsg_version = value

    
    @property
    def ssh_service(self):
        """ Get ssh_service value.

            Notes:
                Indicates if SSH Service is enabled/disabled on a NSG. The value configured for this attribute is used only when instanceSSHOverride is allowed on the associated Gateway Template.

                
                This attribute is named `SSHService` in VSD API.
                
        """
        return self._ssh_service

    @ssh_service.setter
    def ssh_service(self, value):
        """ Set ssh_service value.

            Notes:
                Indicates if SSH Service is enabled/disabled on a NSG. The value configured for this attribute is used only when instanceSSHOverride is allowed on the associated Gateway Template.

                
                This attribute is named `SSHService` in VSD API.
                
        """
        self._ssh_service = value

    
    @property
    def uuid(self):
        """ Get uuid value.

            Notes:
                The Redhat UUID of the NSG

                
                This attribute is named `UUID` in VSD API.
                
        """
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """ Set uuid value.

            Notes:
                The Redhat UUID of the NSG

                
                This attribute is named `UUID` in VSD API.
                
        """
        self._uuid = value

    
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
    def family(self):
        """ Get family value.

            Notes:
                The NSG Family type.

                
        """
        return self._family

    @family.setter
    def family(self, value):
        """ Set family value.

            Notes:
                The NSG Family type.

                
        """
        self._family = value

    
    @property
    def last_configuration_reload_timestamp(self):
        """ Get last_configuration_reload_timestamp value.

            Notes:
                Time stamp of the last known configuration update of the NSG.  This timestamp gets updated when a bootstrap is successful or when a configuration reload request triggered by VSD is successful.

                
                This attribute is named `lastConfigurationReloadTimestamp` in VSD API.
                
        """
        return self._last_configuration_reload_timestamp

    @last_configuration_reload_timestamp.setter
    def last_configuration_reload_timestamp(self, value):
        """ Set last_configuration_reload_timestamp value.

            Notes:
                Time stamp of the last known configuration update of the NSG.  This timestamp gets updated when a bootstrap is successful or when a configuration reload request triggered by VSD is successful.

                
                This attribute is named `lastConfigurationReloadTimestamp` in VSD API.
                
        """
        self._last_configuration_reload_timestamp = value

    
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
    def datapath_id(self):
        """ Get datapath_id value.

            Notes:
                Identifier of the Gateway, based on the systemId

                
                This attribute is named `datapathID` in VSD API.
                
        """
        return self._datapath_id

    @datapath_id.setter
    def datapath_id(self, value):
        """ Set datapath_id value.

            Notes:
                Identifier of the Gateway, based on the systemId

                
                This attribute is named `datapathID` in VSD API.
                
        """
        self._datapath_id = value

    
    @property
    def gateway_config_raw_version(self):
        """ Get gateway_config_raw_version value.

            Notes:
                Release version of NSG, which is used to determine the feature capabilties of NSG.

                
                This attribute is named `gatewayConfigRawVersion` in VSD API.
                
        """
        return self._gateway_config_raw_version

    @gateway_config_raw_version.setter
    def gateway_config_raw_version(self, value):
        """ Set gateway_config_raw_version value.

            Notes:
                Release version of NSG, which is used to determine the feature capabilties of NSG.

                
                This attribute is named `gatewayConfigRawVersion` in VSD API.
                
        """
        self._gateway_config_raw_version = value

    
    @property
    def gateway_config_version(self):
        """ Get gateway_config_version value.

            Notes:
                Interpreted version of NSG, which is used to determine the feature capabilities of NSG.

                
                This attribute is named `gatewayConfigVersion` in VSD API.
                
        """
        return self._gateway_config_version

    @gateway_config_version.setter
    def gateway_config_version(self, value):
        """ Set gateway_config_version value.

            Notes:
                Interpreted version of NSG, which is used to determine the feature capabilities of NSG.

                
                This attribute is named `gatewayConfigVersion` in VSD API.
                
        """
        self._gateway_config_version = value

    
    @property
    def gateway_connected(self):
        """ Get gateway_connected value.

            Notes:
                Indicates status of this gateway

                
                This attribute is named `gatewayConnected` in VSD API.
                
        """
        return self._gateway_connected

    @gateway_connected.setter
    def gateway_connected(self, value):
        """ Set gateway_connected value.

            Notes:
                Indicates status of this gateway

                
                This attribute is named `gatewayConnected` in VSD API.
                
        """
        self._gateway_connected = value

    
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
    def serial_number(self):
        """ Get serial_number value.

            Notes:
                The NSG's serial number

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        """ Set serial_number value.

            Notes:
                The NSG's serial number

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        self._serial_number = value

    
    @property
    def derived_ssh_service_state(self):
        """ Get derived_ssh_service_state value.

            Notes:
                Indicates the SSH Service state on a NSG. This value is derived based on the SSHService configuration on the NSG and the associated Gateway Template.

                
                This attribute is named `derivedSSHServiceState` in VSD API.
                
        """
        return self._derived_ssh_service_state

    @derived_ssh_service_state.setter
    def derived_ssh_service_state(self, value):
        """ Set derived_ssh_service_state value.

            Notes:
                Indicates the SSH Service state on a NSG. This value is derived based on the SSHService configuration on the NSG and the associated Gateway Template.

                
                This attribute is named `derivedSSHServiceState` in VSD API.
                
        """
        self._derived_ssh_service_state = value

    
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
                Personality of the Gateway - NSG, cannot be changed after creation.

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                Personality of the Gateway - NSG, cannot be changed after creation.

                
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
    def network_acceleration(self):
        """ Get network_acceleration value.

            Notes:
                Attribute that enables or disables Network Acceleration (DPDK) on the NSGateway instance.  Changing the value of this field will cause the device to restart at the next configuration reload.

                
                This attribute is named `networkAcceleration` in VSD API.
                
        """
        return self._network_acceleration

    @network_acceleration.setter
    def network_acceleration(self, value):
        """ Set network_acceleration value.

            Notes:
                Attribute that enables or disables Network Acceleration (DPDK) on the NSGateway instance.  Changing the value of this field will cause the device to restart at the next configuration reload.

                
                This attribute is named `networkAcceleration` in VSD API.
                
        """
        self._network_acceleration = value

    
    @property
    def libraries(self):
        """ Get libraries value.

            Notes:
                Transient representation of the same property on NSGInfo.

                
        """
        return self._libraries

    @libraries.setter
    def libraries(self, value):
        """ Set libraries value.

            Notes:
                Transient representation of the same property on NSGInfo.

                
        """
        self._libraries = value

    
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
    def inherited_ssh_service_state(self):
        """ Get inherited_ssh_service_state value.

            Notes:
                Indicates the SSH Service state which is configured on the associated template instance.

                
                This attribute is named `inheritedSSHServiceState` in VSD API.
                
        """
        return self._inherited_ssh_service_state

    @inherited_ssh_service_state.setter
    def inherited_ssh_service_state(self, value):
        """ Set inherited_ssh_service_state value.

            Notes:
                Indicates the SSH Service state which is configured on the associated template instance.

                
                This attribute is named `inheritedSSHServiceState` in VSD API.
                
        """
        self._inherited_ssh_service_state = value

    
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
    def location_id(self):
        """ Get location_id value.

            Notes:
                The NSGateway's Location. NOTE: this is a read only property, it can only be set through the location object

                
                This attribute is named `locationID` in VSD API.
                
        """
        return self._location_id

    @location_id.setter
    def location_id(self, value):
        """ Set location_id value.

            Notes:
                The NSGateway's Location. NOTE: this is a read only property, it can only be set through the location object

                
                This attribute is named `locationID` in VSD API.
                
        """
        self._location_id = value

    
    @property
    def configuration_reload_state(self):
        """ Get configuration_reload_state value.

            Notes:
                Status resulting from a manually triggered configuration reload operation on an NSG.  This value only reflects the state for a manual action requested by the operator, not the automatic periodic configuration reload triggered by the NSG itself.

                
                This attribute is named `configurationReloadState` in VSD API.
                
        """
        return self._configuration_reload_state

    @configuration_reload_state.setter
    def configuration_reload_state(self, value):
        """ Set configuration_reload_state value.

            Notes:
                Status resulting from a manually triggered configuration reload operation on an NSG.  This value only reflects the state for a manual action requested by the operator, not the automatic periodic configuration reload triggered by the NSG itself.

                
                This attribute is named `configurationReloadState` in VSD API.
                
        """
        self._configuration_reload_state = value

    
    @property
    def configuration_status(self):
        """ Get configuration_status value.

            Notes:
                NSG Configuration status represents the NSG update state following a query by the NSG to get the latest version of the infraconfig.json file.  This status will be updated following a Bootstrap request or a Configuration Reload.  Success means that the NSG was able to apply the changes included in the latest infraconfig.json file.  A Failure response will be returned if the NSG was unable to apply the changes; this is normally accompanied with a rollback of the NSG to the previous configuration.

                
                This attribute is named `configurationStatus` in VSD API.
                
        """
        return self._configuration_status

    @configuration_status.setter
    def configuration_status(self, value):
        """ Set configuration_status value.

            Notes:
                NSG Configuration status represents the NSG update state following a query by the NSG to get the latest version of the infraconfig.json file.  This status will be updated following a Bootstrap request or a Configuration Reload.  Success means that the NSG was able to apply the changes included in the latest infraconfig.json file.  A Failure response will be returned if the NSG was unable to apply the changes; this is normally accompanied with a rollback of the NSG to the previous configuration.

                
                This attribute is named `configurationStatus` in VSD API.
                
        """
        self._configuration_status = value

    
    @property
    def configure_load_balancing(self):
        """ Get configure_load_balancing value.

            Notes:
                Describes whether the load balancing behavior used for Fc's in inherited from enterprise or disabled. 

                
                This attribute is named `configureLoadBalancing` in VSD API.
                
        """
        return self._configure_load_balancing

    @configure_load_balancing.setter
    def configure_load_balancing(self, value):
        """ Set configure_load_balancing value.

            Notes:
                Describes whether the load balancing behavior used for Fc's in inherited from enterprise or disabled. 

                
                This attribute is named `configureLoadBalancing` in VSD API.
                
        """
        self._configure_load_balancing = value

    
    @property
    def control_traffic_cos_value(self):
        """ Get control_traffic_cos_value value.

            Notes:
                CoS Value for Self Generated Traffic (Control Traffic). Min is 0 and Max is 7

                
                This attribute is named `controlTrafficCOSValue` in VSD API.
                
        """
        return self._control_traffic_cos_value

    @control_traffic_cos_value.setter
    def control_traffic_cos_value(self, value):
        """ Set control_traffic_cos_value value.

            Notes:
                CoS Value for Self Generated Traffic (Control Traffic). Min is 0 and Max is 7

                
                This attribute is named `controlTrafficCOSValue` in VSD API.
                
        """
        self._control_traffic_cos_value = value

    
    @property
    def control_traffic_dscp_value(self):
        """ Get control_traffic_dscp_value value.

            Notes:
                DSCP Value for Self Generated Traffic (Control Traffic). Min is 0 and Max is 63

                
                This attribute is named `controlTrafficDSCPValue` in VSD API.
                
        """
        return self._control_traffic_dscp_value

    @control_traffic_dscp_value.setter
    def control_traffic_dscp_value(self, value):
        """ Set control_traffic_dscp_value value.

            Notes:
                DSCP Value for Self Generated Traffic (Control Traffic). Min is 0 and Max is 63

                
                This attribute is named `controlTrafficDSCPValue` in VSD API.
                
        """
        self._control_traffic_dscp_value = value

    
    @property
    def bootstrap_id(self):
        """ Get bootstrap_id value.

            Notes:
                The bootstrap details associated with this NSGateway. NOTE: This is a read only property, it can only be set during creation of an NSG.

                
                This attribute is named `bootstrapID` in VSD API.
                
        """
        return self._bootstrap_id

    @bootstrap_id.setter
    def bootstrap_id(self, value):
        """ Set bootstrap_id value.

            Notes:
                The bootstrap details associated with this NSGateway. NOTE: This is a read only property, it can only be set during creation of an NSG.

                
                This attribute is named `bootstrapID` in VSD API.
                
        """
        self._bootstrap_id = value

    
    @property
    def bootstrap_status(self):
        """ Get bootstrap_status value.

            Notes:
                The bootstrap status of this NSGateway. NOTE: This is a read only property.

                
                This attribute is named `bootstrapStatus` in VSD API.
                
        """
        return self._bootstrap_status

    @bootstrap_status.setter
    def bootstrap_status(self, value):
        """ Set bootstrap_status value.

            Notes:
                The bootstrap status of this NSGateway. NOTE: This is a read only property.

                
                This attribute is named `bootstrapStatus` in VSD API.
                
        """
        self._bootstrap_status = value

    
    @property
    def operation_mode(self):
        """ Get operation_mode value.

            Notes:
                Operation mode of NSGateway

                
                This attribute is named `operationMode` in VSD API.
                
        """
        return self._operation_mode

    @operation_mode.setter
    def operation_mode(self, value):
        """ Set operation_mode value.

            Notes:
                Operation mode of NSGateway

                
                This attribute is named `operationMode` in VSD API.
                
        """
        self._operation_mode = value

    
    @property
    def operation_status(self):
        """ Get operation_status value.

            Notes:
                Operation Status of NSGateway

                
                This attribute is named `operationStatus` in VSD API.
                
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, value):
        """ Set operation_status value.

            Notes:
                Operation Status of NSGateway

                
                This attribute is named `operationStatus` in VSD API.
                
        """
        self._operation_status = value

    
    @property
    def product_name(self):
        """ Get product_name value.

            Notes:
                NSG Product Name as reported during bootstrapping.

                
                This attribute is named `productName` in VSD API.
                
        """
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        """ Set product_name value.

            Notes:
                NSG Product Name as reported during bootstrapping.

                
                This attribute is named `productName` in VSD API.
                
        """
        self._product_name = value

    
    @property
    def associated_gateway_security_id(self):
        """ Get associated_gateway_security_id value.

            Notes:
                Read only ID of the associated gateway security object.

                
                This attribute is named `associatedGatewaySecurityID` in VSD API.
                
        """
        return self._associated_gateway_security_id

    @associated_gateway_security_id.setter
    def associated_gateway_security_id(self, value):
        """ Set associated_gateway_security_id value.

            Notes:
                Read only ID of the associated gateway security object.

                
                This attribute is named `associatedGatewaySecurityID` in VSD API.
                
        """
        self._associated_gateway_security_id = value

    
    @property
    def associated_gateway_security_profile_id(self):
        """ Get associated_gateway_security_profile_id value.

            Notes:
                Read only ID of the associated gateway security profile object

                
                This attribute is named `associatedGatewaySecurityProfileID` in VSD API.
                
        """
        return self._associated_gateway_security_profile_id

    @associated_gateway_security_profile_id.setter
    def associated_gateway_security_profile_id(self, value):
        """ Set associated_gateway_security_profile_id value.

            Notes:
                Read only ID of the associated gateway security profile object

                
                This attribute is named `associatedGatewaySecurityProfileID` in VSD API.
                
        """
        self._associated_gateway_security_profile_id = value

    
    @property
    def associated_nsg_info_id(self):
        """ Get associated_nsg_info_id value.

            Notes:
                Read only ID of the associated NSG info object

                
                This attribute is named `associatedNSGInfoID` in VSD API.
                
        """
        return self._associated_nsg_info_id

    @associated_nsg_info_id.setter
    def associated_nsg_info_id(self, value):
        """ Set associated_nsg_info_id value.

            Notes:
                Read only ID of the associated NSG info object

                
                This attribute is named `associatedNSGInfoID` in VSD API.
                
        """
        self._associated_nsg_info_id = value

    
    @property
    def associated_nsg_upgrade_profile_id(self):
        """ Get associated_nsg_upgrade_profile_id value.

            Notes:
                The UUID of the NSG Upgrade Profile associated to this NSG instance.

                
                This attribute is named `associatedNSGUpgradeProfileID` in VSD API.
                
        """
        return self._associated_nsg_upgrade_profile_id

    @associated_nsg_upgrade_profile_id.setter
    def associated_nsg_upgrade_profile_id(self, value):
        """ Set associated_nsg_upgrade_profile_id value.

            Notes:
                The UUID of the NSG Upgrade Profile associated to this NSG instance.

                
                This attribute is named `associatedNSGUpgradeProfileID` in VSD API.
                
        """
        self._associated_nsg_upgrade_profile_id = value

    
    @property
    def associated_overlay_management_profile_id(self):
        """ Get associated_overlay_management_profile_id value.

            Notes:
                The ID of the associated Overlay Management Profile

                
                This attribute is named `associatedOverlayManagementProfileID` in VSD API.
                
        """
        return self._associated_overlay_management_profile_id

    @associated_overlay_management_profile_id.setter
    def associated_overlay_management_profile_id(self, value):
        """ Set associated_overlay_management_profile_id value.

            Notes:
                The ID of the associated Overlay Management Profile

                
                This attribute is named `associatedOverlayManagementProfileID` in VSD API.
                
        """
        self._associated_overlay_management_profile_id = value

    
    @property
    def functions(self):
        """ Get functions value.

            Notes:
                List of supported functions. This is only relevant for NSG-UBR and will be set to UBR by default in case an NSG-UBR is created. For a regular NSG, this will be set to null.

                
        """
        return self._functions

    @functions.setter
    def functions(self, value):
        """ Set functions value.

            Notes:
                List of supported functions. This is only relevant for NSG-UBR and will be set to UBR by default in case an NSG-UBR is created. For a regular NSG, this will be set to null.

                
        """
        self._functions = value

    
    @property
    def tunnel_shaping(self):
        """ Get tunnel_shaping value.

            Notes:
                Indicates if the UBR will perform tunnel shaping to the NSG when a tunnel shaper is associated to the NSG.

                
                This attribute is named `tunnelShaping` in VSD API.
                
        """
        return self._tunnel_shaping

    @tunnel_shaping.setter
    def tunnel_shaping(self, value):
        """ Set tunnel_shaping value.

            Notes:
                Indicates if the UBR will perform tunnel shaping to the NSG when a tunnel shaper is associated to the NSG.

                
                This attribute is named `tunnelShaping` in VSD API.
                
        """
        self._tunnel_shaping = value

    
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
    def syslog_level(self):
        """ Get syslog_level value.

            Notes:
                The minimal logging level of the messages the NSG will be reporting to the external syslog server that has been configured on the Infrastructure Gateway Profile.

                
                This attribute is named `syslogLevel` in VSD API.
                
        """
        return self._syslog_level

    @syslog_level.setter
    def syslog_level(self, value):
        """ Set syslog_level value.

            Notes:
                The minimal logging level of the messages the NSG will be reporting to the external syslog server that has been configured on the Infrastructure Gateway Profile.

                
                This attribute is named `syslogLevel` in VSD API.
                
        """
        self._syslog_level = value

    
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
    