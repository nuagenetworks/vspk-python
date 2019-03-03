# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc, 2017 Nokia
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


__all__ = ['NUVSDSession', 'NUAddressMap', 'NUAddressRange', 'NUAggregateMetadata', 'NUAlarm', 'NUAllAlarm', 'NUAllGateway', 'NUAllRedundancyGroup', 'NUApplication', 'NUApplicationBinding', 'NUApplicationperformancemanagement', 'NUApplicationperformancemanagementbinding', 'NUAutoDiscoverCluster', 'NUAutodiscovereddatacenter', 'NUAutoDiscoveredGateway', 'NUAutoDiscoverHypervisorFromCluster', 'NUAvatar', 'NUBFDSession', 'NUBGPNeighbor', 'NUBGPPeer', 'NUBGPProfile', 'NUBootstrap', 'NUBootstrapActivation', 'NUBRConnection', 'NUBridgeInterface', 'NUBulkStatistics', 'NUCaptivePortalProfile', 'NUCertificate', 'NUCloudMgmtSystem', 'NUCommand', 'NUConnectionendpoint', 'NUContainer', 'NUContainerInterface', 'NUContainerResync', 'NUCOSRemarkingPolicy', 'NUCOSRemarkingPolicyTable', 'NUCSNATPool', 'NUCTranslationMap', 'NUCustomProperty', 'NUDefaultGateway', 'NUDemarcationService', 'NUDeploymentFailure', 'NUDestinationurl', 'NUDHCPOption', 'NUDiskStat', 'NUDomain', 'NUDomainFIPAclTemplate', 'NUDomainFIPAclTemplateEntry', 'NUDomainTemplate', 'NUDownloadProgress', 'NUDSCPForwardingClassMapping', 'NUDSCPForwardingClassTable', 'NUDSCPRemarkingPolicy', 'NUDSCPRemarkingPolicyTable', 'NUDUCGroup', 'NUDUCGroupBinding', 'NUEgressACLEntryTemplate', 'NUEgressACLTemplate', 'NUEgressAdvFwdEntryTemplate', 'NUEgressAdvFwdTemplate', 'NUEgressProfile', 'NUEgressQOSPolicy', 'NUEnterprise', 'NUEnterpriseNetwork', 'NUEnterprisePermission', 'NUEnterpriseProfile', 'NUEnterpriseSecuredData', 'NUEnterpriseSecurity', 'NUEventLog', 'NUFirewallAcl', 'NUFirewallRule', 'NUFloatingIp', 'NUForwardingPathList', 'NUForwardingPathListEntry', 'NUGateway', 'NUGatewayRedundantPort', 'NUGatewaySecuredData', 'NUGatewaySecurity', 'NUGatewaysLocation', 'NUGatewayTemplate', 'NUGlobalMetadata', 'NUGroup', 'NUGroupKeyEncryptionProfile', 'NUHostInterface', 'NUHSC', 'NUIKECertificate', 'NUIKEEncryptionprofile', 'NUIKEGateway', 'NUIKEGatewayConfig', 'NUIKEGatewayConnection', 'NUIKEGatewayProfile', 'NUIKEPSK', 'NUIKESubnet', 'NUInfrastructureAccessProfile', 'NUInfrastructureConfig', 'NUInfrastructureEVDFProfile', 'NUInfrastructureGatewayProfile', 'NUInfrastructureVscProfile', 'NUIngressACLEntryTemplate', 'NUIngressACLTemplate', 'NUIngressAdvFwdEntryTemplate', 'NUIngressAdvFwdTemplate', 'NUIngressProfile', 'NUIngressQOSPolicy', 'NUIPFilterProfile', 'NUIPReservation', 'NUIPv6FilterProfile', 'NUJob', 'NUKeyServerMember', 'NUKeyServerMonitor', 'NUKeyServerMonitorEncryptedSeed', 'NUKeyServerMonitorSeed', 'NUKeyServerMonitorSEK', 'NUL2Domain', 'NUL2DomainTemplate', 'NUL4Service', 'NUL4ServiceGroup', 'NUL7applicationsignature', 'NULDAPConfiguration', 'NULicense', 'NULicenseStatus', 'NULink', 'NULocation', 'NULTEInformation', 'NULtestatistics', 'NUMACFilterProfile', 'NUMe', 'NUMetadata', 'NUMirrorDestination', 'NUMonitoringPort', 'NUMonitorscope', 'NUMultiCastChannelMap', 'NUMultiCastList', 'NUMultiCastRange', 'NUMultiNICVPort', 'NUNATMapEntry', 'NUNetconfManager', 'NUNetconfProfile', 'NUNetconfSession', 'NUNetworkLayout', 'NUNetworkMacroGroup', 'NUNetworkPerformanceBinding', 'NUNetworkPerformanceMeasurement', 'NUNextHop', 'NUNSGateway', 'NUNSGatewayMonitor', 'NUNSGatewaysCount', 'NUNSGatewaySummary', 'NUNSGatewayTemplate', 'NUNSGGroup', 'NUNSGInfo', 'NUNSGPatchProfile', 'NUNSGRoutingPolicyBinding', 'NUNSGUpgradeProfile', 'NUNSPort', 'NUNSPortInfo', 'NUNSPortTemplate', 'NUNSRedundantGatewayGroup', 'NUOSPFArea', 'NUOSPFInstance', 'NUOSPFInterface', 'NUOverlayAddressPool', 'NUOverlayManagementProfile', 'NUOverlayManagementSubnetProfile', 'NUOverlayMirrorDestination', 'NUOverlayMirrorDestinationTemplate', 'NUOverlayPATNATEntry', 'NUPatch', 'NUPATIPEntry', 'NUPATMapper', 'NUPATNATPool', 'NUPerformanceMonitor', 'NUPermission', 'NUPGExpression', 'NUPGExpressionTemplate', 'NUPolicyDecision', 'NUPolicyEntry', 'NUPolicyGroup', 'NUPolicyGroupCategory', 'NUPolicyGroupTemplate', 'NUPolicyObjectGroup', 'NUPolicyStatement', 'NUPort', 'NUPortMapping', 'NUPortTemplate', 'NUProxyARPFilter', 'NUPSNATPool', 'NUPSPATMap', 'NUPTranslationMap', 'NUPublicNetworkMacro', 'NUQOS', 'NUQosPolicer', 'NURateLimiter', 'NURedirectionTarget', 'NURedirectionTargetTemplate', 'NURedundancyGroup', 'NURedundantPort', 'NURoutingPolicy', 'NUSaaSApplicationGroup', 'NUSaaSApplicationType', 'NUSAPEgressQoSProfile', 'NUSAPIngressQoSProfile', 'NUSharedNetworkResource', 'NUShuntLink', 'NUSiteInfo', 'NUSPATSourcesPool', 'NUSSHKey', 'NUSSIDConnection', 'NUStaticRoute', 'NUStatistics', 'NUStatisticsPolicy', 'NUStatsCollectorInfo', 'NUSubnet', 'NUSubnetTemplate', 'NUSyslogDestination', 'NUSystemConfig', 'NUTCA', 'NUTier', 'NUTrunk', 'NUUnderlay', 'NUUplinkConnection', 'NUUplinkRD', 'NUUser', 'NUUserContext', 'NUVCenter', 'NUVCenterCluster', 'NUVCenterDataCenter', 'NUVCenterEAMConfig', 'NUVCenterHypervisor', 'NUVCenterVRSConfig', 'NUVirtualFirewallPolicy', 'NUVirtualFirewallRule', 'NUVirtualIP', 'NUVLAN', 'NUVLANTemplate', 'NUVM', 'NUVMInterface', 'NUVMResync', 'NUVNF', 'NUVNFCatalog', 'NUVNFDescriptor', 'NUVNFDomainMapping', 'NUVNFInterface', 'NUVNFInterfaceDescriptor', 'NUVNFMetadata', 'NUVNFThresholdPolicy', 'NUVPNConnection', 'NUVPort', 'NUVPortMirror', 'NUVRS', 'NUVRSAddressRange', 'NUVRSMetrics', 'NUVRSRedeploymentpolicy', 'NUVSC', 'NUVSD', 'NUVSDComponent', 'NUVsgRedundantPort', 'NUVSP', 'NUWANService', 'NUWebCategory', 'NUWebDomainName', 'NUWirelessPort', 'NUZFBAutoAssignment', 'NUZFBRequest', 'NUZone', 'NUZoneTemplate']

from .nuaddressmap import NUAddressMap
from .nuaddressrange import NUAddressRange
from .nuaggregatemetadata import NUAggregateMetadata
from .nualarm import NUAlarm
from .nuallalarm import NUAllAlarm
from .nuallgateway import NUAllGateway
from .nuallredundancygroup import NUAllRedundancyGroup
from .nuapplication import NUApplication
from .nuapplicationbinding import NUApplicationBinding
from .nuapplicationperformancemanagement import NUApplicationperformancemanagement
from .nuapplicationperformancemanagementbinding import NUApplicationperformancemanagementbinding
from .nuautodiscovercluster import NUAutoDiscoverCluster
from .nuautodiscovereddatacenter import NUAutodiscovereddatacenter
from .nuautodiscoveredgateway import NUAutoDiscoveredGateway
from .nuautodiscoverhypervisorfromcluster import NUAutoDiscoverHypervisorFromCluster
from .nuavatar import NUAvatar
from .nubfdsession import NUBFDSession
from .nubgpneighbor import NUBGPNeighbor
from .nubgppeer import NUBGPPeer
from .nubgpprofile import NUBGPProfile
from .nubootstrap import NUBootstrap
from .nubootstrapactivation import NUBootstrapActivation
from .nubrconnection import NUBRConnection
from .nubridgeinterface import NUBridgeInterface
from .nubulkstatistics import NUBulkStatistics
from .nucaptiveportalprofile import NUCaptivePortalProfile
from .nucertificate import NUCertificate
from .nucloudmgmtsystem import NUCloudMgmtSystem
from .nucommand import NUCommand
from .nuconnectionendpoint import NUConnectionendpoint
from .nucontainer import NUContainer
from .nucontainerinterface import NUContainerInterface
from .nucontainerresync import NUContainerResync
from .nucosremarkingpolicy import NUCOSRemarkingPolicy
from .nucosremarkingpolicytable import NUCOSRemarkingPolicyTable
from .nucsnatpool import NUCSNATPool
from .nuctranslationmap import NUCTranslationMap
from .nucustomproperty import NUCustomProperty
from .nudefaultgateway import NUDefaultGateway
from .nudemarcationservice import NUDemarcationService
from .nudeploymentfailure import NUDeploymentFailure
from .nudestinationurl import NUDestinationurl
from .nudhcpoption import NUDHCPOption
from .nudiskstat import NUDiskStat
from .nudomain import NUDomain
from .nudomainfipacltemplate import NUDomainFIPAclTemplate
from .nudomainfipacltemplateentry import NUDomainFIPAclTemplateEntry
from .nudomaintemplate import NUDomainTemplate
from .nudownloadprogress import NUDownloadProgress
from .nudscpforwardingclassmapping import NUDSCPForwardingClassMapping
from .nudscpforwardingclasstable import NUDSCPForwardingClassTable
from .nudscpremarkingpolicy import NUDSCPRemarkingPolicy
from .nudscpremarkingpolicytable import NUDSCPRemarkingPolicyTable
from .nuducgroup import NUDUCGroup
from .nuducgroupbinding import NUDUCGroupBinding
from .nuegressaclentrytemplate import NUEgressACLEntryTemplate
from .nuegressacltemplate import NUEgressACLTemplate
from .nuegressadvfwdentrytemplate import NUEgressAdvFwdEntryTemplate
from .nuegressadvfwdtemplate import NUEgressAdvFwdTemplate
from .nuegressprofile import NUEgressProfile
from .nuegressqospolicy import NUEgressQOSPolicy
from .nuenterprise import NUEnterprise
from .nuenterprisenetwork import NUEnterpriseNetwork
from .nuenterprisepermission import NUEnterprisePermission
from .nuenterpriseprofile import NUEnterpriseProfile
from .nuenterprisesecureddata import NUEnterpriseSecuredData
from .nuenterprisesecurity import NUEnterpriseSecurity
from .nueventlog import NUEventLog
from .nufirewallacl import NUFirewallAcl
from .nufirewallrule import NUFirewallRule
from .nufloatingip import NUFloatingIp
from .nuforwardingpathlist import NUForwardingPathList
from .nuforwardingpathlistentry import NUForwardingPathListEntry
from .nugateway import NUGateway
from .nugatewayredundantport import NUGatewayRedundantPort
from .nugatewaysecureddata import NUGatewaySecuredData
from .nugatewaysecurity import NUGatewaySecurity
from .nugatewayslocation import NUGatewaysLocation
from .nugatewaytemplate import NUGatewayTemplate
from .nuglobalmetadata import NUGlobalMetadata
from .nugroup import NUGroup
from .nugroupkeyencryptionprofile import NUGroupKeyEncryptionProfile
from .nuhostinterface import NUHostInterface
from .nuhsc import NUHSC
from .nuikecertificate import NUIKECertificate
from .nuikeencryptionprofile import NUIKEEncryptionprofile
from .nuikegateway import NUIKEGateway
from .nuikegatewayconfig import NUIKEGatewayConfig
from .nuikegatewayconnection import NUIKEGatewayConnection
from .nuikegatewayprofile import NUIKEGatewayProfile
from .nuikepsk import NUIKEPSK
from .nuikesubnet import NUIKESubnet
from .nuinfrastructureaccessprofile import NUInfrastructureAccessProfile
from .nuinfrastructureconfig import NUInfrastructureConfig
from .nuinfrastructureevdfprofile import NUInfrastructureEVDFProfile
from .nuinfrastructuregatewayprofile import NUInfrastructureGatewayProfile
from .nuinfrastructurevscprofile import NUInfrastructureVscProfile
from .nuingressaclentrytemplate import NUIngressACLEntryTemplate
from .nuingressacltemplate import NUIngressACLTemplate
from .nuingressadvfwdentrytemplate import NUIngressAdvFwdEntryTemplate
from .nuingressadvfwdtemplate import NUIngressAdvFwdTemplate
from .nuingressprofile import NUIngressProfile
from .nuingressqospolicy import NUIngressQOSPolicy
from .nuipfilterprofile import NUIPFilterProfile
from .nuipreservation import NUIPReservation
from .nuipv6filterprofile import NUIPv6FilterProfile
from .nujob import NUJob
from .nukeyservermember import NUKeyServerMember
from .nukeyservermonitor import NUKeyServerMonitor
from .nukeyservermonitorencryptedseed import NUKeyServerMonitorEncryptedSeed
from .nukeyservermonitorseed import NUKeyServerMonitorSeed
from .nukeyservermonitorsek import NUKeyServerMonitorSEK
from .nul2domain import NUL2Domain
from .nul2domaintemplate import NUL2DomainTemplate
from .nul4service import NUL4Service
from .nul4servicegroup import NUL4ServiceGroup
from .nul7applicationsignature import NUL7applicationsignature
from .nuldapconfiguration import NULDAPConfiguration
from .nulicense import NULicense
from .nulicensestatus import NULicenseStatus
from .nulink import NULink
from .nulocation import NULocation
from .nulteinformation import NULTEInformation
from .nultestatistics import NULtestatistics
from .numacfilterprofile import NUMACFilterProfile
from .nume import NUMe
from .numetadata import NUMetadata
from .numirrordestination import NUMirrorDestination
from .numonitoringport import NUMonitoringPort
from .numonitorscope import NUMonitorscope
from .numulticastchannelmap import NUMultiCastChannelMap
from .numulticastlist import NUMultiCastList
from .numulticastrange import NUMultiCastRange
from .numultinicvport import NUMultiNICVPort
from .nunatmapentry import NUNATMapEntry
from .nunetconfmanager import NUNetconfManager
from .nunetconfprofile import NUNetconfProfile
from .nunetconfsession import NUNetconfSession
from .nunetworklayout import NUNetworkLayout
from .nunetworkmacrogroup import NUNetworkMacroGroup
from .nunetworkperformancebinding import NUNetworkPerformanceBinding
from .nunetworkperformancemeasurement import NUNetworkPerformanceMeasurement
from .nunexthop import NUNextHop
from .nunsgateway import NUNSGateway
from .nunsgatewaymonitor import NUNSGatewayMonitor
from .nunsgatewayscount import NUNSGatewaysCount
from .nunsgatewaysummary import NUNSGatewaySummary
from .nunsgatewaytemplate import NUNSGatewayTemplate
from .nunsggroup import NUNSGGroup
from .nunsginfo import NUNSGInfo
from .nunsgpatchprofile import NUNSGPatchProfile
from .nunsgroutingpolicybinding import NUNSGRoutingPolicyBinding
from .nunsgupgradeprofile import NUNSGUpgradeProfile
from .nunsport import NUNSPort
from .nunsportinfo import NUNSPortInfo
from .nunsporttemplate import NUNSPortTemplate
from .nunsredundantgatewaygroup import NUNSRedundantGatewayGroup
from .nuospfarea import NUOSPFArea
from .nuospfinstance import NUOSPFInstance
from .nuospfinterface import NUOSPFInterface
from .nuoverlayaddresspool import NUOverlayAddressPool
from .nuoverlaymanagementprofile import NUOverlayManagementProfile
from .nuoverlaymanagementsubnetprofile import NUOverlayManagementSubnetProfile
from .nuoverlaymirrordestination import NUOverlayMirrorDestination
from .nuoverlaymirrordestinationtemplate import NUOverlayMirrorDestinationTemplate
from .nuoverlaypatnatentry import NUOverlayPATNATEntry
from .nupatch import NUPatch
from .nupatipentry import NUPATIPEntry
from .nupatmapper import NUPATMapper
from .nupatnatpool import NUPATNATPool
from .nuperformancemonitor import NUPerformanceMonitor
from .nupermission import NUPermission
from .nupgexpression import NUPGExpression
from .nupgexpressiontemplate import NUPGExpressionTemplate
from .nupolicydecision import NUPolicyDecision
from .nupolicyentry import NUPolicyEntry
from .nupolicygroup import NUPolicyGroup
from .nupolicygroupcategory import NUPolicyGroupCategory
from .nupolicygrouptemplate import NUPolicyGroupTemplate
from .nupolicyobjectgroup import NUPolicyObjectGroup
from .nupolicystatement import NUPolicyStatement
from .nuport import NUPort
from .nuportmapping import NUPortMapping
from .nuporttemplate import NUPortTemplate
from .nuproxyarpfilter import NUProxyARPFilter
from .nupsnatpool import NUPSNATPool
from .nupspatmap import NUPSPATMap
from .nuptranslationmap import NUPTranslationMap
from .nupublicnetworkmacro import NUPublicNetworkMacro
from .nuqos import NUQOS
from .nuqospolicer import NUQosPolicer
from .nuratelimiter import NURateLimiter
from .nuredirectiontarget import NURedirectionTarget
from .nuredirectiontargettemplate import NURedirectionTargetTemplate
from .nuredundancygroup import NURedundancyGroup
from .nuredundantport import NURedundantPort
from .nuroutingpolicy import NURoutingPolicy
from .nusaasapplicationgroup import NUSaaSApplicationGroup
from .nusaasapplicationtype import NUSaaSApplicationType
from .nusapegressqosprofile import NUSAPEgressQoSProfile
from .nusapingressqosprofile import NUSAPIngressQoSProfile
from .nusharednetworkresource import NUSharedNetworkResource
from .nushuntlink import NUShuntLink
from .nusiteinfo import NUSiteInfo
from .nuspatsourcespool import NUSPATSourcesPool
from .nusshkey import NUSSHKey
from .nussidconnection import NUSSIDConnection
from .nustaticroute import NUStaticRoute
from .nustatistics import NUStatistics
from .nustatisticspolicy import NUStatisticsPolicy
from .nustatscollectorinfo import NUStatsCollectorInfo
from .nusubnet import NUSubnet
from .nusubnettemplate import NUSubnetTemplate
from .nusyslogdestination import NUSyslogDestination
from .nusystemconfig import NUSystemConfig
from .nutca import NUTCA
from .nutier import NUTier
from .nutrunk import NUTrunk
from .nuunderlay import NUUnderlay
from .nuuplinkconnection import NUUplinkConnection
from .nuuplinkrd import NUUplinkRD
from .nuuser import NUUser
from .nuusercontext import NUUserContext
from .nuvcenter import NUVCenter
from .nuvcentercluster import NUVCenterCluster
from .nuvcenterdatacenter import NUVCenterDataCenter
from .nuvcentereamconfig import NUVCenterEAMConfig
from .nuvcenterhypervisor import NUVCenterHypervisor
from .nuvcentervrsconfig import NUVCenterVRSConfig
from .nuvirtualfirewallpolicy import NUVirtualFirewallPolicy
from .nuvirtualfirewallrule import NUVirtualFirewallRule
from .nuvirtualip import NUVirtualIP
from .nuvlan import NUVLAN
from .nuvlantemplate import NUVLANTemplate
from .nuvm import NUVM
from .nuvminterface import NUVMInterface
from .nuvmresync import NUVMResync
from .nuvnf import NUVNF
from .nuvnfcatalog import NUVNFCatalog
from .nuvnfdescriptor import NUVNFDescriptor
from .nuvnfdomainmapping import NUVNFDomainMapping
from .nuvnfinterface import NUVNFInterface
from .nuvnfinterfacedescriptor import NUVNFInterfaceDescriptor
from .nuvnfmetadata import NUVNFMetadata
from .nuvnfthresholdpolicy import NUVNFThresholdPolicy
from .nuvpnconnection import NUVPNConnection
from .nuvport import NUVPort
from .nuvportmirror import NUVPortMirror
from .nuvrs import NUVRS
from .nuvrsaddressrange import NUVRSAddressRange
from .nuvrsmetrics import NUVRSMetrics
from .nuvrsredeploymentpolicy import NUVRSRedeploymentpolicy
from .nuvsc import NUVSC
from .nuvsd import NUVSD
from .nuvsdcomponent import NUVSDComponent
from .nuvsgredundantport import NUVsgRedundantPort
from .nuvsp import NUVSP
from .nuwanservice import NUWANService
from .nuwebcategory import NUWebCategory
from .nuwebdomainname import NUWebDomainName
from .nuwirelessport import NUWirelessPort
from .nuzfbautoassignment import NUZFBAutoAssignment
from .nuzfbrequest import NUZFBRequest
from .nuzone import NUZone
from .nuzonetemplate import NUZoneTemplate
from .nuvsdsession import NUVSDSession
from .sdkinfo import SDKInfo

def __setup_bambou():
    """ Avoid having bad behavior when using importlib.import_module method
    """
    import pkg_resources
    from bambou import BambouConfig, NURESTModelController

    default_attrs = pkg_resources.resource_filename(__name__, '/resources/attrs_defaults.ini')
    BambouConfig.set_default_values_config_file(default_attrs)

    NURESTModelController.register_model(NUAddressMap)
    NURESTModelController.register_model(NUAddressRange)
    NURESTModelController.register_model(NUAggregateMetadata)
    NURESTModelController.register_model(NUAlarm)
    NURESTModelController.register_model(NUAllAlarm)
    NURESTModelController.register_model(NUAllGateway)
    NURESTModelController.register_model(NUAllRedundancyGroup)
    NURESTModelController.register_model(NUApplication)
    NURESTModelController.register_model(NUApplicationBinding)
    NURESTModelController.register_model(NUApplicationperformancemanagement)
    NURESTModelController.register_model(NUApplicationperformancemanagementbinding)
    NURESTModelController.register_model(NUAutoDiscoverCluster)
    NURESTModelController.register_model(NUAutodiscovereddatacenter)
    NURESTModelController.register_model(NUAutoDiscoveredGateway)
    NURESTModelController.register_model(NUAutoDiscoverHypervisorFromCluster)
    NURESTModelController.register_model(NUAvatar)
    NURESTModelController.register_model(NUBFDSession)
    NURESTModelController.register_model(NUBGPNeighbor)
    NURESTModelController.register_model(NUBGPPeer)
    NURESTModelController.register_model(NUBGPProfile)
    NURESTModelController.register_model(NUBootstrap)
    NURESTModelController.register_model(NUBootstrapActivation)
    NURESTModelController.register_model(NUBRConnection)
    NURESTModelController.register_model(NUBridgeInterface)
    NURESTModelController.register_model(NUBulkStatistics)
    NURESTModelController.register_model(NUCaptivePortalProfile)
    NURESTModelController.register_model(NUCertificate)
    NURESTModelController.register_model(NUCloudMgmtSystem)
    NURESTModelController.register_model(NUCommand)
    NURESTModelController.register_model(NUConnectionendpoint)
    NURESTModelController.register_model(NUContainer)
    NURESTModelController.register_model(NUContainerInterface)
    NURESTModelController.register_model(NUContainerResync)
    NURESTModelController.register_model(NUCOSRemarkingPolicy)
    NURESTModelController.register_model(NUCOSRemarkingPolicyTable)
    NURESTModelController.register_model(NUCSNATPool)
    NURESTModelController.register_model(NUCTranslationMap)
    NURESTModelController.register_model(NUCustomProperty)
    NURESTModelController.register_model(NUDefaultGateway)
    NURESTModelController.register_model(NUDemarcationService)
    NURESTModelController.register_model(NUDeploymentFailure)
    NURESTModelController.register_model(NUDestinationurl)
    NURESTModelController.register_model(NUDHCPOption)
    NURESTModelController.register_model(NUDiskStat)
    NURESTModelController.register_model(NUDomain)
    NURESTModelController.register_model(NUDomainFIPAclTemplate)
    NURESTModelController.register_model(NUDomainFIPAclTemplateEntry)
    NURESTModelController.register_model(NUDomainTemplate)
    NURESTModelController.register_model(NUDownloadProgress)
    NURESTModelController.register_model(NUDSCPForwardingClassMapping)
    NURESTModelController.register_model(NUDSCPForwardingClassTable)
    NURESTModelController.register_model(NUDSCPRemarkingPolicy)
    NURESTModelController.register_model(NUDSCPRemarkingPolicyTable)
    NURESTModelController.register_model(NUDUCGroup)
    NURESTModelController.register_model(NUDUCGroupBinding)
    NURESTModelController.register_model(NUEgressACLEntryTemplate)
    NURESTModelController.register_model(NUEgressACLTemplate)
    NURESTModelController.register_model(NUEgressAdvFwdEntryTemplate)
    NURESTModelController.register_model(NUEgressAdvFwdTemplate)
    NURESTModelController.register_model(NUEgressProfile)
    NURESTModelController.register_model(NUEgressQOSPolicy)
    NURESTModelController.register_model(NUEnterprise)
    NURESTModelController.register_model(NUEnterpriseNetwork)
    NURESTModelController.register_model(NUEnterprisePermission)
    NURESTModelController.register_model(NUEnterpriseProfile)
    NURESTModelController.register_model(NUEnterpriseSecuredData)
    NURESTModelController.register_model(NUEnterpriseSecurity)
    NURESTModelController.register_model(NUEventLog)
    NURESTModelController.register_model(NUFirewallAcl)
    NURESTModelController.register_model(NUFirewallRule)
    NURESTModelController.register_model(NUFloatingIp)
    NURESTModelController.register_model(NUForwardingPathList)
    NURESTModelController.register_model(NUForwardingPathListEntry)
    NURESTModelController.register_model(NUGateway)
    NURESTModelController.register_model(NUGatewayRedundantPort)
    NURESTModelController.register_model(NUGatewaySecuredData)
    NURESTModelController.register_model(NUGatewaySecurity)
    NURESTModelController.register_model(NUGatewaysLocation)
    NURESTModelController.register_model(NUGatewayTemplate)
    NURESTModelController.register_model(NUGlobalMetadata)
    NURESTModelController.register_model(NUGroup)
    NURESTModelController.register_model(NUGroupKeyEncryptionProfile)
    NURESTModelController.register_model(NUHostInterface)
    NURESTModelController.register_model(NUHSC)
    NURESTModelController.register_model(NUIKECertificate)
    NURESTModelController.register_model(NUIKEEncryptionprofile)
    NURESTModelController.register_model(NUIKEGateway)
    NURESTModelController.register_model(NUIKEGatewayConfig)
    NURESTModelController.register_model(NUIKEGatewayConnection)
    NURESTModelController.register_model(NUIKEGatewayProfile)
    NURESTModelController.register_model(NUIKEPSK)
    NURESTModelController.register_model(NUIKESubnet)
    NURESTModelController.register_model(NUInfrastructureAccessProfile)
    NURESTModelController.register_model(NUInfrastructureConfig)
    NURESTModelController.register_model(NUInfrastructureEVDFProfile)
    NURESTModelController.register_model(NUInfrastructureGatewayProfile)
    NURESTModelController.register_model(NUInfrastructureVscProfile)
    NURESTModelController.register_model(NUIngressACLEntryTemplate)
    NURESTModelController.register_model(NUIngressACLTemplate)
    NURESTModelController.register_model(NUIngressAdvFwdEntryTemplate)
    NURESTModelController.register_model(NUIngressAdvFwdTemplate)
    NURESTModelController.register_model(NUIngressProfile)
    NURESTModelController.register_model(NUIngressQOSPolicy)
    NURESTModelController.register_model(NUIPFilterProfile)
    NURESTModelController.register_model(NUIPReservation)
    NURESTModelController.register_model(NUIPv6FilterProfile)
    NURESTModelController.register_model(NUJob)
    NURESTModelController.register_model(NUKeyServerMember)
    NURESTModelController.register_model(NUKeyServerMonitor)
    NURESTModelController.register_model(NUKeyServerMonitorEncryptedSeed)
    NURESTModelController.register_model(NUKeyServerMonitorSeed)
    NURESTModelController.register_model(NUKeyServerMonitorSEK)
    NURESTModelController.register_model(NUL2Domain)
    NURESTModelController.register_model(NUL2DomainTemplate)
    NURESTModelController.register_model(NUL4Service)
    NURESTModelController.register_model(NUL4ServiceGroup)
    NURESTModelController.register_model(NUL7applicationsignature)
    NURESTModelController.register_model(NULDAPConfiguration)
    NURESTModelController.register_model(NULicense)
    NURESTModelController.register_model(NULicenseStatus)
    NURESTModelController.register_model(NULink)
    NURESTModelController.register_model(NULocation)
    NURESTModelController.register_model(NULTEInformation)
    NURESTModelController.register_model(NULtestatistics)
    NURESTModelController.register_model(NUMACFilterProfile)
    NURESTModelController.register_model(NUMe)
    NURESTModelController.register_model(NUMetadata)
    NURESTModelController.register_model(NUMirrorDestination)
    NURESTModelController.register_model(NUMonitoringPort)
    NURESTModelController.register_model(NUMonitorscope)
    NURESTModelController.register_model(NUMultiCastChannelMap)
    NURESTModelController.register_model(NUMultiCastList)
    NURESTModelController.register_model(NUMultiCastRange)
    NURESTModelController.register_model(NUMultiNICVPort)
    NURESTModelController.register_model(NUNATMapEntry)
    NURESTModelController.register_model(NUNetconfManager)
    NURESTModelController.register_model(NUNetconfProfile)
    NURESTModelController.register_model(NUNetconfSession)
    NURESTModelController.register_model(NUNetworkLayout)
    NURESTModelController.register_model(NUNetworkMacroGroup)
    NURESTModelController.register_model(NUNetworkPerformanceBinding)
    NURESTModelController.register_model(NUNetworkPerformanceMeasurement)
    NURESTModelController.register_model(NUNextHop)
    NURESTModelController.register_model(NUNSGateway)
    NURESTModelController.register_model(NUNSGatewayMonitor)
    NURESTModelController.register_model(NUNSGatewaysCount)
    NURESTModelController.register_model(NUNSGatewaySummary)
    NURESTModelController.register_model(NUNSGatewayTemplate)
    NURESTModelController.register_model(NUNSGGroup)
    NURESTModelController.register_model(NUNSGInfo)
    NURESTModelController.register_model(NUNSGPatchProfile)
    NURESTModelController.register_model(NUNSGRoutingPolicyBinding)
    NURESTModelController.register_model(NUNSGUpgradeProfile)
    NURESTModelController.register_model(NUNSPort)
    NURESTModelController.register_model(NUNSPortInfo)
    NURESTModelController.register_model(NUNSPortTemplate)
    NURESTModelController.register_model(NUNSRedundantGatewayGroup)
    NURESTModelController.register_model(NUOSPFArea)
    NURESTModelController.register_model(NUOSPFInstance)
    NURESTModelController.register_model(NUOSPFInterface)
    NURESTModelController.register_model(NUOverlayAddressPool)
    NURESTModelController.register_model(NUOverlayManagementProfile)
    NURESTModelController.register_model(NUOverlayManagementSubnetProfile)
    NURESTModelController.register_model(NUOverlayMirrorDestination)
    NURESTModelController.register_model(NUOverlayMirrorDestinationTemplate)
    NURESTModelController.register_model(NUOverlayPATNATEntry)
    NURESTModelController.register_model(NUPatch)
    NURESTModelController.register_model(NUPATIPEntry)
    NURESTModelController.register_model(NUPATMapper)
    NURESTModelController.register_model(NUPATNATPool)
    NURESTModelController.register_model(NUPerformanceMonitor)
    NURESTModelController.register_model(NUPermission)
    NURESTModelController.register_model(NUPGExpression)
    NURESTModelController.register_model(NUPGExpressionTemplate)
    NURESTModelController.register_model(NUPolicyDecision)
    NURESTModelController.register_model(NUPolicyEntry)
    NURESTModelController.register_model(NUPolicyGroup)
    NURESTModelController.register_model(NUPolicyGroupCategory)
    NURESTModelController.register_model(NUPolicyGroupTemplate)
    NURESTModelController.register_model(NUPolicyObjectGroup)
    NURESTModelController.register_model(NUPolicyStatement)
    NURESTModelController.register_model(NUPort)
    NURESTModelController.register_model(NUPortMapping)
    NURESTModelController.register_model(NUPortTemplate)
    NURESTModelController.register_model(NUProxyARPFilter)
    NURESTModelController.register_model(NUPSNATPool)
    NURESTModelController.register_model(NUPSPATMap)
    NURESTModelController.register_model(NUPTranslationMap)
    NURESTModelController.register_model(NUPublicNetworkMacro)
    NURESTModelController.register_model(NUQOS)
    NURESTModelController.register_model(NUQosPolicer)
    NURESTModelController.register_model(NURateLimiter)
    NURESTModelController.register_model(NURedirectionTarget)
    NURESTModelController.register_model(NURedirectionTargetTemplate)
    NURESTModelController.register_model(NURedundancyGroup)
    NURESTModelController.register_model(NURedundantPort)
    NURESTModelController.register_model(NURoutingPolicy)
    NURESTModelController.register_model(NUSaaSApplicationGroup)
    NURESTModelController.register_model(NUSaaSApplicationType)
    NURESTModelController.register_model(NUSAPEgressQoSProfile)
    NURESTModelController.register_model(NUSAPIngressQoSProfile)
    NURESTModelController.register_model(NUSharedNetworkResource)
    NURESTModelController.register_model(NUShuntLink)
    NURESTModelController.register_model(NUSiteInfo)
    NURESTModelController.register_model(NUSPATSourcesPool)
    NURESTModelController.register_model(NUSSHKey)
    NURESTModelController.register_model(NUSSIDConnection)
    NURESTModelController.register_model(NUStaticRoute)
    NURESTModelController.register_model(NUStatistics)
    NURESTModelController.register_model(NUStatisticsPolicy)
    NURESTModelController.register_model(NUStatsCollectorInfo)
    NURESTModelController.register_model(NUSubnet)
    NURESTModelController.register_model(NUSubnetTemplate)
    NURESTModelController.register_model(NUSyslogDestination)
    NURESTModelController.register_model(NUSystemConfig)
    NURESTModelController.register_model(NUTCA)
    NURESTModelController.register_model(NUTier)
    NURESTModelController.register_model(NUTrunk)
    NURESTModelController.register_model(NUUnderlay)
    NURESTModelController.register_model(NUUplinkConnection)
    NURESTModelController.register_model(NUUplinkRD)
    NURESTModelController.register_model(NUUser)
    NURESTModelController.register_model(NUUserContext)
    NURESTModelController.register_model(NUVCenter)
    NURESTModelController.register_model(NUVCenterCluster)
    NURESTModelController.register_model(NUVCenterDataCenter)
    NURESTModelController.register_model(NUVCenterEAMConfig)
    NURESTModelController.register_model(NUVCenterHypervisor)
    NURESTModelController.register_model(NUVCenterVRSConfig)
    NURESTModelController.register_model(NUVirtualFirewallPolicy)
    NURESTModelController.register_model(NUVirtualFirewallRule)
    NURESTModelController.register_model(NUVirtualIP)
    NURESTModelController.register_model(NUVLAN)
    NURESTModelController.register_model(NUVLANTemplate)
    NURESTModelController.register_model(NUVM)
    NURESTModelController.register_model(NUVMInterface)
    NURESTModelController.register_model(NUVMResync)
    NURESTModelController.register_model(NUVNF)
    NURESTModelController.register_model(NUVNFCatalog)
    NURESTModelController.register_model(NUVNFDescriptor)
    NURESTModelController.register_model(NUVNFDomainMapping)
    NURESTModelController.register_model(NUVNFInterface)
    NURESTModelController.register_model(NUVNFInterfaceDescriptor)
    NURESTModelController.register_model(NUVNFMetadata)
    NURESTModelController.register_model(NUVNFThresholdPolicy)
    NURESTModelController.register_model(NUVPNConnection)
    NURESTModelController.register_model(NUVPort)
    NURESTModelController.register_model(NUVPortMirror)
    NURESTModelController.register_model(NUVRS)
    NURESTModelController.register_model(NUVRSAddressRange)
    NURESTModelController.register_model(NUVRSMetrics)
    NURESTModelController.register_model(NUVRSRedeploymentpolicy)
    NURESTModelController.register_model(NUVSC)
    NURESTModelController.register_model(NUVSD)
    NURESTModelController.register_model(NUVSDComponent)
    NURESTModelController.register_model(NUVsgRedundantPort)
    NURESTModelController.register_model(NUVSP)
    NURESTModelController.register_model(NUWANService)
    NURESTModelController.register_model(NUWebCategory)
    NURESTModelController.register_model(NUWebDomainName)
    NURESTModelController.register_model(NUWirelessPort)
    NURESTModelController.register_model(NUZFBAutoAssignment)
    NURESTModelController.register_model(NUZFBRequest)
    NURESTModelController.register_model(NUZone)
    NURESTModelController.register_model(NUZoneTemplate)
    

__setup_bambou()