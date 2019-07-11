.. _nuglobalmetadata:

nuglobalmetadata
===========================================

.. class:: nuglobalmetadata.NUGlobalMetadata(bambou.nurest_object.NUMetaRESTObject,):

Metadata associated to a entity.


Attributes
----------


- ``name``: name of the Metadata.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the Metadata.

- ``metadata_tag_ids``: metadata tag IDs associated with this metadata you can filter metadata based on this attribute for example  X-Nuage-Filter: '2d6fb627-603b-421c-b63a-eb0a6d712761' IN metadataTagIDs 

- ``network_notification_disabled``: specifies metadata changes need to be notified to controller,by default it is notified

- ``blob`` (**Mandatory**): Metadata that describes about the entity attached to it.

- ``global_metadata``: specifies metadata is global or local

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`numetadatatag.NUMetadataTag<numetadatatag>`                                                                                                                ``metadata_tags`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuinfrastructureconfig.NUInfrastructureConfig<nuinfrastructureconfig>`

- :ref:`nuvmresync.NUVMResync<nuvmresync>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`numultinicvport.NUMultiNICVPort<numultinicvport>`

- :ref:`nugroupkeyencryptionprofile.NUGroupKeyEncryptionProfile<nugroupkeyencryptionprofile>`

- :ref:`numirrordestination.NUMirrorDestination<numirrordestination>`

- :ref:`nulicense.NULicense<nulicense>`

- :ref:`nuikegatewayconfig.NUIKEGatewayConfig<nuikegatewayconfig>`

- :ref:`nupublicnetworkmacro.NUPublicNetworkMacro<nupublicnetworkmacro>`

- :ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`

- :ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`

- :ref:`nuikesubnet.NUIKESubnet<nuikesubnet>`

- :ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`

- :ref:`numulticastrange.NUMultiCastRange<numulticastrange>`

- :ref:`nuipreservation.NUIPReservation<nuipreservation>`

- :ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`

- :ref:`nustatistics.NUStatistics<nustatistics>`

- :ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

- :ref:`nuapplicationservice.NUApplicationService<nuapplicationservice>`

- :ref:`nudscpforwardingclasstable.NUDSCPForwardingClassTable<nudscpforwardingclasstable>`

- :ref:`nuendpoint.NUEndPoint<nuendpoint>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nuenterprisesecureddata.NUEnterpriseSecuredData<nuenterprisesecureddata>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nuredundantport.NURedundantPort<nuredundantport>`

- :ref:`nuikeencryptionprofile.NUIKEEncryptionprofile<nuikeencryptionprofile>`

- :ref:`nusiteinfo.NUSiteInfo<nusiteinfo>`

- :ref:`nuvcentercluster.NUVCenterCluster<nuvcentercluster>`

- :ref:`nuredirectiontargettemplate.NURedirectionTargetTemplate<nuredirectiontargettemplate>`

- :ref:`nucontainer.NUContainer<nucontainer>`

- :ref:`nudomainfipacltemplateentry.NUDomainFIPAclTemplateEntry<nudomainfipacltemplateentry>`

- :ref:`nuexternalappservice.NUExternalAppService<nuexternalappservice>`

- :ref:`nucontainerresync.NUContainerResync<nucontainerresync>`

- :ref:`nufloatingip.NUFloatingIp<nufloatingip>`

- :ref:`nuvcenter.NUVCenter<nuvcenter>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nuuplinkrd.NUUplinkRD<nuuplinkrd>`

- :ref:`nunatmapentry.NUNATMapEntry<nunatmapentry>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nuvsp.NUVSP<nuvsp>`

- :ref:`nuvportmirror.NUVPortMirror<nuvportmirror>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nuvcentereamconfig.NUVCenterEAMConfig<nuvcentereamconfig>`

- :ref:`nunetworklayout.NUNetworkLayout<nunetworklayout>`

- :ref:`nubfdsession.NUBFDSession<nubfdsession>`

- :ref:`nupolicygrouptemplate.NUPolicyGroupTemplate<nupolicygrouptemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nueventlog.NUEventLog<nueventlog>`

- :ref:`nuinfrastructureaccessprofile.NUInfrastructureAccessProfile<nuinfrastructureaccessprofile>`

- :ref:`nuikegatewayconnection.NUIKEGatewayConnection<nuikegatewayconnection>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nudscpforwardingclassmapping.NUDSCPForwardingClassMapping<nudscpforwardingclassmapping>`

- :ref:`nuinfrastructuregatewayprofile.NUInfrastructureGatewayProfile<nuinfrastructuregatewayprofile>`

- :ref:`nuvcentervrsconfig.NUVCenterVRSConfig<nuvcentervrsconfig>`

- :ref:`nuegressqospolicy.NUEgressQOSPolicy<nuegressqospolicy>`

- :ref:`nuingressexternalservicetemplate.NUIngressExternalServiceTemplate<nuingressexternalservicetemplate>`

- :ref:`nuvirtualip.NUVirtualIP<nuvirtualip>`

- :ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`

- :ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`

- :ref:`nustaticroute.NUStaticRoute<nustaticroute>`

- :ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`

- :ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`

- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nugatewaysecureddata.NUGatewaySecuredData<nugatewaysecureddata>`

- :ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nujob.NUJob<nujob>`

- :ref:`nuflowsecuritypolicy.NUFlowSecurityPolicy<nuflowsecuritypolicy>`

- :ref:`nuavatar.NUAvatar<nuavatar>`

- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`

- :ref:`nupermission.NUPermission<nupermission>`

- :ref:`nuqos.NUQOS<nuqos>`

- :ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`

- :ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`

- :ref:`nuldapconfiguration.NULDAPConfiguration<nuldapconfiguration>`

- :ref:`nutier.NUTier<nutier>`

- :ref:`nupolicydecision.NUPolicyDecision<nupolicydecision>`

- :ref:`nukeyservermonitorseed.NUKeyServerMonitorSeed<nukeyservermonitorseed>`

- :ref:`nuvcenterhypervisor.NUVCenterHypervisor<nuvcenterhypervisor>`

- :ref:`nufloatingipacltemplate.NUFloatingIPACLTemplate<nufloatingipacltemplate>`

- :ref:`nunetworkmacrogroup.NUNetworkMacroGroup<nunetworkmacrogroup>`

- :ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`

- :ref:`nuikecertificate.NUIKECertificate<nuikecertificate>`

- :ref:`nukeyservermonitorencryptedseed.NUKeyServerMonitorEncryptedSeed<nukeyservermonitorencryptedseed>`

- :ref:`nugatewaysecurity.NUGatewaySecurity<nugatewaysecurity>`

- :ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`

- :ref:`nustatscollectorinfo.NUStatsCollectorInfo<nustatscollectorinfo>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nucertificate.NUCertificate<nucertificate>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nutca.NUTCA<nutca>`

- :ref:`nuvpnconnection.NUVPNConnection<nuvpnconnection>`

- :ref:`nuingressexternalservicetemplateentry.NUIngressExternalServiceTemplateEntry<nuingressexternalservicetemplateentry>`

- :ref:`nuvsdcomponent.NUVSDComponent<nuvsdcomponent>`

- :ref:`nunsporttemplate.NUNSPortTemplate<nunsporttemplate>`

- :ref:`nukeyservermember.NUKeyServerMember<nukeyservermember>`

- :ref:`nuikegatewayprofile.NUIKEGatewayProfile<nuikegatewayprofile>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nuvrsaddressrange.NUVRSAddressRange<nuvrsaddressrange>`

- :ref:`nuinfrastructurevscprofile.NUInfrastructureVscProfile<nuinfrastructurevscprofile>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`nudomainfipacltemplate.NUDomainFIPAclTemplate<nudomainfipacltemplate>`

- :ref:`nuaddressmap.NUAddressMap<nuaddressmap>`

- :ref:`nubgpprofile.NUBGPProfile<nubgpprofile>`

- :ref:`nultestatistics.NULtestatistics<nultestatistics>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nubulkstatistics.NUBulkStatistics<nubulkstatistics>`

- :ref:`nubootstrap.NUBootstrap<nubootstrap>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvm.NUVM<nuvm>`

- :ref:`nubgppeer.NUBGPPeer<nubgppeer>`

- :ref:`nucloudmgmtsystem.NUCloudMgmtSystem<nucloudmgmtsystem>`

- :ref:`numonitoringport.NUMonitoringPort<numonitoringport>`

- :ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`

- :ref:`nugroup.NUGroup<nugroup>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuexternalservice.NUExternalService<nuexternalservice>`

- :ref:`numetadatatag.NUMetadataTag<numetadatatag>`

- :ref:`numulticastlist.NUMultiCastList<numulticastlist>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuflowforwardingpolicy.NUFlowForwardingPolicy<nuflowforwardingpolicy>`

- :ref:`nuflow.NUFlow<nuflow>`

- :ref:`nulink.NULink<nulink>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuwanservice.NUWANService<nuwanservice>`

- :ref:`nuvcenterdatacenter.NUVCenterDataCenter<nuvcenterdatacenter>`

- :ref:`nuvsd.NUVSD<nuvsd>`

- :ref:`nugatewaytemplate.NUGatewayTemplate<nugatewaytemplate>`

- :ref:`nuzfbrequest.NUZFBRequest<nuzfbrequest>`

- :ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`

- :ref:`nuaddressrange.NUAddressRange<nuaddressrange>`

- :ref:`nuroutingpolicy.NURoutingPolicy<nuroutingpolicy>`

- :ref:`nualarm.NUAlarm<nualarm>`

- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nuingressqospolicy.NUIngressQOSPolicy<nuingressqospolicy>`

- :ref:`nukeyservermonitorsek.NUKeyServerMonitorSEK<nukeyservermonitorsek>`

- :ref:`nume.NUMe<nume>`

- :ref:`nusystemconfig.NUSystemConfig<nusystemconfig>`

- :ref:`nuallalarm.NUAllAlarm<nuallalarm>`

- :ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`

- :ref:`nulocation.NULocation<nulocation>`

- :ref:`nuzonetemplate.NUZoneTemplate<nuzonetemplate>`

- :ref:`nukeyservernotification.NUKeyServerNotification<nukeyservernotification>`

- :ref:`nufloatingipacltemplateentry.NUFloatingIPACLTemplateEntry<nufloatingipacltemplateentry>`

- :ref:`nubootstrapactivation.NUBootstrapActivation<nubootstrapactivation>`

- :ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`

- :ref:`nuenterprisesecurity.NUEnterpriseSecurity<nuenterprisesecurity>`

- :ref:`nunexthop.NUNextHop<nunexthop>`

- :ref:`nuikegateway.NUIKEGateway<nuikegateway>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nuratelimiter.NURateLimiter<nuratelimiter>`

- :ref:`nuikepsk.NUIKEPSK<nuikepsk>`

- :ref:`nuporttemplate.NUPortTemplate<nuporttemplate>`

