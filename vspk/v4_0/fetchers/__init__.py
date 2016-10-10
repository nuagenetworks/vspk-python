# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__all__ = ['NUAddressMapsFetcher', 'NUAddressRangesFetcher', 'NUAggregateMetadatasFetcher', 'NUAlarmsFetcher', 'NUAllAlarmsFetcher', 'NUApplicationBindingsFetcher', 'NUApplicationperformancemanagementbindingsFetcher', 'NUApplicationperformancemanagementsFetcher', 'NUApplicationsFetcher', 'NUApplicationServicesFetcher', 'NUAutoDiscoverClustersFetcher', 'NUAutodiscovereddatacentersFetcher', 'NUAutoDiscoveredGatewaysFetcher', 'NUAutoDiscoverHypervisorFromClustersFetcher', 'NUAvatarsFetcher', 'NUBGPNeighborsFetcher', 'NUBGPPeersFetcher', 'NUBGPProfilesFetcher', 'NUBootstrapActivationsFetcher', 'NUBootstrapsFetcher', 'NUBRConnectionsFetcher', 'NUBridgeInterfacesFetcher', 'NUBulkStatisticsFetcher', 'NUCertificatesFetcher', 'NUCloudMgmtSystemsFetcher', 'NUContainerInterfacesFetcher', 'NUContainerResyncsFetcher', 'NUContainersFetcher', 'NUDemarcationServicesFetcher', 'NUDHCPOptionsFetcher', 'NUDiskStatsFetcher', 'NUDomainFIPAclTemplateEntriesFetcher', 'NUDomainFIPAclTemplatesFetcher', 'NUDomainsFetcher', 'NUDomainTemplatesFetcher', 'NUDSCPForwardingClassMappingsFetcher', 'NUDSCPForwardingClassTablesFetcher', 'NUEgressACLEntryTemplatesFetcher', 'NUEgressACLTemplatesFetcher', 'NUEgressQOSPoliciesFetcher', 'NUEndPointsFetcher', 'NUEnterpriseNetworksFetcher', 'NUEnterprisePermissionsFetcher', 'NUEnterpriseProfilesFetcher', 'NUEnterprisesFetcher', 'NUEnterpriseSecuredDatasFetcher', 'NUEnterpriseSecuritiesFetcher', 'NUEventLogsFetcher', 'NUExternalAppServicesFetcher', 'NUExternalServicesFetcher', 'NUFloatingIPACLTemplateEntriesFetcher', 'NUFloatingIPACLTemplatesFetcher', 'NUFloatingIpsFetcher', 'NUFlowForwardingPoliciesFetcher', 'NUFlowsFetcher', 'NUFlowSecurityPoliciesFetcher', 'NUGatewaysFetcher', 'NUGatewaySecuredDatasFetcher', 'NUGatewaySecuritiesFetcher', 'NUGatewayTemplatesFetcher', 'NUGlobalMetadatasFetcher', 'NUGroupKeyEncryptionProfilesFetcher', 'NUGroupsFetcher', 'NUHostInterfacesFetcher', 'NUHSCsFetcher', 'NUIKECertificatesFetcher', 'NUIKEEncryptionprofilesFetcher', 'NUIKEGatewayConfigsFetcher', 'NUIKEGatewayConnectionsFetcher', 'NUIKEGatewayProfilesFetcher', 'NUIKEGatewaysFetcher', 'NUIKEPSKsFetcher', 'NUIKESubnetsFetcher', 'NUInfrastructureaccessprofilesFetcher', 'NUInfrastructureConfigsFetcher', 'NUInfrastructureGatewayProfilesFetcher', 'NUInfrastructureVscProfilesFetcher', 'NUIngressACLEntryTemplatesFetcher', 'NUIngressACLTemplatesFetcher', 'NUIngressAdvFwdEntryTemplatesFetcher', 'NUIngressAdvFwdTemplatesFetcher', 'NUIngressExternalServiceTemplateEntriesFetcher', 'NUIngressExternalServiceTemplatesFetcher', 'NUIPReservationsFetcher', 'NUJobsFetcher', 'NUKeyServerMembersFetcher', 'NUKeyServerMonitorEncryptedSeedsFetcher', 'NUKeyServerMonitorsFetcher', 'NUKeyServerMonitorSeedsFetcher', 'NUKeyServerMonitorSEKsFetcher', 'NUKeyServerNotificationsFetcher', 'NUL2DomainsFetcher', 'NUL2DomainTemplatesFetcher', 'NUL7applicationsignaturesFetcher', 'NULDAPConfigurationsFetcher', 'NULicensesFetcher', 'NULicenseStatusFetcher', 'NULinksFetcher', 'NULocationsFetcher', 'NUMesFetcher', 'NUMetadatasFetcher', 'NUMetadataTagsFetcher', 'NUMirrorDestinationsFetcher', 'NUMonitoringPortsFetcher', 'NUMonitorscopesFetcher', 'NUMultiCastChannelMapsFetcher', 'NUMultiCastListsFetcher', 'NUMultiCastRangesFetcher', 'NUMultiNICVPortsFetcher', 'NUNATMapEntriesFetcher', 'NUNetworkLayoutsFetcher', 'NUNetworkMacroGroupsFetcher', 'NUNetworkPerformanceBindingsFetcher', 'NUNetworkPerformanceMeasurementsFetcher', 'NUNextHopAddressFetcher', 'NUNextHopsFetcher', 'NUNSGatewaysFetcher', 'NUNSGatewayTemplatesFetcher', 'NUNSGInfosFetcher', 'NUNSPortsFetcher', 'NUNSPortTemplatesFetcher', 'NUNSRedundantGatewayGroupsFetcher', 'NUOverlayAddressPoolsFetcher', 'NUOverlayPATNATEntriesFetcher', 'NUPATIPEntriesFetcher', 'NUPATMappersFetcher', 'NUPATNATPoolsFetcher', 'NUPerformanceMonitorsFetcher', 'NUPermissionsFetcher', 'NUPolicyDecisionsFetcher', 'NUPolicyGroupsFetcher', 'NUPolicyGroupTemplatesFetcher', 'NUPortMappingsFetcher', 'NUPortsFetcher', 'NUPortTemplatesFetcher', 'NUPublicNetworkMacrosFetcher', 'NUQOSsFetcher', 'NURateLimitersFetcher', 'NURedirectionTargetsFetcher', 'NURedirectionTargetTemplatesFetcher', 'NURedundancyGroupsFetcher', 'NURedundantPortsFetcher', 'NURoutingPoliciesFetcher', 'NUSharedNetworkResourcesFetcher', 'NUSiteInfosFetcher', 'NUStaticRoutesFetcher', 'NUStatisticsFetcher', 'NUStatisticsPoliciesFetcher', 'NUStatsCollectorInfosFetcher', 'NUSubnetsFetcher', 'NUSubnetTemplatesFetcher', 'NUSystemConfigsFetcher', 'NUTCAsFetcher', 'NUTiersFetcher', 'NUUplinkConnectionsFetcher', 'NUUplinkRDsFetcher', 'NUUsersFetcher', 'NUVCenterClustersFetcher', 'NUVCenterDataCentersFetcher', 'NUVCenterEAMConfigsFetcher', 'NUVCenterHypervisorsFetcher', 'NUVCentersFetcher', 'NUVCenterVRSConfigsFetcher', 'NUViasFetcher', 'NUVirtualIPsFetcher', 'NUVLANsFetcher', 'NUVLANTemplatesFetcher', 'NUVMInterfacesFetcher', 'NUVMResyncsFetcher', 'NUVMsFetcher', 'NUVPNConnectionsFetcher', 'NUVPortMirrorsFetcher', 'NUVPortsFetcher', 'NUVRSAddressRangesFetcher', 'NUVRSMetricsFetcher', 'NUVRSRedeploymentpoliciesFetcher', 'NUVRSsFetcher', 'NUVSCsFetcher', 'NUVSDComponentsFetcher', 'NUVSDsFetcher', 'NUVsgRedundantPortsFetcher', 'NUVSPsFetcher', 'NUWANServicesFetcher', 'NUZFBAutoAssignmentsFetcher', 'NUZFBRequestsFetcher', 'NUZonesFetcher', 'NUZoneTemplatesFetcher']

from .nuaddressmaps_fetcher import NUAddressMapsFetcher
from .nuaddressranges_fetcher import NUAddressRangesFetcher
from .nuaggregatemetadatas_fetcher import NUAggregateMetadatasFetcher
from .nualarms_fetcher import NUAlarmsFetcher
from .nuallalarms_fetcher import NUAllAlarmsFetcher
from .nuapplicationbindings_fetcher import NUApplicationBindingsFetcher
from .nuapplicationperformancemanagementbindings_fetcher import NUApplicationperformancemanagementbindingsFetcher
from .nuapplicationperformancemanagements_fetcher import NUApplicationperformancemanagementsFetcher
from .nuapplications_fetcher import NUApplicationsFetcher
from .nuapplicationservices_fetcher import NUApplicationServicesFetcher
from .nuautodiscoverclusters_fetcher import NUAutoDiscoverClustersFetcher
from .nuautodiscovereddatacenters_fetcher import NUAutodiscovereddatacentersFetcher
from .nuautodiscoveredgateways_fetcher import NUAutoDiscoveredGatewaysFetcher
from .nuautodiscoverhypervisorfromclusters_fetcher import NUAutoDiscoverHypervisorFromClustersFetcher
from .nuavatars_fetcher import NUAvatarsFetcher
from .nubgpneighbors_fetcher import NUBGPNeighborsFetcher
from .nubgppeers_fetcher import NUBGPPeersFetcher
from .nubgpprofiles_fetcher import NUBGPProfilesFetcher
from .nubootstrapactivations_fetcher import NUBootstrapActivationsFetcher
from .nubootstraps_fetcher import NUBootstrapsFetcher
from .nubrconnections_fetcher import NUBRConnectionsFetcher
from .nubridgeinterfaces_fetcher import NUBridgeInterfacesFetcher
from .nubulkstatistics_fetcher import NUBulkStatisticsFetcher
from .nucertificates_fetcher import NUCertificatesFetcher
from .nucloudmgmtsystems_fetcher import NUCloudMgmtSystemsFetcher
from .nucontainerinterfaces_fetcher import NUContainerInterfacesFetcher
from .nucontainerresyncs_fetcher import NUContainerResyncsFetcher
from .nucontainers_fetcher import NUContainersFetcher
from .nudemarcationservices_fetcher import NUDemarcationServicesFetcher
from .nudhcpoptions_fetcher import NUDHCPOptionsFetcher
from .nudiskstats_fetcher import NUDiskStatsFetcher
from .nudomainfipacltemplateentries_fetcher import NUDomainFIPAclTemplateEntriesFetcher
from .nudomainfipacltemplates_fetcher import NUDomainFIPAclTemplatesFetcher
from .nudomains_fetcher import NUDomainsFetcher
from .nudomaintemplates_fetcher import NUDomainTemplatesFetcher
from .nudscpforwardingclassmappings_fetcher import NUDSCPForwardingClassMappingsFetcher
from .nudscpforwardingclasstables_fetcher import NUDSCPForwardingClassTablesFetcher
from .nuegressaclentrytemplates_fetcher import NUEgressACLEntryTemplatesFetcher
from .nuegressacltemplates_fetcher import NUEgressACLTemplatesFetcher
from .nuegressqospolicies_fetcher import NUEgressQOSPoliciesFetcher
from .nuendpoints_fetcher import NUEndPointsFetcher
from .nuenterprisenetworks_fetcher import NUEnterpriseNetworksFetcher
from .nuenterprisepermissions_fetcher import NUEnterprisePermissionsFetcher
from .nuenterpriseprofiles_fetcher import NUEnterpriseProfilesFetcher
from .nuenterprises_fetcher import NUEnterprisesFetcher
from .nuenterprisesecureddatas_fetcher import NUEnterpriseSecuredDatasFetcher
from .nuenterprisesecurities_fetcher import NUEnterpriseSecuritiesFetcher
from .nueventlogs_fetcher import NUEventLogsFetcher
from .nuexternalappservices_fetcher import NUExternalAppServicesFetcher
from .nuexternalservices_fetcher import NUExternalServicesFetcher
from .nufloatingipacltemplateentries_fetcher import NUFloatingIPACLTemplateEntriesFetcher
from .nufloatingipacltemplates_fetcher import NUFloatingIPACLTemplatesFetcher
from .nufloatingips_fetcher import NUFloatingIpsFetcher
from .nuflowforwardingpolicies_fetcher import NUFlowForwardingPoliciesFetcher
from .nuflows_fetcher import NUFlowsFetcher
from .nuflowsecuritypolicies_fetcher import NUFlowSecurityPoliciesFetcher
from .nugateways_fetcher import NUGatewaysFetcher
from .nugatewaysecureddatas_fetcher import NUGatewaySecuredDatasFetcher
from .nugatewaysecurities_fetcher import NUGatewaySecuritiesFetcher
from .nugatewaytemplates_fetcher import NUGatewayTemplatesFetcher
from .nuglobalmetadatas_fetcher import NUGlobalMetadatasFetcher
from .nugroupkeyencryptionprofiles_fetcher import NUGroupKeyEncryptionProfilesFetcher
from .nugroups_fetcher import NUGroupsFetcher
from .nuhostinterfaces_fetcher import NUHostInterfacesFetcher
from .nuhscs_fetcher import NUHSCsFetcher
from .nuikecertificates_fetcher import NUIKECertificatesFetcher
from .nuikeencryptionprofiles_fetcher import NUIKEEncryptionprofilesFetcher
from .nuikegatewayconfigs_fetcher import NUIKEGatewayConfigsFetcher
from .nuikegatewayconnections_fetcher import NUIKEGatewayConnectionsFetcher
from .nuikegatewayprofiles_fetcher import NUIKEGatewayProfilesFetcher
from .nuikegateways_fetcher import NUIKEGatewaysFetcher
from .nuikepsks_fetcher import NUIKEPSKsFetcher
from .nuikesubnets_fetcher import NUIKESubnetsFetcher
from .nuinfrastructureaccessprofiles_fetcher import NUInfrastructureaccessprofilesFetcher
from .nuinfrastructureconfigs_fetcher import NUInfrastructureConfigsFetcher
from .nuinfrastructuregatewayprofiles_fetcher import NUInfrastructureGatewayProfilesFetcher
from .nuinfrastructurevscprofiles_fetcher import NUInfrastructureVscProfilesFetcher
from .nuingressaclentrytemplates_fetcher import NUIngressACLEntryTemplatesFetcher
from .nuingressacltemplates_fetcher import NUIngressACLTemplatesFetcher
from .nuingressadvfwdentrytemplates_fetcher import NUIngressAdvFwdEntryTemplatesFetcher
from .nuingressadvfwdtemplates_fetcher import NUIngressAdvFwdTemplatesFetcher
from .nuingressexternalservicetemplateentries_fetcher import NUIngressExternalServiceTemplateEntriesFetcher
from .nuingressexternalservicetemplates_fetcher import NUIngressExternalServiceTemplatesFetcher
from .nuipreservations_fetcher import NUIPReservationsFetcher
from .nujobs_fetcher import NUJobsFetcher
from .nukeyservermembers_fetcher import NUKeyServerMembersFetcher
from .nukeyservermonitorencryptedseeds_fetcher import NUKeyServerMonitorEncryptedSeedsFetcher
from .nukeyservermonitors_fetcher import NUKeyServerMonitorsFetcher
from .nukeyservermonitorseeds_fetcher import NUKeyServerMonitorSeedsFetcher
from .nukeyservermonitorseks_fetcher import NUKeyServerMonitorSEKsFetcher
from .nukeyservernotifications_fetcher import NUKeyServerNotificationsFetcher
from .nul2domains_fetcher import NUL2DomainsFetcher
from .nul2domaintemplates_fetcher import NUL2DomainTemplatesFetcher
from .nul7applicationsignatures_fetcher import NUL7applicationsignaturesFetcher
from .nuldapconfigurations_fetcher import NULDAPConfigurationsFetcher
from .nulicenses_fetcher import NULicensesFetcher
from .nulicensestatus_fetcher import NULicenseStatusFetcher
from .nulinks_fetcher import NULinksFetcher
from .nulocations_fetcher import NULocationsFetcher
from .numes_fetcher import NUMesFetcher
from .numetadatas_fetcher import NUMetadatasFetcher
from .numetadatatags_fetcher import NUMetadataTagsFetcher
from .numirrordestinations_fetcher import NUMirrorDestinationsFetcher
from .numonitoringports_fetcher import NUMonitoringPortsFetcher
from .numonitorscopes_fetcher import NUMonitorscopesFetcher
from .numulticastchannelmaps_fetcher import NUMultiCastChannelMapsFetcher
from .numulticastlists_fetcher import NUMultiCastListsFetcher
from .numulticastranges_fetcher import NUMultiCastRangesFetcher
from .numultinicvports_fetcher import NUMultiNICVPortsFetcher
from .nunatmapentries_fetcher import NUNATMapEntriesFetcher
from .nunetworklayouts_fetcher import NUNetworkLayoutsFetcher
from .nunetworkmacrogroups_fetcher import NUNetworkMacroGroupsFetcher
from .nunetworkperformancebindings_fetcher import NUNetworkPerformanceBindingsFetcher
from .nunetworkperformancemeasurements_fetcher import NUNetworkPerformanceMeasurementsFetcher
from .nunexthopaddress_fetcher import NUNextHopAddressFetcher
from .nunexthops_fetcher import NUNextHopsFetcher
from .nunsgateways_fetcher import NUNSGatewaysFetcher
from .nunsgatewaytemplates_fetcher import NUNSGatewayTemplatesFetcher
from .nunsginfos_fetcher import NUNSGInfosFetcher
from .nunsports_fetcher import NUNSPortsFetcher
from .nunsporttemplates_fetcher import NUNSPortTemplatesFetcher
from .nunsredundantgatewaygroups_fetcher import NUNSRedundantGatewayGroupsFetcher
from .nuoverlayaddresspools_fetcher import NUOverlayAddressPoolsFetcher
from .nuoverlaypatnatentries_fetcher import NUOverlayPATNATEntriesFetcher
from .nupatipentries_fetcher import NUPATIPEntriesFetcher
from .nupatmappers_fetcher import NUPATMappersFetcher
from .nupatnatpools_fetcher import NUPATNATPoolsFetcher
from .nuperformancemonitors_fetcher import NUPerformanceMonitorsFetcher
from .nupermissions_fetcher import NUPermissionsFetcher
from .nupolicydecisions_fetcher import NUPolicyDecisionsFetcher
from .nupolicygroups_fetcher import NUPolicyGroupsFetcher
from .nupolicygrouptemplates_fetcher import NUPolicyGroupTemplatesFetcher
from .nuportmappings_fetcher import NUPortMappingsFetcher
from .nuports_fetcher import NUPortsFetcher
from .nuporttemplates_fetcher import NUPortTemplatesFetcher
from .nupublicnetworkmacros_fetcher import NUPublicNetworkMacrosFetcher
from .nuqoss_fetcher import NUQOSsFetcher
from .nuratelimiters_fetcher import NURateLimitersFetcher
from .nuredirectiontargets_fetcher import NURedirectionTargetsFetcher
from .nuredirectiontargettemplates_fetcher import NURedirectionTargetTemplatesFetcher
from .nuredundancygroups_fetcher import NURedundancyGroupsFetcher
from .nuredundantports_fetcher import NURedundantPortsFetcher
from .nuroutingpolicies_fetcher import NURoutingPoliciesFetcher
from .nusharednetworkresources_fetcher import NUSharedNetworkResourcesFetcher
from .nusiteinfos_fetcher import NUSiteInfosFetcher
from .nustaticroutes_fetcher import NUStaticRoutesFetcher
from .nustatistics_fetcher import NUStatisticsFetcher
from .nustatisticspolicies_fetcher import NUStatisticsPoliciesFetcher
from .nustatscollectorinfos_fetcher import NUStatsCollectorInfosFetcher
from .nusubnets_fetcher import NUSubnetsFetcher
from .nusubnettemplates_fetcher import NUSubnetTemplatesFetcher
from .nusystemconfigs_fetcher import NUSystemConfigsFetcher
from .nutcas_fetcher import NUTCAsFetcher
from .nutiers_fetcher import NUTiersFetcher
from .nuuplinkconnections_fetcher import NUUplinkConnectionsFetcher
from .nuuplinkrds_fetcher import NUUplinkRDsFetcher
from .nuusers_fetcher import NUUsersFetcher
from .nuvcenterclusters_fetcher import NUVCenterClustersFetcher
from .nuvcenterdatacenters_fetcher import NUVCenterDataCentersFetcher
from .nuvcentereamconfigs_fetcher import NUVCenterEAMConfigsFetcher
from .nuvcenterhypervisors_fetcher import NUVCenterHypervisorsFetcher
from .nuvcenters_fetcher import NUVCentersFetcher
from .nuvcentervrsconfigs_fetcher import NUVCenterVRSConfigsFetcher
from .nuvias_fetcher import NUViasFetcher
from .nuvirtualips_fetcher import NUVirtualIPsFetcher
from .nuvlans_fetcher import NUVLANsFetcher
from .nuvlantemplates_fetcher import NUVLANTemplatesFetcher
from .nuvminterfaces_fetcher import NUVMInterfacesFetcher
from .nuvmresyncs_fetcher import NUVMResyncsFetcher
from .nuvms_fetcher import NUVMsFetcher
from .nuvpnconnections_fetcher import NUVPNConnectionsFetcher
from .nuvportmirrors_fetcher import NUVPortMirrorsFetcher
from .nuvports_fetcher import NUVPortsFetcher
from .nuvrsaddressranges_fetcher import NUVRSAddressRangesFetcher
from .nuvrsmetrics_fetcher import NUVRSMetricsFetcher
from .nuvrsredeploymentpolicies_fetcher import NUVRSRedeploymentpoliciesFetcher
from .nuvrss_fetcher import NUVRSsFetcher
from .nuvscs_fetcher import NUVSCsFetcher
from .nuvsdcomponents_fetcher import NUVSDComponentsFetcher
from .nuvsds_fetcher import NUVSDsFetcher
from .nuvsgredundantports_fetcher import NUVsgRedundantPortsFetcher
from .nuvsps_fetcher import NUVSPsFetcher
from .nuwanservices_fetcher import NUWANServicesFetcher
from .nuzfbautoassignments_fetcher import NUZFBAutoAssignmentsFetcher
from .nuzfbrequests_fetcher import NUZFBRequestsFetcher
from .nuzones_fetcher import NUZonesFetcher
from .nuzonetemplates_fetcher import NUZoneTemplatesFetcher