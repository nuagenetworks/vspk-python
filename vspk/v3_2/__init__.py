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

__all__ = ['NUVSDSession', 'NUAddressRange', 'NUAggregateMetadata', 'NUAlarm', 'NUApp', 'NUApplicationService', 'NUAutoDiscoveredGateway', 'NUBGPPeer', 'NUBootstrap', 'NUBootstrapActivation', 'NUBridgeInterface', 'NUCertificate', 'NUCloudMgmtSystem', 'NUDHCPOption', 'NUDiskStat', 'NUDomain', 'NUDomainTemplate', 'NUDSCPForwardingClassMapping', 'NUDSCPForwardingClassTable', 'NUEgressACLEntryTemplate', 'NUEgressACLTemplate', 'NUEgressQOSPolicy', 'NUEndPoint', 'NUEnterprise', 'NUEnterpriseNetwork', 'NUEnterprisePermission', 'NUEnterpriseProfile', 'NUEventLog', 'NUExternalAppService', 'NUExternalService', 'NUFloatingIp', 'NUFlow', 'NUFlowForwardingPolicy', 'NUFlowSecurityPolicy', 'NUGateway', 'NUGatewayTemplate', 'NUGlobalMetadata', 'NUGroup', 'NUGroupKeyEncryptionProfile', 'NUHostInterface', 'NUHSC', 'NUInfrastructureConfig', 'NUInfrastructureGatewayProfile', 'NUInfrastructurePortProfile', 'NUInfrastructureVscProfile', 'NUIngressACLEntryTemplate', 'NUIngressACLTemplate', 'NUIngressAdvFwdEntryTemplate', 'NUIngressAdvFwdTemplate', 'NUIngressExternalServiceTemplate', 'NUIngressExternalServiceTemplateEntry', 'NUIPReservation', 'NUJob', 'NUKeyServerMonitor', 'NUKeyServerMonitorEncryptedSeed', 'NUKeyServerMonitorEncryptedSEK', 'NUKeyServerMonitorSeed', 'NUKeyServerMonitorSEK', 'NUL2Domain', 'NUL2DomainTemplate', 'NULDAPConfiguration', 'NULicense', 'NULocation', 'NUMe', 'NUMetadata', 'NUMetadataTag', 'NUMirrorDestination', 'NUMonitoringPort', 'NUMultiCastChannelMap', 'NUMultiCastList', 'NUMultiCastRange', 'NUMultiNICVPort', 'NUNATMapEntry', 'NUNetworkLayout', 'NUNetworkMacroGroup', 'NUNSGateway', 'NUNSGatewayTemplate', 'NUNSPort', 'NUNSPortStaticConfiguration', 'NUNSPortTemplate', 'NUNSRedundantGatewayGroup', 'NUPATNATPool', 'NUPermission', 'NUPolicyDecision', 'NUPolicyGroup', 'NUPolicyGroupTemplate', 'NUPort', 'NUPortTemplate', 'NUPublicNetworkMacro', 'NUQOS', 'NURateLimiter', 'NURedirectionTarget', 'NURedirectionTargetTemplate', 'NURedundancyGroup', 'NURedundantPort', 'NUSharedNetworkResource', 'NUSiteInfo', 'NUStaticRoute', 'NUStatistics', 'NUStatisticsPolicy', 'NUStatsCollectorInfo', 'NUSubnet', 'NUSubnetTemplate', 'NUSystemConfig', 'NUTCA', 'NUTier', 'NUUplinkRD', 'NUUser', 'NUVCenter', 'NUVCenterCluster', 'NUVCenterDataCenter', 'NUVCenterEAMConfig', 'NUVCenterHypervisor', 'NUVCenterVRSConfig', 'NUVirtualIP', 'NUVLAN', 'NUVLANTemplate', 'NUVM', 'NUVMInterface', 'NUVMResync', 'NUVPNConnection', 'NUVPort', 'NUVPortMirror', 'NUVRS', 'NUVRSAddressRange', 'NUVSC', 'NUVSD', 'NUVSDComponent', 'NUVsgRedundantPort', 'NUVSP', 'NUWANService', 'NUZone', 'NUZoneTemplate']

from .nuaddressrange import NUAddressRange
from .nuaggregatemetadata import NUAggregateMetadata
from .nualarm import NUAlarm
from .nuapp import NUApp
from .nuapplicationservice import NUApplicationService
from .nuautodiscoveredgateway import NUAutoDiscoveredGateway
from .nubgppeer import NUBGPPeer
from .nubootstrap import NUBootstrap
from .nubootstrapactivation import NUBootstrapActivation
from .nubridgeinterface import NUBridgeInterface
from .nucertificate import NUCertificate
from .nucloudmgmtsystem import NUCloudMgmtSystem
from .nudhcpoption import NUDHCPOption
from .nudiskstat import NUDiskStat
from .nudomain import NUDomain
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
from .nueventlog import NUEventLog
from .nuexternalappservice import NUExternalAppService
from .nuexternalservice import NUExternalService
from .nufloatingip import NUFloatingIp
from .nuflow import NUFlow
from .nuflowforwardingpolicy import NUFlowForwardingPolicy
from .nuflowsecuritypolicy import NUFlowSecurityPolicy
from .nugateway import NUGateway
from .nugatewaytemplate import NUGatewayTemplate
from .nuglobalmetadata import NUGlobalMetadata
from .nugroup import NUGroup
from .nugroupkeyencryptionprofile import NUGroupKeyEncryptionProfile
from .nuhostinterface import NUHostInterface
from .nuhsc import NUHSC
from .nuinfrastructureconfig import NUInfrastructureConfig
from .nuinfrastructuregatewayprofile import NUInfrastructureGatewayProfile
from .nuinfrastructureportprofile import NUInfrastructurePortProfile
from .nuinfrastructurevscprofile import NUInfrastructureVscProfile
from .nuingressaclentrytemplate import NUIngressACLEntryTemplate
from .nuingressacltemplate import NUIngressACLTemplate
from .nuingressadvfwdentrytemplate import NUIngressAdvFwdEntryTemplate
from .nuingressadvfwdtemplate import NUIngressAdvFwdTemplate
from .nuingressexternalservicetemplate import NUIngressExternalServiceTemplate
from .nuingressexternalservicetemplateentry import NUIngressExternalServiceTemplateEntry
from .nuipreservation import NUIPReservation
from .nujob import NUJob
from .nukeyservermonitor import NUKeyServerMonitor
from .nukeyservermonitorencryptedseed import NUKeyServerMonitorEncryptedSeed
from .nukeyservermonitorencryptedsek import NUKeyServerMonitorEncryptedSEK
from .nukeyservermonitorseed import NUKeyServerMonitorSeed
from .nukeyservermonitorsek import NUKeyServerMonitorSEK
from .nul2domain import NUL2Domain
from .nul2domaintemplate import NUL2DomainTemplate
from .nuldapconfiguration import NULDAPConfiguration
from .nulicense import NULicense
from .nulocation import NULocation
from .nume import NUMe
from .numetadata import NUMetadata
from .numetadatatag import NUMetadataTag
from .numirrordestination import NUMirrorDestination
from .numonitoringport import NUMonitoringPort
from .numulticastchannelmap import NUMultiCastChannelMap
from .numulticastlist import NUMultiCastList
from .numulticastrange import NUMultiCastRange
from .numultinicvport import NUMultiNICVPort
from .nunatmapentry import NUNATMapEntry
from .nunetworklayout import NUNetworkLayout
from .nunetworkmacrogroup import NUNetworkMacroGroup
from .nunsgateway import NUNSGateway
from .nunsgatewaytemplate import NUNSGatewayTemplate
from .nunsport import NUNSPort
from .nunsportstaticconfiguration import NUNSPortStaticConfiguration
from .nunsporttemplate import NUNSPortTemplate
from .nunsredundantgatewaygroup import NUNSRedundantGatewayGroup
from .nupatnatpool import NUPATNATPool
from .nupermission import NUPermission
from .nupolicydecision import NUPolicyDecision
from .nupolicygroup import NUPolicyGroup
from .nupolicygrouptemplate import NUPolicyGroupTemplate
from .nuport import NUPort
from .nuporttemplate import NUPortTemplate
from .nupublicnetworkmacro import NUPublicNetworkMacro
from .nuqos import NUQOS
from .nuratelimiter import NURateLimiter
from .nuredirectiontarget import NURedirectionTarget
from .nuredirectiontargettemplate import NURedirectionTargetTemplate
from .nuredundancygroup import NURedundancyGroup
from .nuredundantport import NURedundantPort
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
from .nuuplinkrd import NUUplinkRD
from .nuuser import NUUser
from .nuvcenter import NUVCenter
from .nuvcentercluster import NUVCenterCluster
from .nuvcenterdatacenter import NUVCenterDataCenter
from .nuvcentereamconfig import NUVCenterEAMConfig
from .nuvcenterhypervisor import NUVCenterHypervisor
from .nuvcentervrsconfig import NUVCenterVRSConfig
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
from .nuvsc import NUVSC
from .nuvsd import NUVSD
from .nuvsdcomponent import NUVSDComponent
from .nuvsgredundantport import NUVsgRedundantPort
from .nuvsp import NUVSP
from .nuwanservice import NUWANService
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

    NURESTModelController.register_model(NUAddressRange)
    NURESTModelController.register_model(NUAggregateMetadata)
    NURESTModelController.register_model(NUAlarm)
    NURESTModelController.register_model(NUApp)
    NURESTModelController.register_model(NUApplicationService)
    NURESTModelController.register_model(NUAutoDiscoveredGateway)
    NURESTModelController.register_model(NUBGPPeer)
    NURESTModelController.register_model(NUBootstrap)
    NURESTModelController.register_model(NUBootstrapActivation)
    NURESTModelController.register_model(NUBridgeInterface)
    NURESTModelController.register_model(NUCertificate)
    NURESTModelController.register_model(NUCloudMgmtSystem)
    NURESTModelController.register_model(NUDHCPOption)
    NURESTModelController.register_model(NUDiskStat)
    NURESTModelController.register_model(NUDomain)
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
    NURESTModelController.register_model(NUEventLog)
    NURESTModelController.register_model(NUExternalAppService)
    NURESTModelController.register_model(NUExternalService)
    NURESTModelController.register_model(NUFloatingIp)
    NURESTModelController.register_model(NUFlow)
    NURESTModelController.register_model(NUFlowForwardingPolicy)
    NURESTModelController.register_model(NUFlowSecurityPolicy)
    NURESTModelController.register_model(NUGateway)
    NURESTModelController.register_model(NUGatewayTemplate)
    NURESTModelController.register_model(NUGlobalMetadata)
    NURESTModelController.register_model(NUGroup)
    NURESTModelController.register_model(NUGroupKeyEncryptionProfile)
    NURESTModelController.register_model(NUHostInterface)
    NURESTModelController.register_model(NUHSC)
    NURESTModelController.register_model(NUInfrastructureConfig)
    NURESTModelController.register_model(NUInfrastructureGatewayProfile)
    NURESTModelController.register_model(NUInfrastructurePortProfile)
    NURESTModelController.register_model(NUInfrastructureVscProfile)
    NURESTModelController.register_model(NUIngressACLEntryTemplate)
    NURESTModelController.register_model(NUIngressACLTemplate)
    NURESTModelController.register_model(NUIngressAdvFwdEntryTemplate)
    NURESTModelController.register_model(NUIngressAdvFwdTemplate)
    NURESTModelController.register_model(NUIngressExternalServiceTemplate)
    NURESTModelController.register_model(NUIngressExternalServiceTemplateEntry)
    NURESTModelController.register_model(NUIPReservation)
    NURESTModelController.register_model(NUJob)
    NURESTModelController.register_model(NUKeyServerMonitor)
    NURESTModelController.register_model(NUKeyServerMonitorEncryptedSeed)
    NURESTModelController.register_model(NUKeyServerMonitorEncryptedSEK)
    NURESTModelController.register_model(NUKeyServerMonitorSeed)
    NURESTModelController.register_model(NUKeyServerMonitorSEK)
    NURESTModelController.register_model(NUL2Domain)
    NURESTModelController.register_model(NUL2DomainTemplate)
    NURESTModelController.register_model(NULDAPConfiguration)
    NURESTModelController.register_model(NULicense)
    NURESTModelController.register_model(NULocation)
    NURESTModelController.register_model(NUMe)
    NURESTModelController.register_model(NUMetadata)
    NURESTModelController.register_model(NUMetadataTag)
    NURESTModelController.register_model(NUMirrorDestination)
    NURESTModelController.register_model(NUMonitoringPort)
    NURESTModelController.register_model(NUMultiCastChannelMap)
    NURESTModelController.register_model(NUMultiCastList)
    NURESTModelController.register_model(NUMultiCastRange)
    NURESTModelController.register_model(NUMultiNICVPort)
    NURESTModelController.register_model(NUNATMapEntry)
    NURESTModelController.register_model(NUNetworkLayout)
    NURESTModelController.register_model(NUNetworkMacroGroup)
    NURESTModelController.register_model(NUNSGateway)
    NURESTModelController.register_model(NUNSGatewayTemplate)
    NURESTModelController.register_model(NUNSPort)
    NURESTModelController.register_model(NUNSPortStaticConfiguration)
    NURESTModelController.register_model(NUNSPortTemplate)
    NURESTModelController.register_model(NUNSRedundantGatewayGroup)
    NURESTModelController.register_model(NUPATNATPool)
    NURESTModelController.register_model(NUPermission)
    NURESTModelController.register_model(NUPolicyDecision)
    NURESTModelController.register_model(NUPolicyGroup)
    NURESTModelController.register_model(NUPolicyGroupTemplate)
    NURESTModelController.register_model(NUPort)
    NURESTModelController.register_model(NUPortTemplate)
    NURESTModelController.register_model(NUPublicNetworkMacro)
    NURESTModelController.register_model(NUQOS)
    NURESTModelController.register_model(NURateLimiter)
    NURESTModelController.register_model(NURedirectionTarget)
    NURESTModelController.register_model(NURedirectionTargetTemplate)
    NURESTModelController.register_model(NURedundancyGroup)
    NURESTModelController.register_model(NURedundantPort)
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
    NURESTModelController.register_model(NUUplinkRD)
    NURESTModelController.register_model(NUUser)
    NURESTModelController.register_model(NUVCenter)
    NURESTModelController.register_model(NUVCenterCluster)
    NURESTModelController.register_model(NUVCenterDataCenter)
    NURESTModelController.register_model(NUVCenterEAMConfig)
    NURESTModelController.register_model(NUVCenterHypervisor)
    NURESTModelController.register_model(NUVCenterVRSConfig)
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
    NURESTModelController.register_model(NUVSC)
    NURESTModelController.register_model(NUVSD)
    NURESTModelController.register_model(NUVSDComponent)
    NURESTModelController.register_model(NUVsgRedundantPort)
    NURESTModelController.register_model(NUVSP)
    NURESTModelController.register_model(NUWANService)
    NURESTModelController.register_model(NUZone)
    NURESTModelController.register_model(NUZoneTemplate)
    

__setup_bambou()