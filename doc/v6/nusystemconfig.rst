.. _nusystemconfig:

nusystemconfig
===========================================

.. class:: nusystemconfig.NUSystemConfig(bambou.nurest_object.NUMetaRESTObject,):

The System Configuration which can be dynamically managed using REST Api.


Attributes
----------


- ``aar_flow_stats_interval``: AAR flow statistics collection interval in seconds.

- ``aar_probe_stats_interval``: AAR probe statistics collection interval in seconds.

- ``acl_allow_origin``: Defines the domains allowed for access control list.

- ``ecmp_count``: System Default Equal-cost multi-path routing count. Every Domain derives ECMP count from this value unless specifically set for the domain.

- ``ldap_max_config``: Maximum number of LDAP configurations.

- ``ldap_sync_interval``: LDAP Sync-Up task interval in seconds.

- ``ldap_trust_store_certifcate``: Location of the truststore which is need to store LDAP server certificates. Default is cacerts located in java.home/lib/security/cacerts. Uncomment below setting if you need to use a different file

- ``ldap_trust_store_password``: Password to access the truststore. Uncomment below line to change its value.

- ``ad_gateway_purge_time``: Timer in seconds for undefined VMs or auto-discovered NSGateway instances to be deleted from VSD.

- ``rd_lower_limit``: Route distinguisher (RD) lower limit.

- ``rd_public_network_lower_limit``: Route distinguisher (RD) public network lower limit.

- ``rd_public_network_upper_limit``: Route distinguisher (RD) public network upper limit.

- ``rd_upper_limit``: Route distinguisher (RD) upper limit.

- ``zfb_bootstrap_enabled``: Whether the NSG should auto bootstrap using ZFB

- ``zfb_request_retry_timer``: Retry time for the ZFB daemon to recheck ZFBRequest Status in seconds

- ``zfb_scheduler_stale_request_timeout``: Time for the ZFB scheduler to wait in seconds before deleting a stale request

- ``pgid_lower_limit``: Lower limit for the policy group ID.

- ``pgid_upper_limit``: Upper limit for the policy group ID.

- ``dhcp_option_size``: Defines total DHCP options that can be set on a domain.

- ``vlanid_lower_limit``: Offset for the Per domain VLAN ID for gateways of type HWVTEP

- ``vlanid_upper_limit``: Upper limit for the per domain VLAN ID for gateways of type HWVTEP

- ``vm_cache_size``: Least Recently Used (LRU) Map size for VMs, this value has to be set based on the amount of memory given to VSD's JVM.

- ``vm_purge_time``: Timer in seconds for undefined VMs to be deleted.

- ``vm_resync_deletion_wait_time``: After performing a resync on VMs, if no controller returns with a VM request within the specified timeframe then it will be deleted. The deletion wait time is in minutes.

- ``vm_resync_outstanding_interval``: Outstanding VM resync interval (in seconds). System wide value.

- ``vm_unreachable_cleanup_time``: Timer in seconds for unreachable VMs to be marked for cleanup.

- ``vm_unreachable_time``: Timer in seconds for considering a VM as unreachable.

- ``vnf_task_timeout``: Timeout for VNF task running on the NSG by the NSG Agent (in seconds).

- ``vnid_lower_limit``: Virtual network ID offset

- ``vnid_public_network_lower_limit``: Virtual network ID public network lower limit

- ``vnid_public_network_upper_limit``: Virtual network ID public network upper limit

- ``vnid_upper_limit``: Virtual network ID upper limit

- ``api_key_renewal_interval``: Defines the interval in seconds, before the expiry time, which can be used to renew the apiKey by making the '/me' API call. Minimum value is 60 s (1 minute) and maximum is 300 s (5 minutes).

- ``api_key_validity``: Defines the apiKey validity duration in seconds. Default and maximum values are 24 hours (86400 s) and minimum value is 10 minutes (600 s).

- ``vport_init_stateful_timer``: Defines the timeout in seconds for vport initialization to stateful. Default value is 300 seconds and the timeout should be within a range going from 0 to 86400 seconds.

- ``ipv6_extended_prefixes_enabled``: Allows the creation of IPv6 subnets and routes with masks longer than /64.

- ``lru_cache_size_per_subnet``: Least Recently Used (LRU) Cache map size per subnet.  Serves to hold the deleted VM instances' IP addresses.

- ``vsc_on_same_version_as_vsd``: This flag is used to indicate that whether VSC is on the same version as VSD or not.

- ``vsdaar_application_version``: Version of the current imported Application Signatures.

- ``vsdaar_application_version_publish_date``: Determines the time that Application Signatures were published and added in the VSD or if the signatures used are the ones that came with the current version of VSD.

- ``vsd_read_only_mode``: True means VSD readonly mode enabled. False means VSD readonly mode disabled.

- ``vsd_upgrade_is_complete``: This flag is used to indicate whether VSD upgrade is complete. It is expected that csproot will set the value to true after VSD upgrade is complete and ensuring that all VSC's audits and Gateway audits with VSD are completed.

- ``nsg_uplink_hold_down_timer``: In case of a dual-uplink NSG, the hold down time in seconds, after which an uplink connection that recovered from failure is re-used.

- ``as_number``: System's Autonomous System (AS) number. Used in the automatic generation of Route Target (RT) and Route Distinguisher (RD) numbers.

- ``vss_stats_interval``: VSS statistics collection frequency in seconds.

- ``rt_lower_limit``: Route target (RT) lower limit.

- ``rt_public_network_lower_limit``: Route target (RT) public network lower limit.

- ``rt_public_network_upper_limit``: Route target (RT) public network upper limit.

- ``rt_upper_limit``: Route target (RT) upper limit

- ``evpnbgp_community_tag_as_number``: Autonomous System Number used for 'EVPNBGPCommunityTag' generation.

- ``evpnbgp_community_tag_lower_limit``: EVPNBGPCommunityTag lower limit

- ``evpnbgp_community_tag_upper_limit``: EVPNBGPCommunityTag upper limit

- ``ca_certificates_expiry_time``: CA Certificates expiry date with time

- ``saa_s_applications_publish_date``: Determines the time that SaaS applications were imported in VSD or if they are the ones that came with this version of VSD (built-in).

- ``page_max_size``: Defines upper bound for the page size. Configured or input page size should be less than this max page size.

- ``page_size``: Defines the page size for the results returned by the ReST call. This value can not exceed what has been defined in 'pageMaxSize'.

- ``maintenance_mode_enabled``: Indicates if the VSD is configured in maintenance mode. This is typically enabled during the VSD upgrade window and when enabled the VSD would support only a subset of functionality.

- ``last_executed_migration_phase``: Indicates the last successfully executed phase of online schema migration. This value is set automatically upon execution of online schema migration scripts.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``gateway_probe_interval``: Gateway probe interval in seconds.

- ``gateway_probe_window``: Gateway probe window in seconds.

- ``gateway_rebalancing_interval``: Gateway rebalancing interval in seconds.

- ``max_failed_logins``: Maximum failed login attempts before the account is locked. 0 = not enforced (unlimited attempts). This is not enforced if LDAP is used for authorization

- ``max_response``: Defines maximum results returned by the REST call (allowed maximum value is 5000).

- ``rbac_enabled``: Enables the advanced granular permissions feature. This should not be enabled without prior discussion and agreement with the Nuage Product team, as this feature is only qualified for a limited set of use cases.

- ``accumulate_licenses_enabled``: Whether the various VRS license flavours be merged in one pool.

- ``vcin_load_balancer_ip``: If VCIN Active/Standby is enabled, this needs to be the load-balancer IP which sits in front of the Active and Standby VCIN nodes. The VRS will make its API calls to this load-balancer

- ``ddns_user_agent_email``: The email address to be used in the provider API as part of the IP Address update.

- ``web_cat_srv_url``: Indicates web categorization service url. Applicable only for web filtering type CLOUD_SERVICE

- ``web_filtering_type``: Indicates the type of web filtering. Possible values are CLOUD_SERVICE, VM

- ``fec_feedback_timer``: Forward Error Correction feedback timer in seconds. Possible values are 1, 2, 3, 4 or 5.

- ``secondary_as_number``: Autonomous System Number, used for secondary RT auto-generation.

- ``secondary_rt_lower_limit``: Secondary route target lower limit.

- ``secondary_rt_upper_limit``: Secondary route target upper limit.

- ``reflexive_aclicmp_timeout``: Defines the timeout in seconds for reflexive ACLs that are of type ICMP. Supported in Virtual Cloud Services (VCS) only.

- ``reflexive_acl_non_tcp_timeout``: Defines the timeout in seconds for reflexive ACLs that are not of type TCP.

- ``reflexive_acltcp_timeout``: Defines the timeout in seconds for reflexive ACLs that are of type TCP.

- ``denied_flow_collection_enabled``: When this option is selected, VSS will only store flows that are denied by security policy (implicit or explicit ACLs). This requires a valid VSS license and Flow Collection enabled.

- ``per_domain_vlan_id_enabled``: Determines whether per domain VLAN ID generation is required.

- ``service_id_upper_limit``: Service ID upper limit system wide value.

- ``netconf7x50_routing_policy_validation_enabled``: Indicates if Routing Policy Definition validation is enabled for Netconf 7x50.

- ``key_server_monitor_enabled``: Enable the keyserver debug monitor (ie. ksmon command)

- ``key_server_vsd_data_synchronization_interval``: KeyServer time in seconds between full resyncs of VSD data (just in case of missed events)

- ``keystore_password``: Password to access vsd key store for enabling es security.

- ``offset_customer_id``: Customer ID offset, this value has to be set before JBoss starts, following its starting, any change of value will be ignored. This is a system wide value.

- ``offset_service_id``: Service ID offset, this value has to be set before JBoss starts during the time of VSD installation, from thereon, any change of value will be ignored. This is a system wide value.

- ``threat_intelligence_enabled``: Enables IP based threat intelligence. This requires Flow Collection to be enabled.

- ``threat_prevention_feed_server_proxy_port``: Feed server download port for Threat Prevention VNF

- ``threat_prevention_server``: Specifies the Threat Prevention Management server location.

- ``threat_prevention_server_password``: Password to access Threat Prevention Server Password

- ``threat_prevention_server_proxy_port``: Destination TCP Port on the Proxy to connect to the Threat Prevention Management Server

- ``threat_prevention_server_username``: Username to accessThreat Prevention management Server.

- ``threat_prevention_syslog_proxy_port``: Syslog server port for Threat Prevention Service

- ``signature_update_through_cloud_enabled``: Indicates if Threat Prevention Signature updates are enabled through Cloud.

- ``virtual_firewall_rules_enabled``: Enable Virtual Firewall Rule creation and management. This will be available only with VSS license

- ``ejabberd_license_expiry_time``: Ejabberd License expiry date with time

- ``ejbca_nsg_certificate_profile``: EJBCA NSG Certificate Profile

- ``ejbca_nsg_end_entity_profile``: EJBCA NSG End Entity Profile

- ``ejbca_ocsp_responder_cn``: EJBCA OCSP Responder CommonName

- ``ejbca_ocsp_responder_uri``: EJBCA OCSP Responder URI

- ``ejbca_vsp_root_ca``: EJBCA VSP CA

- ``alarms_max_per_object``: Maximum alarms per object for example max distinct alarms for specific VM (min = 5, max =20)

- ``elastic_cluster_name``: Specifies the name of the Elastic Search Cluster.

- ``elastic_search_license_expiry_time``: Elastic Search License expiry date with time

- ``allow_enterprise_avatar_on_nsg``: When enabled, it allows Enterprise Avatar (image) to be populated on the NSGateway bootstrapping portal and blocked page notification.

- ``global_mac_address``: the MAC Address to use for those subnets that have the useGlobalMAC flag enabled.

- ``global_network_macro_groups_enabled``: Indicates if global network macro groups is enabled.  When enabled, all network macro groups created in Platform Configuration will be available to all enterprises.

- ``flow_collection_enabled``: Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires 'statisticsEnabled'.

- ``flow_drop_timeout``: Timeout in seconds after which the traffic will be dropped, if the flow limit exceeds.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``embedded_metadata_size``: This value limits the number of embedded Metadata objects returned in the API call. 

- ``imported_saa_s_applications_version``: Version of the current imported SaaS Application Type Master List.

- ``inactive_timeout``: Defines the inactive timeout for the client. If the client is inactive for more than the timeout value, server clears off all the cached information regarding the client. This value should be greater than the maximum timeout for the event processor. Value is in milliseconds.

- ``infrastructure_bgpas_number``: Autonomous System Number, Used for Infrastructure BGP PE_CE.

- ``enhanced_security_enabled``: Indicates if Enhanced Security is enabled for Routing Protocols.

- ``interface_id_lower_limit``: Lower limit for interface Id configured on SRLinux device.

- ``interface_id_upper_limit``: Upper limit for interface Id configured on SRLinux device.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_tunnel_type``: Default Domain Tunnel Type.

- ``google_maps_api_key``: Google Maps API Key used to display maps on Nuage UI applications

- ``loopback_intf_lower_limit`` (**Mandatory**): Lower limit of the domain Loopback Interface for gateways of type HWVTEP.

- ``loopback_intf_upper_limit`` (**Mandatory**): Upper limit of the domain Loopback Interface for gateways of type HWVTEP.

- ``post_processor_threads_count``: Post processor thread count.

- ``creation_date``: Time stamp when this object was created.

- ``srl_yang_validation_enabled``: Indicates if IPv4 Filter, IPv6 Filter, QoS Profile, BGP Neighbor Session and Routing Policy Blob validation is enabled for SRL.

- ``group_key_default_sek_generation_interval``: Group Key Encryption Profile Default SEK Generation Interval in seconds.

- ``group_key_default_sek_lifetime``: Group Key Encryption Profile Default SEK Lifetime in seconds.

- ``group_key_default_sek_payload_encryption_algorithm``: Group Key Encryption Profile Default Sek Payload Encryption Algorithm.

- ``group_key_default_sek_payload_signing_algorithm``: Group Key Encryption Profile Default Sek Payload Signing Algorithm.

- ``group_key_default_seed_generation_interval``: Group Key Encryption Profile Default Seed Generation Interval in seconds.

- ``group_key_default_seed_lifetime``: Group Key Encryption Profile Default Seed Lifetime in seconds.

- ``group_key_default_seed_payload_authentication_algorithm``: Group Key Encryption Profile Default Seed Payload Authentication Algorithm.

- ``group_key_default_seed_payload_encryption_algorithm``: Group Key Encryption Profile Default Seed Payload Encryption Algorithm.

- ``group_key_default_seed_payload_signing_algorithm``: Group Key Encryption Profile Default Seed Payload Signature Algorithm.

- ``group_key_default_traffic_authentication_algorithm``: Group Key Encryption Profile Default Traffic Authentication Algorithm.

- ``group_key_default_traffic_encryption_algorithm``: Group Key Encryption Profile Default Traffic Encryption Algorithm.

- ``group_key_default_traffic_encryption_key_lifetime``: Group Key Encryption Profile Default Traffic Encryption Key Lifetime in seconds.

- ``group_key_generation_interval_on_forced_re_key``: Time in seconds before new keys will be generated in the case of a forced re-key event

- ``group_key_generation_interval_on_revoke``: Time in seconds before new keys will be generated in the case of a revoke event

- ``group_key_minimum_sek_generation_interval``: Group Key Encryption Profile Minimum SEK Generation Interval in seconds.

- ``group_key_minimum_sek_lifetime``: Group Key Encryption Profile Minimum SEK Lifetime in seconds.

- ``group_key_minimum_seed_generation_interval``: Group Key Encryption Profile Default Seed Generation Interval in seconds.

- ``group_key_minimum_seed_lifetime``: Group Key Encryption Profile Default Seed Lifetime in seconds.

- ``group_key_minimum_traffic_encryption_key_lifetime``: Group Key Encryption Profile Minimum TEK Lifetime in seconds.

- ``es_security_enabled``: Indicates if VSD is communicating with elasticsearch over a secure channel using https.

- ``nsg_bootstrap_endpoint``: NSG Bootstrap Endpoint

- ``nsg_config_endpoint``: NSG Config Endpoint

- ``nsg_local_ui_url``: The bootstrapping UI URL on NSGateway. The URL will be redirected on NSG to its localhost so that the bootstrapping server on the NSGateway may handle the request.

- ``esi_id``: ESI ID offset

- ``csproot_authentication_method``: Authentication method for csproot when local authentication is not used for CSP organization

- ``stack_trace_enabled``: Set value to TRUE to enable stacktraces in the ReST calls.

- ``stateful_aclicmp_timeout``: Defines the timeout in seconds for stateful ACLs that are of type ICMP. Supported in Virtual Cloud Services (VCS) only.

- ``stateful_acl_non_tcp_timeout``: Defines the timeout in seconds for stateful ACLs that are not of type TCP.

- ``stateful_acltcp_timeout``: Defines the timeout in seconds for stateful ACLs that are of type TCP.

- ``static_wan_service_purge_time``: Timer in seconds for an unreacheable static WAN Services to be deleted.

- ``statistics_enabled``: This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

- ``stats_collector_address``: Specify the IP address(es) of the stats collector.

- ``stats_collector_port``: Specify the port number(s) of the stats collector.

- ``stats_collector_proto_buf_port``: Specify the protobuf port number(s) of the stats collector.

- ``stats_database_proxy``: The location of a public proxy to statistics database server in <FQDN>:<PORT> format.

- ``stats_max_data_points``: Specifies the maximum number of statistics data points to support.

- ``stats_min_duration``: The minimum duration for statistics to be displayed on UI in seconds. Default is 30 days in seconds (2592000 s).

- ``stats_number_of_data_points``: Specifies number of data points.

- ``stats_tsdb_server_address``: Specifies the Elastic Search server location.

- ``sticky_ecmp_idle_timeout``: Sticky ECMP Idle Timeout in seconds.

- ``attach_probe_to_ipsec_npm``: Flag to attach or remove system generated probes to system generated Network Performance Measurement (NPM) probes for IPSec.

- ``attach_probe_to_vxlannpm``: Flag to attach or remove system generated probes to system generated Network Performance Measurement (NPM) probes for VxLAN.

- ``subnet_resync_interval``: Following a resync on a subnet, another resync on the same subnet will be allowed based on the completion of the previous subnet resync plus the defined wait time in minutes.

- ``subnet_resync_outstanding_interval``: Outstanding subnet resync interval (in seconds). System wide value.

- ``customer_id_upper_limit``: Customer ID value upper limit. This is a system wide value.

- ``customer_key``: Customer key associated with the license.

- ``avatar_base_path``: Defines location, on VSD, where image files needs to be copied to. The Avatar Base URL should be configured to read the files from this location.

- ``avatar_base_url``: Defines the URL to read the avatar image files.

- ``event_log_cleanup_interval``: VSD event logs cleanup task execution interval in seconds.

- ``event_log_entry_max_age``: Maximum age in days for cleanup of the eventlog entries. On every periodic interval run, any eventlog entries older than this max age will be deleted.

- ``event_processor_interval``: Defines time interval in milliseconds when events collected for a client should be processed.

- ``event_processor_max_events_count``: Defines the maximum number of events to be collected in case of events burst.

- ``event_processor_timeout``: Defines the maximum time period in milliseconds for the ReST server to wait before sending the events from the system.

- ``owner``: Identifies the user that has created this object.

- ``two_factor_code_expiry``: Two Factor Code Expiration time in seconds for bootstrapping gateways. (min = 60, max = 604800)

- ``two_factor_code_length``: The number of characters in the generated Two Factor Code for bootstrapping gateways. (min = 4, max = 10)

- ``two_factor_code_seed_length``: Two Factor Seed length in bytes for generating the bootstrapping code. (min = 0, max = 255)

- ``explicit_acl_matching_enabled``: When this option is selected, VSS will only store allow/denied flows that matches explicit ingress/egress security ACL. This requires a valid VSS license and Flow Collection enabled.

- ``external_id``: External object ID. Used for integration with third party systems

- ``dynamic_wan_service_diff_time``: Timer in seconds for dynamic WAN Services to be considered as not being seen by a 7x50.

- ``syslog_destination_host``: Specifies the remote syslog destination host for VSD logs.

- ``syslog_destination_port``: Specified the remote syslog destination port for VSD.

- ``sysmon_cleanup_task_interval``: Sysmon cleanup task run interval in seconds.

- ``sysmon_node_presence_timeout``: Time interval in seconds at which sysmon messages are reported by controller.

- ``sysmon_probe_response_timeout``: Probe response timeout in seconds.

- ``sysmon_purge_interval``: Time interval in seconds at which sysmon objects are purged.

- ``system_avatar_data``: CSP Avatar Data

- ``system_avatar_type``: Avatar type - URL or BASE64

- ``system_blocked_page_text``: The text for blocked page html which gets displayed to the end-users when they reach a website that is blocked by Web Filtering ACL. User can possibly include very basic html tags like <p>, <ul> etc. in order to fomat the text displayed to the end-users.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

