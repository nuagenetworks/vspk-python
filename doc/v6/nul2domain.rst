.. _nul2domain:

nul2domain
===========================================

.. class:: nul2domain.NUL2Domain(bambou.nurest_object.NUMetaRESTObject,):

This is the definition of a l2 domain associated with a Enterprise.


Attributes
----------


- ``l2_encap_type``: Default Domain Tunnel Type

- ``dhcp_managed``: decides whether L2Domain / L2Domain template DHCP is managed by VSD

- ``dpi``: determines whether or not Deep packet inspection is enabled

- ``ip_type``: IPv4, DUALSTACK or IPv6

- ``ipv6_address``: IPV6 address of the route - Optional

- ``ipv6_gateway``: The IPv6 address of the gateway of this subnet

- ``vxlanecmp_enabled``: Determines whether VXLAN-ECMP are enabled on this domain.

- ``maintenance_mode``: maintenanceMode is an enum that indicates if the L2Domain is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .

- ``name`` (**Mandatory**): Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``gateway``: The IP address of the gateway of this l2 domain

- ``gateway_mac_address``: The MAC address of the Gateway.

- ``wbx_disable_mac_move``: Disable MAC Move on WBX nodes.

- ``address``: Network address of the L2Domain / L2Domain template defined. 

- ``template_id``: The ID of the L2 Domain template that this L2 Domain object was derived from

- ``service_id``: The service ID used by the VSCs to identify this subnet

- ``description``: A description field provided by the user that identifies the L2Domain / L2Domain template.

- ``netmask``: Netmask of the L2Domain / L2Domain template defined

- ``threat_intelligence_enabled``: Determines whether or not threat intelligence is enabled

- ``flow_collection_enabled``: Determines whether or not flow collection is enabled.

- ``flow_count``: Maximum number of data flows allowed for a VPort.

- ``flow_limit_enabled``: Indicates if flow limit is enabled on this Domain. Possible values are ENABLED or DISABLED.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``vn_id``: Current network's globally unique VXLAN network identifier

- ``enable_dhcpv4``: This read-only value indicates whether IPv4 DHCP is enabled or not. This is applicable in case the L2 Domain is DUALSTACK or IPv4

- ``enable_dhcpv6``: This read-only value indicates whether IPv6 DHCP is enabled or not. This is applicable in case the L2 Domain is DUALSTACK or IPv6

- ``encryption``: Determines whether IPSEC is enabled Possible values are ENABLED, DISABLED, .

- ``ingress_replication_enabled``: Enables ingress replication for the VNI.

- ``interface_id``: SRLinux Interface ID for L2Domain configuration

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``entity_state``: Intermediate State of L2 Domain.

- ``policy_change_status``: None

- ``color``: The color encoded with a traffic engineering constraint such as minimum latency, hops, maximum bandwidth, etc. This is used for NFIX(Network Function Interconnect). Color is applicable only when the selected l2EncapType is MPLSoUDP. Valid range is 1 - 4294967295. 0 for other Tunnel Types.

- ``route_distinguisher``: Route distinguisher that is used by the BGP-EVPN protocol in VSC. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

- ``route_target``: Route target that is used by the BGP-EVPN protocol in VSC. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

- ``routed_vpls_enabled``: Determines whether routed VPLS services are enabled on this domain.

- ``uplink_preference``: Indicates the preferencial path selection for network traffic in this domain - Default is Primary 1 and Secondary 2. Possible values are PRIMARY_SECONDARY, SECONDARY_PRIMARY, PRIMARY, SECONDARY, SYMMETRIC, .

- ``creation_date``: Time stamp when this object was created.

- ``use_global_mac``: Enable this flag to use system configured globalMACAddress as the gateway mac address for managed l2 domains

- ``associated_multicast_channel_map_id``: The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED

- ``associated_shared_network_resource_id``: The ID of the L2 Domain  that this L2 Domain object is pointing to

- ``associated_underlay_id``: The ID of the Underlay entity to which this L2 Domain is associated.

- ``stateful_mode``: This value indicates whether reflexive ACL is enabled or not for the L2Domain. It is 'REFLEXIVE' if enabled, or 'STATEFUL' if reflexive is disabled.

- ``stretched``: Indicates whether this domain is streched,if so remote VM resolutions will be allowed

- ``dual_stack_dynamic_ip_allocation``: This read-only value indicates whether dynamic address allocation is enabled or not at template. This will be applicable when L2 Domain is managed and in dual stack mode

- ``multicast``: Indicates multicast policy on L2Domain.

- ``customer_id``: CustomerID that is used by NETCONF MANAGER to identify this enterprise. This can be configured by root user.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nugateway.NUGateway<nugateway>`                                                                                                                            ``gateways`` 
:ref:`nutca.NUTCA<nutca>`                                                                                                                                        ``tcas`` 
:ref:`nuaddressrange.NUAddressRange<nuaddressrange>`                                                                                                             ``address_ranges`` 
:ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`                                                                                              ``redirection_targets`` 
:ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`                                                                                                    ``redundancy_groups`` 
:ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`                                                                                              ``deployment_failures`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nunetworkperformancebinding.NUNetworkPerformanceBinding<nunetworkperformancebinding>`                                                                      ``network_performance_bindings`` 
:ref:`nupgexpression.NUPGExpression<nupgexpression>`                                                                                                             ``pg_expressions`` 
:ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`                                                                               ``egress_acl_entry_templates`` 
:ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`                                                                                              ``egress_acl_templates`` 
:ref:`nuegressadvfwdtemplate.NUEgressAdvFwdTemplate<nuegressadvfwdtemplate>`                                                                                     ``egress_adv_fwd_templates`` 
:ref:`nuegressauditaclentrytemplate.NUEgressAuditACLEntryTemplate<nuegressauditaclentrytemplate>`                                                                ``egress_audit_acl_entry_templates`` 
:ref:`nuegressauditacltemplate.NUEgressAuditACLTemplate<nuegressauditacltemplate>`                                                                               ``egress_audit_acl_templates`` 
:ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`                                                                                                                   ``dhcp_options`` 
:ref:`nudhcpv6option.NUDHCPv6Option<nudhcpv6option>`                                                                                                             ``dhcpv6_options`` 
:ref:`numirrordestinationgroup.NUMirrorDestinationGroup<numirrordestinationgroup>`                                                                               ``mirror_destination_groups`` 
:ref:`nuvirtualfirewallpolicy.NUVirtualFirewallPolicy<nuvirtualfirewallpolicy>`                                                                                  ``virtual_firewall_policies`` 
:ref:`nuvirtualfirewallrule.NUVirtualFirewallRule<nuvirtualfirewallrule>`                                                                                        ``virtual_firewall_rules`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nuvminterface.NUVMInterface<nuvminterface>`                                                                                                                ``vm_interfaces`` 
:ref:`nuvmipreservation.NUVMIPReservation<nuvmipreservation>`                                                                                                    ``vmip_reservations`` 
:ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`                                                                            ``ingress_acl_entry_templates`` 
:ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`                                                                                           ``ingress_acl_templates`` 
:ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`                                                                                  ``ingress_adv_fwd_templates`` 
:ref:`nuingressauditaclentrytemplate.NUIngressAuditACLEntryTemplate<nuingressauditaclentrytemplate>`                                                             ``ingress_audit_acl_entry_templates`` 
:ref:`nuingressauditacltemplate.NUIngressAuditACLTemplate<nuingressauditacltemplate>`                                                                            ``ingress_audit_acl_templates`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`                                                                                                                ``policy_groups`` 
:ref:`nucontainer.NUContainer<nucontainer>`                                                                                                                      ``containers`` 
:ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`                                                                                           ``container_interfaces`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nuhostinterface.NUHostInterface<nuhostinterface>`                                                                                                          ``host_interfaces`` 
:ref:`nuuplinkrd.NUUplinkRD<nuuplinkrd>`                                                                                                                         ``uplink_rds`` 
:ref:`nuvpnconnection.NUVPNConnection<nuvpnconnection>`                                                                                                          ``vpn_connections`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
:ref:`nuapplication.NUApplication<nuapplication>`                                                                                                                ``applications`` 
:ref:`nuapplicationperformancemanagementbinding.NUApplicationperformancemanagementbinding<nuapplicationperformancemanagementbinding>`                            ``applicationperformancemanagementbindings`` 
:ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`                                                                                                    ``bridge_interfaces`` 
:ref:`nugroup.NUGroup<nugroup>`                                                                                                                                  ``groups`` 
:ref:`nuproxyarpfilter.NUProxyARPFilter<nuproxyarpfilter>`                                                                                                       ``proxy_arp_filters`` 
:ref:`nunsgatewaysummary.NUNSGatewaySummary<nunsgatewaysummary>`                                                                                                 ``ns_gateway_summaries`` 
:ref:`nustaticroute.NUStaticRoute<nustaticroute>`                                                                                                                ``static_routes`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`                                                                                                 ``statistics_policies`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
:ref:`nuoverlaymirrordestination.NUOverlayMirrorDestination<nuoverlaymirrordestination>`                                                                         ``overlay_mirror_destinations`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuethernetsegmentgwgroup.NUEthernetSegmentGWGroup<nuethernetsegmentgwgroup>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

