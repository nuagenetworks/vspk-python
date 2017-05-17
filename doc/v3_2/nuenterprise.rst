.. _nuenterprise:

nuenterprise
===========================================

.. class:: nuenterprise.NUEnterprise(bambou.nurest_object.NUMetaRESTObject,):

Definition of the enterprise object. This is the top level object that represents an organization.


Attributes
----------


- ``ldap_authorization_enabled``: Read-only flag - indicates if LDAP is used for authorization for the enterprise. For detailed explanation, see definition in LDAPConfiguration class

- ``ldap_enabled``: Read-only flag - indicates if LDAP is used for authentication for the enterprise. For detailed explanation, see definition in LDAPConfiguration class

- ``dhcp_lease_interval``: DHCP Lease Interval (in hrs) to be used by an enterprise.

- ``name`` (**Mandatory**): The unique name of the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``receive_multi_cast_list_id``: Readonly Id of the auto generated receive multicast list associated with this enterprise profile

- ``send_multi_cast_list_id``: Readonly Id of the auto generated send multicast list associated with this enterprise profile

- ``description``: A description of the enterprise

- ``allow_advanced_qos_configuration``: Controls whether this enterprise has access to advanced QoS settings

- ``allow_gateway_management``: This flag indicates if the enterprise/organization can manage gateways. If yes then it can create gateway templates, instantiate them etc.

- ``allow_trusted_forwarding_class``: Controls whether QoS policies and templates created under this enterprise set the trusted flag to true

- ``allowed_forwarding_classes``: Allowed Forwarding Classes for this enterprise. Possible values are NONE, A, B, C, D, E, F, G, H, .

- ``floating_ips_quota``: Quota set for the number of floating IPs to be used by an enterprise.

- ``floating_ips_used``: Number of floating IPs used by the enterprise from the assigned floatingIPsQuota

- ``encryption_management_mode``: Readonly encryption management mode of the associated profile

- ``enterprise_profile_id``: Enterprise profile id for this enterprise

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

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
:ref:`nuratelimiter.NURateLimiter<nuratelimiter>`                                                                                                                ``rate_limiters`` 
:ref:`nugateway.NUGateway<nugateway>`                                                                                                                            ``gateways`` 
:ref:`nugatewaytemplate.NUGatewayTemplate<nugatewaytemplate>`                                                                                                    ``gateway_templates`` 
:ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`                                                                                                                   ``patnat_pools`` 
:ref:`nuldapconfiguration.NULDAPConfiguration<nuldapconfiguration>`                                                                                              ``ldap_configurations`` 
:ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`                                                                                                    ``redundancy_groups`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`numetadatatag.NUMetadataTag<numetadatatag>`                                                                                                                ``metadata_tags`` 
:ref:`nunetworkmacrogroup.NUNetworkMacroGroup<nunetworkmacrogroup>`                                                                                              ``network_macro_groups`` 
:ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`                                                                                                 ``key_server_monitors`` 
:ref:`nuegressqospolicy.NUEgressQOSPolicy<nuegressqospolicy>`                                                                                                    ``egress_qos_policies`` 
:ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`                                                                                  ``shared_network_resources`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nuinfrastructureportprofile.NUInfrastructurePortProfile<nuinfrastructureportprofile>`                                                                      ``infrastructure_port_profiles`` 
:ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`                                                                                              ``enterprise_networks`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nudomain.NUDomain<nudomain>`                                                                                                                               ``domains`` 
:ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`                                                                                                       ``domain_templates`` 
:ref:`nuapp.NUApp<nuapp>`                                                                                                                                        ``apps`` 
:ref:`nuapplicationservice.NUApplicationService<nuapplicationservice>`                                                                                           ``application_services`` 
:ref:`nugroup.NUGroup<nugroup>`                                                                                                                                  ``groups`` 
:ref:`nugroupkeyencryptionprofile.NUGroupKeyEncryptionProfile<nugroupkeyencryptionprofile>`                                                                      ``group_key_encryption_profiles`` 
:ref:`nudscpforwardingclasstable.NUDSCPForwardingClassTable<nudscpforwardingclasstable>`                                                                         ``dscp_forwarding_class_tables`` 
:ref:`nuuser.NUUser<nuuser>`                                                                                                                                     ``users`` 
:ref:`nunsgateway.NUNSGateway<nunsgateway>`                                                                                                                      ``ns_gateways`` 
:ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`                                                                                              ``ns_gateway_templates`` 
:ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`                                                                            ``ns_redundant_gateway_groups`` 
:ref:`numulticastlist.NUMultiCastList<numulticastlist>`                                                                                                          ``multi_cast_lists`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
:ref:`nuexternalappservice.NUExternalAppService<nuexternalappservice>`                                                                                           ``external_app_services`` 
:ref:`nuexternalservice.NUExternalService<nuexternalservice>`                                                                                                    ``external_services`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`

- :ref:`nume.NUMe<nume>`

