.. _numetadata:

numetadata
===========================================

.. class:: numetadata.NUMetadata(bambou.nurest_object.NUMetaRESTObject,):

Metadata contains user-defined data that can be attached to any VSD object. The value of a metadata can be interpreted by various external systems for any needs. Local Metadata are directly created under an object.


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

- ``assoc_entity_id``: ID of the entity to which the Metadata is associated to.

- ``assoc_entity_type``: Type of the entity to which the Metadata is associated to.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudefaultgateway.NUDefaultGateway<nudefaultgateway>`

- :ref:`nuinfrastructureconfig.NUInfrastructureConfig<nuinfrastructureconfig>`

- :ref:`nuvmresync.NUVMResync<nuvmresync>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nuallgateway.NUAllGateway<nuallgateway>`

- :ref:`numultinicvport.NUMultiNICVPort<numultinicvport>`

- :ref:`nunetconfsession.NUNetconfSession<nunetconfsession>`

- :ref:`nugroupkeyencryptionprofile.NUGroupKeyEncryptionProfile<nugroupkeyencryptionprofile>`

- :ref:`nuoverlaymirrordestinationtemplate.NUOverlayMirrorDestinationTemplate<nuoverlaymirrordestinationtemplate>`

- :ref:`nuvirtualfirewallrule.NUVirtualFirewallRule<nuvirtualfirewallrule>`

- :ref:`numirrordestination.NUMirrorDestination<numirrordestination>`

- :ref:`nulicense.NULicense<nulicense>`

- :ref:`nuikegatewayconfig.NUIKEGatewayConfig<nuikegatewayconfig>`

- :ref:`numacfilterprofile.NUMACFilterProfile<numacfilterprofile>`

- :ref:`nupublicnetworkmacro.NUPublicNetworkMacro<nupublicnetworkmacro>`

- :ref:`nuqospolicer.NUQosPolicer<nuqospolicer>`

- :ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`

- :ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`

- :ref:`nuikesubnet.NUIKESubnet<nuikesubnet>`

- :ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`

- :ref:`nuforwardingpathlist.NUForwardingPathList<nuforwardingpathlist>`

- :ref:`numulticastrange.NUMultiCastRange<numulticastrange>`

- :ref:`nuipreservation.NUIPReservation<nuipreservation>`

- :ref:`nulteinformation.NULTEInformation<nulteinformation>`

- :ref:`nusaasapplicationtype.NUSaaSApplicationType<nusaasapplicationtype>`

- :ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nuegressadvfwdentrytemplate.NUEgressAdvFwdEntryTemplate<nuegressadvfwdentrytemplate>`

- :ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nupolicyobjectgroup.NUPolicyObjectGroup<nupolicyobjectgroup>`

- :ref:`nustatistics.NUStatistics<nustatistics>`

- :ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`

- :ref:`nunetconfprofile.NUNetconfProfile<nunetconfprofile>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

- :ref:`nuospfinterface.NUOSPFInterface<nuospfinterface>`

- :ref:`nudscpforwardingclasstable.NUDSCPForwardingClassTable<nudscpforwardingclasstable>`

- :ref:`nuusercontext.NUUserContext<nuusercontext>`

- :ref:`nunetconfmanager.NUNetconfManager<nunetconfmanager>`

- :ref:`nupatch.NUPatch<nupatch>`

- :ref:`nuoverlaypatnatentry.NUOverlayPATNATEntry<nuoverlaypatnatentry>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nuctranslationmap.NUCTranslationMap<nuctranslationmap>`

- :ref:`nuenterprisesecureddata.NUEnterpriseSecuredData<nuenterprisesecureddata>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nubrconnection.NUBRConnection<nubrconnection>`

- :ref:`nuredundantport.NURedundantPort<nuredundantport>`

- :ref:`nuvnfthresholdpolicy.NUVNFThresholdPolicy<nuvnfthresholdpolicy>`

- :ref:`nuvnfcatalog.NUVNFCatalog<nuvnfcatalog>`

- :ref:`nutest.NUTest<nutest>`

- :ref:`nuikeencryptionprofile.NUIKEEncryptionprofile<nuikeencryptionprofile>`

- :ref:`nusiteinfo.NUSiteInfo<nusiteinfo>`

- :ref:`nuvcentercluster.NUVCenterCluster<nuvcentercluster>`

- :ref:`nuspatsourcespool.NUSPATSourcesPool<nuspatsourcespool>`

- :ref:`nuforwardingpathlistentry.NUForwardingPathListEntry<nuforwardingpathlistentry>`

- :ref:`nuapplicationbinding.NUApplicationBinding<nuapplicationbinding>`

- :ref:`nuredirectiontargettemplate.NURedirectionTargetTemplate<nuredirectiontargettemplate>`

- :ref:`nucontainer.NUContainer<nucontainer>`

- :ref:`nuvnf.NUVNF<nuvnf>`

- :ref:`nuospfinstance.NUOSPFInstance<nuospfinstance>`

- :ref:`nuwebcategory.NUWebCategory<nuwebcategory>`

- :ref:`nutestrun.NUTestRun<nutestrun>`

- :ref:`nuwebdomainname.NUWebDomainName<nuwebdomainname>`

- :ref:`nuospfarea.NUOSPFArea<nuospfarea>`

- :ref:`nudomainfipacltemplateentry.NUDomainFIPAclTemplateEntry<nudomainfipacltemplateentry>`

- :ref:`nucontainerresync.NUContainerResync<nucontainerresync>`

- :ref:`nufloatingip.NUFloatingIp<nufloatingip>`

- :ref:`nuvcenter.NUVCenter<nuvcenter>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nuuplinkrd.NUUplinkRD<nuuplinkrd>`

- :ref:`nunatmapentry.NUNATMapEntry<nunatmapentry>`

- :ref:`nuvnfmetadata.NUVNFMetadata<nuvnfmetadata>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nuvsp.NUVSP<nuvsp>`

- :ref:`nuvportmirror.NUVPortMirror<nuvportmirror>`

- :ref:`numonitorscope.NUMonitorscope<numonitorscope>`

- :ref:`nuducgroup.NUDUCGroup<nuducgroup>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nuvcentereamconfig.NUVCenterEAMConfig<nuvcentereamconfig>`

- :ref:`nunetworklayout.NUNetworkLayout<nunetworklayout>`

- :ref:`nubfdsession.NUBFDSession<nubfdsession>`

- :ref:`nucosremarkingpolicytable.NUCOSRemarkingPolicyTable<nucosremarkingpolicytable>`

- :ref:`nupolicygrouptemplate.NUPolicyGroupTemplate<nupolicygrouptemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nuinfrastructureevdfprofile.NUInfrastructureEVDFProfile<nuinfrastructureevdfprofile>`

- :ref:`nueventlog.NUEventLog<nueventlog>`

- :ref:`nutrunk.NUTrunk<nutrunk>`

- :ref:`nuvnfdescriptor.NUVNFDescriptor<nuvnfdescriptor>`

- :ref:`nuvnfinterface.NUVNFInterface<nuvnfinterface>`

- :ref:`nuinfrastructureaccessprofile.NUInfrastructureAccessProfile<nuinfrastructureaccessprofile>`

- :ref:`nuikegatewayconnection.NUIKEGatewayConnection<nuikegatewayconnection>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nudscpforwardingclassmapping.NUDSCPForwardingClassMapping<nudscpforwardingclassmapping>`

- :ref:`nuinfrastructuregatewayprofile.NUInfrastructureGatewayProfile<nuinfrastructuregatewayprofile>`

- :ref:`nuvcentervrsconfig.NUVCenterVRSConfig<nuvcentervrsconfig>`

- :ref:`nudscpremarkingpolicytable.NUDSCPRemarkingPolicyTable<nudscpremarkingpolicytable>`

- :ref:`nuegressqospolicy.NUEgressQOSPolicy<nuegressqospolicy>`

- :ref:`nugatewayredundantport.NUGatewayRedundantPort<nugatewayredundantport>`

- :ref:`nufirewallrule.NUFirewallRule<nufirewallrule>`

- :ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`

- :ref:`nuvirtualip.NUVirtualIP<nuvirtualip>`

- :ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`

- :ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`

- :ref:`nustaticroute.NUStaticRoute<nustaticroute>`

- :ref:`nussidconnection.NUSSIDConnection<nussidconnection>`

- :ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`

- :ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`

- :ref:`nupsnatpool.NUPSNATPool<nupsnatpool>`

- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nucontrollervrslink.NUControllerVRSLink<nucontrollervrslink>`

- :ref:`nuegressprofile.NUEgressProfile<nuegressprofile>`

- :ref:`nuapplicationperformancemanagementbinding.NUApplicationperformancemanagementbinding<nuapplicationperformancemanagementbinding>`

- :ref:`nuconnectionendpoint.NUConnectionendpoint<nuconnectionendpoint>`

- :ref:`nushuntlink.NUShuntLink<nushuntlink>`

- :ref:`nuvirtualfirewallpolicy.NUVirtualFirewallPolicy<nuvirtualfirewallpolicy>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nugatewaysecureddata.NUGatewaySecuredData<nugatewaysecureddata>`

- :ref:`nudscpremarkingpolicy.NUDSCPRemarkingPolicy<nudscpremarkingpolicy>`

- :ref:`nunsgatewaysummary.NUNSGatewaySummary<nunsgatewaysummary>`

- :ref:`nufirewallacl.NUFirewallAcl<nufirewallacl>`

- :ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`

- :ref:`nuallredundancygroup.NUAllRedundancyGroup<nuallredundancygroup>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nuipv6filterprofile.NUIPv6FilterProfile<nuipv6filterprofile>`

- :ref:`nuuplinkconnection.NUUplinkConnection<nuuplinkconnection>`

- :ref:`nujob.NUJob<nujob>`

- :ref:`nuvrsinfo.NUvrsInfo<nuvrsinfo>`

- :ref:`nuavatar.NUAvatar<nuavatar>`

- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`

- :ref:`nupermission.NUPermission<nupermission>`

- :ref:`nuqos.NUQOS<nuqos>`

- :ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`

- :ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`

- :ref:`nuldapconfiguration.NULDAPConfiguration<nuldapconfiguration>`

- :ref:`nul7applicationsignature.NUL7applicationsignature<nul7applicationsignature>`

- :ref:`nutier.NUTier<nutier>`

- :ref:`nupolicydecision.NUPolicyDecision<nupolicydecision>`

- :ref:`nuvnfdomainmapping.NUVNFDomainMapping<nuvnfdomainmapping>`

- :ref:`nucustomproperty.NUCustomProperty<nucustomproperty>`

- :ref:`nudhcpv6option.NUDHCPv6Option<nudhcpv6option>`

- :ref:`nukeyservermonitorseed.NUKeyServerMonitorSeed<nukeyservermonitorseed>`

- :ref:`nuvcenterhypervisor.NUVCenterHypervisor<nuvcenterhypervisor>`

- :ref:`nunetworkmacrogroup.NUNetworkMacroGroup<nunetworkmacrogroup>`

- :ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`

- :ref:`nusshkey.NUSSHKey<nusshkey>`

- :ref:`nuikecertificate.NUIKECertificate<nuikecertificate>`

- :ref:`nukeyservermonitorencryptedseed.NUKeyServerMonitorEncryptedSeed<nukeyservermonitorencryptedseed>`

- :ref:`nugatewaysecurity.NUGatewaySecurity<nugatewaysecurity>`

- :ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`

- :ref:`numirrordestinationgroup.NUMirrorDestinationGroup<numirrordestinationgroup>`

- :ref:`nutestdefinition.NUTestDefinition<nutestdefinition>`

- :ref:`nustatscollectorinfo.NUStatsCollectorInfo<nustatscollectorinfo>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nunetworkperformancebinding.NUNetworkPerformanceBinding<nunetworkperformancebinding>`

- :ref:`nucertificate.NUCertificate<nucertificate>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nutca.NUTCA<nutca>`

- :ref:`nunetworkperformancemeasurement.NUNetworkPerformanceMeasurement<nunetworkperformancemeasurement>`

- :ref:`nuvpnconnection.NUVPNConnection<nuvpnconnection>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuvsdcomponent.NUVSDComponent<nuvsdcomponent>`

- :ref:`nunsporttemplate.NUNSPortTemplate<nunsporttemplate>`

- :ref:`nukeyservermember.NUKeyServerMember<nukeyservermember>`

- :ref:`nunsgatewayscount.NUNSGatewaysCount<nunsgatewayscount>`

- :ref:`nuikegatewayprofile.NUIKEGatewayProfile<nuikegatewayprofile>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nuvrsaddressrange.NUVRSAddressRange<nuvrsaddressrange>`

- :ref:`nusapegressqosprofile.NUSAPEgressQoSProfile<nusapegressqosprofile>`

- :ref:`nuvnfinterfacedescriptor.NUVNFInterfaceDescriptor<nuvnfinterfacedescriptor>`

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

- :ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`

- :ref:`nuvm.NUVM<nuvm>`

- :ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`

- :ref:`nubgppeer.NUBGPPeer<nubgppeer>`

- :ref:`nucloudmgmtsystem.NUCloudMgmtSystem<nucloudmgmtsystem>`

- :ref:`nudemarcationservice.NUDemarcationService<nudemarcationservice>`

- :ref:`numonitoringport.NUMonitoringPort<numonitoringport>`

- :ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`

- :ref:`nugroup.NUGroup<nugroup>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nusapingressqosprofile.NUSAPIngressQoSProfile<nusapingressqosprofile>`

- :ref:`nugatewayslocation.NUGatewaysLocation<nugatewayslocation>`

- :ref:`numulticastlist.NUMultiCastList<numulticastlist>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuingressprofile.NUIngressProfile<nuingressprofile>`

- :ref:`nudiskstat.NUDiskStat<nudiskstat>`

- :ref:`nudestinationurl.NUDestinationurl<nudestinationurl>`

- :ref:`nulink.NULink<nulink>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`nutestsuite.NUTestSuite<nutestsuite>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuptranslationmap.NUPTranslationMap<nuptranslationmap>`

- :ref:`nuwanservice.NUWANService<nuwanservice>`

- :ref:`nuoverlaymirrordestination.NUOverlayMirrorDestination<nuoverlaymirrordestination>`

- :ref:`nuvcenterdatacenter.NUVCenterDataCenter<nuvcenterdatacenter>`

- :ref:`nuvsd.NUVSD<nuvsd>`

- :ref:`nugatewaytemplate.NUGatewayTemplate<nugatewaytemplate>`

- :ref:`nuremotevrsinfo.NURemoteVrsInfo<nuremotevrsinfo>`

- :ref:`nusaasapplicationgroup.NUSaaSApplicationGroup<nusaasapplicationgroup>`

- :ref:`nuzfbrequest.NUZFBRequest<nuzfbrequest>`

- :ref:`nunsggroup.NUNSGGroup<nunsggroup>`

- :ref:`nupolicygroupcategory.NUPolicyGroupCategory<nupolicygroupcategory>`

- :ref:`nuipfilterprofile.NUIPFilterProfile<nuipfilterprofile>`

- :ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`

- :ref:`nuaddressrange.NUAddressRange<nuaddressrange>`

- :ref:`nulicensestatus.NULicenseStatus<nulicensestatus>`

- :ref:`nuroutingpolicy.NURoutingPolicy<nuroutingpolicy>`

- :ref:`nupolicyentry.NUPolicyEntry<nupolicyentry>`

- :ref:`nuapplication.NUApplication<nuapplication>`

- :ref:`nupspatmap.NUPSPATMap<nupspatmap>`

- :ref:`nuoverlayaddresspool.NUOverlayAddressPool<nuoverlayaddresspool>`

- :ref:`nucsnatpool.NUCSNATPool<nucsnatpool>`

- :ref:`nualarm.NUAlarm<nualarm>`

- :ref:`nuazurecloud.NUAzureCloud<nuazurecloud>`

- :ref:`nunsgroutingpolicybinding.NUNSGRoutingPolicyBinding<nunsgroutingpolicybinding>`

- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nuingressqospolicy.NUIngressQOSPolicy<nuingressqospolicy>`

- :ref:`nupolicystatement.NUPolicyStatement<nupolicystatement>`

- :ref:`nukeyservermonitorsek.NUKeyServerMonitorSEK<nukeyservermonitorsek>`

- :ref:`nume.NUMe<nume>`

- :ref:`nudomainkindsummary.NUDomainKindSummary<nudomainkindsummary>`

- :ref:`nusystemconfig.NUSystemConfig<nusystemconfig>`

- :ref:`nuallalarm.NUAllAlarm<nuallalarm>`

- :ref:`nucosremarkingpolicy.NUCOSRemarkingPolicy<nucosremarkingpolicy>`

- :ref:`nuducgroupbinding.NUDUCGroupBinding<nuducgroupbinding>`

- :ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`

- :ref:`nulocation.NULocation<nulocation>`

- :ref:`nuzonetemplate.NUZoneTemplate<nuzonetemplate>`

- :ref:`nubootstrapactivation.NUBootstrapActivation<nubootstrapactivation>`

- :ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`

- :ref:`nuenterprisesecurity.NUEnterpriseSecurity<nuenterprisesecurity>`

- :ref:`nunexthop.NUNextHop<nunexthop>`

- :ref:`nuikegateway.NUIKEGateway<nuikegateway>`

- :ref:`nuegressadvfwdtemplate.NUEgressAdvFwdTemplate<nuegressadvfwdtemplate>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nuratelimiter.NURateLimiter<nuratelimiter>`

- :ref:`nuunderlay.NUUnderlay<nuunderlay>`

- :ref:`nuikepsk.NUIKEPSK<nuikepsk>`

- :ref:`nuporttemplate.NUPortTemplate<nuporttemplate>`

- :ref:`nutestsuiterun.NUTestSuiteRun<nutestsuiterun>`

