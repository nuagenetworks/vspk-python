.. _nume:

nume
===========================================

.. class:: nume.NUMe(bambou.nurest_object.NUMetaRESTObject,):

Object that identifies the user functions


Attributes
----------


- ``aar_flow_stats_interval``: AAR flow stats frequency

- ``aar_probe_stats_interval``: AAR Probe stats frequency

- ``api_key_expiry``: The time in epoch milliseconds when the API key will expire.

- ``vss_stats_interval``: VSS flow stats frequency

- ``password`` (**Mandatory**): User password in clear text. Password cannot be a single character asterisk (*)

- ``last_name`` (**Mandatory**): Last name of the user

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``first_name`` (**Mandatory**): First name of the user

- ``disabled``: Status of the user account; true=disabled, false=not disabled; default value = false

- ``elastic_search_address``: elastic search address

- ``flow_collection_enabled``: Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires 'statisticsEnabled'.

- ``email`` (**Mandatory**): Email address of the user

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise_id``: Identifier of the enterprise.

- ``enterprise_name``: Name of the enterprise.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``mobile_number``: Mobile Number of the user

- ``role``: Role of the user.

- ``creation_date``: Time stamp when this object was created.

- ``user_name`` (**Mandatory**): Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).

- ``statistics_enabled``: This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

- ``avatar_data``: URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

- ``avatar_type``: Avatar type.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nul2domain.NUL2Domain<nul2domain>`                                                                                                                         ``l2_domains`` 
:ref:`nul4service.NUL4Service<nul4service>`                                                                                                                      ``l4_services`` 
:ref:`nul4servicegroup.NUL4ServiceGroup<nul4servicegroup>`                                                                                                       ``l4_service_groups`` 
:ref:`nul7applicationsignature.NUL7applicationsignature<nul7applicationsignature>`                                                                               ``l7applicationsignatures`` 
:ref:`nusaasapplicationtype.NUSaaSApplicationType<nusaasapplicationtype>`                                                                                        ``saa_s_application_types`` 
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
:ref:`nuremotevrsinfo.NURemoteVrsInfo<nuremotevrsinfo>`                                                                                                          ``remote_vrs_infos`` 
:ref:`nuperformancemonitor.NUPerformanceMonitor<nuperformancemonitor>`                                                                                           ``performance_monitors`` 
:ref:`nucertificate.NUCertificate<nucertificate>`                                                                                                                ``certificates`` 
:ref:`nutestdefinition.NUTestDefinition<nutestdefinition>`                                                                                                       ``test_definitions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nunetconfglobalconfiguration.NUNetconfGlobalConfiguration<nunetconfglobalconfiguration>`                                                                   ``netconf_global_configurations`` 
:ref:`nunetconfprofile.NUNetconfProfile<nunetconfprofile>`                                                                                                       ``netconf_profiles`` 
:ref:`nunetworklayout.NUNetworkLayout<nunetworklayout>`                                                                                                          ``network_layouts`` 
:ref:`nunetworkperformancemeasurement.NUNetworkPerformanceMeasurement<nunetworkperformancemeasurement>`                                                          ``network_performance_measurements`` 
:ref:`nukeyservermember.NUKeyServerMember<nukeyservermember>`                                                                                                    ``key_server_members`` 
:ref:`nuzfbautoassignment.NUZFBAutoAssignment<nuzfbautoassignment>`                                                                                              ``zfb_auto_assignments`` 
:ref:`nuzfbrequest.NUZFBRequest<nuzfbrequest>`                                                                                                                   ``zfb_requests`` 
:ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`                                                                                                                ``bgp_neighbors`` 
:ref:`nubgpprofile.NUBGPProfile<nubgpprofile>`                                                                                                                   ``bgp_profiles`` 
:ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`                                                                               ``egress_acl_entry_templates`` 
:ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`                                                                                              ``egress_acl_templates`` 
:ref:`nuegressadvfwdentrytemplate.NUEgressAdvFwdEntryTemplate<nuegressadvfwdentrytemplate>`                                                                      ``egress_adv_fwd_entry_templates`` 
:ref:`nudomainfipacltemplate.NUDomainFIPAclTemplate<nudomainfipacltemplate>`                                                                                     ``domain_fip_acl_templates`` 
:ref:`nuegressqospolicy.NUEgressQOSPolicy<nuegressqospolicy>`                                                                                                    ``egress_qos_policies`` 
:ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`                                                                                  ``shared_network_resources`` 
:ref:`nulicense.NULicense<nulicense>`                                                                                                                            ``licenses`` 
:ref:`nulicensestatus.NULicenseStatus<nulicensestatus>`                                                                                                          ``license_status`` 
:ref:`numirrordestination.NUMirrorDestination<numirrordestination>`                                                                                              ``mirror_destinations`` 
:ref:`nuvirtualfirewallpolicy.NUVirtualFirewallPolicy<nuvirtualfirewallpolicy>`                                                                                  ``virtual_firewall_policies`` 
:ref:`nuvirtualfirewallrule.NUVirtualFirewallRule<nuvirtualfirewallrule>`                                                                                        ``virtual_firewall_rules`` 
:ref:`nusiteinfo.NUSiteInfo<nusiteinfo>`                                                                                                                         ``site_infos`` 
:ref:`nuallgateway.NUAllGateway<nuallgateway>`                                                                                                                   ``all_gateways`` 
:ref:`nuallredundancygroup.NUAllRedundancyGroup<nuallredundancygroup>`                                                                                           ``all_redundancy_groups`` 
:ref:`nufloatingip.NUFloatingIp<nufloatingip>`                                                                                                                   ``floating_ips`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nuvminterface.NUVMInterface<nuvminterface>`                                                                                                                ``vm_interfaces`` 
:ref:`nucloudmgmtsystem.NUCloudMgmtSystem<nucloudmgmtsystem>`                                                                                                    ``cloud_mgmt_systems`` 
:ref:`nuunderlay.NUUnderlay<nuunderlay>`                                                                                                                         ``underlays`` 
:ref:`nuvnfcatalog.NUVNFCatalog<nuvnfcatalog>`                                                                                                                   ``vnf_catalogs`` 
:ref:`nuvnfmetadata.NUVNFMetadata<nuvnfmetadata>`                                                                                                                ``vnf_metadatas`` 
:ref:`nuinfrastructureaccessprofile.NUInfrastructureAccessProfile<nuinfrastructureaccessprofile>`                                                                ``infrastructure_access_profiles`` 
:ref:`nuinfrastructureevdfprofile.NUInfrastructureEVDFProfile<nuinfrastructureevdfprofile>`                                                                      ``infrastructure_evdf_profiles`` 
:ref:`nuinfrastructuregatewayprofile.NUInfrastructureGatewayProfile<nuinfrastructuregatewayprofile>`                                                             ``infrastructure_gateway_profiles`` 
:ref:`nuinfrastructurevscprofile.NUInfrastructureVscProfile<nuinfrastructurevscprofile>`                                                                         ``infrastructure_vsc_profiles`` 
:ref:`nuvnfthresholdpolicy.NUVNFThresholdPolicy<nuvnfthresholdpolicy>`                                                                                           ``vnf_threshold_policies`` 
:ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`                                                                            ``ingress_acl_entry_templates`` 
:ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`                                                                                           ``ingress_acl_templates`` 
:ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`                                                                   ``ingress_adv_fwd_entry_templates`` 
:ref:`nuingressqospolicy.NUIngressQOSPolicy<nuingressqospolicy>`                                                                                                 ``ingress_qos_policies`` 
:ref:`nugnmiprofile.NUGNMIProfile<nugnmiprofile>`                                                                                                                ``gnmi_profiles`` 
:ref:`nuenterprise.NUEnterprise<nuenterprise>`                                                                                                                   ``enterprises`` 
:ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`                                                                                              ``enterprise_profiles`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nurole.NURole<nurole>`                                                                                                                                     ``roles`` 
:ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`                                                                                                                ``policy_groups`` 
:ref:`nupolicyobjectgroup.NUPolicyObjectGroup<nupolicyobjectgroup>`                                                                                              ``policy_object_groups`` 
:ref:`nudomain.NUDomain<nudomain>`                                                                                                                               ``domains`` 
:ref:`nucommand.NUCommand<nucommand>`                                                                                                                            ``commands`` 
:ref:`nuzone.NUZone<nuzone>`                                                                                                                                     ``zones`` 
:ref:`nucontainer.NUContainer<nucontainer>`                                                                                                                      ``containers`` 
:ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`                                                                                           ``container_interfaces`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nuqospolicer.NUQosPolicer<nuqospolicer>`                                                                                                                   ``qos_policers`` 
:ref:`nucosremarkingpolicytable.NUCOSRemarkingPolicyTable<nucosremarkingpolicytable>`                                                                            ``cos_remarking_policy_tables`` 
:ref:`nuhostinterface.NUHostInterface<nuhostinterface>`                                                                                                          ``host_interfaces`` 
:ref:`nuroutingpolicy.NURoutingPolicy<nuroutingpolicy>`                                                                                                          ``routing_policies`` 
:ref:`nuuplinkrd.NUUplinkRD<nuuplinkrd>`                                                                                                                         ``uplink_rds`` 
:ref:`nuapplication.NUApplication<nuapplication>`                                                                                                                ``applications`` 
:ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`                                                 ``applicationperformancemanagements`` 
:ref:`nuvrs.NUVRS<nuvrs>`                                                                                                                                        ``vrss`` 
:ref:`nuvcentervrsconfig.NUVCenterVRSConfig<nuvcentervrsconfig>`                                                                                                 ``vcenter_vrs_configs`` 
:ref:`nuvrsinfo.NUvrsInfo<nuvrsinfo>`                                                                                                                            ``vrs_infos`` 
:ref:`nudscpremarkingpolicytable.NUDSCPRemarkingPolicyTable<nudscpremarkingpolicytable>`                                                                         ``dscp_remarking_policy_tables`` 
:ref:`nuvsdconfig.NUVSDConfig<nuvsdconfig>`                                                                                                                      ``vsd_configs`` 
:ref:`nuuser.NUUser<nuuser>`                                                                                                                                     ``users`` 
:ref:`nuusercontext.NUUserContext<nuusercontext>`                                                                                                                ``user_contexts`` 
:ref:`nunsgateway.NUNSGateway<nunsgateway>`                                                                                                                      ``ns_gateways`` 
:ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`                                                                                              ``ns_gateway_templates`` 
:ref:`nunsggroup.NUNSGGroup<nunsggroup>`                                                                                                                         ``nsg_groups`` 
:ref:`nunsginfo.NUNSGInfo<nunsginfo>`                                                                                                                            ``nsg_infos`` 
:ref:`nunsgmigrationprofile.NUNSGMigrationProfile<nunsgmigrationprofile>`                                                                                        ``nsg_migration_profiles`` 
:ref:`nunsgpatchprofile.NUNSGPatchProfile<nunsgpatchprofile>`                                                                                                    ``nsg_patch_profiles`` 
:ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`                                                                            ``ns_redundant_gateway_groups`` 
:ref:`nunsgupgradeprofile.NUNSGUpgradeProfile<nunsgupgradeprofile>`                                                                                              ``nsg_upgrade_profiles`` 
:ref:`nuesilmpolicy.NUEsIlmPolicy<nuesilmpolicy>`                                                                                                                ``es_ilm_policies`` 
:ref:`nuesindexconfig.NUEsIndexConfig<nuesindexconfig>`                                                                                                          ``es_index_configs`` 
:ref:`nuvsp.NUVSP<nuvsp>`                                                                                                                                        ``vsps`` 
:ref:`nustaticroute.NUStaticRoute<nustaticroute>`                                                                                                                ``static_routes`` 
:ref:`nustatscollectorinfo.NUStatsCollectorInfo<nustatscollectorinfo>`                                                                                           ``stats_collector_infos`` 
:ref:`nustatisticsprofile.NUStatisticsprofile<nustatisticsprofile>`                                                                                              ``statisticsprofiles`` 
:ref:`nuethernetsegmentgwgroup.NUEthernetSegmentGWGroup<nuethernetsegmentgwgroup>`                                                                               ``ethernet_segment_gw_groups`` 
:ref:`nusubnet.NUSubnet<nusubnet>`                                                                                                                               ``subnets`` 
:ref:`nuducgroup.NUDUCGroup<nuducgroup>`                                                                                                                         ``duc_groups`` 
:ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`                                                                                        ``multi_cast_channel_maps`` 
:ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`                                                                                  ``auto_discovered_gateways`` 
:ref:`nuoverlaymirrordestination.NUOverlayMirrorDestination<nuoverlaymirrordestination>`                                                                         ``overlay_mirror_destinations`` 
:ref:`nusystemconfig.NUSystemConfig<nusystemconfig>`                                                                                                             ``system_configs`` 
================================================================================================================================================               ==========================================================================================


