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


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUSystemConfig(NURESTObject):
    """ Represents a SystemConfig in the VSD

        Notes:
            The system configuration which can be dynamically managed using rest api.
    """

    __rest_name__ = "systemconfig"
    __resource_name__ = "systemconfigs"

    
    ## Constants
    
    CONST_GROUP_KEY_DEFAULT_TRAFFIC_AUTHENTICATION_ALGORITHM_HMAC_SHA512 = "HMAC_SHA512"
    
    CONST_GROUP_KEY_DEFAULT_TRAFFIC_AUTHENTICATION_ALGORITHM_HMAC_MD5 = "HMAC_MD5"
    
    CONST_GROUP_KEY_DEFAULT_TRAFFIC_ENCRYPTION_ALGORITHM_AES_256_CBC = "AES_256_CBC"
    
    CONST_CSPROOT_AUTHENTICATION_METHOD_LDAP = "LDAP"
    
    CONST_SYSTEM_AVATAR_TYPE_URL = "URL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_GROUP_KEY_DEFAULT_SEK_PAYLOAD_SIGNING_ALGORITHM_SHA384WITHRSA = "SHA384withRSA"
    
    CONST_GROUP_KEY_DEFAULT_SEED_PAYLOAD_SIGNING_ALGORITHM_SHA512WITHRSA = "SHA512withRSA"
    
    CONST_GROUP_KEY_DEFAULT_SEK_PAYLOAD_ENCRYPTION_ALGORITHM_RSA_1024 = "RSA_1024"
    
    CONST_GROUP_KEY_DEFAULT_SEED_PAYLOAD_AUTHENTICATION_ALGORITHM_HMAC_SHA512 = "HMAC_SHA512"
    
    CONST_GROUP_KEY_DEFAULT_TRAFFIC_AUTHENTICATION_ALGORITHM_HMAC_SHA1 = "HMAC_SHA1"
    
    CONST_GROUP_KEY_DEFAULT_SEED_PAYLOAD_AUTHENTICATION_ALGORITHM_HMAC_SHA1 = "HMAC_SHA1"
    
    CONST_GROUP_KEY_DEFAULT_SEED_PAYLOAD_ENCRYPTION_ALGORITHM_AES_256_CBC = "AES_256_CBC"
    
    CONST_GROUP_KEY_DEFAULT_SEED_PAYLOAD_SIGNING_ALGORITHM_SHA384WITHRSA = "SHA384withRSA"
    
    CONST_GROUP_KEY_DEFAULT_TRAFFIC_ENCRYPTION_ALGORITHM_TRIPLE_DES_CBC = "TRIPLE_DES_CBC"
    
    CONST_GROUP_KEY_DEFAULT_TRAFFIC_AUTHENTICATION_ALGORITHM_HMAC_SHA256 = "HMAC_SHA256"
    
    CONST_CSPROOT_AUTHENTICATION_METHOD_LOCAL = "LOCAL"
    
    CONST_GROUP_KEY_DEFAULT_SEK_PAYLOAD_SIGNING_ALGORITHM_SHA224WITHRSA = "SHA224withRSA"
    
    CONST_GROUP_KEY_DEFAULT_TRAFFIC_ENCRYPTION_ALGORITHM_AES_128_CBC = "AES_128_CBC"
    
    CONST_GROUP_KEY_DEFAULT_SEED_PAYLOAD_AUTHENTICATION_ALGORITHM_HMAC_SHA256 = "HMAC_SHA256"
    
    CONST_DOMAIN_TUNNEL_TYPE_VXLAN = "VXLAN"
    
    CONST_GROUP_KEY_DEFAULT_SEK_PAYLOAD_SIGNING_ALGORITHM_SHA1WITHRSA = "SHA1withRSA"
    
    CONST_GROUP_KEY_DEFAULT_SEK_PAYLOAD_SIGNING_ALGORITHM_SHA256WITHRSA = "SHA256withRSA"
    
    CONST_DOMAIN_TUNNEL_TYPE_GRE = "GRE"
    
    CONST_GROUP_KEY_DEFAULT_SEED_PAYLOAD_SIGNING_ALGORITHM_SHA224WITHRSA = "SHA224withRSA"
    
    CONST_DOMAIN_TUNNEL_TYPE_DC_DEFAULT = "DC_DEFAULT"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_GROUP_KEY_DEFAULT_SEED_PAYLOAD_SIGNING_ALGORITHM_SHA1WITHRSA = "SHA1withRSA"
    
    CONST_SYSTEM_AVATAR_TYPE_COMPUTEDURL = "COMPUTEDURL"
    
    CONST_GROUP_KEY_DEFAULT_TRAFFIC_AUTHENTICATION_ALGORITHM_HMAC_SHA384 = "HMAC_SHA384"
    
    CONST_GROUP_KEY_DEFAULT_SEED_PAYLOAD_SIGNING_ALGORITHM_SHA256WITHRSA = "SHA256withRSA"
    
    CONST_GROUP_KEY_DEFAULT_SEED_PAYLOAD_ENCRYPTION_ALGORITHM_TRIPLE_DES_CBC = "TRIPLE_DES_CBC"
    
    CONST_GROUP_KEY_DEFAULT_TRAFFIC_ENCRYPTION_ALGORITHM_AES_192_CBC = "AES_192_CBC"
    
    CONST_GROUP_KEY_DEFAULT_SEED_PAYLOAD_ENCRYPTION_ALGORITHM_AES_128_CBC = "AES_128_CBC"
    
    CONST_SYSTEM_AVATAR_TYPE_BASE64 = "BASE64"
    
    CONST_GROUP_KEY_DEFAULT_SEK_PAYLOAD_SIGNING_ALGORITHM_SHA512WITHRSA = "SHA512withRSA"
    
    

    def __init__(self, **kwargs):
        """ Initializes a SystemConfig instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> systemconfig = NUSystemConfig(id=u'xxxx-xxx-xxx-xxx', name=u'SystemConfig')
                >>> systemconfig = NUSystemConfig(data=my_dict)
        """

        super(NUSystemConfig, self).__init__()

        # Read/Write Attributes
        
        self._acl_allow_origin = None
        self._ecmp_count = None
        self._ldap_sync_interval = None
        self._ldap_trust_store_certifcate = None
        self._ldap_trust_store_password = None
        self._ad_gateway_purge_time = None
        self._rd_lower_limit = None
        self._rd_public_network_lower_limit = None
        self._rd_public_network_upper_limit = None
        self._rd_upper_limit = None
        self._zfb_bootstrap_enabled = None
        self._zfb_request_retry_timer = None
        self._zfb_scheduler_stale_request_timeout = None
        self._dhcp_option_size = None
        self._vm_cache_size = None
        self._vm_purge_time = None
        self._vm_resync_deletion_wait_time = None
        self._vm_resync_outstanding_interval = None
        self._vm_unreachable_cleanup_time = None
        self._vm_unreachable_time = None
        self._vnid_lower_limit = None
        self._vnid_public_network_lower_limit = None
        self._vnid_public_network_upper_limit = None
        self._vnid_upper_limit = None
        self._api_key_renewal_interval = None
        self._api_key_validity = None
        self._vport_init_stateful_timer = None
        self._lru_cache_size_per_subnet = None
        self._vsc_on_same_version_as_vsd = None
        self._vsd_read_only_mode = None
        self._vsd_upgrade_is_complete = None
        self._as_number = None
        self._rt_lower_limit = None
        self._rt_public_network_lower_limit = None
        self._rt_public_network_upper_limit = None
        self._rt_upper_limit = None
        self._evpnbgp_community_tag_as_number = None
        self._evpnbgp_community_tag_lower_limit = None
        self._evpnbgp_community_tag_upper_limit = None
        self._page_max_size = None
        self._page_size = None
        self._last_updated_by = None
        self._max_failed_logins = None
        self._max_response = None
        self._performance_path_selection_vnid = None
        self._service_id_upper_limit = None
        self._key_server_monitor_enabled = None
        self._key_server_vsd_data_synchronization_interval = None
        self._offset_customer_id = None
        self._offset_service_id = None
        self._ejbca_nsg_certificate_profile = None
        self._ejbca_nsg_end_entity_profile = None
        self._ejbca_ocsp_responder_cn = None
        self._ejbca_ocsp_responder_uri = None
        self._ejbca_vsp_root_ca = None
        self._alarms_max_per_object = None
        self._elastic_cluster_name = None
        self._elastic_search_ui_address = None
        self._allow_enterprise_avatar_on_nsg = None
        self._global_mac_address = None
        self._inactive_timeout = None
        self._entity_scope = None
        self._domain_tunnel_type = None
        self._post_processor_threads_count = None
        self._group_key_default_sek_generation_interval = None
        self._group_key_default_sek_lifetime = None
        self._group_key_default_sek_payload_encryption_algorithm = None
        self._group_key_default_sek_payload_signing_algorithm = None
        self._group_key_default_seed_generation_interval = None
        self._group_key_default_seed_lifetime = None
        self._group_key_default_seed_payload_authentication_algorithm = None
        self._group_key_default_seed_payload_encryption_algorithm = None
        self._group_key_default_seed_payload_signing_algorithm = None
        self._group_key_default_traffic_authentication_algorithm = None
        self._group_key_default_traffic_encryption_algorithm = None
        self._group_key_default_traffic_encryption_key_lifetime = None
        self._group_key_generation_interval_on_forced_re_key = None
        self._group_key_generation_interval_on_revoke = None
        self._group_key_minimum_sek_generation_interval = None
        self._group_key_minimum_sek_lifetime = None
        self._group_key_minimum_seed_generation_interval = None
        self._group_key_minimum_seed_lifetime = None
        self._group_key_minimum_traffic_encryption_key_lifetime = None
        self._nsg_bootstrap_endpoint = None
        self._nsg_config_endpoint = None
        self._nsg_local_ui_url = None
        self._esi_id = None
        self._csproot_authentication_method = None
        self._stack_trace_enabled = None
        self._stateful_acl_non_tcp_timeout = None
        self._stateful_acltcp_timeout = None
        self._static_wan_service_purge_time = None
        self._statistics_enabled = None
        self._stats_collector_address = None
        self._stats_collector_port = None
        self._stats_collector_proto_buf_port = None
        self._stats_max_data_points = None
        self._stats_min_duration = None
        self._stats_number_of_data_points = None
        self._stats_tsdb_server_address = None
        self._sticky_ecmp_idle_timeout = None
        self._subnet_resync_interval = None
        self._subnet_resync_outstanding_interval = None
        self._customer_id_upper_limit = None
        self._customer_key = None
        self._avatar_base_path = None
        self._avatar_base_url = None
        self._event_log_cleanup_interval = None
        self._event_log_entry_max_age = None
        self._event_processor_interval = None
        self._event_processor_max_events_count = None
        self._event_processor_timeout = None
        self._two_factor_code_expiry = None
        self._two_factor_code_length = None
        self._two_factor_code_seed_length = None
        self._external_id = None
        self._dynamic_wan_service_diff_time = None
        self._syslog_destination_host = None
        self._syslog_destination_port = None
        self._sysmon_cleanup_task_interval = None
        self._sysmon_node_presence_timeout = None
        self._sysmon_probe_response_timeout = None
        self._system_avatar_data = None
        self._system_avatar_type = None
        
        self.expose_attribute(local_name="acl_allow_origin", remote_name="ACLAllowOrigin", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ecmp_count", remote_name="ECMPCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ldap_sync_interval", remote_name="LDAPSyncInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ldap_trust_store_certifcate", remote_name="LDAPTrustStoreCertifcate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ldap_trust_store_password", remote_name="LDAPTrustStorePassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ad_gateway_purge_time", remote_name="ADGatewayPurgeTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rd_lower_limit", remote_name="RDLowerLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rd_public_network_lower_limit", remote_name="RDPublicNetworkLowerLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rd_public_network_upper_limit", remote_name="RDPublicNetworkUpperLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rd_upper_limit", remote_name="RDUpperLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zfb_bootstrap_enabled", remote_name="ZFBBootstrapEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zfb_request_retry_timer", remote_name="ZFBRequestRetryTimer", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zfb_scheduler_stale_request_timeout", remote_name="ZFBSchedulerStaleRequestTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dhcp_option_size", remote_name="DHCPOptionSize", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vm_cache_size", remote_name="VMCacheSize", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vm_purge_time", remote_name="VMPurgeTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vm_resync_deletion_wait_time", remote_name="VMResyncDeletionWaitTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vm_resync_outstanding_interval", remote_name="VMResyncOutstandingInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vm_unreachable_cleanup_time", remote_name="VMUnreachableCleanupTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vm_unreachable_time", remote_name="VMUnreachableTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vnid_lower_limit", remote_name="VNIDLowerLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vnid_public_network_lower_limit", remote_name="VNIDPublicNetworkLowerLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vnid_public_network_upper_limit", remote_name="VNIDPublicNetworkUpperLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vnid_upper_limit", remote_name="VNIDUpperLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="api_key_renewal_interval", remote_name="APIKeyRenewalInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="api_key_validity", remote_name="APIKeyValidity", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vport_init_stateful_timer", remote_name="VPortInitStatefulTimer", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="lru_cache_size_per_subnet", remote_name="LRUCacheSizePerSubnet", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vsc_on_same_version_as_vsd", remote_name="VSCOnSameVersionAsVSD", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vsd_read_only_mode", remote_name="VSDReadOnlyMode", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vsd_upgrade_is_complete", remote_name="VSDUpgradeIsComplete", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="as_number", remote_name="ASNumber", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rt_lower_limit", remote_name="RTLowerLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rt_public_network_lower_limit", remote_name="RTPublicNetworkLowerLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rt_public_network_upper_limit", remote_name="RTPublicNetworkUpperLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rt_upper_limit", remote_name="RTUpperLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="evpnbgp_community_tag_as_number", remote_name="EVPNBGPCommunityTagASNumber", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="evpnbgp_community_tag_lower_limit", remote_name="EVPNBGPCommunityTagLowerLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="evpnbgp_community_tag_upper_limit", remote_name="EVPNBGPCommunityTagUpperLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="page_max_size", remote_name="pageMaxSize", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="page_size", remote_name="pageSize", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="max_failed_logins", remote_name="maxFailedLogins", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="max_response", remote_name="maxResponse", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="performance_path_selection_vnid", remote_name="performancePathSelectionVNID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="service_id_upper_limit", remote_name="serviceIDUpperLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="key_server_monitor_enabled", remote_name="keyServerMonitorEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="key_server_vsd_data_synchronization_interval", remote_name="keyServerVSDDataSynchronizationInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="offset_customer_id", remote_name="offsetCustomerID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="offset_service_id", remote_name="offsetServiceID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ejbca_nsg_certificate_profile", remote_name="ejbcaNSGCertificateProfile", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ejbca_nsg_end_entity_profile", remote_name="ejbcaNSGEndEntityProfile", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ejbca_ocsp_responder_cn", remote_name="ejbcaOCSPResponderCN", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ejbca_ocsp_responder_uri", remote_name="ejbcaOCSPResponderURI", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ejbca_vsp_root_ca", remote_name="ejbcaVspRootCa", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="alarms_max_per_object", remote_name="alarmsMaxPerObject", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="elastic_cluster_name", remote_name="elasticClusterName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="elastic_search_ui_address", remote_name="elasticSearchUIAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allow_enterprise_avatar_on_nsg", remote_name="allowEnterpriseAvatarOnNSG", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="global_mac_address", remote_name="globalMACAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="inactive_timeout", remote_name="inactiveTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="domain_tunnel_type", remote_name="domainTunnelType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DC_DEFAULT', u'GRE', u'VXLAN'])
        self.expose_attribute(local_name="post_processor_threads_count", remote_name="postProcessorThreadsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_default_sek_generation_interval", remote_name="groupKeyDefaultSEKGenerationInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_default_sek_lifetime", remote_name="groupKeyDefaultSEKLifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_default_sek_payload_encryption_algorithm", remote_name="groupKeyDefaultSEKPayloadEncryptionAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'RSA_1024'])
        self.expose_attribute(local_name="group_key_default_sek_payload_signing_algorithm", remote_name="groupKeyDefaultSEKPayloadSigningAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'SHA1withRSA', u'SHA224withRSA', u'SHA256withRSA', u'SHA384withRSA', u'SHA512withRSA'])
        self.expose_attribute(local_name="group_key_default_seed_generation_interval", remote_name="groupKeyDefaultSeedGenerationInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_default_seed_lifetime", remote_name="groupKeyDefaultSeedLifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_default_seed_payload_authentication_algorithm", remote_name="groupKeyDefaultSeedPayloadAuthenticationAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'HMAC_SHA1', u'HMAC_SHA256', u'HMAC_SHA512'])
        self.expose_attribute(local_name="group_key_default_seed_payload_encryption_algorithm", remote_name="groupKeyDefaultSeedPayloadEncryptionAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'AES_128_CBC', u'AES_256_CBC', u'TRIPLE_DES_CBC'])
        self.expose_attribute(local_name="group_key_default_seed_payload_signing_algorithm", remote_name="groupKeyDefaultSeedPayloadSigningAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'SHA1withRSA', u'SHA224withRSA', u'SHA256withRSA', u'SHA384withRSA', u'SHA512withRSA'])
        self.expose_attribute(local_name="group_key_default_traffic_authentication_algorithm", remote_name="groupKeyDefaultTrafficAuthenticationAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'HMAC_MD5', u'HMAC_SHA1', u'HMAC_SHA256', u'HMAC_SHA384', u'HMAC_SHA512'])
        self.expose_attribute(local_name="group_key_default_traffic_encryption_algorithm", remote_name="groupKeyDefaultTrafficEncryptionAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'AES_128_CBC', u'AES_192_CBC', u'AES_256_CBC', u'TRIPLE_DES_CBC'])
        self.expose_attribute(local_name="group_key_default_traffic_encryption_key_lifetime", remote_name="groupKeyDefaultTrafficEncryptionKeyLifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_generation_interval_on_forced_re_key", remote_name="groupKeyGenerationIntervalOnForcedReKey", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_generation_interval_on_revoke", remote_name="groupKeyGenerationIntervalOnRevoke", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_minimum_sek_generation_interval", remote_name="groupKeyMinimumSEKGenerationInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_minimum_sek_lifetime", remote_name="groupKeyMinimumSEKLifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_minimum_seed_generation_interval", remote_name="groupKeyMinimumSeedGenerationInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_minimum_seed_lifetime", remote_name="groupKeyMinimumSeedLifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="group_key_minimum_traffic_encryption_key_lifetime", remote_name="groupKeyMinimumTrafficEncryptionKeyLifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_bootstrap_endpoint", remote_name="nsgBootstrapEndpoint", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_config_endpoint", remote_name="nsgConfigEndpoint", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_local_ui_url", remote_name="nsgLocalUiUrl", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="esi_id", remote_name="esiID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="csproot_authentication_method", remote_name="csprootAuthenticationMethod", attribute_type=str, is_required=False, is_unique=False, choices=[u'LDAP', u'LOCAL'])
        self.expose_attribute(local_name="stack_trace_enabled", remote_name="stackTraceEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stateful_acl_non_tcp_timeout", remote_name="statefulACLNonTCPTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stateful_acltcp_timeout", remote_name="statefulACLTCPTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="static_wan_service_purge_time", remote_name="staticWANServicePurgeTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="statistics_enabled", remote_name="statisticsEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_collector_address", remote_name="statsCollectorAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_collector_port", remote_name="statsCollectorPort", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_collector_proto_buf_port", remote_name="statsCollectorProtoBufPort", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_max_data_points", remote_name="statsMaxDataPoints", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_min_duration", remote_name="statsMinDuration", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_number_of_data_points", remote_name="statsNumberOfDataPoints", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_tsdb_server_address", remote_name="statsTSDBServerAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sticky_ecmp_idle_timeout", remote_name="stickyECMPIdleTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="subnet_resync_interval", remote_name="subnetResyncInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="subnet_resync_outstanding_interval", remote_name="subnetResyncOutstandingInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="customer_id_upper_limit", remote_name="customerIDUpperLimit", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="customer_key", remote_name="customerKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="avatar_base_path", remote_name="avatarBasePath", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="avatar_base_url", remote_name="avatarBaseURL", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="event_log_cleanup_interval", remote_name="eventLogCleanupInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="event_log_entry_max_age", remote_name="eventLogEntryMaxAge", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="event_processor_interval", remote_name="eventProcessorInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="event_processor_max_events_count", remote_name="eventProcessorMaxEventsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="event_processor_timeout", remote_name="eventProcessorTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="two_factor_code_expiry", remote_name="twoFactorCodeExpiry", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="two_factor_code_length", remote_name="twoFactorCodeLength", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="two_factor_code_seed_length", remote_name="twoFactorCodeSeedLength", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="dynamic_wan_service_diff_time", remote_name="dynamicWANServiceDiffTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="syslog_destination_host", remote_name="syslogDestinationHost", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="syslog_destination_port", remote_name="syslogDestinationPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sysmon_cleanup_task_interval", remote_name="sysmonCleanupTaskInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sysmon_node_presence_timeout", remote_name="sysmonNodePresenceTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sysmon_probe_response_timeout", remote_name="sysmonProbeResponseTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="system_avatar_data", remote_name="systemAvatarData", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="system_avatar_type", remote_name="systemAvatarType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BASE64', u'COMPUTEDURL', u'URL'])
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def acl_allow_origin(self):
        """ Get acl_allow_origin value.

            Notes:
                Defines the domains allowed for access control list.

                
                This attribute is named `ACLAllowOrigin` in VSD API.
                
        """
        return self._acl_allow_origin

    @acl_allow_origin.setter
    def acl_allow_origin(self, value):
        """ Set acl_allow_origin value.

            Notes:
                Defines the domains allowed for access control list.

                
                This attribute is named `ACLAllowOrigin` in VSD API.
                
        """
        self._acl_allow_origin = value

    
    @property
    def ecmp_count(self):
        """ Get ecmp_count value.

            Notes:
                System Default Equal-cost multi-path routing count,Every Domain derives ECMP count from this value unless specifically set for the domain

                
                This attribute is named `ECMPCount` in VSD API.
                
        """
        return self._ecmp_count

    @ecmp_count.setter
    def ecmp_count(self, value):
        """ Set ecmp_count value.

            Notes:
                System Default Equal-cost multi-path routing count,Every Domain derives ECMP count from this value unless specifically set for the domain

                
                This attribute is named `ECMPCount` in VSD API.
                
        """
        self._ecmp_count = value

    
    @property
    def ldap_sync_interval(self):
        """ Get ldap_sync_interval value.

            Notes:
                LDAP Sync-Up task interval in seconds.

                
                This attribute is named `LDAPSyncInterval` in VSD API.
                
        """
        return self._ldap_sync_interval

    @ldap_sync_interval.setter
    def ldap_sync_interval(self, value):
        """ Set ldap_sync_interval value.

            Notes:
                LDAP Sync-Up task interval in seconds.

                
                This attribute is named `LDAPSyncInterval` in VSD API.
                
        """
        self._ldap_sync_interval = value

    
    @property
    def ldap_trust_store_certifcate(self):
        """ Get ldap_trust_store_certifcate value.

            Notes:
                Location of the truststore which is need to store LDAP server certificates. Default is cacerts located in java.home/lib/security/cacerts. Uncomment below setting if you need to use a different file

                
                This attribute is named `LDAPTrustStoreCertifcate` in VSD API.
                
        """
        return self._ldap_trust_store_certifcate

    @ldap_trust_store_certifcate.setter
    def ldap_trust_store_certifcate(self, value):
        """ Set ldap_trust_store_certifcate value.

            Notes:
                Location of the truststore which is need to store LDAP server certificates. Default is cacerts located in java.home/lib/security/cacerts. Uncomment below setting if you need to use a different file

                
                This attribute is named `LDAPTrustStoreCertifcate` in VSD API.
                
        """
        self._ldap_trust_store_certifcate = value

    
    @property
    def ldap_trust_store_password(self):
        """ Get ldap_trust_store_password value.

            Notes:
                Password to access the truststore. Uncomment below line to change its value.

                
                This attribute is named `LDAPTrustStorePassword` in VSD API.
                
        """
        return self._ldap_trust_store_password

    @ldap_trust_store_password.setter
    def ldap_trust_store_password(self, value):
        """ Set ldap_trust_store_password value.

            Notes:
                Password to access the truststore. Uncomment below line to change its value.

                
                This attribute is named `LDAPTrustStorePassword` in VSD API.
                
        """
        self._ldap_trust_store_password = value

    
    @property
    def ad_gateway_purge_time(self):
        """ Get ad_gateway_purge_time value.

            Notes:
                Timers in sec for undefined vms to be deleted(min =7200, max = 86400).

                
                This attribute is named `ADGatewayPurgeTime` in VSD API.
                
        """
        return self._ad_gateway_purge_time

    @ad_gateway_purge_time.setter
    def ad_gateway_purge_time(self, value):
        """ Set ad_gateway_purge_time value.

            Notes:
                Timers in sec for undefined vms to be deleted(min =7200, max = 86400).

                
                This attribute is named `ADGatewayPurgeTime` in VSD API.
                
        """
        self._ad_gateway_purge_time = value

    
    @property
    def rd_lower_limit(self):
        """ Get rd_lower_limit value.

            Notes:
                route distinguisher lower limit

                
                This attribute is named `RDLowerLimit` in VSD API.
                
        """
        return self._rd_lower_limit

    @rd_lower_limit.setter
    def rd_lower_limit(self, value):
        """ Set rd_lower_limit value.

            Notes:
                route distinguisher lower limit

                
                This attribute is named `RDLowerLimit` in VSD API.
                
        """
        self._rd_lower_limit = value

    
    @property
    def rd_public_network_lower_limit(self):
        """ Get rd_public_network_lower_limit value.

            Notes:
                route distinguisher public network lower limit

                
                This attribute is named `RDPublicNetworkLowerLimit` in VSD API.
                
        """
        return self._rd_public_network_lower_limit

    @rd_public_network_lower_limit.setter
    def rd_public_network_lower_limit(self, value):
        """ Set rd_public_network_lower_limit value.

            Notes:
                route distinguisher public network lower limit

                
                This attribute is named `RDPublicNetworkLowerLimit` in VSD API.
                
        """
        self._rd_public_network_lower_limit = value

    
    @property
    def rd_public_network_upper_limit(self):
        """ Get rd_public_network_upper_limit value.

            Notes:
                route distinguisher public network upper limit

                
                This attribute is named `RDPublicNetworkUpperLimit` in VSD API.
                
        """
        return self._rd_public_network_upper_limit

    @rd_public_network_upper_limit.setter
    def rd_public_network_upper_limit(self, value):
        """ Set rd_public_network_upper_limit value.

            Notes:
                route distinguisher public network upper limit

                
                This attribute is named `RDPublicNetworkUpperLimit` in VSD API.
                
        """
        self._rd_public_network_upper_limit = value

    
    @property
    def rd_upper_limit(self):
        """ Get rd_upper_limit value.

            Notes:
                route distinguisher upper limit

                
                This attribute is named `RDUpperLimit` in VSD API.
                
        """
        return self._rd_upper_limit

    @rd_upper_limit.setter
    def rd_upper_limit(self, value):
        """ Set rd_upper_limit value.

            Notes:
                route distinguisher upper limit

                
                This attribute is named `RDUpperLimit` in VSD API.
                
        """
        self._rd_upper_limit = value

    
    @property
    def zfb_bootstrap_enabled(self):
        """ Get zfb_bootstrap_enabled value.

            Notes:
                Whether the NSG should auto bootstrap using ZFB

                
                This attribute is named `ZFBBootstrapEnabled` in VSD API.
                
        """
        return self._zfb_bootstrap_enabled

    @zfb_bootstrap_enabled.setter
    def zfb_bootstrap_enabled(self, value):
        """ Set zfb_bootstrap_enabled value.

            Notes:
                Whether the NSG should auto bootstrap using ZFB

                
                This attribute is named `ZFBBootstrapEnabled` in VSD API.
                
        """
        self._zfb_bootstrap_enabled = value

    
    @property
    def zfb_request_retry_timer(self):
        """ Get zfb_request_retry_timer value.

            Notes:
                Retry time for the ZFB daemon to recheck ZFBRequest Status in seconds

                
                This attribute is named `ZFBRequestRetryTimer` in VSD API.
                
        """
        return self._zfb_request_retry_timer

    @zfb_request_retry_timer.setter
    def zfb_request_retry_timer(self, value):
        """ Set zfb_request_retry_timer value.

            Notes:
                Retry time for the ZFB daemon to recheck ZFBRequest Status in seconds

                
                This attribute is named `ZFBRequestRetryTimer` in VSD API.
                
        """
        self._zfb_request_retry_timer = value

    
    @property
    def zfb_scheduler_stale_request_timeout(self):
        """ Get zfb_scheduler_stale_request_timeout value.

            Notes:
                Time for the ZFB scheduler to wait in seconds before deleting a stale request

                
                This attribute is named `ZFBSchedulerStaleRequestTimeout` in VSD API.
                
        """
        return self._zfb_scheduler_stale_request_timeout

    @zfb_scheduler_stale_request_timeout.setter
    def zfb_scheduler_stale_request_timeout(self, value):
        """ Set zfb_scheduler_stale_request_timeout value.

            Notes:
                Time for the ZFB scheduler to wait in seconds before deleting a stale request

                
                This attribute is named `ZFBSchedulerStaleRequestTimeout` in VSD API.
                
        """
        self._zfb_scheduler_stale_request_timeout = value

    
    @property
    def dhcp_option_size(self):
        """ Get dhcp_option_size value.

            Notes:
                Defines total DHCP options that can be set on a domain.

                
                This attribute is named `DHCPOptionSize` in VSD API.
                
        """
        return self._dhcp_option_size

    @dhcp_option_size.setter
    def dhcp_option_size(self, value):
        """ Set dhcp_option_size value.

            Notes:
                Defines total DHCP options that can be set on a domain.

                
                This attribute is named `DHCPOptionSize` in VSD API.
                
        """
        self._dhcp_option_size = value

    
    @property
    def vm_cache_size(self):
        """ Get vm_cache_size value.

            Notes:
                LRU Map size for vm, this value has to set based on memory given to VSD jvm not finalized.

                
                This attribute is named `VMCacheSize` in VSD API.
                
        """
        return self._vm_cache_size

    @vm_cache_size.setter
    def vm_cache_size(self, value):
        """ Set vm_cache_size value.

            Notes:
                LRU Map size for vm, this value has to set based on memory given to VSD jvm not finalized.

                
                This attribute is named `VMCacheSize` in VSD API.
                
        """
        self._vm_cache_size = value

    
    @property
    def vm_purge_time(self):
        """ Get vm_purge_time value.

            Notes:
                Timers in sec for undefined vms to be deleted.

                
                This attribute is named `VMPurgeTime` in VSD API.
                
        """
        return self._vm_purge_time

    @vm_purge_time.setter
    def vm_purge_time(self, value):
        """ Set vm_purge_time value.

            Notes:
                Timers in sec for undefined vms to be deleted.

                
                This attribute is named `VMPurgeTime` in VSD API.
                
        """
        self._vm_purge_time = value

    
    @property
    def vm_resync_deletion_wait_time(self):
        """ Get vm_resync_deletion_wait_time value.

            Notes:
                After resync on vm , if no controller returns with a VM request with in the below timeframe then it will get deleted deletion wait time in minutes.

                
                This attribute is named `VMResyncDeletionWaitTime` in VSD API.
                
        """
        return self._vm_resync_deletion_wait_time

    @vm_resync_deletion_wait_time.setter
    def vm_resync_deletion_wait_time(self, value):
        """ Set vm_resync_deletion_wait_time value.

            Notes:
                After resync on vm , if no controller returns with a VM request with in the below timeframe then it will get deleted deletion wait time in minutes.

                
                This attribute is named `VMResyncDeletionWaitTime` in VSD API.
                
        """
        self._vm_resync_deletion_wait_time = value

    
    @property
    def vm_resync_outstanding_interval(self):
        """ Get vm_resync_outstanding_interval value.

            Notes:
                Outstanding VM resync interval (in secs). System wide value.

                
                This attribute is named `VMResyncOutstandingInterval` in VSD API.
                
        """
        return self._vm_resync_outstanding_interval

    @vm_resync_outstanding_interval.setter
    def vm_resync_outstanding_interval(self, value):
        """ Set vm_resync_outstanding_interval value.

            Notes:
                Outstanding VM resync interval (in secs). System wide value.

                
                This attribute is named `VMResyncOutstandingInterval` in VSD API.
                
        """
        self._vm_resync_outstanding_interval = value

    
    @property
    def vm_unreachable_cleanup_time(self):
        """ Get vm_unreachable_cleanup_time value.

            Notes:
                Timers in sec for unreachable VMs for cleanup.

                
                This attribute is named `VMUnreachableCleanupTime` in VSD API.
                
        """
        return self._vm_unreachable_cleanup_time

    @vm_unreachable_cleanup_time.setter
    def vm_unreachable_cleanup_time(self, value):
        """ Set vm_unreachable_cleanup_time value.

            Notes:
                Timers in sec for unreachable VMs for cleanup.

                
                This attribute is named `VMUnreachableCleanupTime` in VSD API.
                
        """
        self._vm_unreachable_cleanup_time = value

    
    @property
    def vm_unreachable_time(self):
        """ Get vm_unreachable_time value.

            Notes:
                Timers in sec for unreachable VMs.

                
                This attribute is named `VMUnreachableTime` in VSD API.
                
        """
        return self._vm_unreachable_time

    @vm_unreachable_time.setter
    def vm_unreachable_time(self, value):
        """ Set vm_unreachable_time value.

            Notes:
                Timers in sec for unreachable VMs.

                
                This attribute is named `VMUnreachableTime` in VSD API.
                
        """
        self._vm_unreachable_time = value

    
    @property
    def vnid_lower_limit(self):
        """ Get vnid_lower_limit value.

            Notes:
                Virtual network ID offset

                
                This attribute is named `VNIDLowerLimit` in VSD API.
                
        """
        return self._vnid_lower_limit

    @vnid_lower_limit.setter
    def vnid_lower_limit(self, value):
        """ Set vnid_lower_limit value.

            Notes:
                Virtual network ID offset

                
                This attribute is named `VNIDLowerLimit` in VSD API.
                
        """
        self._vnid_lower_limit = value

    
    @property
    def vnid_public_network_lower_limit(self):
        """ Get vnid_public_network_lower_limit value.

            Notes:
                Virtual network ID public network lower limit

                
                This attribute is named `VNIDPublicNetworkLowerLimit` in VSD API.
                
        """
        return self._vnid_public_network_lower_limit

    @vnid_public_network_lower_limit.setter
    def vnid_public_network_lower_limit(self, value):
        """ Set vnid_public_network_lower_limit value.

            Notes:
                Virtual network ID public network lower limit

                
                This attribute is named `VNIDPublicNetworkLowerLimit` in VSD API.
                
        """
        self._vnid_public_network_lower_limit = value

    
    @property
    def vnid_public_network_upper_limit(self):
        """ Get vnid_public_network_upper_limit value.

            Notes:
                Virtual network ID public network upper limit

                
                This attribute is named `VNIDPublicNetworkUpperLimit` in VSD API.
                
        """
        return self._vnid_public_network_upper_limit

    @vnid_public_network_upper_limit.setter
    def vnid_public_network_upper_limit(self, value):
        """ Set vnid_public_network_upper_limit value.

            Notes:
                Virtual network ID public network upper limit

                
                This attribute is named `VNIDPublicNetworkUpperLimit` in VSD API.
                
        """
        self._vnid_public_network_upper_limit = value

    
    @property
    def vnid_upper_limit(self):
        """ Get vnid_upper_limit value.

            Notes:
                Virtual network ID upper limit

                
                This attribute is named `VNIDUpperLimit` in VSD API.
                
        """
        return self._vnid_upper_limit

    @vnid_upper_limit.setter
    def vnid_upper_limit(self, value):
        """ Set vnid_upper_limit value.

            Notes:
                Virtual network ID upper limit

                
                This attribute is named `VNIDUpperLimit` in VSD API.
                
        """
        self._vnid_upper_limit = value

    
    @property
    def api_key_renewal_interval(self):
        """ Get api_key_renewal_interval value.

            Notes:
                Defines the interval in seconds, before the expiry time, that can used to renew the apiKey by making me API call. Minimum value is 1 min and maximum is 5 min.

                
                This attribute is named `APIKeyRenewalInterval` in VSD API.
                
        """
        return self._api_key_renewal_interval

    @api_key_renewal_interval.setter
    def api_key_renewal_interval(self, value):
        """ Set api_key_renewal_interval value.

            Notes:
                Defines the interval in seconds, before the expiry time, that can used to renew the apiKey by making me API call. Minimum value is 1 min and maximum is 5 min.

                
                This attribute is named `APIKeyRenewalInterval` in VSD API.
                
        """
        self._api_key_renewal_interval = value

    
    @property
    def api_key_validity(self):
        """ Get api_key_validity value.

            Notes:
                Defines the apiKey validity duration in seconds. Default is 24 hours and minimum value is 10 min.

                
                This attribute is named `APIKeyValidity` in VSD API.
                
        """
        return self._api_key_validity

    @api_key_validity.setter
    def api_key_validity(self, value):
        """ Set api_key_validity value.

            Notes:
                Defines the apiKey validity duration in seconds. Default is 24 hours and minimum value is 10 min.

                
                This attribute is named `APIKeyValidity` in VSD API.
                
        """
        self._api_key_validity = value

    
    @property
    def vport_init_stateful_timer(self):
        """ Get vport_init_stateful_timer value.

            Notes:
                Defines the timeout in seconds for vport initialization to stateful. Default value is 300 secs and the timeout should be between 0 to 86400 seconds.

                
                This attribute is named `VPortInitStatefulTimer` in VSD API.
                
        """
        return self._vport_init_stateful_timer

    @vport_init_stateful_timer.setter
    def vport_init_stateful_timer(self, value):
        """ Set vport_init_stateful_timer value.

            Notes:
                Defines the timeout in seconds for vport initialization to stateful. Default value is 300 secs and the timeout should be between 0 to 86400 seconds.

                
                This attribute is named `VPortInitStatefulTimer` in VSD API.
                
        """
        self._vport_init_stateful_timer = value

    
    @property
    def lru_cache_size_per_subnet(self):
        """ Get lru_cache_size_per_subnet value.

            Notes:
                LRU Map size per subnet (to hold the deleted vm's ip addresses).

                
                This attribute is named `LRUCacheSizePerSubnet` in VSD API.
                
        """
        return self._lru_cache_size_per_subnet

    @lru_cache_size_per_subnet.setter
    def lru_cache_size_per_subnet(self, value):
        """ Set lru_cache_size_per_subnet value.

            Notes:
                LRU Map size per subnet (to hold the deleted vm's ip addresses).

                
                This attribute is named `LRUCacheSizePerSubnet` in VSD API.
                
        """
        self._lru_cache_size_per_subnet = value

    
    @property
    def vsc_on_same_version_as_vsd(self):
        """ Get vsc_on_same_version_as_vsd value.

            Notes:
                This flag is used to indicate that whether VSC is on the same version as VSD or not.

                
                This attribute is named `VSCOnSameVersionAsVSD` in VSD API.
                
        """
        return self._vsc_on_same_version_as_vsd

    @vsc_on_same_version_as_vsd.setter
    def vsc_on_same_version_as_vsd(self, value):
        """ Set vsc_on_same_version_as_vsd value.

            Notes:
                This flag is used to indicate that whether VSC is on the same version as VSD or not.

                
                This attribute is named `VSCOnSameVersionAsVSD` in VSD API.
                
        """
        self._vsc_on_same_version_as_vsd = value

    
    @property
    def vsd_read_only_mode(self):
        """ Get vsd_read_only_mode value.

            Notes:
                True means VSD readonly mode enabled. False means VSD readonly mode disabled

                
                This attribute is named `VSDReadOnlyMode` in VSD API.
                
        """
        return self._vsd_read_only_mode

    @vsd_read_only_mode.setter
    def vsd_read_only_mode(self, value):
        """ Set vsd_read_only_mode value.

            Notes:
                True means VSD readonly mode enabled. False means VSD readonly mode disabled

                
                This attribute is named `VSDReadOnlyMode` in VSD API.
                
        """
        self._vsd_read_only_mode = value

    
    @property
    def vsd_upgrade_is_complete(self):
        """ Get vsd_upgrade_is_complete value.

            Notes:
                This flag is used to indicate that whether VSD upgrade is complete,it is expected that csproot will set to true,after VSD upgrade is complete and also making sure that all VSC's audits and Gateway audits with VSD are done

                
                This attribute is named `VSDUpgradeIsComplete` in VSD API.
                
        """
        return self._vsd_upgrade_is_complete

    @vsd_upgrade_is_complete.setter
    def vsd_upgrade_is_complete(self, value):
        """ Set vsd_upgrade_is_complete value.

            Notes:
                This flag is used to indicate that whether VSD upgrade is complete,it is expected that csproot will set to true,after VSD upgrade is complete and also making sure that all VSC's audits and Gateway audits with VSD are done

                
                This attribute is named `VSDUpgradeIsComplete` in VSD API.
                
        """
        self._vsd_upgrade_is_complete = value

    
    @property
    def as_number(self):
        """ Get as_number value.

            Notes:
                 Autonomous System Number,Used for RT/RD auto-generation

                
                This attribute is named `ASNumber` in VSD API.
                
        """
        return self._as_number

    @as_number.setter
    def as_number(self, value):
        """ Set as_number value.

            Notes:
                 Autonomous System Number,Used for RT/RD auto-generation

                
                This attribute is named `ASNumber` in VSD API.
                
        """
        self._as_number = value

    
    @property
    def rt_lower_limit(self):
        """ Get rt_lower_limit value.

            Notes:
                route target lower limit

                
                This attribute is named `RTLowerLimit` in VSD API.
                
        """
        return self._rt_lower_limit

    @rt_lower_limit.setter
    def rt_lower_limit(self, value):
        """ Set rt_lower_limit value.

            Notes:
                route target lower limit

                
                This attribute is named `RTLowerLimit` in VSD API.
                
        """
        self._rt_lower_limit = value

    
    @property
    def rt_public_network_lower_limit(self):
        """ Get rt_public_network_lower_limit value.

            Notes:
                route target public network lower limit

                
                This attribute is named `RTPublicNetworkLowerLimit` in VSD API.
                
        """
        return self._rt_public_network_lower_limit

    @rt_public_network_lower_limit.setter
    def rt_public_network_lower_limit(self, value):
        """ Set rt_public_network_lower_limit value.

            Notes:
                route target public network lower limit

                
                This attribute is named `RTPublicNetworkLowerLimit` in VSD API.
                
        """
        self._rt_public_network_lower_limit = value

    
    @property
    def rt_public_network_upper_limit(self):
        """ Get rt_public_network_upper_limit value.

            Notes:
                route target public network upper limit

                
                This attribute is named `RTPublicNetworkUpperLimit` in VSD API.
                
        """
        return self._rt_public_network_upper_limit

    @rt_public_network_upper_limit.setter
    def rt_public_network_upper_limit(self, value):
        """ Set rt_public_network_upper_limit value.

            Notes:
                route target public network upper limit

                
                This attribute is named `RTPublicNetworkUpperLimit` in VSD API.
                
        """
        self._rt_public_network_upper_limit = value

    
    @property
    def rt_upper_limit(self):
        """ Get rt_upper_limit value.

            Notes:
                route target upper limit

                
                This attribute is named `RTUpperLimit` in VSD API.
                
        """
        return self._rt_upper_limit

    @rt_upper_limit.setter
    def rt_upper_limit(self, value):
        """ Set rt_upper_limit value.

            Notes:
                route target upper limit

                
                This attribute is named `RTUpperLimit` in VSD API.
                
        """
        self._rt_upper_limit = value

    
    @property
    def evpnbgp_community_tag_as_number(self):
        """ Get evpnbgp_community_tag_as_number value.

            Notes:
                Autonomous System Number,Used for EVPNBGPCommunityTag auto-generation

                
                This attribute is named `EVPNBGPCommunityTagASNumber` in VSD API.
                
        """
        return self._evpnbgp_community_tag_as_number

    @evpnbgp_community_tag_as_number.setter
    def evpnbgp_community_tag_as_number(self, value):
        """ Set evpnbgp_community_tag_as_number value.

            Notes:
                Autonomous System Number,Used for EVPNBGPCommunityTag auto-generation

                
                This attribute is named `EVPNBGPCommunityTagASNumber` in VSD API.
                
        """
        self._evpnbgp_community_tag_as_number = value

    
    @property
    def evpnbgp_community_tag_lower_limit(self):
        """ Get evpnbgp_community_tag_lower_limit value.

            Notes:
                EVPNBGPCommunityTag lower limit

                
                This attribute is named `EVPNBGPCommunityTagLowerLimit` in VSD API.
                
        """
        return self._evpnbgp_community_tag_lower_limit

    @evpnbgp_community_tag_lower_limit.setter
    def evpnbgp_community_tag_lower_limit(self, value):
        """ Set evpnbgp_community_tag_lower_limit value.

            Notes:
                EVPNBGPCommunityTag lower limit

                
                This attribute is named `EVPNBGPCommunityTagLowerLimit` in VSD API.
                
        """
        self._evpnbgp_community_tag_lower_limit = value

    
    @property
    def evpnbgp_community_tag_upper_limit(self):
        """ Get evpnbgp_community_tag_upper_limit value.

            Notes:
                EVPNBGPCommunityTag upper limit

                
                This attribute is named `EVPNBGPCommunityTagUpperLimit` in VSD API.
                
        """
        return self._evpnbgp_community_tag_upper_limit

    @evpnbgp_community_tag_upper_limit.setter
    def evpnbgp_community_tag_upper_limit(self, value):
        """ Set evpnbgp_community_tag_upper_limit value.

            Notes:
                EVPNBGPCommunityTag upper limit

                
                This attribute is named `EVPNBGPCommunityTagUpperLimit` in VSD API.
                
        """
        self._evpnbgp_community_tag_upper_limit = value

    
    @property
    def page_max_size(self):
        """ Get page_max_size value.

            Notes:
                Defines upper bound for the page size. Configured or input page size should be less than this max page size.

                
                This attribute is named `pageMaxSize` in VSD API.
                
        """
        return self._page_max_size

    @page_max_size.setter
    def page_max_size(self, value):
        """ Set page_max_size value.

            Notes:
                Defines upper bound for the page size. Configured or input page size should be less than this max page size.

                
                This attribute is named `pageMaxSize` in VSD API.
                
        """
        self._page_max_size = value

    
    @property
    def page_size(self):
        """ Get page_size value.

            Notes:
                Defines the page size for the results returned by the REST call.

                
                This attribute is named `pageSize` in VSD API.
                
        """
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        """ Set page_size value.

            Notes:
                Defines the page size for the results returned by the REST call.

                
                This attribute is named `pageSize` in VSD API.
                
        """
        self._page_size = value

    
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
    def max_failed_logins(self):
        """ Get max_failed_logins value.

            Notes:
                Maximum failed login attempts before the account is locked (min = 5, max = 10). 0 = not enforced (unlimited attempts). This is not enforced if LDAP is used for authorization

                
                This attribute is named `maxFailedLogins` in VSD API.
                
        """
        return self._max_failed_logins

    @max_failed_logins.setter
    def max_failed_logins(self, value):
        """ Set max_failed_logins value.

            Notes:
                Maximum failed login attempts before the account is locked (min = 5, max = 10). 0 = not enforced (unlimited attempts). This is not enforced if LDAP is used for authorization

                
                This attribute is named `maxFailedLogins` in VSD API.
                
        """
        self._max_failed_logins = value

    
    @property
    def max_response(self):
        """ Get max_response value.

            Notes:
                Defines maximum results returned by the REST call (allowed max=5000).

                
                This attribute is named `maxResponse` in VSD API.
                
        """
        return self._max_response

    @max_response.setter
    def max_response(self, value):
        """ Set max_response value.

            Notes:
                Defines maximum results returned by the REST call (allowed max=5000).

                
                This attribute is named `maxResponse` in VSD API.
                
        """
        self._max_response = value

    
    @property
    def performance_path_selection_vnid(self):
        """ Get performance_path_selection_vnid value.

            Notes:
                performance Path Selection Virtual Network ID

                
                This attribute is named `performancePathSelectionVNID` in VSD API.
                
        """
        return self._performance_path_selection_vnid

    @performance_path_selection_vnid.setter
    def performance_path_selection_vnid(self, value):
        """ Set performance_path_selection_vnid value.

            Notes:
                performance Path Selection Virtual Network ID

                
                This attribute is named `performancePathSelectionVNID` in VSD API.
                
        """
        self._performance_path_selection_vnid = value

    
    @property
    def service_id_upper_limit(self):
        """ Get service_id_upper_limit value.

            Notes:
                Service id upper limit system wide value

                
                This attribute is named `serviceIDUpperLimit` in VSD API.
                
        """
        return self._service_id_upper_limit

    @service_id_upper_limit.setter
    def service_id_upper_limit(self, value):
        """ Set service_id_upper_limit value.

            Notes:
                Service id upper limit system wide value

                
                This attribute is named `serviceIDUpperLimit` in VSD API.
                
        """
        self._service_id_upper_limit = value

    
    @property
    def key_server_monitor_enabled(self):
        """ Get key_server_monitor_enabled value.

            Notes:
                Enable the keyserver debug monitor (ie. ksmon command)

                
                This attribute is named `keyServerMonitorEnabled` in VSD API.
                
        """
        return self._key_server_monitor_enabled

    @key_server_monitor_enabled.setter
    def key_server_monitor_enabled(self, value):
        """ Set key_server_monitor_enabled value.

            Notes:
                Enable the keyserver debug monitor (ie. ksmon command)

                
                This attribute is named `keyServerMonitorEnabled` in VSD API.
                
        """
        self._key_server_monitor_enabled = value

    
    @property
    def key_server_vsd_data_synchronization_interval(self):
        """ Get key_server_vsd_data_synchronization_interval value.

            Notes:
                KeyServer time in seconds between full resyncs of VSD data (just in case of missed events)

                
                This attribute is named `keyServerVSDDataSynchronizationInterval` in VSD API.
                
        """
        return self._key_server_vsd_data_synchronization_interval

    @key_server_vsd_data_synchronization_interval.setter
    def key_server_vsd_data_synchronization_interval(self, value):
        """ Set key_server_vsd_data_synchronization_interval value.

            Notes:
                KeyServer time in seconds between full resyncs of VSD data (just in case of missed events)

                
                This attribute is named `keyServerVSDDataSynchronizationInterval` in VSD API.
                
        """
        self._key_server_vsd_data_synchronization_interval = value

    
    @property
    def offset_customer_id(self):
        """ Get offset_customer_id value.

            Notes:
                Customer id offset, this value has to be set before jboss starts , after that any change of value is ignored (minexclusive = 0, max = 20000) system wide value

                
                This attribute is named `offsetCustomerID` in VSD API.
                
        """
        return self._offset_customer_id

    @offset_customer_id.setter
    def offset_customer_id(self, value):
        """ Set offset_customer_id value.

            Notes:
                Customer id offset, this value has to be set before jboss starts , after that any change of value is ignored (minexclusive = 0, max = 20000) system wide value

                
                This attribute is named `offsetCustomerID` in VSD API.
                
        """
        self._offset_customer_id = value

    
    @property
    def offset_service_id(self):
        """ Get offset_service_id value.

            Notes:
                Service id offset, this value has to be set before jboss starts during install time, after that any change of value is ignored (minexclusive = 0, max = 40000) system wide value

                
                This attribute is named `offsetServiceID` in VSD API.
                
        """
        return self._offset_service_id

    @offset_service_id.setter
    def offset_service_id(self, value):
        """ Set offset_service_id value.

            Notes:
                Service id offset, this value has to be set before jboss starts during install time, after that any change of value is ignored (minexclusive = 0, max = 40000) system wide value

                
                This attribute is named `offsetServiceID` in VSD API.
                
        """
        self._offset_service_id = value

    
    @property
    def ejbca_nsg_certificate_profile(self):
        """ Get ejbca_nsg_certificate_profile value.

            Notes:
                EJBCA NSG Certificate Profile

                
                This attribute is named `ejbcaNSGCertificateProfile` in VSD API.
                
        """
        return self._ejbca_nsg_certificate_profile

    @ejbca_nsg_certificate_profile.setter
    def ejbca_nsg_certificate_profile(self, value):
        """ Set ejbca_nsg_certificate_profile value.

            Notes:
                EJBCA NSG Certificate Profile

                
                This attribute is named `ejbcaNSGCertificateProfile` in VSD API.
                
        """
        self._ejbca_nsg_certificate_profile = value

    
    @property
    def ejbca_nsg_end_entity_profile(self):
        """ Get ejbca_nsg_end_entity_profile value.

            Notes:
                EJBCA NSG End Entity Profile

                
                This attribute is named `ejbcaNSGEndEntityProfile` in VSD API.
                
        """
        return self._ejbca_nsg_end_entity_profile

    @ejbca_nsg_end_entity_profile.setter
    def ejbca_nsg_end_entity_profile(self, value):
        """ Set ejbca_nsg_end_entity_profile value.

            Notes:
                EJBCA NSG End Entity Profile

                
                This attribute is named `ejbcaNSGEndEntityProfile` in VSD API.
                
        """
        self._ejbca_nsg_end_entity_profile = value

    
    @property
    def ejbca_ocsp_responder_cn(self):
        """ Get ejbca_ocsp_responder_cn value.

            Notes:
                EJBCA OCSP Responder CommonName

                
                This attribute is named `ejbcaOCSPResponderCN` in VSD API.
                
        """
        return self._ejbca_ocsp_responder_cn

    @ejbca_ocsp_responder_cn.setter
    def ejbca_ocsp_responder_cn(self, value):
        """ Set ejbca_ocsp_responder_cn value.

            Notes:
                EJBCA OCSP Responder CommonName

                
                This attribute is named `ejbcaOCSPResponderCN` in VSD API.
                
        """
        self._ejbca_ocsp_responder_cn = value

    
    @property
    def ejbca_ocsp_responder_uri(self):
        """ Get ejbca_ocsp_responder_uri value.

            Notes:
                EJBCA OCSP Responder URI

                
                This attribute is named `ejbcaOCSPResponderURI` in VSD API.
                
        """
        return self._ejbca_ocsp_responder_uri

    @ejbca_ocsp_responder_uri.setter
    def ejbca_ocsp_responder_uri(self, value):
        """ Set ejbca_ocsp_responder_uri value.

            Notes:
                EJBCA OCSP Responder URI

                
                This attribute is named `ejbcaOCSPResponderURI` in VSD API.
                
        """
        self._ejbca_ocsp_responder_uri = value

    
    @property
    def ejbca_vsp_root_ca(self):
        """ Get ejbca_vsp_root_ca value.

            Notes:
                EJBCA VSP CA

                
                This attribute is named `ejbcaVspRootCa` in VSD API.
                
        """
        return self._ejbca_vsp_root_ca

    @ejbca_vsp_root_ca.setter
    def ejbca_vsp_root_ca(self, value):
        """ Set ejbca_vsp_root_ca value.

            Notes:
                EJBCA VSP CA

                
                This attribute is named `ejbcaVspRootCa` in VSD API.
                
        """
        self._ejbca_vsp_root_ca = value

    
    @property
    def alarms_max_per_object(self):
        """ Get alarms_max_per_object value.

            Notes:
                Maximum alarms per object for example max distinct alarms for specific VM (min = 5, max =20)

                
                This attribute is named `alarmsMaxPerObject` in VSD API.
                
        """
        return self._alarms_max_per_object

    @alarms_max_per_object.setter
    def alarms_max_per_object(self, value):
        """ Set alarms_max_per_object value.

            Notes:
                Maximum alarms per object for example max distinct alarms for specific VM (min = 5, max =20)

                
                This attribute is named `alarmsMaxPerObject` in VSD API.
                
        """
        self._alarms_max_per_object = value

    
    @property
    def elastic_cluster_name(self):
        """ Get elastic_cluster_name value.

            Notes:
                Specifies the name of the Elastic Search Cluster.

                
                This attribute is named `elasticClusterName` in VSD API.
                
        """
        return self._elastic_cluster_name

    @elastic_cluster_name.setter
    def elastic_cluster_name(self, value):
        """ Set elastic_cluster_name value.

            Notes:
                Specifies the name of the Elastic Search Cluster.

                
                This attribute is named `elasticClusterName` in VSD API.
                
        """
        self._elastic_cluster_name = value

    
    @property
    def elastic_search_ui_address(self):
        """ Get elastic_search_ui_address value.

            Notes:
                Specifies the server address Elastic Search Cluster.

                
                This attribute is named `elasticSearchUIAddress` in VSD API.
                
        """
        return self._elastic_search_ui_address

    @elastic_search_ui_address.setter
    def elastic_search_ui_address(self, value):
        """ Set elastic_search_ui_address value.

            Notes:
                Specifies the server address Elastic Search Cluster.

                
                This attribute is named `elasticSearchUIAddress` in VSD API.
                
        """
        self._elastic_search_ui_address = value

    
    @property
    def allow_enterprise_avatar_on_nsg(self):
        """ Get allow_enterprise_avatar_on_nsg value.

            Notes:
                Allow Enterprise Avatar to be populated on NSG Portal

                
                This attribute is named `allowEnterpriseAvatarOnNSG` in VSD API.
                
        """
        return self._allow_enterprise_avatar_on_nsg

    @allow_enterprise_avatar_on_nsg.setter
    def allow_enterprise_avatar_on_nsg(self, value):
        """ Set allow_enterprise_avatar_on_nsg value.

            Notes:
                Allow Enterprise Avatar to be populated on NSG Portal

                
                This attribute is named `allowEnterpriseAvatarOnNSG` in VSD API.
                
        """
        self._allow_enterprise_avatar_on_nsg = value

    
    @property
    def global_mac_address(self):
        """ Get global_mac_address value.

            Notes:
                the MAC Address to use for those subnets that have the useGlobalMAC flag enabled.

                
                This attribute is named `globalMACAddress` in VSD API.
                
        """
        return self._global_mac_address

    @global_mac_address.setter
    def global_mac_address(self, value):
        """ Set global_mac_address value.

            Notes:
                the MAC Address to use for those subnets that have the useGlobalMAC flag enabled.

                
                This attribute is named `globalMACAddress` in VSD API.
                
        """
        self._global_mac_address = value

    
    @property
    def inactive_timeout(self):
        """ Get inactive_timeout value.

            Notes:
                Defines the inactive timeout for the client. If the client is inactive for more than timeout, server clears off all the cache/information regarding the client. This value should be greater than event processor max timeout

                
                This attribute is named `inactiveTimeout` in VSD API.
                
        """
        return self._inactive_timeout

    @inactive_timeout.setter
    def inactive_timeout(self, value):
        """ Set inactive_timeout value.

            Notes:
                Defines the inactive timeout for the client. If the client is inactive for more than timeout, server clears off all the cache/information regarding the client. This value should be greater than event processor max timeout

                
                This attribute is named `inactiveTimeout` in VSD API.
                
        """
        self._inactive_timeout = value

    
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
    def domain_tunnel_type(self):
        """ Get domain_tunnel_type value.

            Notes:
                Default Domain Tunnel Type .Possible values are VXLAN,GRE Possible values are DC_DEFAULT, GRE, VXLAN, .

                
                This attribute is named `domainTunnelType` in VSD API.
                
        """
        return self._domain_tunnel_type

    @domain_tunnel_type.setter
    def domain_tunnel_type(self, value):
        """ Set domain_tunnel_type value.

            Notes:
                Default Domain Tunnel Type .Possible values are VXLAN,GRE Possible values are DC_DEFAULT, GRE, VXLAN, .

                
                This attribute is named `domainTunnelType` in VSD API.
                
        """
        self._domain_tunnel_type = value

    
    @property
    def post_processor_threads_count(self):
        """ Get post_processor_threads_count value.

            Notes:
                Post processor thread count.

                
                This attribute is named `postProcessorThreadsCount` in VSD API.
                
        """
        return self._post_processor_threads_count

    @post_processor_threads_count.setter
    def post_processor_threads_count(self, value):
        """ Set post_processor_threads_count value.

            Notes:
                Post processor thread count.

                
                This attribute is named `postProcessorThreadsCount` in VSD API.
                
        """
        self._post_processor_threads_count = value

    
    @property
    def group_key_default_sek_generation_interval(self):
        """ Get group_key_default_sek_generation_interval value.

            Notes:
                Group Key Encryption Profile Default SEK Generation Interval

                
                This attribute is named `groupKeyDefaultSEKGenerationInterval` in VSD API.
                
        """
        return self._group_key_default_sek_generation_interval

    @group_key_default_sek_generation_interval.setter
    def group_key_default_sek_generation_interval(self, value):
        """ Set group_key_default_sek_generation_interval value.

            Notes:
                Group Key Encryption Profile Default SEK Generation Interval

                
                This attribute is named `groupKeyDefaultSEKGenerationInterval` in VSD API.
                
        """
        self._group_key_default_sek_generation_interval = value

    
    @property
    def group_key_default_sek_lifetime(self):
        """ Get group_key_default_sek_lifetime value.

            Notes:
                Group Key Encryption Profile Default SEK Lifetime

                
                This attribute is named `groupKeyDefaultSEKLifetime` in VSD API.
                
        """
        return self._group_key_default_sek_lifetime

    @group_key_default_sek_lifetime.setter
    def group_key_default_sek_lifetime(self, value):
        """ Set group_key_default_sek_lifetime value.

            Notes:
                Group Key Encryption Profile Default SEK Lifetime

                
                This attribute is named `groupKeyDefaultSEKLifetime` in VSD API.
                
        """
        self._group_key_default_sek_lifetime = value

    
    @property
    def group_key_default_sek_payload_encryption_algorithm(self):
        """ Get group_key_default_sek_payload_encryption_algorithm value.

            Notes:
                Group Key Encryption Profile Default Sek Payload Encryption Algorithm.

                
                This attribute is named `groupKeyDefaultSEKPayloadEncryptionAlgorithm` in VSD API.
                
        """
        return self._group_key_default_sek_payload_encryption_algorithm

    @group_key_default_sek_payload_encryption_algorithm.setter
    def group_key_default_sek_payload_encryption_algorithm(self, value):
        """ Set group_key_default_sek_payload_encryption_algorithm value.

            Notes:
                Group Key Encryption Profile Default Sek Payload Encryption Algorithm.

                
                This attribute is named `groupKeyDefaultSEKPayloadEncryptionAlgorithm` in VSD API.
                
        """
        self._group_key_default_sek_payload_encryption_algorithm = value

    
    @property
    def group_key_default_sek_payload_signing_algorithm(self):
        """ Get group_key_default_sek_payload_signing_algorithm value.

            Notes:
                Group Key Encryption Profile Default Sek Payload Signing Algorithm.

                
                This attribute is named `groupKeyDefaultSEKPayloadSigningAlgorithm` in VSD API.
                
        """
        return self._group_key_default_sek_payload_signing_algorithm

    @group_key_default_sek_payload_signing_algorithm.setter
    def group_key_default_sek_payload_signing_algorithm(self, value):
        """ Set group_key_default_sek_payload_signing_algorithm value.

            Notes:
                Group Key Encryption Profile Default Sek Payload Signing Algorithm.

                
                This attribute is named `groupKeyDefaultSEKPayloadSigningAlgorithm` in VSD API.
                
        """
        self._group_key_default_sek_payload_signing_algorithm = value

    
    @property
    def group_key_default_seed_generation_interval(self):
        """ Get group_key_default_seed_generation_interval value.

            Notes:
                Group Key Encryption Profile Default Seed Generation Interval

                
                This attribute is named `groupKeyDefaultSeedGenerationInterval` in VSD API.
                
        """
        return self._group_key_default_seed_generation_interval

    @group_key_default_seed_generation_interval.setter
    def group_key_default_seed_generation_interval(self, value):
        """ Set group_key_default_seed_generation_interval value.

            Notes:
                Group Key Encryption Profile Default Seed Generation Interval

                
                This attribute is named `groupKeyDefaultSeedGenerationInterval` in VSD API.
                
        """
        self._group_key_default_seed_generation_interval = value

    
    @property
    def group_key_default_seed_lifetime(self):
        """ Get group_key_default_seed_lifetime value.

            Notes:
                Group Key Encryption Profile Default Seed Lifetime

                
                This attribute is named `groupKeyDefaultSeedLifetime` in VSD API.
                
        """
        return self._group_key_default_seed_lifetime

    @group_key_default_seed_lifetime.setter
    def group_key_default_seed_lifetime(self, value):
        """ Set group_key_default_seed_lifetime value.

            Notes:
                Group Key Encryption Profile Default Seed Lifetime

                
                This attribute is named `groupKeyDefaultSeedLifetime` in VSD API.
                
        """
        self._group_key_default_seed_lifetime = value

    
    @property
    def group_key_default_seed_payload_authentication_algorithm(self):
        """ Get group_key_default_seed_payload_authentication_algorithm value.

            Notes:
                Group Key Encryption Profile Default Seed Payload Authentication Algorithm.

                
                This attribute is named `groupKeyDefaultSeedPayloadAuthenticationAlgorithm` in VSD API.
                
        """
        return self._group_key_default_seed_payload_authentication_algorithm

    @group_key_default_seed_payload_authentication_algorithm.setter
    def group_key_default_seed_payload_authentication_algorithm(self, value):
        """ Set group_key_default_seed_payload_authentication_algorithm value.

            Notes:
                Group Key Encryption Profile Default Seed Payload Authentication Algorithm.

                
                This attribute is named `groupKeyDefaultSeedPayloadAuthenticationAlgorithm` in VSD API.
                
        """
        self._group_key_default_seed_payload_authentication_algorithm = value

    
    @property
    def group_key_default_seed_payload_encryption_algorithm(self):
        """ Get group_key_default_seed_payload_encryption_algorithm value.

            Notes:
                Group Key Encryption Profile Default Seed Payload Encryption Algorithm.

                
                This attribute is named `groupKeyDefaultSeedPayloadEncryptionAlgorithm` in VSD API.
                
        """
        return self._group_key_default_seed_payload_encryption_algorithm

    @group_key_default_seed_payload_encryption_algorithm.setter
    def group_key_default_seed_payload_encryption_algorithm(self, value):
        """ Set group_key_default_seed_payload_encryption_algorithm value.

            Notes:
                Group Key Encryption Profile Default Seed Payload Encryption Algorithm.

                
                This attribute is named `groupKeyDefaultSeedPayloadEncryptionAlgorithm` in VSD API.
                
        """
        self._group_key_default_seed_payload_encryption_algorithm = value

    
    @property
    def group_key_default_seed_payload_signing_algorithm(self):
        """ Get group_key_default_seed_payload_signing_algorithm value.

            Notes:
                Group Key Encryption Profile Default Seed Payload Signature Algorithm.

                
                This attribute is named `groupKeyDefaultSeedPayloadSigningAlgorithm` in VSD API.
                
        """
        return self._group_key_default_seed_payload_signing_algorithm

    @group_key_default_seed_payload_signing_algorithm.setter
    def group_key_default_seed_payload_signing_algorithm(self, value):
        """ Set group_key_default_seed_payload_signing_algorithm value.

            Notes:
                Group Key Encryption Profile Default Seed Payload Signature Algorithm.

                
                This attribute is named `groupKeyDefaultSeedPayloadSigningAlgorithm` in VSD API.
                
        """
        self._group_key_default_seed_payload_signing_algorithm = value

    
    @property
    def group_key_default_traffic_authentication_algorithm(self):
        """ Get group_key_default_traffic_authentication_algorithm value.

            Notes:
                Group Key Encryption Profile Default Traffic Authentication Algorithm.

                
                This attribute is named `groupKeyDefaultTrafficAuthenticationAlgorithm` in VSD API.
                
        """
        return self._group_key_default_traffic_authentication_algorithm

    @group_key_default_traffic_authentication_algorithm.setter
    def group_key_default_traffic_authentication_algorithm(self, value):
        """ Set group_key_default_traffic_authentication_algorithm value.

            Notes:
                Group Key Encryption Profile Default Traffic Authentication Algorithm.

                
                This attribute is named `groupKeyDefaultTrafficAuthenticationAlgorithm` in VSD API.
                
        """
        self._group_key_default_traffic_authentication_algorithm = value

    
    @property
    def group_key_default_traffic_encryption_algorithm(self):
        """ Get group_key_default_traffic_encryption_algorithm value.

            Notes:
                Group Key Encryption Profile Default Traffic Encryption Algorithm.

                
                This attribute is named `groupKeyDefaultTrafficEncryptionAlgorithm` in VSD API.
                
        """
        return self._group_key_default_traffic_encryption_algorithm

    @group_key_default_traffic_encryption_algorithm.setter
    def group_key_default_traffic_encryption_algorithm(self, value):
        """ Set group_key_default_traffic_encryption_algorithm value.

            Notes:
                Group Key Encryption Profile Default Traffic Encryption Algorithm.

                
                This attribute is named `groupKeyDefaultTrafficEncryptionAlgorithm` in VSD API.
                
        """
        self._group_key_default_traffic_encryption_algorithm = value

    
    @property
    def group_key_default_traffic_encryption_key_lifetime(self):
        """ Get group_key_default_traffic_encryption_key_lifetime value.

            Notes:
                Group Key Encryption Profile Default Traffic Encryption Key Lifetime

                
                This attribute is named `groupKeyDefaultTrafficEncryptionKeyLifetime` in VSD API.
                
        """
        return self._group_key_default_traffic_encryption_key_lifetime

    @group_key_default_traffic_encryption_key_lifetime.setter
    def group_key_default_traffic_encryption_key_lifetime(self, value):
        """ Set group_key_default_traffic_encryption_key_lifetime value.

            Notes:
                Group Key Encryption Profile Default Traffic Encryption Key Lifetime

                
                This attribute is named `groupKeyDefaultTrafficEncryptionKeyLifetime` in VSD API.
                
        """
        self._group_key_default_traffic_encryption_key_lifetime = value

    
    @property
    def group_key_generation_interval_on_forced_re_key(self):
        """ Get group_key_generation_interval_on_forced_re_key value.

            Notes:
                Time in seconds before new keys will be generated in the case of a forced re-key event

                
                This attribute is named `groupKeyGenerationIntervalOnForcedReKey` in VSD API.
                
        """
        return self._group_key_generation_interval_on_forced_re_key

    @group_key_generation_interval_on_forced_re_key.setter
    def group_key_generation_interval_on_forced_re_key(self, value):
        """ Set group_key_generation_interval_on_forced_re_key value.

            Notes:
                Time in seconds before new keys will be generated in the case of a forced re-key event

                
                This attribute is named `groupKeyGenerationIntervalOnForcedReKey` in VSD API.
                
        """
        self._group_key_generation_interval_on_forced_re_key = value

    
    @property
    def group_key_generation_interval_on_revoke(self):
        """ Get group_key_generation_interval_on_revoke value.

            Notes:
                Time in seconds before new keys will be generated in the case of a revoke event

                
                This attribute is named `groupKeyGenerationIntervalOnRevoke` in VSD API.
                
        """
        return self._group_key_generation_interval_on_revoke

    @group_key_generation_interval_on_revoke.setter
    def group_key_generation_interval_on_revoke(self, value):
        """ Set group_key_generation_interval_on_revoke value.

            Notes:
                Time in seconds before new keys will be generated in the case of a revoke event

                
                This attribute is named `groupKeyGenerationIntervalOnRevoke` in VSD API.
                
        """
        self._group_key_generation_interval_on_revoke = value

    
    @property
    def group_key_minimum_sek_generation_interval(self):
        """ Get group_key_minimum_sek_generation_interval value.

            Notes:
                Group Key Encryption Profile Minimum SEK Generation Interval

                
                This attribute is named `groupKeyMinimumSEKGenerationInterval` in VSD API.
                
        """
        return self._group_key_minimum_sek_generation_interval

    @group_key_minimum_sek_generation_interval.setter
    def group_key_minimum_sek_generation_interval(self, value):
        """ Set group_key_minimum_sek_generation_interval value.

            Notes:
                Group Key Encryption Profile Minimum SEK Generation Interval

                
                This attribute is named `groupKeyMinimumSEKGenerationInterval` in VSD API.
                
        """
        self._group_key_minimum_sek_generation_interval = value

    
    @property
    def group_key_minimum_sek_lifetime(self):
        """ Get group_key_minimum_sek_lifetime value.

            Notes:
                Group Key Encryption Profile Minimum SEK Lifetime

                
                This attribute is named `groupKeyMinimumSEKLifetime` in VSD API.
                
        """
        return self._group_key_minimum_sek_lifetime

    @group_key_minimum_sek_lifetime.setter
    def group_key_minimum_sek_lifetime(self, value):
        """ Set group_key_minimum_sek_lifetime value.

            Notes:
                Group Key Encryption Profile Minimum SEK Lifetime

                
                This attribute is named `groupKeyMinimumSEKLifetime` in VSD API.
                
        """
        self._group_key_minimum_sek_lifetime = value

    
    @property
    def group_key_minimum_seed_generation_interval(self):
        """ Get group_key_minimum_seed_generation_interval value.

            Notes:
                Group Key Encryption Profile Default Seed Generation Interval

                
                This attribute is named `groupKeyMinimumSeedGenerationInterval` in VSD API.
                
        """
        return self._group_key_minimum_seed_generation_interval

    @group_key_minimum_seed_generation_interval.setter
    def group_key_minimum_seed_generation_interval(self, value):
        """ Set group_key_minimum_seed_generation_interval value.

            Notes:
                Group Key Encryption Profile Default Seed Generation Interval

                
                This attribute is named `groupKeyMinimumSeedGenerationInterval` in VSD API.
                
        """
        self._group_key_minimum_seed_generation_interval = value

    
    @property
    def group_key_minimum_seed_lifetime(self):
        """ Get group_key_minimum_seed_lifetime value.

            Notes:
                Group Key Encryption Profile Default Seed Lifetime

                
                This attribute is named `groupKeyMinimumSeedLifetime` in VSD API.
                
        """
        return self._group_key_minimum_seed_lifetime

    @group_key_minimum_seed_lifetime.setter
    def group_key_minimum_seed_lifetime(self, value):
        """ Set group_key_minimum_seed_lifetime value.

            Notes:
                Group Key Encryption Profile Default Seed Lifetime

                
                This attribute is named `groupKeyMinimumSeedLifetime` in VSD API.
                
        """
        self._group_key_minimum_seed_lifetime = value

    
    @property
    def group_key_minimum_traffic_encryption_key_lifetime(self):
        """ Get group_key_minimum_traffic_encryption_key_lifetime value.

            Notes:
                Group Key Encryption Profile Minimum TEK Lifetime

                
                This attribute is named `groupKeyMinimumTrafficEncryptionKeyLifetime` in VSD API.
                
        """
        return self._group_key_minimum_traffic_encryption_key_lifetime

    @group_key_minimum_traffic_encryption_key_lifetime.setter
    def group_key_minimum_traffic_encryption_key_lifetime(self, value):
        """ Set group_key_minimum_traffic_encryption_key_lifetime value.

            Notes:
                Group Key Encryption Profile Minimum TEK Lifetime

                
                This attribute is named `groupKeyMinimumTrafficEncryptionKeyLifetime` in VSD API.
                
        """
        self._group_key_minimum_traffic_encryption_key_lifetime = value

    
    @property
    def nsg_bootstrap_endpoint(self):
        """ Get nsg_bootstrap_endpoint value.

            Notes:
                NSG Bootstrap Endpoint

                
                This attribute is named `nsgBootstrapEndpoint` in VSD API.
                
        """
        return self._nsg_bootstrap_endpoint

    @nsg_bootstrap_endpoint.setter
    def nsg_bootstrap_endpoint(self, value):
        """ Set nsg_bootstrap_endpoint value.

            Notes:
                NSG Bootstrap Endpoint

                
                This attribute is named `nsgBootstrapEndpoint` in VSD API.
                
        """
        self._nsg_bootstrap_endpoint = value

    
    @property
    def nsg_config_endpoint(self):
        """ Get nsg_config_endpoint value.

            Notes:
                NSG Config Endpoint

                
                This attribute is named `nsgConfigEndpoint` in VSD API.
                
        """
        return self._nsg_config_endpoint

    @nsg_config_endpoint.setter
    def nsg_config_endpoint(self, value):
        """ Set nsg_config_endpoint value.

            Notes:
                NSG Config Endpoint

                
                This attribute is named `nsgConfigEndpoint` in VSD API.
                
        """
        self._nsg_config_endpoint = value

    
    @property
    def nsg_local_ui_url(self):
        """ Get nsg_local_ui_url value.

            Notes:
                NSG Local UI URL - will be redirected on NSG to localhost

                
                This attribute is named `nsgLocalUiUrl` in VSD API.
                
        """
        return self._nsg_local_ui_url

    @nsg_local_ui_url.setter
    def nsg_local_ui_url(self, value):
        """ Set nsg_local_ui_url value.

            Notes:
                NSG Local UI URL - will be redirected on NSG to localhost

                
                This attribute is named `nsgLocalUiUrl` in VSD API.
                
        """
        self._nsg_local_ui_url = value

    
    @property
    def esi_id(self):
        """ Get esi_id value.

            Notes:
                ESI ID offset

                
                This attribute is named `esiID` in VSD API.
                
        """
        return self._esi_id

    @esi_id.setter
    def esi_id(self, value):
        """ Set esi_id value.

            Notes:
                ESI ID offset

                
                This attribute is named `esiID` in VSD API.
                
        """
        self._esi_id = value

    
    @property
    def csproot_authentication_method(self):
        """ Get csproot_authentication_method value.

            Notes:
                Authentication method for csproot when local authentication is not used for CSP organization

                
                This attribute is named `csprootAuthenticationMethod` in VSD API.
                
        """
        return self._csproot_authentication_method

    @csproot_authentication_method.setter
    def csproot_authentication_method(self, value):
        """ Set csproot_authentication_method value.

            Notes:
                Authentication method for csproot when local authentication is not used for CSP organization

                
                This attribute is named `csprootAuthenticationMethod` in VSD API.
                
        """
        self._csproot_authentication_method = value

    
    @property
    def stack_trace_enabled(self):
        """ Get stack_trace_enabled value.

            Notes:
                True to enable stacktrace in the REST call.

                
                This attribute is named `stackTraceEnabled` in VSD API.
                
        """
        return self._stack_trace_enabled

    @stack_trace_enabled.setter
    def stack_trace_enabled(self, value):
        """ Set stack_trace_enabled value.

            Notes:
                True to enable stacktrace in the REST call.

                
                This attribute is named `stackTraceEnabled` in VSD API.
                
        """
        self._stack_trace_enabled = value

    
    @property
    def stateful_acl_non_tcp_timeout(self):
        """ Get stateful_acl_non_tcp_timeout value.

            Notes:
                Defines the timeout in seconds for stateful ACLs that are not of type TCP.

                
                This attribute is named `statefulACLNonTCPTimeout` in VSD API.
                
        """
        return self._stateful_acl_non_tcp_timeout

    @stateful_acl_non_tcp_timeout.setter
    def stateful_acl_non_tcp_timeout(self, value):
        """ Set stateful_acl_non_tcp_timeout value.

            Notes:
                Defines the timeout in seconds for stateful ACLs that are not of type TCP.

                
                This attribute is named `statefulACLNonTCPTimeout` in VSD API.
                
        """
        self._stateful_acl_non_tcp_timeout = value

    
    @property
    def stateful_acltcp_timeout(self):
        """ Get stateful_acltcp_timeout value.

            Notes:
                Defines the timeout in seconds for stateful ACLs that are of type TCP.

                
                This attribute is named `statefulACLTCPTimeout` in VSD API.
                
        """
        return self._stateful_acltcp_timeout

    @stateful_acltcp_timeout.setter
    def stateful_acltcp_timeout(self, value):
        """ Set stateful_acltcp_timeout value.

            Notes:
                Defines the timeout in seconds for stateful ACLs that are of type TCP.

                
                This attribute is named `statefulACLTCPTimeout` in VSD API.
                
        """
        self._stateful_acltcp_timeout = value

    
    @property
    def static_wan_service_purge_time(self):
        """ Get static_wan_service_purge_time value.

            Notes:
                Timers in sec for unreacheable static WAN Services to be deleted.

                
                This attribute is named `staticWANServicePurgeTime` in VSD API.
                
        """
        return self._static_wan_service_purge_time

    @static_wan_service_purge_time.setter
    def static_wan_service_purge_time(self, value):
        """ Set static_wan_service_purge_time value.

            Notes:
                Timers in sec for unreacheable static WAN Services to be deleted.

                
                This attribute is named `staticWANServicePurgeTime` in VSD API.
                
        """
        self._static_wan_service_purge_time = value

    
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
    def stats_collector_address(self):
        """ Get stats_collector_address value.

            Notes:
                Specify the ip address(es) of the stats collector.

                
                This attribute is named `statsCollectorAddress` in VSD API.
                
        """
        return self._stats_collector_address

    @stats_collector_address.setter
    def stats_collector_address(self, value):
        """ Set stats_collector_address value.

            Notes:
                Specify the ip address(es) of the stats collector.

                
                This attribute is named `statsCollectorAddress` in VSD API.
                
        """
        self._stats_collector_address = value

    
    @property
    def stats_collector_port(self):
        """ Get stats_collector_port value.

            Notes:
                Specify the port number(s) of the stats collector.

                
                This attribute is named `statsCollectorPort` in VSD API.
                
        """
        return self._stats_collector_port

    @stats_collector_port.setter
    def stats_collector_port(self, value):
        """ Set stats_collector_port value.

            Notes:
                Specify the port number(s) of the stats collector.

                
                This attribute is named `statsCollectorPort` in VSD API.
                
        """
        self._stats_collector_port = value

    
    @property
    def stats_collector_proto_buf_port(self):
        """ Get stats_collector_proto_buf_port value.

            Notes:
                Specify the protobuf port number(s) of the stats collector.

                
                This attribute is named `statsCollectorProtoBufPort` in VSD API.
                
        """
        return self._stats_collector_proto_buf_port

    @stats_collector_proto_buf_port.setter
    def stats_collector_proto_buf_port(self, value):
        """ Set stats_collector_proto_buf_port value.

            Notes:
                Specify the protobuf port number(s) of the stats collector.

                
                This attribute is named `statsCollectorProtoBufPort` in VSD API.
                
        """
        self._stats_collector_proto_buf_port = value

    
    @property
    def stats_max_data_points(self):
        """ Get stats_max_data_points value.

            Notes:
                Specifies the maximum number of data points to support.

                
                This attribute is named `statsMaxDataPoints` in VSD API.
                
        """
        return self._stats_max_data_points

    @stats_max_data_points.setter
    def stats_max_data_points(self, value):
        """ Set stats_max_data_points value.

            Notes:
                Specifies the maximum number of data points to support.

                
                This attribute is named `statsMaxDataPoints` in VSD API.
                
        """
        self._stats_max_data_points = value

    
    @property
    def stats_min_duration(self):
        """ Get stats_min_duration value.

            Notes:
                Default minimum duration for statistics to be displayed in UI is 30 days in seconds.

                
                This attribute is named `statsMinDuration` in VSD API.
                
        """
        return self._stats_min_duration

    @stats_min_duration.setter
    def stats_min_duration(self, value):
        """ Set stats_min_duration value.

            Notes:
                Default minimum duration for statistics to be displayed in UI is 30 days in seconds.

                
                This attribute is named `statsMinDuration` in VSD API.
                
        """
        self._stats_min_duration = value

    
    @property
    def stats_number_of_data_points(self):
        """ Get stats_number_of_data_points value.

            Notes:
                Specifies number of data points.

                
                This attribute is named `statsNumberOfDataPoints` in VSD API.
                
        """
        return self._stats_number_of_data_points

    @stats_number_of_data_points.setter
    def stats_number_of_data_points(self, value):
        """ Set stats_number_of_data_points value.

            Notes:
                Specifies number of data points.

                
                This attribute is named `statsNumberOfDataPoints` in VSD API.
                
        """
        self._stats_number_of_data_points = value

    
    @property
    def stats_tsdb_server_address(self):
        """ Get stats_tsdb_server_address value.

            Notes:
                Specifies the TSDB server location.

                
                This attribute is named `statsTSDBServerAddress` in VSD API.
                
        """
        return self._stats_tsdb_server_address

    @stats_tsdb_server_address.setter
    def stats_tsdb_server_address(self, value):
        """ Set stats_tsdb_server_address value.

            Notes:
                Specifies the TSDB server location.

                
                This attribute is named `statsTSDBServerAddress` in VSD API.
                
        """
        self._stats_tsdb_server_address = value

    
    @property
    def sticky_ecmp_idle_timeout(self):
        """ Get sticky_ecmp_idle_timeout value.

            Notes:
                sticky ECMP Idle Timeout in seconds

                
                This attribute is named `stickyECMPIdleTimeout` in VSD API.
                
        """
        return self._sticky_ecmp_idle_timeout

    @sticky_ecmp_idle_timeout.setter
    def sticky_ecmp_idle_timeout(self, value):
        """ Set sticky_ecmp_idle_timeout value.

            Notes:
                sticky ECMP Idle Timeout in seconds

                
                This attribute is named `stickyECMPIdleTimeout` in VSD API.
                
        """
        self._sticky_ecmp_idle_timeout = value

    
    @property
    def subnet_resync_interval(self):
        """ Get subnet_resync_interval value.

            Notes:
                After resync on a subnet , another resync on the same subnet is allowed based on the below value subnet resync complete wait time in min.

                
                This attribute is named `subnetResyncInterval` in VSD API.
                
        """
        return self._subnet_resync_interval

    @subnet_resync_interval.setter
    def subnet_resync_interval(self, value):
        """ Set subnet_resync_interval value.

            Notes:
                After resync on a subnet , another resync on the same subnet is allowed based on the below value subnet resync complete wait time in min.

                
                This attribute is named `subnetResyncInterval` in VSD API.
                
        """
        self._subnet_resync_interval = value

    
    @property
    def subnet_resync_outstanding_interval(self):
        """ Get subnet_resync_outstanding_interval value.

            Notes:
                Outstanding subnet resync interval (in secs). System wide value.

                
                This attribute is named `subnetResyncOutstandingInterval` in VSD API.
                
        """
        return self._subnet_resync_outstanding_interval

    @subnet_resync_outstanding_interval.setter
    def subnet_resync_outstanding_interval(self, value):
        """ Set subnet_resync_outstanding_interval value.

            Notes:
                Outstanding subnet resync interval (in secs). System wide value.

                
                This attribute is named `subnetResyncOutstandingInterval` in VSD API.
                
        """
        self._subnet_resync_outstanding_interval = value

    
    @property
    def customer_id_upper_limit(self):
        """ Get customer_id_upper_limit value.

            Notes:
                Customer id upper limit, system wide value

                
                This attribute is named `customerIDUpperLimit` in VSD API.
                
        """
        return self._customer_id_upper_limit

    @customer_id_upper_limit.setter
    def customer_id_upper_limit(self, value):
        """ Set customer_id_upper_limit value.

            Notes:
                Customer id upper limit, system wide value

                
                This attribute is named `customerIDUpperLimit` in VSD API.
                
        """
        self._customer_id_upper_limit = value

    
    @property
    def customer_key(self):
        """ Get customer_key value.

            Notes:
                Customer key associated with the licese

                
                This attribute is named `customerKey` in VSD API.
                
        """
        return self._customer_key

    @customer_key.setter
    def customer_key(self, value):
        """ Set customer_key value.

            Notes:
                Customer key associated with the licese

                
                This attribute is named `customerKey` in VSD API.
                
        """
        self._customer_key = value

    
    @property
    def avatar_base_path(self):
        """ Get avatar_base_path value.

            Notes:
                Defines location where image files needs to be copied. Above URL should be configured to read the file from this location.

                
                This attribute is named `avatarBasePath` in VSD API.
                
        """
        return self._avatar_base_path

    @avatar_base_path.setter
    def avatar_base_path(self, value):
        """ Set avatar_base_path value.

            Notes:
                Defines location where image files needs to be copied. Above URL should be configured to read the file from this location.

                
                This attribute is named `avatarBasePath` in VSD API.
                
        """
        self._avatar_base_path = value

    
    @property
    def avatar_base_url(self):
        """ Get avatar_base_url value.

            Notes:
                Defines the url to read the avatar image files

                
                This attribute is named `avatarBaseURL` in VSD API.
                
        """
        return self._avatar_base_url

    @avatar_base_url.setter
    def avatar_base_url(self, value):
        """ Set avatar_base_url value.

            Notes:
                Defines the url to read the avatar image files

                
                This attribute is named `avatarBaseURL` in VSD API.
                
        """
        self._avatar_base_url = value

    
    @property
    def event_log_cleanup_interval(self):
        """ Get event_log_cleanup_interval value.

            Notes:
                Cleanup task run interval in seconds.

                
                This attribute is named `eventLogCleanupInterval` in VSD API.
                
        """
        return self._event_log_cleanup_interval

    @event_log_cleanup_interval.setter
    def event_log_cleanup_interval(self, value):
        """ Set event_log_cleanup_interval value.

            Notes:
                Cleanup task run interval in seconds.

                
                This attribute is named `eventLogCleanupInterval` in VSD API.
                
        """
        self._event_log_cleanup_interval = value

    
    @property
    def event_log_entry_max_age(self):
        """ Get event_log_entry_max_age value.

            Notes:
                Maximum age in days for cleanup of the eventlog entries. On every periodic interval run, any eventlog entries older than this max age will be deleted.

                
                This attribute is named `eventLogEntryMaxAge` in VSD API.
                
        """
        return self._event_log_entry_max_age

    @event_log_entry_max_age.setter
    def event_log_entry_max_age(self, value):
        """ Set event_log_entry_max_age value.

            Notes:
                Maximum age in days for cleanup of the eventlog entries. On every periodic interval run, any eventlog entries older than this max age will be deleted.

                
                This attribute is named `eventLogEntryMaxAge` in VSD API.
                
        """
        self._event_log_entry_max_age = value

    
    @property
    def event_processor_interval(self):
        """ Get event_processor_interval value.

            Notes:
                Defines time interval in milliseconds when events collected for a client should be processed.

                
                This attribute is named `eventProcessorInterval` in VSD API.
                
        """
        return self._event_processor_interval

    @event_processor_interval.setter
    def event_processor_interval(self, value):
        """ Set event_processor_interval value.

            Notes:
                Defines time interval in milliseconds when events collected for a client should be processed.

                
                This attribute is named `eventProcessorInterval` in VSD API.
                
        """
        self._event_processor_interval = value

    
    @property
    def event_processor_max_events_count(self):
        """ Get event_processor_max_events_count value.

            Notes:
                Defines the maximum number of events to be collected in case of events burst.

                
                This attribute is named `eventProcessorMaxEventsCount` in VSD API.
                
        """
        return self._event_processor_max_events_count

    @event_processor_max_events_count.setter
    def event_processor_max_events_count(self, value):
        """ Set event_processor_max_events_count value.

            Notes:
                Defines the maximum number of events to be collected in case of events burst.

                
                This attribute is named `eventProcessorMaxEventsCount` in VSD API.
                
        """
        self._event_processor_max_events_count = value

    
    @property
    def event_processor_timeout(self):
        """ Get event_processor_timeout value.

            Notes:
                Defines the maximum time period in milliseconds for the Rest server to wait before sending the events from the system.

                
                This attribute is named `eventProcessorTimeout` in VSD API.
                
        """
        return self._event_processor_timeout

    @event_processor_timeout.setter
    def event_processor_timeout(self, value):
        """ Set event_processor_timeout value.

            Notes:
                Defines the maximum time period in milliseconds for the Rest server to wait before sending the events from the system.

                
                This attribute is named `eventProcessorTimeout` in VSD API.
                
        """
        self._event_processor_timeout = value

    
    @property
    def two_factor_code_expiry(self):
        """ Get two_factor_code_expiry value.

            Notes:
                Two Factor Code Expiry in Seconds

                
                This attribute is named `twoFactorCodeExpiry` in VSD API.
                
        """
        return self._two_factor_code_expiry

    @two_factor_code_expiry.setter
    def two_factor_code_expiry(self, value):
        """ Set two_factor_code_expiry value.

            Notes:
                Two Factor Code Expiry in Seconds

                
                This attribute is named `twoFactorCodeExpiry` in VSD API.
                
        """
        self._two_factor_code_expiry = value

    
    @property
    def two_factor_code_length(self):
        """ Get two_factor_code_length value.

            Notes:
                Two Factor Code Length

                
                This attribute is named `twoFactorCodeLength` in VSD API.
                
        """
        return self._two_factor_code_length

    @two_factor_code_length.setter
    def two_factor_code_length(self, value):
        """ Set two_factor_code_length value.

            Notes:
                Two Factor Code Length

                
                This attribute is named `twoFactorCodeLength` in VSD API.
                
        """
        self._two_factor_code_length = value

    
    @property
    def two_factor_code_seed_length(self):
        """ Get two_factor_code_seed_length value.

            Notes:
                Two Factor Seed length in bytes

                
                This attribute is named `twoFactorCodeSeedLength` in VSD API.
                
        """
        return self._two_factor_code_seed_length

    @two_factor_code_seed_length.setter
    def two_factor_code_seed_length(self, value):
        """ Set two_factor_code_seed_length value.

            Notes:
                Two Factor Seed length in bytes

                
                This attribute is named `twoFactorCodeSeedLength` in VSD API.
                
        """
        self._two_factor_code_seed_length = value

    
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
    def dynamic_wan_service_diff_time(self):
        """ Get dynamic_wan_service_diff_time value.

            Notes:
                Timers in sec for  dynamic WAN Services to be considered not seen by 7X50.

                
                This attribute is named `dynamicWANServiceDiffTime` in VSD API.
                
        """
        return self._dynamic_wan_service_diff_time

    @dynamic_wan_service_diff_time.setter
    def dynamic_wan_service_diff_time(self, value):
        """ Set dynamic_wan_service_diff_time value.

            Notes:
                Timers in sec for  dynamic WAN Services to be considered not seen by 7X50.

                
                This attribute is named `dynamicWANServiceDiffTime` in VSD API.
                
        """
        self._dynamic_wan_service_diff_time = value

    
    @property
    def syslog_destination_host(self):
        """ Get syslog_destination_host value.

            Notes:
                Specifies the remote syslog destination host

                
                This attribute is named `syslogDestinationHost` in VSD API.
                
        """
        return self._syslog_destination_host

    @syslog_destination_host.setter
    def syslog_destination_host(self, value):
        """ Set syslog_destination_host value.

            Notes:
                Specifies the remote syslog destination host

                
                This attribute is named `syslogDestinationHost` in VSD API.
                
        """
        self._syslog_destination_host = value

    
    @property
    def syslog_destination_port(self):
        """ Get syslog_destination_port value.

            Notes:
                Specified the remote syslog destination port

                
                This attribute is named `syslogDestinationPort` in VSD API.
                
        """
        return self._syslog_destination_port

    @syslog_destination_port.setter
    def syslog_destination_port(self, value):
        """ Set syslog_destination_port value.

            Notes:
                Specified the remote syslog destination port

                
                This attribute is named `syslogDestinationPort` in VSD API.
                
        """
        self._syslog_destination_port = value

    
    @property
    def sysmon_cleanup_task_interval(self):
        """ Get sysmon_cleanup_task_interval value.

            Notes:
                Sysmon cleanup task run interval in seconds.

                
                This attribute is named `sysmonCleanupTaskInterval` in VSD API.
                
        """
        return self._sysmon_cleanup_task_interval

    @sysmon_cleanup_task_interval.setter
    def sysmon_cleanup_task_interval(self, value):
        """ Set sysmon_cleanup_task_interval value.

            Notes:
                Sysmon cleanup task run interval in seconds.

                
                This attribute is named `sysmonCleanupTaskInterval` in VSD API.
                
        """
        self._sysmon_cleanup_task_interval = value

    
    @property
    def sysmon_node_presence_timeout(self):
        """ Get sysmon_node_presence_timeout value.

            Notes:
                Node presence timeout in seconds if no messages.

                
                This attribute is named `sysmonNodePresenceTimeout` in VSD API.
                
        """
        return self._sysmon_node_presence_timeout

    @sysmon_node_presence_timeout.setter
    def sysmon_node_presence_timeout(self, value):
        """ Set sysmon_node_presence_timeout value.

            Notes:
                Node presence timeout in seconds if no messages.

                
                This attribute is named `sysmonNodePresenceTimeout` in VSD API.
                
        """
        self._sysmon_node_presence_timeout = value

    
    @property
    def sysmon_probe_response_timeout(self):
        """ Get sysmon_probe_response_timeout value.

            Notes:
                Probe response timeout in seconds.

                
                This attribute is named `sysmonProbeResponseTimeout` in VSD API.
                
        """
        return self._sysmon_probe_response_timeout

    @sysmon_probe_response_timeout.setter
    def sysmon_probe_response_timeout(self, value):
        """ Set sysmon_probe_response_timeout value.

            Notes:
                Probe response timeout in seconds.

                
                This attribute is named `sysmonProbeResponseTimeout` in VSD API.
                
        """
        self._sysmon_probe_response_timeout = value

    
    @property
    def system_avatar_data(self):
        """ Get system_avatar_data value.

            Notes:
                CSP Avatar Data

                
                This attribute is named `systemAvatarData` in VSD API.
                
        """
        return self._system_avatar_data

    @system_avatar_data.setter
    def system_avatar_data(self, value):
        """ Set system_avatar_data value.

            Notes:
                CSP Avatar Data

                
                This attribute is named `systemAvatarData` in VSD API.
                
        """
        self._system_avatar_data = value

    
    @property
    def system_avatar_type(self):
        """ Get system_avatar_type value.

            Notes:
                None

                
                This attribute is named `systemAvatarType` in VSD API.
                
        """
        return self._system_avatar_type

    @system_avatar_type.setter
    def system_avatar_type(self, value):
        """ Set system_avatar_type value.

            Notes:
                None

                
                This attribute is named `systemAvatarType` in VSD API.
                
        """
        self._system_avatar_type = value

    

    