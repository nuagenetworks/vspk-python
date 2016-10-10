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

__all__ = ['NUVSDSession', 'NUAddressMap', 'NUAddressRange', 'NUAggregateMetadata', 'NUAlarm', 'NUAllAlarm', 'NUApplication', 'NUApplicationBinding', 'NUApplicationperformancemanagement', 'NUApplicationperformancemanagementbinding', 'NUApplicationService', 'NUAutoDiscoverCluster', 'NUAutodiscovereddatacenter', 'NUAutoDiscoveredGateway', 'NUAutoDiscoverHypervisorFromCluster', 'NUAvatar', 'NUBGPNeighbor', 'NUBGPPeer', 'NUBGPProfile', 'NUBootstrap', 'NUBootstrapActivation', 'NUBRConnection', 'NUBridgeInterface', 'NUBulkStatistics', 'NUCertificate', 'NUCloudMgmtSystem', 'NUContainer', 'NUContainerInterface', 'NUContainerResync', 'NUDemarcationService', 'NUDHCPOption', 'NUDiskStat', 'NUDomain', 'NUDomainFIPAclTemplate', 'NUDomainFIPAclTemplateEntry', 'NUDomainTemplate', 'NUDSCPForwardingClassMapping', 'NUDSCPForwardingClassTable', 'NUEgressACLEntryTemplate', 'NUEgressACLTemplate', 'NUEgressQOSPolicy', 'NUEndPoint', 'NUEnterprise', 'NUEnterpriseNetwork', 'NUEnterprisePermission', 'NUEnterpriseProfile', 'NUEnterpriseSecuredData', 'NUEnterpriseSecurity', 'NUEventLog', 'NUExternalAppService', 'NUExternalService', 'NUFloatingIp', 'NUFloatingIPACLTemplate', 'NUFloatingIPACLTemplateEntry', 'NUFlow', 'NUFlowForwardingPolicy', 'NUFlowSecurityPolicy', 'NUGateway', 'NUGatewaySecuredData', 'NUGatewaySecurity', 'NUGatewayTemplate', 'NUGlobalMetadata', 'NUGroup', 'NUGroupKeyEncryptionProfile', 'NUHostInterface', 'NUHSC', 'NUIKECertificate', 'NUIKEEncryptionprofile', 'NUIKEGateway', 'NUIKEGatewayConfig', 'NUIKEGatewayConnection', 'NUIKEGatewayProfile', 'NUIKEPSK', 'NUIKESubnet', 'NUInfrastructureaccessprofile', 'NUInfrastructureConfig', 'NUInfrastructureGatewayProfile', 'NUInfrastructureVscProfile', 'NUIngressACLEntryTemplate', 'NUIngressACLTemplate', 'NUIngressAdvFwdEntryTemplate', 'NUIngressAdvFwdTemplate', 'NUIngressExternalServiceTemplate', 'NUIngressExternalServiceTemplateEntry', 'NUIPReservation', 'NUJob', 'NUKeyServerMember', 'NUKeyServerMonitor', 'NUKeyServerMonitorEncryptedSeed', 'NUKeyServerMonitorSeed', 'NUKeyServerMonitorSEK', 'NUKeyServerNotification', 'NUL2Domain', 'NUL2DomainTemplate', 'NUL7applicationsignature', 'NULDAPConfiguration', 'NULicense', 'NULicenseStatus', 'NULink', 'NULocation', 'NUMe', 'NUMetadata', 'NUMetadataTag', 'NUMirrorDestination', 'NUMonitoringPort', 'NUMonitorscope', 'NUMultiCastChannelMap', 'NUMultiCastList', 'NUMultiCastRange', 'NUMultiNICVPort', 'NUNATMapEntry', 'NUNetworkLayout', 'NUNetworkMacroGroup', 'NUNetworkPerformanceBinding', 'NUNetworkPerformanceMeasurement', 'NUNextHop', 'NUNextHopAddress', 'NUNSGateway', 'NUNSGatewayTemplate', 'NUNSGInfo', 'NUNSPort', 'NUNSPortTemplate', 'NUNSRedundantGatewayGroup', 'NUOverlayAddressPool', 'NUOverlayPATNATEntry', 'NUPATIPEntry', 'NUPATMapper', 'NUPATNATPool', 'NUPerformanceMonitor', 'NUPermission', 'NUPolicyDecision', 'NUPolicyGroup', 'NUPolicyGroupTemplate', 'NUPort', 'NUPortMapping', 'NUPortTemplate', 'NUPublicNetworkMacro', 'NUQOS', 'NURateLimiter', 'NURedirectionTarget', 'NURedirectionTargetTemplate', 'NURedundancyGroup', 'NURedundantPort', 'NURoutingPolicy', 'NUSharedNetworkResource', 'NUSiteInfo', 'NUStaticRoute', 'NUStatistics', 'NUStatisticsPolicy', 'NUStatsCollectorInfo', 'NUSubnet', 'NUSubnetTemplate', 'NUSystemConfig', 'NUTCA', 'NUTier', 'NUUplinkConnection', 'NUUplinkRD', 'NUUser', 'NUVCenter', 'NUVCenterCluster', 'NUVCenterDataCenter', 'NUVCenterEAMConfig', 'NUVCenterHypervisor', 'NUVCenterVRSConfig', 'NUVia', 'NUVirtualIP', 'NUVLAN', 'NUVLANTemplate', 'NUVM', 'NUVMInterface', 'NUVMResync', 'NUVPNConnection', 'NUVPort', 'NUVPortMirror', 'NUVRS', 'NUVRSAddressRange', 'NUVRSMetrics', 'NUVRSRedeploymentpolicy', 'NUVSC', 'NUVSD', 'NUVSDComponent', 'NUVsgRedundantPort', 'NUVSP', 'NUWANService', 'NUZFBAutoAssignment', 'NUZFBRequest', 'NUZone', 'NUZoneTemplate']

from .nuaddressmap import NUAddressMap
from .nuaddressrange import NUAddressRange
from .nuaggregatemetadata import NUAggregateMetadata
from .nualarm import NUAlarm
from .nuallalarm import NUAllAlarm
from .nuapplication import NUApplication
from .nuapplicationbinding import NUApplicationBinding
from .nuapplicationperformancemanagement import NUApplicationperformancemanagement
from .nuapplicationperformancemanagementbinding import NUApplicationperformancemanagementbinding
from .nuapplicationservice import NUApplicationService
from .nuautodiscovercluster import NUAutoDiscoverCluster
from .nuautodiscovereddatacenter import NUAutodiscovereddatacenter
from .nuautodiscoveredgateway import NUAutoDiscoveredGateway
from .nuautodiscoverhypervisorfromcluster import NUAutoDiscoverHypervisorFromCluster
from .nuavatar import NUAvatar
from .nubgpneighbor import NUBGPNeighbor
from .nubgppeer import NUBGPPeer
from .nubgpprofile import NUBGPProfile
from .nubootstrap import NUBootstrap
from .nubootstrapactivation import NUBootstrapActivation
from .nubrconnection import NUBRConnection
from .nubridgeinterface import NUBridgeInterface
from .nubulkstatistics import NUBulkStatistics
from .nucertificate import NUCertificate
from .nucloudmgmtsystem import NUCloudMgmtSystem
from .nucontainer import NUContainer
from .nucontainerinterface import NUContainerInterface
from .nucontainerresync import NUContainerResync
from .nudemarcationservice import NUDemarcationService
from .nudhcpoption import NUDHCPOption
from .nudiskstat import NUDiskStat
from .nudomain import NUDomain
from .nudomainfipacltemplate import NUDomainFIPAclTemplate
from .nudomainfipacltemplateentry import NUDomainFIPAclTemplateEntry
from .nudomaintemplate import NUDomainTemplate
from .nudscpforwardingclassmapping import NUDSCPForwardingClassMapping
from .nudscpforwardingclasstable import NUDSCPForwardingClassTable
from .nuegressaclentrytemplate import NUEgressACLEntryTemplate
from .nuegressacltemplate import NUEgressACLTemplate
from .nuegressqospolicy import NUEgressQOSPolicy
from .nuendpoint import NUEndPoint
from .nuenterprise import NUEnterprise
from .nuenterprisenetwork import NUEnterpriseNetwork
from .nuenterprisepermission import NUEnterprisePermission
from .nuenterpriseprofile import NUEnterpriseProfile
from .nuenterprisesecureddata import NUEnterpriseSecuredData
from .nuenterprisesecurity import NUEnterpriseSecurity
from .nueventlog import NUEventLog
from .nuexternalappservice import NUExternalAppService
from .nuexternalservice import NUExternalService
from .nufloatingip import NUFloatingIp
from .nufloatingipacltemplate import NUFloatingIPACLTemplate
from .nufloatingipacltemplateentry import NUFloatingIPACLTemplateEntry
from .nuflow import NUFlow
from .nuflowforwardingpolicy import NUFlowForwardingPolicy
from .nuflowsecuritypolicy import NUFlowSecurityPolicy
from .nugateway import NUGateway
from .nugatewaysecureddata import NUGatewaySecuredData
from .nugatewaysecurity import NUGatewaySecurity
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
from .nuinfrastructureaccessprofile import NUInfrastructureaccessprofile
from .nuinfrastructureconfig import NUInfrastructureConfig
from .nuinfrastructuregatewayprofile import NUInfrastructureGatewayProfile
from .nuinfrastructurevscprofile import NUInfrastructureVscProfile
from .nuingressaclentrytemplate import NUIngressACLEntryTemplate
from .nuingressacltemplate import NUIngressACLTemplate
from .nuingressadvfwdentrytemplate import NUIngressAdvFwdEntryTemplate
from .nuingressadvfwdtemplate import NUIngressAdvFwdTemplate
from .nuingressexternalservicetemplate import NUIngressExternalServiceTemplate
from .nuingressexternalservicetemplateentry import NUIngressExternalServiceTemplateEntry
from .nuipreservation import NUIPReservation
from .nujob import NUJob
from .nukeyservermember import NUKeyServerMember
from .nukeyservermonitor import NUKeyServerMonitor
from .nukeyservermonitorencryptedseed import NUKeyServerMonitorEncryptedSeed
from .nukeyservermonitorseed import NUKeyServerMonitorSeed
from .nukeyservermonitorsek import NUKeyServerMonitorSEK
from .nukeyservernotification import NUKeyServerNotification
from .nul2domain import NUL2Domain
from .nul2domaintemplate import NUL2DomainTemplate
from .nul7applicationsignature import NUL7applicationsignature
from .nuldapconfiguration import NULDAPConfiguration
from .nulicense import NULicense
from .nulicensestatus import NULicenseStatus
from .nulink import NULink
from .nulocation import NULocation
from .nume import NUMe
from .numetadata import NUMetadata
from .numetadatatag import NUMetadataTag
from .numirrordestination import NUMirrorDestination
from .numonitoringport import NUMonitoringPort
from .numonitorscope import NUMonitorscope
from .numulticastchannelmap import NUMultiCastChannelMap
from .numulticastlist import NUMultiCastList
from .numulticastrange import NUMultiCastRange
from .numultinicvport import NUMultiNICVPort
from .nunatmapentry import NUNATMapEntry
from .nunetworklayout import NUNetworkLayout
from .nunetworkmacrogroup import NUNetworkMacroGroup
from .nunetworkperformancebinding import NUNetworkPerformanceBinding
from .nunetworkperformancemeasurement import NUNetworkPerformanceMeasurement
from .nunexthop import NUNextHop
from .nunexthopaddress import NUNextHopAddress
from .nunsgateway import NUNSGateway
from .nunsgatewaytemplate import NUNSGatewayTemplate
from .nunsginfo import NUNSGInfo
from .nunsport import NUNSPort
from .nunsporttemplate import NUNSPortTemplate
from .nunsredundantgatewaygroup import NUNSRedundantGatewayGroup
from .nuoverlayaddresspool import NUOverlayAddressPool
from .nuoverlaypatnatentry import NUOverlayPATNATEntry
from .nupatipentry import NUPATIPEntry
from .nupatmapper import NUPATMapper
from .nupatnatpool import NUPATNATPool
from .nuperformancemonitor import NUPerformanceMonitor
from .nupermission import NUPermission
from .nupolicydecision import NUPolicyDecision
from .nupolicygroup import NUPolicyGroup
from .nupolicygrouptemplate import NUPolicyGroupTemplate
from .nuport import NUPort
from .nuportmapping import NUPortMapping
from .nuporttemplate import NUPortTemplate
from .nupublicnetworkmacro import NUPublicNetworkMacro
from .nuqos import NUQOS
from .nuratelimiter import NURateLimiter
from .nuredirectiontarget import NURedirectionTarget
from .nuredirectiontargettemplate import NURedirectionTargetTemplate
from .nuredundancygroup import NURedundancyGroup
from .nuredundantport import NURedundantPort
from .nuroutingpolicy import NURoutingPolicy
from .nusharednetworkresource import NUSharedNetworkResource
from .nusiteinfo import NUSiteInfo
from .nustaticroute import NUStaticRoute
from .nustatistics import NUStatistics
from .nustatisticspolicy import NUStatisticsPolicy
from .nustatscollectorinfo import NUStatsCollectorInfo
from .nusubnet import NUSubnet
from .nusubnettemplate import NUSubnetTemplate
from .nusystemconfig import NUSystemConfig
from .nutca import NUTCA
from .nutier import NUTier
from .nuuplinkconnection import NUUplinkConnection
from .nuuplinkrd import NUUplinkRD
from .nuuser import NUUser
from .nuvcenter import NUVCenter
from .nuvcentercluster import NUVCenterCluster
from .nuvcenterdatacenter import NUVCenterDataCenter
from .nuvcentereamconfig import NUVCenterEAMConfig
from .nuvcenterhypervisor import NUVCenterHypervisor
from .nuvcentervrsconfig import NUVCenterVRSConfig
from .nuvia import NUVia
from .nuvirtualip import NUVirtualIP
from .nuvlan import NUVLAN
from .nuvlantemplate import NUVLANTemplate
from .nuvm import NUVM
from .nuvminterface import NUVMInterface
from .nuvmresync import NUVMResync
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
    NURESTModelController.register_model(NUApplication)
    NURESTModelController.register_model(NUApplicationBinding)
    NURESTModelController.register_model(NUApplicationperformancemanagement)
    NURESTModelController.register_model(NUApplicationperformancemanagementbinding)
    NURESTModelController.register_model(NUApplicationService)
    NURESTModelController.register_model(NUAutoDiscoverCluster)
    NURESTModelController.register_model(NUAutodiscovereddatacenter)
    NURESTModelController.register_model(NUAutoDiscoveredGateway)
    NURESTModelController.register_model(NUAutoDiscoverHypervisorFromCluster)
    NURESTModelController.register_model(NUAvatar)
    NURESTModelController.register_model(NUBGPNeighbor)
    NURESTModelController.register_model(NUBGPPeer)
    NURESTModelController.register_model(NUBGPProfile)
    NURESTModelController.register_model(NUBootstrap)
    NURESTModelController.register_model(NUBootstrapActivation)
    NURESTModelController.register_model(NUBRConnection)
    NURESTModelController.register_model(NUBridgeInterface)
    NURESTModelController.register_model(NUBulkStatistics)
    NURESTModelController.register_model(NUCertificate)
    NURESTModelController.register_model(NUCloudMgmtSystem)
    NURESTModelController.register_model(NUContainer)
    NURESTModelController.register_model(NUContainerInterface)
    NURESTModelController.register_model(NUContainerResync)
    NURESTModelController.register_model(NUDemarcationService)
    NURESTModelController.register_model(NUDHCPOption)
    NURESTModelController.register_model(NUDiskStat)
    NURESTModelController.register_model(NUDomain)
    NURESTModelController.register_model(NUDomainFIPAclTemplate)
    NURESTModelController.register_model(NUDomainFIPAclTemplateEntry)
    NURESTModelController.register_model(NUDomainTemplate)
    NURESTModelController.register_model(NUDSCPForwardingClassMapping)
    NURESTModelController.register_model(NUDSCPForwardingClassTable)
    NURESTModelController.register_model(NUEgressACLEntryTemplate)
    NURESTModelController.register_model(NUEgressACLTemplate)
    NURESTModelController.register_model(NUEgressQOSPolicy)
    NURESTModelController.register_model(NUEndPoint)
    NURESTModelController.register_model(NUEnterprise)
    NURESTModelController.register_model(NUEnterpriseNetwork)
    NURESTModelController.register_model(NUEnterprisePermission)
    NURESTModelController.register_model(NUEnterpriseProfile)
    NURESTModelController.register_model(NUEnterpriseSecuredData)
    NURESTModelController.register_model(NUEnterpriseSecurity)
    NURESTModelController.register_model(NUEventLog)
    NURESTModelController.register_model(NUExternalAppService)
    NURESTModelController.register_model(NUExternalService)
    NURESTModelController.register_model(NUFloatingIp)
    NURESTModelController.register_model(NUFloatingIPACLTemplate)
    NURESTModelController.register_model(NUFloatingIPACLTemplateEntry)
    NURESTModelController.register_model(NUFlow)
    NURESTModelController.register_model(NUFlowForwardingPolicy)
    NURESTModelController.register_model(NUFlowSecurityPolicy)
    NURESTModelController.register_model(NUGateway)
    NURESTModelController.register_model(NUGatewaySecuredData)
    NURESTModelController.register_model(NUGatewaySecurity)
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
    NURESTModelController.register_model(NUInfrastructureaccessprofile)
    NURESTModelController.register_model(NUInfrastructureConfig)
    NURESTModelController.register_model(NUInfrastructureGatewayProfile)
    NURESTModelController.register_model(NUInfrastructureVscProfile)
    NURESTModelController.register_model(NUIngressACLEntryTemplate)
    NURESTModelController.register_model(NUIngressACLTemplate)
    NURESTModelController.register_model(NUIngressAdvFwdEntryTemplate)
    NURESTModelController.register_model(NUIngressAdvFwdTemplate)
    NURESTModelController.register_model(NUIngressExternalServiceTemplate)
    NURESTModelController.register_model(NUIngressExternalServiceTemplateEntry)
    NURESTModelController.register_model(NUIPReservation)
    NURESTModelController.register_model(NUJob)
    NURESTModelController.register_model(NUKeyServerMember)
    NURESTModelController.register_model(NUKeyServerMonitor)
    NURESTModelController.register_model(NUKeyServerMonitorEncryptedSeed)
    NURESTModelController.register_model(NUKeyServerMonitorSeed)
    NURESTModelController.register_model(NUKeyServerMonitorSEK)
    NURESTModelController.register_model(NUKeyServerNotification)
    NURESTModelController.register_model(NUL2Domain)
    NURESTModelController.register_model(NUL2DomainTemplate)
    NURESTModelController.register_model(NUL7applicationsignature)
    NURESTModelController.register_model(NULDAPConfiguration)
    NURESTModelController.register_model(NULicense)
    NURESTModelController.register_model(NULicenseStatus)
    NURESTModelController.register_model(NULink)
    NURESTModelController.register_model(NULocation)
    NURESTModelController.register_model(NUMe)
    NURESTModelController.register_model(NUMetadata)
    NURESTModelController.register_model(NUMetadataTag)
    NURESTModelController.register_model(NUMirrorDestination)
    NURESTModelController.register_model(NUMonitoringPort)
    NURESTModelController.register_model(NUMonitorscope)
    NURESTModelController.register_model(NUMultiCastChannelMap)
    NURESTModelController.register_model(NUMultiCastList)
    NURESTModelController.register_model(NUMultiCastRange)
    NURESTModelController.register_model(NUMultiNICVPort)
    NURESTModelController.register_model(NUNATMapEntry)
    NURESTModelController.register_model(NUNetworkLayout)
    NURESTModelController.register_model(NUNetworkMacroGroup)
    NURESTModelController.register_model(NUNetworkPerformanceBinding)
    NURESTModelController.register_model(NUNetworkPerformanceMeasurement)
    NURESTModelController.register_model(NUNextHop)
    NURESTModelController.register_model(NUNextHopAddress)
    NURESTModelController.register_model(NUNSGateway)
    NURESTModelController.register_model(NUNSGatewayTemplate)
    NURESTModelController.register_model(NUNSGInfo)
    NURESTModelController.register_model(NUNSPort)
    NURESTModelController.register_model(NUNSPortTemplate)
    NURESTModelController.register_model(NUNSRedundantGatewayGroup)
    NURESTModelController.register_model(NUOverlayAddressPool)
    NURESTModelController.register_model(NUOverlayPATNATEntry)
    NURESTModelController.register_model(NUPATIPEntry)
    NURESTModelController.register_model(NUPATMapper)
    NURESTModelController.register_model(NUPATNATPool)
    NURESTModelController.register_model(NUPerformanceMonitor)
    NURESTModelController.register_model(NUPermission)
    NURESTModelController.register_model(NUPolicyDecision)
    NURESTModelController.register_model(NUPolicyGroup)
    NURESTModelController.register_model(NUPolicyGroupTemplate)
    NURESTModelController.register_model(NUPort)
    NURESTModelController.register_model(NUPortMapping)
    NURESTModelController.register_model(NUPortTemplate)
    NURESTModelController.register_model(NUPublicNetworkMacro)
    NURESTModelController.register_model(NUQOS)
    NURESTModelController.register_model(NURateLimiter)
    NURESTModelController.register_model(NURedirectionTarget)
    NURESTModelController.register_model(NURedirectionTargetTemplate)
    NURESTModelController.register_model(NURedundancyGroup)
    NURESTModelController.register_model(NURedundantPort)
    NURESTModelController.register_model(NURoutingPolicy)
    NURESTModelController.register_model(NUSharedNetworkResource)
    NURESTModelController.register_model(NUSiteInfo)
    NURESTModelController.register_model(NUStaticRoute)
    NURESTModelController.register_model(NUStatistics)
    NURESTModelController.register_model(NUStatisticsPolicy)
    NURESTModelController.register_model(NUStatsCollectorInfo)
    NURESTModelController.register_model(NUSubnet)
    NURESTModelController.register_model(NUSubnetTemplate)
    NURESTModelController.register_model(NUSystemConfig)
    NURESTModelController.register_model(NUTCA)
    NURESTModelController.register_model(NUTier)
    NURESTModelController.register_model(NUUplinkConnection)
    NURESTModelController.register_model(NUUplinkRD)
    NURESTModelController.register_model(NUUser)
    NURESTModelController.register_model(NUVCenter)
    NURESTModelController.register_model(NUVCenterCluster)
    NURESTModelController.register_model(NUVCenterDataCenter)
    NURESTModelController.register_model(NUVCenterEAMConfig)
    NURESTModelController.register_model(NUVCenterHypervisor)
    NURESTModelController.register_model(NUVCenterVRSConfig)
    NURESTModelController.register_model(NUVia)
    NURESTModelController.register_model(NUVirtualIP)
    NURESTModelController.register_model(NUVLAN)
    NURESTModelController.register_model(NUVLANTemplate)
    NURESTModelController.register_model(NUVM)
    NURESTModelController.register_model(NUVMInterface)
    NURESTModelController.register_model(NUVMResync)
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
    NURESTModelController.register_model(NUZFBAutoAssignment)
    NURESTModelController.register_model(NUZFBRequest)
    NURESTModelController.register_model(NUZone)
    NURESTModelController.register_model(NUZoneTemplate)
    

__setup_bambou()