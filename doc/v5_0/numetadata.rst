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


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nugroupkeyencryptionprofile.NUGroupKeyEncryptionProfile<nugroupkeyencryptionprofile>`

- :ref:`nuipfilterprofile.NUIPFilterProfile<nuipfilterprofile>`

- :ref:`nuqos.NUQOS<nuqos>`

- :ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`

- :ref:`nubgppeer.NUBGPPeer<nubgppeer>`

- :ref:`nuikepsk.NUIKEPSK<nuikepsk>`

- :ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`

- :ref:`nuoverlaymirrordestination.NUOverlayMirrorDestination<nuoverlaymirrordestination>`

- :ref:`nuvirtualip.NUVirtualIP<nuvirtualip>`

- :ref:`nupspatmap.NUPSPATMap<nupspatmap>`

- :ref:`nuegressadvfwdentrytemplate.NUEgressAdvFwdEntryTemplate<nuegressadvfwdentrytemplate>`

- :ref:`nudscpforwardingclasstable.NUDSCPForwardingClassTable<nudscpforwardingclasstable>`

- :ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`

- :ref:`nutca.NUTCA<nutca>`

- :ref:`nusapegressqosprofile.NUSAPEgressQoSProfile<nusapegressqosprofile>`

- :ref:`numacfilterprofile.NUMACFilterProfile<numacfilterprofile>`

- :ref:`nuvnfdescriptor.NUVNFDescriptor<nuvnfdescriptor>`

- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nuapplication.NUApplication<nuapplication>`

- :ref:`nuikegatewayprofile.NUIKEGatewayProfile<nuikegatewayprofile>`

- :ref:`nuikesubnet.NUIKESubnet<nuikesubnet>`

- :ref:`nuinfrastructuregatewayprofile.NUInfrastructureGatewayProfile<nuinfrastructuregatewayprofile>`

- :ref:`nudiskstat.NUDiskStat<nudiskstat>`

- :ref:`nuegressadvfwdtemplate.NUEgressAdvFwdTemplate<nuegressadvfwdtemplate>`

- :ref:`nuvnfinterface.NUVNFInterface<nuvnfinterface>`

- :ref:`nuvcentereamconfig.NUVCenterEAMConfig<nuvcentereamconfig>`

- :ref:`nuroutingpolicy.NURoutingPolicy<nuroutingpolicy>`

- :ref:`nuenterprisesecurity.NUEnterpriseSecurity<nuenterprisesecurity>`

- :ref:`nucloudmgmtsystem.NUCloudMgmtSystem<nucloudmgmtsystem>`

- :ref:`nuvcentervrsconfig.NUVCenterVRSConfig<nuvcentervrsconfig>`

- :ref:`nuducgroup.NUDUCGroup<nuducgroup>`

- :ref:`nunexthop.NUNextHop<nunexthop>`

- :ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`

- :ref:`nuinfrastructurevscprofile.NUInfrastructureVscProfile<nuinfrastructurevscprofile>`

- :ref:`nupermission.NUPermission<nupermission>`

- :ref:`nucosremarkingpolicy.NUCOSRemarkingPolicy<nucosremarkingpolicy>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuipreservation.NUIPReservation<nuipreservation>`

- :ref:`nuoverlayaddresspool.NUOverlayAddressPool<nuoverlayaddresspool>`

- :ref:`nuratelimiter.NURateLimiter<nuratelimiter>`

- :ref:`nuredirectiontargettemplate.NURedirectionTargetTemplate<nuredirectiontargettemplate>`

- :ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`

- :ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`

- :ref:`nuwanservice.NUWANService<nuwanservice>`

- :ref:`nuikegatewayconnection.NUIKEGatewayConnection<nuikegatewayconnection>`

- :ref:`nuvnfdomainmapping.NUVNFDomainMapping<nuvnfdomainmapping>`

- :ref:`nufirewallacl.NUFirewallAcl<nufirewallacl>`

- :ref:`nugatewayredundantport.NUGatewayRedundantPort<nugatewayredundantport>`

- :ref:`nunetworklayout.NUNetworkLayout<nunetworklayout>`

- :ref:`nuvnfinterfacedescriptor.NUVNFInterfaceDescriptor<nuvnfinterfacedescriptor>`

- :ref:`nupatch.NUPatch<nupatch>`

- :ref:`nunsggroup.NUNSGGroup<nunsggroup>`

- :ref:`nuvsdcomponent.NUVSDComponent<nuvsdcomponent>`

- :ref:`nuavatar.NUAvatar<nuavatar>`

- :ref:`nuinfrastructureevdfprofile.NUInfrastructureEVDFProfile<nuinfrastructureevdfprofile>`

- :ref:`nubootstrapactivation.NUBootstrapActivation<nubootstrapactivation>`

- :ref:`nulicensestatus.NULicenseStatus<nulicensestatus>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nuipv6filterprofile.NUIPv6FilterProfile<nuipv6filterprofile>`

- :ref:`nuvsp.NUVSP<nuvsp>`

- :ref:`nusaasapplicationtype.NUSaaSApplicationType<nusaasapplicationtype>`

- :ref:`numirrordestination.NUMirrorDestination<numirrordestination>`

- :ref:`nunetconfsession.NUNetconfSession<nunetconfsession>`

- :ref:`nunetconfprofile.NUNetconfProfile<nunetconfprofile>`

- :ref:`nuredundantport.NURedundantPort<nuredundantport>`

- :ref:`nuvnfthresholdpolicy.NUVNFThresholdPolicy<nuvnfthresholdpolicy>`

- :ref:`nussidconnection.NUSSIDConnection<nussidconnection>`

- :ref:`nuaddressmap.NUAddressMap<nuaddressmap>`

- :ref:`nuoverlaypatnatentry.NUOverlayPATNATEntry<nuoverlaypatnatentry>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nutier.NUTier<nutier>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nuingressqospolicy.NUIngressQOSPolicy<nuingressqospolicy>`

- :ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`

- :ref:`nupolicygroupcategory.NUPolicyGroupCategory<nupolicygroupcategory>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nucontainer.NUContainer<nucontainer>`

- :ref:`nuldapconfiguration.NULDAPConfiguration<nuldapconfiguration>`

- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nukeyservermonitorencryptedseed.NUKeyServerMonitorEncryptedSeed<nukeyservermonitorencryptedseed>`

- :ref:`nugatewaytemplate.NUGatewayTemplate<nugatewaytemplate>`

- :ref:`nuallgateway.NUAllGateway<nuallgateway>`

- :ref:`nucertificate.NUCertificate<nucertificate>`

- :ref:`nuzonetemplate.NUZoneTemplate<nuzonetemplate>`

- :ref:`nukeyservermonitorseed.NUKeyServerMonitorSeed<nukeyservermonitorseed>`

- :ref:`nulteinformation.NULTEInformation<nulteinformation>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuoverlaymirrordestinationtemplate.NUOverlayMirrorDestinationTemplate<nuoverlaymirrordestinationtemplate>`

- :ref:`nuforwardingpathlist.NUForwardingPathList<nuforwardingpathlist>`

- :ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`

- :ref:`nuzfbrequest.NUZFBRequest<nuzfbrequest>`

- :ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`

- :ref:`nustaticroute.NUStaticRoute<nustaticroute>`

- :ref:`nuconnectionendpoint.NUConnectionendpoint<nuconnectionendpoint>`

- :ref:`nujob.NUJob<nujob>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nugatewaysecureddata.NUGatewaySecuredData<nugatewaysecureddata>`

- :ref:`nutrunk.NUTrunk<nutrunk>`

- :ref:`nugroup.NUGroup<nugroup>`

- :ref:`nupolicyentry.NUPolicyEntry<nupolicyentry>`

- :ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`

- :ref:`nuqospolicer.NUQosPolicer<nuqospolicer>`

- :ref:`nuusercontext.NUUserContext<nuusercontext>`

- :ref:`nulicense.NULicense<nulicense>`

- :ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`

- :ref:`nunetconfmanager.NUNetconfManager<nunetconfmanager>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nuvcentercluster.NUVCenterCluster<nuvcentercluster>`

- :ref:`numulticastrange.NUMultiCastRange<numulticastrange>`

- :ref:`nuegressprofile.NUEgressProfile<nuegressprofile>`

- :ref:`nunetworkmacrogroup.NUNetworkMacroGroup<nunetworkmacrogroup>`

- :ref:`nudscpremarkingpolicy.NUDSCPRemarkingPolicy<nudscpremarkingpolicy>`

- :ref:`nuinfrastructureaccessprofile.NUInfrastructureAccessProfile<nuinfrastructureaccessprofile>`

- :ref:`nuapplicationbinding.NUApplicationBinding<nuapplicationbinding>`

- :ref:`nudestinationurl.NUDestinationurl<nudestinationurl>`

- :ref:`nuvnfcatalog.NUVNFCatalog<nuvnfcatalog>`

- :ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`

- :ref:`nuforwardingpathlistentry.NUForwardingPathListEntry<nuforwardingpathlistentry>`

- :ref:`nuegressqospolicy.NUEgressQOSPolicy<nuegressqospolicy>`

- :ref:`nuvcenterhypervisor.NUVCenterHypervisor<nuvcenterhypervisor>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nunatmapentry.NUNATMapEntry<nunatmapentry>`

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

- :ref:`nupolicyobjectgroup.NUPolicyObjectGroup<nupolicyobjectgroup>`

- :ref:`nuvirtualfirewallrule.NUVirtualFirewallRule<nuvirtualfirewallrule>`

- :ref:`nudscpremarkingpolicytable.NUDSCPRemarkingPolicyTable<nudscpremarkingpolicytable>`

- :ref:`nuptranslationmap.NUPTranslationMap<nuptranslationmap>`

- :ref:`nuwebdomainname.NUWebDomainName<nuwebdomainname>`

- :ref:`nuikegatewayconfig.NUIKEGatewayConfig<nuikegatewayconfig>`

- :ref:`nucsnatpool.NUCSNATPool<nucsnatpool>`

- :ref:`nushuntlink.NUShuntLink<nushuntlink>`

- :ref:`nuvcenter.NUVCenter<nuvcenter>`

- :ref:`nubulkstatistics.NUBulkStatistics<nubulkstatistics>`

- :ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`

- :ref:`nultestatistics.NULtestatistics<nultestatistics>`

- :ref:`nulocation.NULocation<nulocation>`

- :ref:`nunetworkperformancebinding.NUNetworkPerformanceBinding<nunetworkperformancebinding>`

- :ref:`nudscpforwardingclassmapping.NUDSCPForwardingClassMapping<nudscpforwardingclassmapping>`

- :ref:`nudefaultgateway.NUDefaultGateway<nudefaultgateway>`

- :ref:`nusaasapplicationgroup.NUSaaSApplicationGroup<nusaasapplicationgroup>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuikegateway.NUIKEGateway<nuikegateway>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nuenterprisesecureddata.NUEnterpriseSecuredData<nuenterprisesecureddata>`

- :ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`

- :ref:`nuducgroupbinding.NUDUCGroupBinding<nuducgroupbinding>`

- :ref:`nuikecertificate.NUIKECertificate<nuikecertificate>`

- :ref:`nustatscollectorinfo.NUStatsCollectorInfo<nustatscollectorinfo>`

- :ref:`nuporttemplate.NUPortTemplate<nuporttemplate>`

- :ref:`nugatewayslocation.NUGatewaysLocation<nugatewayslocation>`

- :ref:`nul7applicationsignature.NUL7applicationsignature<nul7applicationsignature>`

- :ref:`nuospfinstance.NUOSPFInstance<nuospfinstance>`

- :ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`

- :ref:`nukeyservermember.NUKeyServerMember<nukeyservermember>`

- :ref:`nupolicystatement.NUPolicyStatement<nupolicystatement>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`

- :ref:`nuuplinkrd.NUUplinkRD<nuuplinkrd>`

- :ref:`nuvm.NUVM<nuvm>`

- :ref:`nuvsd.NUVSD<nuvsd>`

- :ref:`nunsgroutingpolicybinding.NUNSGRoutingPolicyBinding<nunsgroutingpolicybinding>`

- :ref:`nunsgatewayscount.NUNSGatewaysCount<nunsgatewayscount>`

- :ref:`nubootstrap.NUBootstrap<nubootstrap>`

- :ref:`nubgpprofile.NUBGPProfile<nubgpprofile>`

- :ref:`nuctranslationmap.NUCTranslationMap<nuctranslationmap>`

- :ref:`nupublicnetworkmacro.NUPublicNetworkMacro<nupublicnetworkmacro>`

- :ref:`nudomainfipacltemplateentry.NUDomainFIPAclTemplateEntry<nudomainfipacltemplateentry>`

- :ref:`nuaddressrange.NUAddressRange<nuaddressrange>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nusiteinfo.NUSiteInfo<nusiteinfo>`

- :ref:`nunsgatewaysummary.NUNSGatewaySummary<nunsgatewaysummary>`

- :ref:`nuvirtualfirewallpolicy.NUVirtualFirewallPolicy<nuvirtualfirewallpolicy>`

- :ref:`nuvmresync.NUVMResync<nuvmresync>`

- :ref:`nugatewaysecurity.NUGatewaySecurity<nugatewaysecurity>`

- :ref:`nupolicydecision.NUPolicyDecision<nupolicydecision>`

- :ref:`nuapplicationperformancemanagementbinding.NUApplicationperformancemanagementbinding<nuapplicationperformancemanagementbinding>`

- :ref:`nuspatsourcespool.NUSPATSourcesPool<nuspatsourcespool>`

- :ref:`nualarm.NUAlarm<nualarm>`

- :ref:`nufloatingip.NUFloatingIp<nufloatingip>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`numonitoringport.NUMonitoringPort<numonitoringport>`

- :ref:`nuvnfmetadata.NUVNFMetadata<nuvnfmetadata>`

- :ref:`nusapingressqosprofile.NUSAPIngressQoSProfile<nusapingressqosprofile>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`nukeyservermonitorsek.NUKeyServerMonitorSEK<nukeyservermonitorsek>`

- :ref:`nucosremarkingpolicytable.NUCOSRemarkingPolicyTable<nucosremarkingpolicytable>`

- :ref:`nuvportmirror.NUVPortMirror<nuvportmirror>`

- :ref:`nupsnatpool.NUPSNATPool<nupsnatpool>`

- :ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`

- :ref:`nuvpnconnection.NUVPNConnection<nuvpnconnection>`

- :ref:`nucontainerresync.NUContainerResync<nucontainerresync>`

- :ref:`nuvnf.NUVNF<nuvnf>`

- :ref:`nuallredundancygroup.NUAllRedundancyGroup<nuallredundancygroup>`

- :ref:`nuallalarm.NUAllAlarm<nuallalarm>`

- :ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`

- :ref:`nusystemconfig.NUSystemConfig<nusystemconfig>`

- :ref:`nuikeencryptionprofile.NUIKEEncryptionprofile<nuikeencryptionprofile>`

- :ref:`nupolicygrouptemplate.NUPolicyGroupTemplate<nupolicygrouptemplate>`

- :ref:`nuinfrastructureconfig.NUInfrastructureConfig<nuinfrastructureconfig>`

- :ref:`nuingressprofile.NUIngressProfile<nuingressprofile>`

- :ref:`nubrconnection.NUBRConnection<nubrconnection>`

- :ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`

- :ref:`numulticastlist.NUMultiCastList<numulticastlist>`

- :ref:`nudemarcationservice.NUDemarcationService<nudemarcationservice>`

- :ref:`nufirewallrule.NUFirewallRule<nufirewallrule>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nuvrsaddressrange.NUVRSAddressRange<nuvrsaddressrange>`

- :ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`

- :ref:`nuuplinkconnection.NUUplinkConnection<nuuplinkconnection>`

- :ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`

- :ref:`nunetworkperformancemeasurement.NUNetworkPerformanceMeasurement<nunetworkperformancemeasurement>`

- :ref:`nuospfarea.NUOSPFArea<nuospfarea>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nulink.NULink<nulink>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

- :ref:`numonitorscope.NUMonitorscope<numonitorscope>`

