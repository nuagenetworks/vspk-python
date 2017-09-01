.. _nusystemconfig:

nusystemconfig
===========================================

.. class:: nusystemconfig.NUSystemConfig(bambou.nurest_object.NUMetaRESTObject,):

The system configuration which can be dynamically managed using rest api.


Attributes
----------


- ``aar_flow_stats_interval``: AAR flow statistics collection frequency

- ``aar_probe_stats_interval``: AAR probe statistics collection frequency

- ``acl_allow_origin``: Defines the domains allowed for access control list.

- ``ecmp_count``: System Default Equal-cost multi-path routing count,Every Domain derives ECMP count from this value unless specifically set for the domain

- ``ldap_sync_interval``: LDAP Sync-Up task interval in seconds.

- ``ldap_trust_store_certifcate``: Location of the truststore which is need to store LDAP server certificates. Default is cacerts located in java.home/lib/security/cacerts. Uncomment below setting if you need to use a different file

- ``ldap_trust_store_password``: Password to access the truststore. Uncomment below line to change its value.

- ``ad_gateway_purge_time``: Timers in sec for undefined vms to be deleted(min =7200, max = 86400).

- ``rd_lower_limit``: route distinguisher lower limit

- ``rd_public_network_lower_limit``: route distinguisher public network lower limit

- ``rd_public_network_upper_limit``: route distinguisher public network upper limit

- ``rd_upper_limit``: route distinguisher upper limit

- ``zfb_bootstrap_enabled``: Whether the NSG should auto bootstrap using ZFB

- ``zfb_request_retry_timer``: Retry time for the ZFB daemon to recheck ZFBRequest Status in seconds

- ``zfb_scheduler_stale_request_timeout``: Time for the ZFB scheduler to wait in seconds before deleting a stale request

- ``pgid_lower_limit``: Lower limit for the policy group id.

- ``pgid_upper_limit``: Upper limit for the policy group id.

- ``dhcp_option_size``: Defines total DHCP options that can be set on a domain.

- ``vlanid_lower_limit``: None

- ``vlanid_upper_limit``: None

- ``vm_cache_size``: LRU Map size for vm, this value has to set based on memory given to VSD jvm not finalized.

- ``vm_purge_time``: Timers in sec for undefined vms to be deleted.

- ``vm_resync_deletion_wait_time``: After resync on vm , if no controller returns with a VM request with in the below timeframe then it will get deleted deletion wait time in minutes.

- ``vm_resync_outstanding_interval``: Outstanding VM resync interval (in secs). System wide value.

- ``vm_unreachable_cleanup_time``: Timers in sec for unreachable VMs for cleanup.

- ``vm_unreachable_time``: Timers in sec for unreachable VMs.

- ``vnf_task_timeout``: Timeout for VNF task for nsg agent

- ``vnid_lower_limit``: Virtual network ID offset

- ``vnid_public_network_lower_limit``: Virtual network ID public network lower limit

- ``vnid_public_network_upper_limit``: Virtual network ID public network upper limit

- ``vnid_upper_limit``: Virtual network ID upper limit

- ``api_key_renewal_interval``: Defines the interval in seconds, before the expiry time, that can used to renew the apiKey by making me API call. Minimum value is 1 min and maximum is 5 min.

- ``api_key_validity``: Defines the apiKey validity duration in seconds. Default is 24 hours and minimum value is 10 min.

- ``vport_init_stateful_timer``: Defines the timeout in seconds for vport initialization to stateful. Default value is 300 secs and the timeout should be between 0 to 86400 seconds.

- ``lru_cache_size_per_subnet``: LRU Map size per subnet (to hold the deleted vm's ip addresses).

- ``vsc_on_same_version_as_vsd``: This flag is used to indicate that whether VSC is on the same version as VSD or not.

- ``vsd_read_only_mode``: True means VSD readonly mode enabled. False means VSD readonly mode disabled

- ``vsd_upgrade_is_complete``: This flag is used to indicate that whether VSD upgrade is complete,it is expected that csproot will set to true,after VSD upgrade is complete and also making sure that all VSC's audits and Gateway audits with VSD are done

- ``as_number``:  Autonomous System Number,Used for RT/RD auto-generation

- ``vss_stats_interval``: VSS statistics collection frequency

- ``rt_lower_limit``: route target lower limit

- ``rt_public_network_lower_limit``: route target public network lower limit

- ``rt_public_network_upper_limit``: route target public network upper limit

- ``rt_upper_limit``: route target upper limit

- ``evpnbgp_community_tag_as_number``: Autonomous System Number,Used for EVPNBGPCommunityTag auto-generation

- ``evpnbgp_community_tag_lower_limit``: EVPNBGPCommunityTag lower limit

- ``evpnbgp_community_tag_upper_limit``: EVPNBGPCommunityTag upper limit

- ``page_max_size``: Defines upper bound for the page size. Configured or input page size should be less than this max page size.

- ``page_size``: Defines the page size for the results returned by the REST call.

- ``last_updated_by``: ID of the user who last updated the object.

- ``max_failed_logins``: Maximum failed login attempts before the account is locked (min = 5, max = 10). 0 = not enforced (unlimited attempts). This is not enforced if LDAP is used for authorization

- ``max_response``: Defines maximum results returned by the REST call (allowed max=5000).

- ``accumulate_licenses_enabled``: Whether the various VRS license flavours be merged in one pool

- ``per_domain_vlan_id_enabled``: None

- ``performance_path_selection_vnid``: performance Path Selection Virtual Network ID

- ``service_id_upper_limit``: Service id upper limit system wide value

- ``key_server_monitor_enabled``: Enable the keyserver debug monitor (ie. ksmon command)

- ``key_server_vsd_data_synchronization_interval``: KeyServer time in seconds between full resyncs of VSD data (just in case of missed events)

- ``offset_customer_id``: Customer id offset, this value has to be set before jboss starts , after that any change of value is ignored (minexclusive = 0, max = 20000) system wide value

- ``offset_service_id``: Service id offset, this value has to be set before jboss starts during install time, after that any change of value is ignored (minexclusive = 0, max = 40000) system wide value

- ``ejbca_nsg_certificate_profile``: EJBCA NSG Certificate Profile

- ``ejbca_nsg_end_entity_profile``: EJBCA NSG End Entity Profile

- ``ejbca_ocsp_responder_cn``: EJBCA OCSP Responder CommonName

- ``ejbca_ocsp_responder_uri``: EJBCA OCSP Responder URI

- ``ejbca_vsp_root_ca``: EJBCA VSP CA

- ``alarms_max_per_object``: Maximum alarms per object for example max distinct alarms for specific VM (min = 5, max =20)

- ``elastic_cluster_name``: Specifies the name of the Elastic Search Cluster.

- ``allow_enterprise_avatar_on_nsg``: Allow Enterprise Avatar to be populated on NSG Portal

- ``global_mac_address``: the MAC Address to use for those subnets that have the useGlobalMAC flag enabled.

- ``flow_collection_enabled``: Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires "statisticsEnabled".

- ``inactive_timeout``: Defines the inactive timeout for the client. If the client is inactive for more than timeout, server clears off all the cache/information regarding the client. This value should be greater than event processor max timeout

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_tunnel_type``: Default Domain Tunnel Type .Possible values are VXLAN,GRE Possible values are DC_DEFAULT, GRE, VXLAN, .

- ``post_processor_threads_count``: Post processor thread count.

- ``group_key_default_sek_generation_interval``: Group Key Encryption Profile Default SEK Generation Interval

- ``group_key_default_sek_lifetime``: Group Key Encryption Profile Default SEK Lifetime

- ``group_key_default_sek_payload_encryption_algorithm``: Group Key Encryption Profile Default Sek Payload Encryption Algorithm.

- ``group_key_default_sek_payload_signing_algorithm``: Group Key Encryption Profile Default Sek Payload Signing Algorithm.

- ``group_key_default_seed_generation_interval``: Group Key Encryption Profile Default Seed Generation Interval

- ``group_key_default_seed_lifetime``: Group Key Encryption Profile Default Seed Lifetime

- ``group_key_default_seed_payload_authentication_algorithm``: Group Key Encryption Profile Default Seed Payload Authentication Algorithm.

- ``group_key_default_seed_payload_encryption_algorithm``: Group Key Encryption Profile Default Seed Payload Encryption Algorithm.

- ``group_key_default_seed_payload_signing_algorithm``: Group Key Encryption Profile Default Seed Payload Signature Algorithm.

- ``group_key_default_traffic_authentication_algorithm``: Group Key Encryption Profile Default Traffic Authentication Algorithm.

- ``group_key_default_traffic_encryption_algorithm``: Group Key Encryption Profile Default Traffic Encryption Algorithm.

- ``group_key_default_traffic_encryption_key_lifetime``: Group Key Encryption Profile Default Traffic Encryption Key Lifetime

- ``group_key_generation_interval_on_forced_re_key``: Time in seconds before new keys will be generated in the case of a forced re-key event

- ``group_key_generation_interval_on_revoke``: Time in seconds before new keys will be generated in the case of a revoke event

- ``group_key_minimum_sek_generation_interval``: Group Key Encryption Profile Minimum SEK Generation Interval

- ``group_key_minimum_sek_lifetime``: Group Key Encryption Profile Minimum SEK Lifetime

- ``group_key_minimum_seed_generation_interval``: Group Key Encryption Profile Default Seed Generation Interval

- ``group_key_minimum_seed_lifetime``: Group Key Encryption Profile Default Seed Lifetime

- ``group_key_minimum_traffic_encryption_key_lifetime``: Group Key Encryption Profile Minimum TEK Lifetime

- ``nsg_bootstrap_endpoint``: NSG Bootstrap Endpoint

- ``nsg_config_endpoint``: NSG Config Endpoint

- ``nsg_local_ui_url``: NSG Local UI URL - will be redirected on NSG to localhost

- ``esi_id``: ESI ID offset

- ``csproot_authentication_method``: Authentication method for csproot when local authentication is not used for CSP organization

- ``stack_trace_enabled``: True to enable stacktrace in the REST call.

- ``stateful_acl_non_tcp_timeout``: Defines the timeout in seconds for stateful ACLs that are not of type TCP.

- ``stateful_acltcp_timeout``: Defines the timeout in seconds for stateful ACLs that are of type TCP.

- ``static_wan_service_purge_time``: Timers in sec for unreacheable static WAN Services to be deleted.

- ``statistics_enabled``: This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

- ``stats_collector_address``: Specify the ip address(es) of the stats collector.

- ``stats_collector_port``: Specify the port number(s) of the stats collector.

- ``stats_collector_proto_buf_port``: Specify the protobuf port number(s) of the stats collector.

- ``stats_max_data_points``: Specifies the maximum number of data points to support.

- ``stats_min_duration``: Default minimum duration for statistics to be displayed in UI is 30 days in seconds.

- ``stats_number_of_data_points``: Specifies number of data points.

- ``stats_tsdb_server_address``: Specifies the TSDB server location.

- ``sticky_ecmp_idle_timeout``: sticky ECMP Idle Timeout in seconds

- ``attach_probe_to_ipsec_npm``: Flag to attach/remove system generated probe to system generated NPM for IPSEC.

- ``attach_probe_to_vxlannpm``: Flag to attach/remove system generated probe to system generated NPM for VXLAN.

- ``subnet_resync_interval``: After resync on a subnet , another resync on the same subnet is allowed based on the below value subnet resync complete wait time in min.

- ``subnet_resync_outstanding_interval``: Outstanding subnet resync interval (in secs). System wide value.

- ``customer_id_upper_limit``: Customer id upper limit, system wide value

- ``customer_key``: Customer key associated with the licese

- ``avatar_base_path``: Defines location where image files needs to be copied. Above URL should be configured to read the file from this location.

- ``avatar_base_url``: Defines the url to read the avatar image files

- ``event_log_cleanup_interval``: Cleanup task run interval in seconds.

- ``event_log_entry_max_age``: Maximum age in days for cleanup of the eventlog entries. On every periodic interval run, any eventlog entries older than this max age will be deleted.

- ``event_processor_interval``: Defines time interval in milliseconds when events collected for a client should be processed.

- ``event_processor_max_events_count``: Defines the maximum number of events to be collected in case of events burst.

- ``event_processor_timeout``: Defines the maximum time period in milliseconds for the Rest server to wait before sending the events from the system.

- ``two_factor_code_expiry``: Two Factor Code Expiry in Seconds

- ``two_factor_code_length``: Two Factor Code Length

- ``two_factor_code_seed_length``: Two Factor Seed length in bytes

- ``external_id``: External object ID. Used for integration with third party systems

- ``dynamic_wan_service_diff_time``: Timers in sec for  dynamic WAN Services to be considered not seen by 7X50.

- ``syslog_destination_host``: Specifies the remote syslog destination host

- ``syslog_destination_port``: Specified the remote syslog destination port

- ``sysmon_cleanup_task_interval``: Sysmon cleanup task run interval in seconds.

- ``sysmon_node_presence_timeout``: Time interval in seconds at which sysmon messages are reported by controller.

- ``sysmon_probe_response_timeout``: Probe response timeout in seconds.

- ``system_avatar_data``: CSP Avatar Data

- ``system_avatar_type``: None




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

