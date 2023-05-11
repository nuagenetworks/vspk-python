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

- ``assoc_entity_type``: Type of the entity to which the Profile belongs to.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nugroupkeyencryptionprofile.NUGroupKeyEncryptionProfile<nugroupkeyencryptionprofile>`

- :ref:`nuqos.NUQOS<nuqos>`

- :ref:`nuinfrastructureaccessprofile.NUInfrastructureAccessProfile<nuinfrastructureaccessprofile>`

- :ref:`nubgppeer.NUBGPPeer<nubgppeer>`

- :ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nuvirtualip.NUVirtualIP<nuvirtualip>`

- :ref:`nupspatmap.NUPSPATMap<nupspatmap>`

- :ref:`nuegressadvfwdentrytemplate.NUEgressAdvFwdEntryTemplate<nuegressadvfwdentrytemplate>`

- :ref:`nudscpforwardingclasstable.NUDSCPForwardingClassTable<nudscpforwardingclasstable>`

- :ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nutca.NUTCA<nutca>`

- :ref:`nusapegressqosprofile.NUSAPEgressQoSProfile<nusapegressqosprofile>`

- :ref:`nuikesubnet.NUIKESubnet<nuikesubnet>`

- :ref:`numacfilterprofile.NUMACFilterProfile<numacfilterprofile>`

- :ref:`nuvnfdescriptor.NUVNFDescriptor<nuvnfdescriptor>`

- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nuapplication.NUApplication<nuapplication>`

- :ref:`nuikegatewayprofile.NUIKEGatewayProfile<nuikegatewayprofile>`

- :ref:`nuoverlaymirrordestination.NUOverlayMirrorDestination<nuoverlaymirrordestination>`

- :ref:`nuinfrastructuregatewayprofile.NUInfrastructureGatewayProfile<nuinfrastructuregatewayprofile>`

- :ref:`nudiskstat.NUDiskStat<nudiskstat>`

- :ref:`nuvnfinterface.NUVNFInterface<nuvnfinterface>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nulocation.NULocation<nulocation>`

- :ref:`nuenterprisesecurity.NUEnterpriseSecurity<nuenterprisesecurity>`

- :ref:`nuvcentervrsconfig.NUVCenterVRSConfig<nuvcentervrsconfig>`

- :ref:`nuducgroup.NUDUCGroup<nuducgroup>`

- :ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`

- :ref:`nuinfrastructurevscprofile.NUInfrastructureVscProfile<nuinfrastructurevscprofile>`

- :ref:`nupermission.NUPermission<nupermission>`

- :ref:`nucosremarkingpolicy.NUCOSRemarkingPolicy<nucosremarkingpolicy>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuipreservation.NUIPReservation<nuipreservation>`

- :ref:`nuredirectiontargettemplate.NURedirectionTargetTemplate<nuredirectiontargettemplate>`

- :ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`

- :ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`

- :ref:`nuwanservice.NUWANService<nuwanservice>`

- :ref:`nuikegatewayconnection.NUIKEGatewayConnection<nuikegatewayconnection>`

- :ref:`nuvnfdomainmapping.NUVNFDomainMapping<nuvnfdomainmapping>`

- :ref:`nufirewallacl.NUFirewallAcl<nufirewallacl>`

- :ref:`nugatewayredundantport.NUGatewayRedundantPort<nugatewayredundantport>`

- :ref:`nusystemconfig.NUSystemConfig<nusystemconfig>`

- :ref:`nuvnfinterfacedescriptor.NUVNFInterfaceDescriptor<nuvnfinterfacedescriptor>`

- :ref:`nupatch.NUPatch<nupatch>`

- :ref:`nuavatar.NUAvatar<nuavatar>`

- :ref:`nuoverlayaddresspool.NUOverlayAddressPool<nuoverlayaddresspool>`

- :ref:`nubootstrapactivation.NUBootstrapActivation<nubootstrapactivation>`

- :ref:`nulicensestatus.NULicenseStatus<nulicensestatus>`

- :ref:`nulteinformation.NULTEInformation<nulteinformation>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nuipv6filterprofile.NUIPv6FilterProfile<nuipv6filterprofile>`

- :ref:`nuvsp.NUVSP<nuvsp>`

- :ref:`nusaasapplicationtype.NUSaaSApplicationType<nusaasapplicationtype>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nunetconfsession.NUNetconfSession<nunetconfsession>`

- :ref:`nunetconfprofile.NUNetconfProfile<nunetconfprofile>`

- :ref:`nuredundantport.NURedundantPort<nuredundantport>`

- :ref:`nudscpforwardingclassmapping.NUDSCPForwardingClassMapping<nudscpforwardingclassmapping>`

- :ref:`nupolicyobjectgroup.NUPolicyObjectGroup<nupolicyobjectgroup>`

- :ref:`nuporttemplate.NUPortTemplate<nuporttemplate>`

- :ref:`nuaddressmap.NUAddressMap<nuaddressmap>`

- :ref:`nuoverlaypatnatentry.NUOverlayPATNATEntry<nuoverlaypatnatentry>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nuvsd.NUVSD<nuvsd>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuvpnconnection.NUVPNConnection<nuvpnconnection>`

- :ref:`nupolicystatement.NUPolicyStatement<nupolicystatement>`

- :ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`

- :ref:`nupolicygroupcategory.NUPolicyGroupCategory<nupolicygroupcategory>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nucontainer.NUContainer<nucontainer>`

- :ref:`nuforwardingpathlist.NUForwardingPathList<nuforwardingpathlist>`

- :ref:`nukeyservermonitorencryptedseed.NUKeyServerMonitorEncryptedSeed<nukeyservermonitorencryptedseed>`

- :ref:`nugatewaytemplate.NUGatewayTemplate<nugatewaytemplate>`

- :ref:`nuallgateway.NUAllGateway<nuallgateway>`

- :ref:`nuuplinkrd.NUUplinkRD<nuuplinkrd>`

- :ref:`nukeyservermonitorseed.NUKeyServerMonitorSeed<nukeyservermonitorseed>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuoverlaymirrordestinationtemplate.NUOverlayMirrorDestinationTemplate<nuoverlaymirrordestinationtemplate>`

- :ref:`nuldapconfiguration.NULDAPConfiguration<nuldapconfiguration>`

- :ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`

- :ref:`nuzfbrequest.NUZFBRequest<nuzfbrequest>`

- :ref:`nuvsdcomponent.NUVSDComponent<nuvsdcomponent>`

- :ref:`nustaticroute.NUStaticRoute<nustaticroute>`

- :ref:`nuconnectionendpoint.NUConnectionendpoint<nuconnectionendpoint>`

- :ref:`nujob.NUJob<nujob>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nugatewaysecureddata.NUGatewaySecuredData<nugatewaysecureddata>`

- :ref:`nutrunk.NUTrunk<nutrunk>`

- :ref:`nugroup.NUGroup<nugroup>`

- :ref:`nusapingressqosprofile.NUSAPIngressQoSProfile<nusapingressqosprofile>`

- :ref:`nupolicyentry.NUPolicyEntry<nupolicyentry>`

- :ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`

- :ref:`nunetworklayout.NUNetworkLayout<nunetworklayout>`

- :ref:`nuqospolicer.NUQosPolicer<nuqospolicer>`

- :ref:`nucertificate.NUCertificate<nucertificate>`

- :ref:`nulicense.NULicense<nulicense>`

- :ref:`nucloudmgmtsystem.NUCloudMgmtSystem<nucloudmgmtsystem>`

- :ref:`nunetconfmanager.NUNetconfManager<nunetconfmanager>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nudscpremarkingpolicytable.NUDSCPRemarkingPolicyTable<nudscpremarkingpolicytable>`

- :ref:`nuvcentercluster.NUVCenterCluster<nuvcentercluster>`

- :ref:`nudscpremarkingpolicy.NUDSCPRemarkingPolicy<nudscpremarkingpolicy>`

- :ref:`nuegressprofile.NUEgressProfile<nuegressprofile>`

- :ref:`nunetworkmacrogroup.NUNetworkMacroGroup<nunetworkmacrogroup>`

- :ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`

- :ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`

- :ref:`nuapplicationbinding.NUApplicationBinding<nuapplicationbinding>`

- :ref:`nudestinationurl.NUDestinationurl<nudestinationurl>`

- :ref:`nuvnfcatalog.NUVNFCatalog<nuvnfcatalog>`

- :ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`

- :ref:`nuforwardingpathlistentry.NUForwardingPathListEntry<nuforwardingpathlistentry>`

- :ref:`nuegressqospolicy.NUEgressQOSPolicy<nuegressqospolicy>`

- :ref:`nunexthop.NUNextHop<nunexthop>`

- :ref:`numirrordestination.NUMirrorDestination<numirrordestination>`

- :ref:`nutier.NUTier<nutier>`

- :ref:`nudomainfipacltemplate.NUDomainFIPAclTemplate<nudomainfipacltemplate>`

- :ref:`nuospfinterface.NUOSPFInterface<nuospfinterface>`

- :ref:`nuunderlay.NUUnderlay<nuunderlay>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`numultinicvport.NUMultiNICVPort<numultinicvport>`

- :ref:`nuwebcategory.NUWebCategory<nuwebcategory>`

- :ref:`nubfdsession.NUBFDSession<nubfdsession>`

- :ref:`nustatistics.NUStatistics<nustatistics>`

- :ref:`nunsporttemplate.NUNSPortTemplate<nunsporttemplate>`

- :ref:`nusshkey.NUSSHKey<nusshkey>`

- :ref:`nueventlog.NUEventLog<nueventlog>`

- :ref:`nuvcenterdatacenter.NUVCenterDataCenter<nuvcenterdatacenter>`

- :ref:`nucustomproperty.NUCustomProperty<nucustomproperty>`

- :ref:`nultestatistics.NULtestatistics<nultestatistics>`

- :ref:`nuvirtualfirewallrule.NUVirtualFirewallRule<nuvirtualfirewallrule>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nuptranslationmap.NUPTranslationMap<nuptranslationmap>`

- :ref:`nuwebdomainname.NUWebDomainName<nuwebdomainname>`

- :ref:`nuikegateway.NUIKEGateway<nuikegateway>`

- :ref:`nucsnatpool.NUCSNATPool<nucsnatpool>`

- :ref:`nustatscollectorinfo.NUStatsCollectorInfo<nustatscollectorinfo>`

- :ref:`nuvcenter.NUVCenter<nuvcenter>`

- :ref:`nubulkstatistics.NUBulkStatistics<nubulkstatistics>`

- :ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`

- :ref:`nuingressqospolicy.NUIngressQOSPolicy<nuingressqospolicy>`

- :ref:`nuroutingpolicy.NURoutingPolicy<nuroutingpolicy>`

- :ref:`nunetworkperformancebinding.NUNetworkPerformanceBinding<nunetworkperformancebinding>`

- :ref:`nuvnfthresholdpolicy.NUVNFThresholdPolicy<nuvnfthresholdpolicy>`

- :ref:`nudefaultgateway.NUDefaultGateway<nudefaultgateway>`

- :ref:`nusaasapplicationgroup.NUSaaSApplicationGroup<nusaasapplicationgroup>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuikegatewayconfig.NUIKEGatewayConfig<nuikegatewayconfig>`

- :ref:`nuingressprofile.NUIngressProfile<nuingressprofile>`

- :ref:`nuospfinstance.NUOSPFInstance<nuospfinstance>`

- :ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`

- :ref:`nuducgroupbinding.NUDUCGroupBinding<nuducgroupbinding>`

- :ref:`nulink.NULink<nulink>`

- :ref:`nushuntlink.NUShuntLink<nushuntlink>`

- :ref:`nussidconnection.NUSSIDConnection<nussidconnection>`

- :ref:`nuegressadvfwdtemplate.NUEgressAdvFwdTemplate<nuegressadvfwdtemplate>`

- :ref:`nuusercontext.NUUserContext<nuusercontext>`

- :ref:`nugatewayslocation.NUGatewaysLocation<nugatewayslocation>`

- :ref:`nul7applicationsignature.NUL7applicationsignature<nul7applicationsignature>`

- :ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`

- :ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`

- :ref:`nukeyservermember.NUKeyServerMember<nukeyservermember>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`

- :ref:`nuzonetemplate.NUZoneTemplate<nuzonetemplate>`

- :ref:`nunsggroup.NUNSGGroup<nunsggroup>`

- :ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`

- :ref:`nusiteinfo.NUSiteInfo<nusiteinfo>`

- :ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`

- :ref:`nunsgroutingpolicybinding.NUNSGRoutingPolicyBinding<nunsgroutingpolicybinding>`

- :ref:`nunsgatewayscount.NUNSGatewaysCount<nunsgatewayscount>`

- :ref:`nubootstrap.NUBootstrap<nubootstrap>`

- :ref:`nubgpprofile.NUBGPProfile<nubgpprofile>`

- :ref:`nuctranslationmap.NUCTranslationMap<nuctranslationmap>`

- :ref:`nupublicnetworkmacro.NUPublicNetworkMacro<nupublicnetworkmacro>`

- :ref:`nudomainfipacltemplateentry.NUDomainFIPAclTemplateEntry<nudomainfipacltemplateentry>`

- :ref:`nuinfrastructureevdfprofile.NUInfrastructureEVDFProfile<nuinfrastructureevdfprofile>`

- :ref:`nuaddressrange.NUAddressRange<nuaddressrange>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nuvm.NUVM<nuvm>`

- :ref:`nunsgatewaysummary.NUNSGatewaySummary<nunsgatewaysummary>`

- :ref:`nuvirtualfirewallpolicy.NUVirtualFirewallPolicy<nuvirtualfirewallpolicy>`

- :ref:`nuvmresync.NUVMResync<nuvmresync>`

- :ref:`nugatewaysecurity.NUGatewaySecurity<nugatewaysecurity>`

- :ref:`nupolicydecision.NUPolicyDecision<nupolicydecision>`

- :ref:`nuapplicationperformancemanagementbinding.NUApplicationperformancemanagementbinding<nuapplicationperformancemanagementbinding>`

- :ref:`nuspatsourcespool.NUSPATSourcesPool<nuspatsourcespool>`

- :ref:`nufloatingip.NUFloatingIp<nufloatingip>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`numonitoringport.NUMonitoringPort<numonitoringport>`

- :ref:`numonitorscope.NUMonitorscope<numonitorscope>`

- :ref:`nuipfilterprofile.NUIPFilterProfile<nuipfilterprofile>`

- :ref:`numulticastrange.NUMultiCastRange<numulticastrange>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`nukeyservermonitorsek.NUKeyServerMonitorSEK<nukeyservermonitorsek>`

- :ref:`nucosremarkingpolicytable.NUCOSRemarkingPolicyTable<nucosremarkingpolicytable>`

- :ref:`nuvportmirror.NUVPortMirror<nuvportmirror>`

- :ref:`nupsnatpool.NUPSNATPool<nupsnatpool>`

- :ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`

- :ref:`nucontainerresync.NUContainerResync<nucontainerresync>`

- :ref:`nuvnf.NUVNF<nuvnf>`

- :ref:`nuallredundancygroup.NUAllRedundancyGroup<nuallredundancygroup>`

- :ref:`nuallalarm.NUAllAlarm<nuallalarm>`

- :ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`

- :ref:`nuikepsk.NUIKEPSK<nuikepsk>`

- :ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`

- :ref:`nuvcentereamconfig.NUVCenterEAMConfig<nuvcentereamconfig>`

- :ref:`nuikeencryptionprofile.NUIKEEncryptionprofile<nuikeencryptionprofile>`

- :ref:`nupolicygrouptemplate.NUPolicyGroupTemplate<nupolicygrouptemplate>`

- :ref:`nuinfrastructureconfig.NUInfrastructureConfig<nuinfrastructureconfig>`

- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nunatmapentry.NUNATMapEntry<nunatmapentry>`

- :ref:`nuratelimiter.NURateLimiter<nuratelimiter>`

- :ref:`numulticastlist.NUMultiCastList<numulticastlist>`

- :ref:`nuenterprisesecureddata.NUEnterpriseSecuredData<nuenterprisesecureddata>`

- :ref:`nudemarcationservice.NUDemarcationService<nudemarcationservice>`

- :ref:`nubrconnection.NUBRConnection<nubrconnection>`

- :ref:`nufirewallrule.NUFirewallRule<nufirewallrule>`

- :ref:`nualarm.NUAlarm<nualarm>`

- :ref:`nuvrsaddressrange.NUVRSAddressRange<nuvrsaddressrange>`

- :ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`

- :ref:`nuuplinkconnection.NUUplinkConnection<nuuplinkconnection>`

- :ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`

- :ref:`nunetworkperformancemeasurement.NUNetworkPerformanceMeasurement<nunetworkperformancemeasurement>`

- :ref:`nuospfarea.NUOSPFArea<nuospfarea>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuikecertificate.NUIKECertificate<nuikecertificate>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

- :ref:`nuvnfmetadata.NUVNFMetadata<nuvnfmetadata>`

- :ref:`nuvcenterhypervisor.NUVCenterHypervisor<nuvcenterhypervisor>`

