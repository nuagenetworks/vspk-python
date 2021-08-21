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

- :ref:`nuoverlaymirrordestination.NUOverlayMirrorDestination<nuoverlaymirrordestination>`

- :ref:`nuvirtualip.NUVirtualIP<nuvirtualip>`

- :ref:`nupspatmap.NUPSPATMap<nupspatmap>`

- :ref:`nuegressadvfwdentrytemplate.NUEgressAdvFwdEntryTemplate<nuegressadvfwdentrytemplate>`

- :ref:`nudscpforwardingclasstable.NUDSCPForwardingClassTable<nudscpforwardingclasstable>`

- :ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nuconnectionendpoint.NUConnectionendpoint<nuconnectionendpoint>`

- :ref:`nutca.NUTCA<nutca>`

- :ref:`nusapegressqosprofile.NUSAPEgressQoSProfile<nusapegressqosprofile>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`numacfilterprofile.NUMACFilterProfile<numacfilterprofile>`

- :ref:`nugroup.NUGroup<nugroup>`

- :ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nuikesubnet.NUIKESubnet<nuikesubnet>`

- :ref:`nuinfrastructuregatewayprofile.NUInfrastructureGatewayProfile<nuinfrastructuregatewayprofile>`

- :ref:`nudiskstat.NUDiskStat<nudiskstat>`

- :ref:`nuegressadvfwdtemplate.NUEgressAdvFwdTemplate<nuegressadvfwdtemplate>`

- :ref:`nuvnfinterface.NUVNFInterface<nuvnfinterface>`

- :ref:`nuvcentereamconfig.NUVCenterEAMConfig<nuvcentereamconfig>`

- :ref:`nulocation.NULocation<nulocation>`

- :ref:`nuenterprisesecurity.NUEnterpriseSecurity<nuenterprisesecurity>`

- :ref:`nuvcentervrsconfig.NUVCenterVRSConfig<nuvcentervrsconfig>`

- :ref:`nuducgroup.NUDUCGroup<nuducgroup>`

- :ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`

- :ref:`nuinfrastructurevscprofile.NUInfrastructureVscProfile<nuinfrastructurevscprofile>`

- :ref:`nusapingressqosprofile.NUSAPIngressQoSProfile<nusapingressqosprofile>`

- :ref:`nucosremarkingpolicy.NUCOSRemarkingPolicy<nucosremarkingpolicy>`

- :ref:`nuipreservation.NUIPReservation<nuipreservation>`

- :ref:`nuredirectiontargettemplate.NURedirectionTargetTemplate<nuredirectiontargettemplate>`

- :ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`

- :ref:`nuapplicationbinding.NUApplicationBinding<nuapplicationbinding>`

- :ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`

- :ref:`nuwanservice.NUWANService<nuwanservice>`

- :ref:`nuikegatewayconnection.NUIKEGatewayConnection<nuikegatewayconnection>`

- :ref:`nuvnfdomainmapping.NUVNFDomainMapping<nuvnfdomainmapping>`

- :ref:`nufirewallacl.NUFirewallAcl<nufirewallacl>`

- :ref:`nugatewayredundantport.NUGatewayRedundantPort<nugatewayredundantport>`

- :ref:`nunetworklayout.NUNetworkLayout<nunetworklayout>`

- :ref:`nuvnfinterfacedescriptor.NUVNFInterfaceDescriptor<nuvnfinterfacedescriptor>`

- :ref:`nupatch.NUPatch<nupatch>`

- :ref:`nuvsdcomponent.NUVSDComponent<nuvsdcomponent>`

- :ref:`nuavatar.NUAvatar<nuavatar>`

- :ref:`nuoverlayaddresspool.NUOverlayAddressPool<nuoverlayaddresspool>`

- :ref:`nubootstrapactivation.NUBootstrapActivation<nubootstrapactivation>`

- :ref:`nulicensestatus.NULicenseStatus<nulicensestatus>`

- :ref:`nucloudmgmtsystem.NUCloudMgmtSystem<nucloudmgmtsystem>`

- :ref:`nuipv6filterprofile.NUIPv6FilterProfile<nuipv6filterprofile>`

- :ref:`nuvsp.NUVSP<nuvsp>`

- :ref:`nusaasapplicationtype.NUSaaSApplicationType<nusaasapplicationtype>`

- :ref:`numirrordestination.NUMirrorDestination<numirrordestination>`

- :ref:`nunetconfsession.NUNetconfSession<nunetconfsession>`

- :ref:`nunetconfprofile.NUNetconfProfile<nunetconfprofile>`

- :ref:`nuredundantport.NURedundantPort<nuredundantport>`

- :ref:`nunsggroup.NUNSGGroup<nunsggroup>`

- :ref:`nuvnfthresholdpolicy.NUVNFThresholdPolicy<nuvnfthresholdpolicy>`

- :ref:`nupolicyobjectgroup.NUPolicyObjectGroup<nupolicyobjectgroup>`

- :ref:`nuporttemplate.NUPortTemplate<nuporttemplate>`

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

- :ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`

- :ref:`nuforwardingpathlist.NUForwardingPathList<nuforwardingpathlist>`

- :ref:`nukeyservermonitorencryptedseed.NUKeyServerMonitorEncryptedSeed<nukeyservermonitorencryptedseed>`

- :ref:`nupolicyentry.NUPolicyEntry<nupolicyentry>`

- :ref:`nuuplinkrd.NUUplinkRD<nuuplinkrd>`

- :ref:`nukeyservermonitorseed.NUKeyServerMonitorSeed<nukeyservermonitorseed>`

- :ref:`nugatewaytemplate.NUGatewayTemplate<nugatewaytemplate>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuoverlaymirrordestinationtemplate.NUOverlayMirrorDestinationTemplate<nuoverlaymirrordestinationtemplate>`

- :ref:`nuldapconfiguration.NULDAPConfiguration<nuldapconfiguration>`

- :ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`

- :ref:`nuzfbrequest.NUZFBRequest<nuzfbrequest>`

- :ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`

- :ref:`nustaticroute.NUStaticRoute<nustaticroute>`

- :ref:`nuinfrastructureevdfprofile.NUInfrastructureEVDFProfile<nuinfrastructureevdfprofile>`

- :ref:`nujob.NUJob<nujob>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nugatewaysecureddata.NUGatewaySecuredData<nugatewaysecureddata>`

- :ref:`nutrunk.NUTrunk<nutrunk>`

- :ref:`nuvnfdescriptor.NUVNFDescriptor<nuvnfdescriptor>`

- :ref:`nuptranslationmap.NUPTranslationMap<nuptranslationmap>`

- :ref:`nuducgroupbinding.NUDUCGroupBinding<nuducgroupbinding>`

- :ref:`nueventlog.NUEventLog<nueventlog>`

- :ref:`nulicense.NULicense<nulicense>`

- :ref:`nuikeencryptionprofile.NUIKEEncryptionprofile<nuikeencryptionprofile>`

- :ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`

- :ref:`nunetconfmanager.NUNetconfManager<nunetconfmanager>`

- :ref:`nulteinformation.NULTEInformation<nulteinformation>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nuinfrastructureconfig.NUInfrastructureConfig<nuinfrastructureconfig>`

- :ref:`nudscpremarkingpolicy.NUDSCPRemarkingPolicy<nudscpremarkingpolicy>`

- :ref:`nupermission.NUPermission<nupermission>`

- :ref:`nuegressprofile.NUEgressProfile<nuegressprofile>`

- :ref:`nunetworkmacrogroup.NUNetworkMacroGroup<nunetworkmacrogroup>`

- :ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`

- :ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`

- :ref:`nuallgateway.NUAllGateway<nuallgateway>`

- :ref:`nudestinationurl.NUDestinationurl<nudestinationurl>`

- :ref:`nuvnfcatalog.NUVNFCatalog<nuvnfcatalog>`

- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nuforwardingpathlistentry.NUForwardingPathListEntry<nuforwardingpathlistentry>`

- :ref:`numulticastlist.NUMultiCastList<numulticastlist>`

- :ref:`nunexthop.NUNextHop<nunexthop>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nutier.NUTier<nutier>`

- :ref:`nudomainfipacltemplate.NUDomainFIPAclTemplate<nudomainfipacltemplate>`

- :ref:`nuospfinterface.NUOSPFInterface<nuospfinterface>`

- :ref:`nuaddressmap.NUAddressMap<nuaddressmap>`

- :ref:`nuunderlay.NUUnderlay<nuunderlay>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`numultinicvport.NUMultiNICVPort<numultinicvport>`

- :ref:`nuwebcategory.NUWebCategory<nuwebcategory>`

- :ref:`nubfdsession.NUBFDSession<nubfdsession>`

- :ref:`nustatistics.NUStatistics<nustatistics>`

- :ref:`nunsporttemplate.NUNSPortTemplate<nunsporttemplate>`

- :ref:`nusshkey.NUSSHKey<nusshkey>`

- :ref:`nucertificate.NUCertificate<nucertificate>`

- :ref:`nuvcenterdatacenter.NUVCenterDataCenter<nuvcenterdatacenter>`

- :ref:`nucustomproperty.NUCustomProperty<nucustomproperty>`

- :ref:`nultestatistics.NULtestatistics<nultestatistics>`

- :ref:`nuvirtualfirewallrule.NUVirtualFirewallRule<nuvirtualfirewallrule>`

- :ref:`nudomainfipacltemplateentry.NUDomainFIPAclTemplateEntry<nudomainfipacltemplateentry>`

- :ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`

- :ref:`nuwebdomainname.NUWebDomainName<nuwebdomainname>`

- :ref:`nuikegatewayconfig.NUIKEGatewayConfig<nuikegatewayconfig>`

- :ref:`nucsnatpool.NUCSNATPool<nucsnatpool>`

- :ref:`nushuntlink.NUShuntLink<nushuntlink>`

- :ref:`nuvcenter.NUVCenter<nuvcenter>`

- :ref:`nubulkstatistics.NUBulkStatistics<nubulkstatistics>`

- :ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`

- :ref:`nuroutingpolicy.NURoutingPolicy<nuroutingpolicy>`

- :ref:`numulticastrange.NUMultiCastRange<numulticastrange>`

- :ref:`nunetworkperformancebinding.NUNetworkPerformanceBinding<nunetworkperformancebinding>`

- :ref:`nudscpforwardingclassmapping.NUDSCPForwardingClassMapping<nudscpforwardingclassmapping>`

- :ref:`nudefaultgateway.NUDefaultGateway<nudefaultgateway>`

- :ref:`nusaasapplicationgroup.NUSaaSApplicationGroup<nusaasapplicationgroup>`

- :ref:`nugatewayslocation.NUGatewaysLocation<nugatewayslocation>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuikegateway.NUIKEGateway<nuikegateway>`

- :ref:`nuingressprofile.NUIngressProfile<nuingressprofile>`

- :ref:`nuenterprisesecureddata.NUEnterpriseSecuredData<nuenterprisesecureddata>`

- :ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`

- :ref:`nuqospolicer.NUQosPolicer<nuqospolicer>`

- :ref:`nuikecertificate.NUIKECertificate<nuikecertificate>`

- :ref:`nustatscollectorinfo.NUStatsCollectorInfo<nustatscollectorinfo>`

- :ref:`nussidconnection.NUSSIDConnection<nussidconnection>`

- :ref:`nuusercontext.NUUserContext<nuusercontext>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nul7applicationsignature.NUL7applicationsignature<nul7applicationsignature>`

- :ref:`nuospfinstance.NUOSPFInstance<nuospfinstance>`

- :ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`

- :ref:`nukeyservermember.NUKeyServerMember<nukeyservermember>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`

- :ref:`nuzonetemplate.NUZoneTemplate<nuzonetemplate>`

- :ref:`nusiteinfo.NUSiteInfo<nusiteinfo>`

- :ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`

- :ref:`nunsgroutingpolicybinding.NUNSGRoutingPolicyBinding<nunsgroutingpolicybinding>`

- :ref:`nunsgatewayscount.NUNSGatewaysCount<nunsgatewayscount>`

- :ref:`nuvrsaddressrange.NUVRSAddressRange<nuvrsaddressrange>`

- :ref:`nubgpprofile.NUBGPProfile<nubgpprofile>`

- :ref:`nuegressqospolicy.NUEgressQOSPolicy<nuegressqospolicy>`

- :ref:`nupublicnetworkmacro.NUPublicNetworkMacro<nupublicnetworkmacro>`

- :ref:`nudscpremarkingpolicytable.NUDSCPRemarkingPolicyTable<nudscpremarkingpolicytable>`

- :ref:`nuingressqospolicy.NUIngressQOSPolicy<nuingressqospolicy>`

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

- :ref:`nuvnfmetadata.NUVNFMetadata<nuvnfmetadata>`

- :ref:`nuipfilterprofile.NUIPFilterProfile<nuipfilterprofile>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nuapplication.NUApplication<nuapplication>`

- :ref:`nukeyservermonitorsek.NUKeyServerMonitorSEK<nukeyservermonitorsek>`

- :ref:`nucosremarkingpolicytable.NUCOSRemarkingPolicyTable<nucosremarkingpolicytable>`

- :ref:`nuvportmirror.NUVPortMirror<nuvportmirror>`

- :ref:`nupsnatpool.NUPSNATPool<nupsnatpool>`

- :ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`

- :ref:`nucontainerresync.NUContainerResync<nucontainerresync>`

- :ref:`nuvnf.NUVNF<nuvnf>`

- :ref:`nuallredundancygroup.NUAllRedundancyGroup<nuallredundancygroup>`

- :ref:`nuallalarm.NUAllAlarm<nuallalarm>`

- :ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`

- :ref:`nusystemconfig.NUSystemConfig<nusystemconfig>`

- :ref:`nuratelimiter.NURateLimiter<nuratelimiter>`

- :ref:`nupolicygrouptemplate.NUPolicyGroupTemplate<nupolicygrouptemplate>`

- :ref:`nuvcentercluster.NUVCenterCluster<nuvcentercluster>`

- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nunatmapentry.NUNATMapEntry<nunatmapentry>`

- :ref:`nucontainer.NUContainer<nucontainer>`

- :ref:`nudemarcationservice.NUDemarcationService<nudemarcationservice>`

- :ref:`nubrconnection.NUBRConnection<nubrconnection>`

- :ref:`nuikegatewayprofile.NUIKEGatewayProfile<nuikegatewayprofile>`

- :ref:`nufirewallrule.NUFirewallRule<nufirewallrule>`

- :ref:`nualarm.NUAlarm<nualarm>`

- :ref:`nubootstrap.NUBootstrap<nubootstrap>`

- :ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`

- :ref:`nuuplinkconnection.NUUplinkConnection<nuuplinkconnection>`

- :ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`

- :ref:`nunetworkperformancemeasurement.NUNetworkPerformanceMeasurement<nunetworkperformancemeasurement>`

- :ref:`nuospfarea.NUOSPFArea<nuospfarea>`

- :ref:`nuikepsk.NUIKEPSK<nuikepsk>`

- :ref:`nuctranslationmap.NUCTranslationMap<nuctranslationmap>`

- :ref:`nulink.NULink<nulink>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

- :ref:`numonitorscope.NUMonitorscope<numonitorscope>`

- :ref:`nuvcenterhypervisor.NUVCenterHypervisor<nuvcenterhypervisor>`

