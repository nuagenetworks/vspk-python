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

__all__ = ['NUAddressRangesFetcher', 'NUAggregateMetadatasFetcher', 'NUAlarmsFetcher', 'NUApplicationServicesFetcher', 'NUAppsFetcher', 'NUAutoDiscoveredGatewaysFetcher', 'NUBGPPeersFetcher', 'NUBootstrapActivationsFetcher', 'NUBootstrapsFetcher', 'NUBridgeInterfacesFetcher', 'NUCertificatesFetcher', 'NUCloudMgmtSystemsFetcher', 'NUDHCPOptionsFetcher', 'NUDiskStatsFetcher', 'NUDomainsFetcher', 'NUDomainTemplatesFetcher', 'NUDSCPForwardingClassMappingsFetcher', 'NUDSCPForwardingClassTablesFetcher', 'NUEgressACLEntryTemplatesFetcher', 'NUEgressACLTemplatesFetcher', 'NUEgressQOSPoliciesFetcher', 'NUEndPointsFetcher', 'NUEnterpriseNetworksFetcher', 'NUEnterprisePermissionsFetcher', 'NUEnterpriseProfilesFetcher', 'NUEnterprisesFetcher', 'NUEventLogsFetcher', 'NUExternalAppServicesFetcher', 'NUExternalServicesFetcher', 'NUFloatingIpsFetcher', 'NUFlowForwardingPoliciesFetcher', 'NUFlowsFetcher', 'NUFlowSecurityPoliciesFetcher', 'NUGatewaysFetcher', 'NUGatewayTemplatesFetcher', 'NUGlobalMetadatasFetcher', 'NUGroupKeyEncryptionProfilesFetcher', 'NUGroupsFetcher', 'NUHostInterfacesFetcher', 'NUHSCsFetcher', 'NUInfrastructureConfigsFetcher', 'NUInfrastructureGatewayProfilesFetcher', 'NUInfrastructurePortProfilesFetcher', 'NUInfrastructureVscProfilesFetcher', 'NUIngressACLEntryTemplatesFetcher', 'NUIngressACLTemplatesFetcher', 'NUIngressAdvFwdEntryTemplatesFetcher', 'NUIngressAdvFwdTemplatesFetcher', 'NUIngressExternalServiceTemplateEntriesFetcher', 'NUIngressExternalServiceTemplatesFetcher', 'NUIPReservationsFetcher', 'NUJobsFetcher', 'NUKeyServerMonitorEncryptedSeedsFetcher', 'NUKeyServerMonitorEncryptedSEKsFetcher', 'NUKeyServerMonitorsFetcher', 'NUKeyServerMonitorSeedsFetcher', 'NUKeyServerMonitorSEKsFetcher', 'NUL2DomainsFetcher', 'NUL2DomainTemplatesFetcher', 'NULDAPConfigurationsFetcher', 'NULicensesFetcher', 'NULocationsFetcher', 'NUMesFetcher', 'NUMetadatasFetcher', 'NUMetadataTagsFetcher', 'NUMirrorDestinationsFetcher', 'NUMonitoringPortsFetcher', 'NUMultiCastChannelMapsFetcher', 'NUMultiCastListsFetcher', 'NUMultiCastRangesFetcher', 'NUMultiNICVPortsFetcher', 'NUNATMapEntriesFetcher', 'NUNetworkLayoutsFetcher', 'NUNetworkMacroGroupsFetcher', 'NUNSGatewaysFetcher', 'NUNSGatewayTemplatesFetcher', 'NUNSPortsFetcher', 'NUNSPortStaticConfigurationsFetcher', 'NUNSPortTemplatesFetcher', 'NUNSRedundantGatewayGroupsFetcher', 'NUPATNATPoolsFetcher', 'NUPermissionsFetcher', 'NUPolicyDecisionsFetcher', 'NUPolicyGroupsFetcher', 'NUPolicyGroupTemplatesFetcher', 'NUPortsFetcher', 'NUPortTemplatesFetcher', 'NUPublicNetworkMacrosFetcher', 'NUQOSsFetcher', 'NURateLimitersFetcher', 'NURedirectionTargetsFetcher', 'NURedirectionTargetTemplatesFetcher', 'NURedundancyGroupsFetcher', 'NURedundantPortsFetcher', 'NUSharedNetworkResourcesFetcher', 'NUSiteInfosFetcher', 'NUStaticRoutesFetcher', 'NUStatisticsFetcher', 'NUStatisticsPoliciesFetcher', 'NUStatsCollectorInfosFetcher', 'NUSubnetsFetcher', 'NUSubnetTemplatesFetcher', 'NUSystemConfigsFetcher', 'NUTCAsFetcher', 'NUTiersFetcher', 'NUUplinkRDsFetcher', 'NUUsersFetcher', 'NUVCenterClustersFetcher', 'NUVCenterDataCentersFetcher', 'NUVCenterEAMConfigsFetcher', 'NUVCenterHypervisorsFetcher', 'NUVCentersFetcher', 'NUVCenterVRSConfigsFetcher', 'NUVirtualIPsFetcher', 'NUVLANsFetcher', 'NUVLANTemplatesFetcher', 'NUVMInterfacesFetcher', 'NUVMResyncsFetcher', 'NUVMsFetcher', 'NUVPNConnectionsFetcher', 'NUVPortMirrorsFetcher', 'NUVPortsFetcher', 'NUVRSAddressRangesFetcher', 'NUVRSsFetcher', 'NUVSCsFetcher', 'NUVSDComponentsFetcher', 'NUVSDsFetcher', 'NUVsgRedundantPortsFetcher', 'NUVSPsFetcher', 'NUWANServicesFetcher', 'NUZonesFetcher', 'NUZoneTemplatesFetcher']

from .nuaddressranges_fetcher import NUAddressRangesFetcher
from .nuaggregatemetadatas_fetcher import NUAggregateMetadatasFetcher
from .nualarms_fetcher import NUAlarmsFetcher
from .nuapplicationservices_fetcher import NUApplicationServicesFetcher
from .nuapps_fetcher import NUAppsFetcher
from .nuautodiscoveredgateways_fetcher import NUAutoDiscoveredGatewaysFetcher
from .nubgppeers_fetcher import NUBGPPeersFetcher
from .nubootstrapactivations_fetcher import NUBootstrapActivationsFetcher
from .nubootstraps_fetcher import NUBootstrapsFetcher
from .nubridgeinterfaces_fetcher import NUBridgeInterfacesFetcher
from .nucertificates_fetcher import NUCertificatesFetcher
from .nucloudmgmtsystems_fetcher import NUCloudMgmtSystemsFetcher
from .nudhcpoptions_fetcher import NUDHCPOptionsFetcher
from .nudiskstats_fetcher import NUDiskStatsFetcher
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
from .nueventlogs_fetcher import NUEventLogsFetcher
from .nuexternalappservices_fetcher import NUExternalAppServicesFetcher
from .nuexternalservices_fetcher import NUExternalServicesFetcher
from .nufloatingips_fetcher import NUFloatingIpsFetcher
from .nuflowforwardingpolicies_fetcher import NUFlowForwardingPoliciesFetcher
from .nuflows_fetcher import NUFlowsFetcher
from .nuflowsecuritypolicies_fetcher import NUFlowSecurityPoliciesFetcher
from .nugateways_fetcher import NUGatewaysFetcher
from .nugatewaytemplates_fetcher import NUGatewayTemplatesFetcher
from .nuglobalmetadatas_fetcher import NUGlobalMetadatasFetcher
from .nugroupkeyencryptionprofiles_fetcher import NUGroupKeyEncryptionProfilesFetcher
from .nugroups_fetcher import NUGroupsFetcher
from .nuhostinterfaces_fetcher import NUHostInterfacesFetcher
from .nuhscs_fetcher import NUHSCsFetcher
from .nuinfrastructureconfigs_fetcher import NUInfrastructureConfigsFetcher
from .nuinfrastructuregatewayprofiles_fetcher import NUInfrastructureGatewayProfilesFetcher
from .nuinfrastructureportprofiles_fetcher import NUInfrastructurePortProfilesFetcher
from .nuinfrastructurevscprofiles_fetcher import NUInfrastructureVscProfilesFetcher
from .nuingressaclentrytemplates_fetcher import NUIngressACLEntryTemplatesFetcher
from .nuingressacltemplates_fetcher import NUIngressACLTemplatesFetcher
from .nuingressadvfwdentrytemplates_fetcher import NUIngressAdvFwdEntryTemplatesFetcher
from .nuingressadvfwdtemplates_fetcher import NUIngressAdvFwdTemplatesFetcher
from .nuingressexternalservicetemplateentries_fetcher import NUIngressExternalServiceTemplateEntriesFetcher
from .nuingressexternalservicetemplates_fetcher import NUIngressExternalServiceTemplatesFetcher
from .nuipreservations_fetcher import NUIPReservationsFetcher
from .nujobs_fetcher import NUJobsFetcher
from .nukeyservermonitorencryptedseeds_fetcher import NUKeyServerMonitorEncryptedSeedsFetcher
from .nukeyservermonitorencryptedseks_fetcher import NUKeyServerMonitorEncryptedSEKsFetcher
from .nukeyservermonitors_fetcher import NUKeyServerMonitorsFetcher
from .nukeyservermonitorseeds_fetcher import NUKeyServerMonitorSeedsFetcher
from .nukeyservermonitorseks_fetcher import NUKeyServerMonitorSEKsFetcher
from .nul2domains_fetcher import NUL2DomainsFetcher
from .nul2domaintemplates_fetcher import NUL2DomainTemplatesFetcher
from .nuldapconfigurations_fetcher import NULDAPConfigurationsFetcher
from .nulicenses_fetcher import NULicensesFetcher
from .nulocations_fetcher import NULocationsFetcher
from .numes_fetcher import NUMesFetcher
from .numetadatas_fetcher import NUMetadatasFetcher
from .numetadatatags_fetcher import NUMetadataTagsFetcher
from .numirrordestinations_fetcher import NUMirrorDestinationsFetcher
from .numonitoringports_fetcher import NUMonitoringPortsFetcher
from .numulticastchannelmaps_fetcher import NUMultiCastChannelMapsFetcher
from .numulticastlists_fetcher import NUMultiCastListsFetcher
from .numulticastranges_fetcher import NUMultiCastRangesFetcher
from .numultinicvports_fetcher import NUMultiNICVPortsFetcher
from .nunatmapentries_fetcher import NUNATMapEntriesFetcher
from .nunetworklayouts_fetcher import NUNetworkLayoutsFetcher
from .nunetworkmacrogroups_fetcher import NUNetworkMacroGroupsFetcher
from .nunsgateways_fetcher import NUNSGatewaysFetcher
from .nunsgatewaytemplates_fetcher import NUNSGatewayTemplatesFetcher
from .nunsports_fetcher import NUNSPortsFetcher
from .nunsportstaticconfigurations_fetcher import NUNSPortStaticConfigurationsFetcher
from .nunsporttemplates_fetcher import NUNSPortTemplatesFetcher
from .nunsredundantgatewaygroups_fetcher import NUNSRedundantGatewayGroupsFetcher
from .nupatnatpools_fetcher import NUPATNATPoolsFetcher
from .nupermissions_fetcher import NUPermissionsFetcher
from .nupolicydecisions_fetcher import NUPolicyDecisionsFetcher
from .nupolicygroups_fetcher import NUPolicyGroupsFetcher
from .nupolicygrouptemplates_fetcher import NUPolicyGroupTemplatesFetcher
from .nuports_fetcher import NUPortsFetcher
from .nuporttemplates_fetcher import NUPortTemplatesFetcher
from .nupublicnetworkmacros_fetcher import NUPublicNetworkMacrosFetcher
from .nuqoss_fetcher import NUQOSsFetcher
from .nuratelimiters_fetcher import NURateLimitersFetcher
from .nuredirectiontargets_fetcher import NURedirectionTargetsFetcher
from .nuredirectiontargettemplates_fetcher import NURedirectionTargetTemplatesFetcher
from .nuredundancygroups_fetcher import NURedundancyGroupsFetcher
from .nuredundantports_fetcher import NURedundantPortsFetcher
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
from .nuuplinkrds_fetcher import NUUplinkRDsFetcher
from .nuusers_fetcher import NUUsersFetcher
from .nuvcenterclusters_fetcher import NUVCenterClustersFetcher
from .nuvcenterdatacenters_fetcher import NUVCenterDataCentersFetcher
from .nuvcentereamconfigs_fetcher import NUVCenterEAMConfigsFetcher
from .nuvcenterhypervisors_fetcher import NUVCenterHypervisorsFetcher
from .nuvcenters_fetcher import NUVCentersFetcher
from .nuvcentervrsconfigs_fetcher import NUVCenterVRSConfigsFetcher
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
from .nuvrss_fetcher import NUVRSsFetcher
from .nuvscs_fetcher import NUVSCsFetcher
from .nuvsdcomponents_fetcher import NUVSDComponentsFetcher
from .nuvsds_fetcher import NUVSDsFetcher
from .nuvsgredundantports_fetcher import NUVsgRedundantPortsFetcher
from .nuvsps_fetcher import NUVSPsFetcher
from .nuwanservices_fetcher import NUWANServicesFetcher
from .nuzones_fetcher import NUZonesFetcher
from .nuzonetemplates_fetcher import NUZoneTemplatesFetcher