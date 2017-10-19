.. _nuenterprise:

nuenterprise
===========================================

.. class:: nuenterprise.NUEnterprise(bambou.nurest_object.NUMetaRESTObject,):

Definition of the enterprise object. This is the top level object that represents an enterprise.


Attributes
----------


- ``ldap_authorization_enabled``: Read-only flag - indicates if LDAP is used for authorization for the enterprise. For detailed explanation, see definition in LDAPConfiguration class

- ``ldap_enabled``: Read-only flag - indicates if LDAP is used for authentication for the enterprise. For detailed explanation, see definition in LDAPConfiguration class

- ``bgp_enabled``: Read only flag to display if BGP is enabled for this enterprise

- ``dhcp_lease_interval``: DHCP Lease Interval (in hrs) to be used by an enterprise.

- ``vnf_management_enabled``: Read only flag to display if VNF management is enabled for this enterprise

- ``name`` (**Mandatory**): The unique name of the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``receive_multi_cast_list_id``: Readonly Id of the auto generated receive multicast list associated with this enterprise profile

- ``send_multi_cast_list_id``: Readonly Id of the auto generated send multicast list associated with this enterprise profile

- ``description``: A description of the enterprise

- ``shared_enterprise``: This flag indicates whether this is a Shared Infrastructure Enterprise or not. Its a read-only attribute and it cannot be set by anybody.

- ``dictionary_version``: L7 Application Type version

- ``allow_advanced_qos_configuration``: Controls whether this enterprise has access to advanced QoS settings

- ``allow_gateway_management``: This flag indicates if the enterprise/organization can manage gateways. If yes then it can create gateway templates, instantiate them etc.

- ``allow_trusted_forwarding_class``: Controls whether QoS policies and templates created under this enterprise set the trusted flag to true

- ``allowed_forwarding_classes``: Allowed Forwarding Classes for this enterprise. Possible values are NONE, A, B, C, D, E, F, G, H, .

- ``floating_ips_quota``: Quota set for the number of floating IPs to be used by an enterprise.

- ``floating_ips_used``: Number of floating IPs used by the enterprise from the assigned floatingIPsQuota

- ``enable_application_performance_management``: This flag indicates if the DPI can be enabled for this enterpriseenterprise/organization.

- ``encryption_management_mode``: Readonly encryption management mode of the associated profile

- ``enterprise_profile_id``: Enterprise profile id for this enterprise

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``local_as``: Local autonomous system for the enterprise

- ``associated_enterprise_security_id``: Readonly Id of the associated group key encryption profile

- ``associated_group_key_encryption_profile_id``: Readonly Id of the associated group key encryption profile

- ``associated_key_server_monitor_id``: Readonly Id of the associated keyserver monitor

- ``customer_id``: CustomerID that is used by VSC to identify this enterprise. This is a read only attribute.

- ``avatar_data``: URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

- ``avatar_type``: Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nul2domain.NUL2Domain<nul2domain>`                                                                                                                         ``l2_domains`` 
:ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`                                                                                                 ``l2_domain_templates`` 
:ref:`nul4service.NUL4Service<nul4service>`                                                                                                                      ``l4_services`` 
:ref:`nul4servicegroup.NUL4ServiceGroup<nul4servicegroup>`                                                                                                       ``l4_service_groups`` 
:ref:`nul7applicationsignature.NUL7applicationsignature<nul7applicationsignature>`                                                                               ``l7applicationsignatures`` 
:ref:`nucaptiveportalprofile.NUCaptivePortalProfile<nucaptiveportalprofile>`                                                                                     ``captive_portal_profiles`` 
:ref:`nuratelimiter.NURateLimiter<nuratelimiter>`                                                                                                                ``rate_limiters`` 
:ref:`nugateway.NUGateway<nugateway>`                                                                                                                            ``gateways`` 
:ref:`nugatewaytemplate.NUGatewayTemplate<nugatewaytemplate>`                                                                                                    ``gateway_templates`` 
:ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`                                                                                                                   ``patnat_pools`` 
:ref:`nuldapconfiguration.NULDAPConfiguration<nuldapconfiguration>`                                                                                              ``ldap_configurations`` 
:ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`                                                                                                    ``redundancy_groups`` 
:ref:`nuperformancemonitor.NUPerformanceMonitor<nuperformancemonitor>`                                                                                           ``performance_monitors`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nunetworkmacrogroup.NUNetworkMacroGroup<nunetworkmacrogroup>`                                                                                              ``network_macro_groups`` 
:ref:`nunetworkperformancemeasurement.NUNetworkPerformanceMeasurement<nunetworkperformancemeasurement>`                                                          ``network_performance_measurements`` 
:ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`                                                                                                 ``key_server_monitors`` 
:ref:`nuzfbrequest.NUZFBRequest<nuzfbrequest>`                                                                                                                   ``zfb_requests`` 
:ref:`nubgpprofile.NUBGPProfile<nubgpprofile>`                                                                                                                   ``bgp_profiles`` 
:ref:`nuegressqospolicy.NUEgressQOSPolicy<nuegressqospolicy>`                                                                                                    ``egress_qos_policies`` 
:ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`                                                                                  ``shared_network_resources`` 
:ref:`nufirewallacl.NUFirewallAcl<nufirewallacl>`                                                                                                                ``firewall_acls`` 
:ref:`nufirewallrule.NUFirewallRule<nufirewallrule>`                                                                                                             ``firewall_rules`` 
:ref:`nuikecertificate.NUIKECertificate<nuikecertificate>`                                                                                                       ``ike_certificates`` 
:ref:`nuikeencryptionprofile.NUIKEEncryptionprofile<nuikeencryptionprofile>`                                                                                     ``ike_encryptionprofiles`` 
:ref:`nuikegateway.NUIKEGateway<nuikegateway>`                                                                                                                   ``ike_gateways`` 
:ref:`nuikegatewayprofile.NUIKEGatewayProfile<nuikegatewayprofile>`                                                                                              ``ike_gateway_profiles`` 
:ref:`nuikepsk.NUIKEPSK<nuikepsk>`                                                                                                                               ``ikepsks`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuallalarm.NUAllAlarm<nuallalarm>`                                                                                                                         ``all_alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nuvnf.NUVNF<nuvnf>`                                                                                                                                        ``vnfs`` 
:ref:`nuvnfmetadata.NUVNFMetadata<nuvnfmetadata>`                                                                                                                ``vnf_metadatas`` 
:ref:`nuingressqospolicy.NUIngressQOSPolicy<nuingressqospolicy>`                                                                                                 ``ingress_qos_policies`` 
:ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`                                                                                              ``enterprise_networks`` 
:ref:`nuenterprisesecurity.NUEnterpriseSecurity<nuenterprisesecurity>`                                                                                           ``enterprise_securities`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nupolicyobjectgroup.NUPolicyObjectGroup<nupolicyobjectgroup>`                                                                                              ``policy_object_groups`` 
:ref:`nudomain.NUDomain<nudomain>`                                                                                                                               ``domains`` 
:ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`                                                                                                       ``domain_templates`` 
:ref:`nucontainer.NUContainer<nucontainer>`                                                                                                                      ``containers`` 
:ref:`nucosremarkingpolicytable.NUCOSRemarkingPolicyTable<nucosremarkingpolicytable>`                                                                            ``cos_remarking_policy_tables`` 
:ref:`nuroutingpolicy.NURoutingPolicy<nuroutingpolicy>`                                                                                                          ``routing_policies`` 
:ref:`nuapplication.NUApplication<nuapplication>`                                                                                                                ``applications`` 
:ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`                                                 ``applicationperformancemanagements`` 
:ref:`nugroup.NUGroup<nugroup>`                                                                                                                                  ``groups`` 
:ref:`nugroupkeyencryptionprofile.NUGroupKeyEncryptionProfile<nugroupkeyencryptionprofile>`                                                                      ``group_key_encryption_profiles`` 
:ref:`nutrunk.NUTrunk<nutrunk>`                                                                                                                                  ``trunks`` 
:ref:`nudscpforwardingclasstable.NUDSCPForwardingClassTable<nudscpforwardingclasstable>`                                                                         ``dscp_forwarding_class_tables`` 
:ref:`nudscpremarkingpolicytable.NUDSCPRemarkingPolicyTable<nudscpremarkingpolicytable>`                                                                         ``dscp_remarking_policy_tables`` 
:ref:`nuuser.NUUser<nuuser>`                                                                                                                                     ``users`` 
:ref:`nunsgateway.NUNSGateway<nunsgateway>`                                                                                                                      ``ns_gateways`` 
:ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`                                                                                              ``ns_gateway_templates`` 
:ref:`nunsggroup.NUNSGGroup<nunsggroup>`                                                                                                                         ``nsg_groups`` 
:ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`                                                                            ``ns_redundant_gateway_groups`` 
:ref:`nupublicnetworkmacro.NUPublicNetworkMacro<nupublicnetworkmacro>`                                                                                           ``public_network_macros`` 
:ref:`numulticastlist.NUMultiCastList<numulticastlist>`                                                                                                          ``multi_cast_lists`` 
:ref:`nuavatar.NUAvatar<nuavatar>`                                                                                                                               ``avatars`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`

- :ref:`nume.NUMe<nume>`

