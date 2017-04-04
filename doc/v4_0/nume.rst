.. _nume:

nume
===========================================

.. class:: nume.NUMe(bambou.nurest_object.NUMetaRESTObject,):

Object that identifies the user functions


Attributes
----------


- ``password`` (**Mandatory**): User password stored as a hash (SHA-1 encrpted)

- ``last_name`` (**Mandatory**): Last name of the user

- ``last_updated_by``: ID of the user who last updated the object.

- ``first_name`` (**Mandatory**): First name of the user

- ``disabled``: Status of the user account; true=disabled, false=not disabled; default value = false

- ``elastic_search_address``: elastic search address

- ``flow_collection_enabled``: Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires "statisticsEnabled".

- ``email`` (**Mandatory**): Email address of the user

- ``enterprise_id``: Identifier of the enterprise.

- ``enterprise_name``: Name of the enterprise.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``mobile_number``: Mobile Number of the user

- ``role``: Role of the user.

- ``user_name`` (**Mandatory**): Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).

- ``statistics_enabled``: This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

- ``avatar_data``: URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

- ``avatar_type``: Avatar type.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nul2domain.NUL2Domain<nul2domain>`                                                                                                                         ``l2_domains`` 
:ref:`nuvcentereamconfig.NUVCenterEAMConfig<nuvcentereamconfig>`                                                                                                 ``vcenter_eam_configs`` 
:ref:`nuratelimiter.NURateLimiter<nuratelimiter>`                                                                                                                ``rate_limiters`` 
:ref:`nugateway.NUGateway<nugateway>`                                                                                                                            ``gateways`` 
:ref:`nugatewaytemplate.NUGatewayTemplate<nugatewaytemplate>`                                                                                                    ``gateway_templates`` 
:ref:`nupatmapper.NUPATMapper<nupatmapper>`                                                                                                                      ``pat_mappers`` 
:ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`                                                                                                                   ``patnat_pools`` 
:ref:`nutca.NUTCA<nutca>`                                                                                                                                        ``tcas`` 
:ref:`nuvcenter.NUVCenter<nuvcenter>`                                                                                                                            ``vcenters`` 
:ref:`nuvcenterhypervisor.NUVCenterHypervisor<nuvcenterhypervisor>`                                                                                              ``vcenter_hypervisors`` 
:ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`                                                                                              ``redirection_targets`` 
:ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`                                                                                                    ``redundancy_groups`` 
:ref:`nuperformancemonitor.NUPerformanceMonitor<nuperformancemonitor>`                                                                                           ``performance_monitors`` 
:ref:`nucertificate.NUCertificate<nucertificate>`                                                                                                                ``certificates`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`numetadatatag.NUMetadataTag<numetadatatag>`                                                                                                                ``metadata_tags`` 
:ref:`nunetworklayout.NUNetworkLayout<nunetworklayout>`                                                                                                          ``network_layouts`` 
:ref:`nukeyservermember.NUKeyServerMember<nukeyservermember>`                                                                                                    ``key_server_members`` 
:ref:`nuzfbautoassignment.NUZFBAutoAssignment<nuzfbautoassignment>`                                                                                              ``zfb_auto_assignments`` 
:ref:`nuzfbrequest.NUZFBRequest<nuzfbrequest>`                                                                                                                   ``zfb_requests`` 
:ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`                                                                                                                ``bgp_neighbors`` 
:ref:`nubgpprofile.NUBGPProfile<nubgpprofile>`                                                                                                                   ``bgp_profiles`` 
:ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`                                                                               ``egress_acl_entry_templates`` 
:ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`                                                                                              ``egress_acl_templates`` 
:ref:`nudomainfipacltemplate.NUDomainFIPAclTemplate<nudomainfipacltemplate>`                                                                                     ``domain_fip_acl_templates`` 
:ref:`nufloatingipacltemplate.NUFloatingIPACLTemplate<nufloatingipacltemplate>`                                                                                  ``floating_ipacl_templates`` 
:ref:`nuegressqospolicy.NUEgressQOSPolicy<nuegressqospolicy>`                                                                                                    ``egress_qos_policies`` 
:ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`                                                                                  ``shared_network_resources`` 
:ref:`nulicense.NULicense<nulicense>`                                                                                                                            ``licenses`` 
:ref:`nulicensestatus.NULicenseStatus<nulicensestatus>`                                                                                                          ``license_status`` 
:ref:`numirrordestination.NUMirrorDestination<numirrordestination>`                                                                                              ``mirror_destinations`` 
:ref:`nusiteinfo.NUSiteInfo<nusiteinfo>`                                                                                                                         ``site_infos`` 
:ref:`nufloatingip.NUFloatingIp<nufloatingip>`                                                                                                                   ``floating_ips`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nuvminterface.NUVMInterface<nuvminterface>`                                                                                                                ``vm_interfaces`` 
:ref:`nucloudmgmtsystem.NUCloudMgmtSystem<nucloudmgmtsystem>`                                                                                                    ``cloud_mgmt_systems`` 
:ref:`nuunderlay.NUUnderlay<nuunderlay>`                                                                                                                         ``underlays`` 
:ref:`nuinfrastructureaccessprofile.NUInfrastructureAccessProfile<nuinfrastructureaccessprofile>`                                                                ``infrastructure_access_profiles`` 
:ref:`nuinfrastructuregatewayprofile.NUInfrastructureGatewayProfile<nuinfrastructuregatewayprofile>`                                                             ``infrastructure_gateway_profiles`` 
:ref:`nuinfrastructurevscprofile.NUInfrastructureVscProfile<nuinfrastructurevscprofile>`                                                                         ``infrastructure_vsc_profiles`` 
:ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`                                                                            ``ingress_acl_entry_templates`` 
:ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`                                                                                           ``ingress_acl_templates`` 
:ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`                                                                   ``ingress_adv_fwd_entry_templates`` 
:ref:`nuenterprise.NUEnterprise<nuenterprise>`                                                                                                                   ``enterprises`` 
:ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`                                                                                              ``enterprise_profiles`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`                                                                                                                ``policy_groups`` 
:ref:`nudomain.NUDomain<nudomain>`                                                                                                                               ``domains`` 
:ref:`nuzone.NUZone<nuzone>`                                                                                                                                     ``zones`` 
:ref:`nucontainer.NUContainer<nucontainer>`                                                                                                                      ``containers`` 
:ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`                                                                                           ``container_interfaces`` 
:ref:`nuhostinterface.NUHostInterface<nuhostinterface>`                                                                                                          ``host_interfaces`` 
:ref:`nuroutingpolicy.NURoutingPolicy<nuroutingpolicy>`                                                                                                          ``routing_policies`` 
:ref:`nuuplinkrd.NUUplinkRD<nuuplinkrd>`                                                                                                                         ``uplink_rds`` 
:ref:`nuapplicationservice.NUApplicationService<nuapplicationservice>`                                                                                           ``application_services`` 
:ref:`nuvcentervrsconfig.NUVCenterVRSConfig<nuvcentervrsconfig>`                                                                                                 ``vcenter_vrs_configs`` 
:ref:`nuuser.NUUser<nuuser>`                                                                                                                                     ``users`` 
:ref:`nunsgateway.NUNSGateway<nunsgateway>`                                                                                                                      ``ns_gateways`` 
:ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`                                                                                              ``ns_gateway_templates`` 
:ref:`nunsggroup.NUNSGGroup<nunsggroup>`                                                                                                                         ``nsg_groups`` 
:ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`                                                                            ``ns_redundant_gateway_groups`` 
:ref:`nuvsp.NUVSP<nuvsp>`                                                                                                                                        ``vsps`` 
:ref:`nustaticroute.NUStaticRoute<nustaticroute>`                                                                                                                ``static_routes`` 
:ref:`nustatscollectorinfo.NUStatsCollectorInfo<nustatscollectorinfo>`                                                                                           ``stats_collector_infos`` 
:ref:`nusubnet.NUSubnet<nusubnet>`                                                                                                                               ``subnets`` 
:ref:`nuducgroup.NUDUCGroup<nuducgroup>`                                                                                                                         ``duc_groups`` 
:ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`                                                                                        ``multi_cast_channel_maps`` 
:ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`                                                                                  ``auto_discovered_gateways`` 
:ref:`nuexternalappservice.NUExternalAppService<nuexternalappservice>`                                                                                           ``external_app_services`` 
:ref:`nuexternalservice.NUExternalService<nuexternalservice>`                                                                                                    ``external_services`` 
:ref:`nusystemconfig.NUSystemConfig<nusystemconfig>`                                                                                                             ``system_configs`` 
================================================================================================================================================               ==========================================================================================


