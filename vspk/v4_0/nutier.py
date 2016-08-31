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



from .fetchers import NUTCAsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVMsFetcher


from .fetchers import NUContainersFetcher


from .fetchers import NUVPortsFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUStatisticsPoliciesFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUTier(NURESTObject):
    """ Represents a Tier in the VSD

        Notes:
            Tier represents a portion of an Application.
    """

    __rest_name__ = "tier"
    __resource_name__ = "tiers"

    
    ## Constants
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ENTITY_METADATA_BINDING = "ENTITY_METADATA_BINDING"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ESI_SEQUENCENO = "ESI_SEQUENCENO"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_POLICING_POLICY = "POLICING_POLICY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VIRTUAL_MACHINE_REPORT = "VIRTUAL_MACHINE_REPORT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EGRESS_ACL_TEMPLATE_ENTRY = "EGRESS_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EGRESS_ACL_TEMPLATE = "EGRESS_ACL_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GEO_VM_EVENT = "GEO_VM_EVENT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SYSTEM_MONITORING = "SYSTEM_MONITORING"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_RTRD_ENTITY = "RTRD_ENTITY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ACLENTRY_LOCATION = "ACLENTRY_LOCATION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ZONE = "ZONE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_CERTIFICATE = "CERTIFICATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VMWARE_VCENTER_HYPERVISOR = "VMWARE_VCENTER_HYPERVISOR"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_IKE_GATEWAY_CONNECTION = "IKE_GATEWAY_CONNECTION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_BOOTSTRAP = "BOOTSTRAP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_CONFIG_RESP = "GATEWAY_CONFIG_RESP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INFRASTRUCTURE_VSC_PROFILE = "INFRASTRUCTURE_VSC_PROFILE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VMWARE_VRS_ADDRESS_RANGE = "VMWARE_VRS_ADDRESS_RANGE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VRS = "VRS"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EGRESS_ACL_ENTRY = "EGRESS_ACL_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VPORT_GATEWAY_RESPONSE = "VPORT_GATEWAY_RESPONSE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_CONFIG = "GATEWAY_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NSPORT_TEMPLATE = "NSPORT_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_SECURITY = "GATEWAY_SECURITY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ENTERPRISE_PERMISSION = "ENTERPRISE_PERMISSION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_APPD_TIER = "APPD_TIER"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NETWORK_ELEMENT = "NETWORK_ELEMENT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EXPORTIMPORT = "EXPORTIMPORT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_PERMISSION = "PERMISSION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ENTERPRISE_NETWORK = "ENTERPRISE_NETWORK"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_VPORT_CONFIG_RESP = "GATEWAY_VPORT_CONFIG_RESP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_KEYSERVER_MONITOR = "KEYSERVER_MONITOR"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_QOS_PRIMITIVE = "QOS_PRIMITIVE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_BACK_HAUL_SERVICE_RESP = "BACK_HAUL_SERVICE_RESP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SUBNET_MAC_ENTRY = "SUBNET_MAC_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_IKE_GATEWAY_PROFILE = "IKE_GATEWAY_PROFILE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_PATCONFIG_CONFIG_RESP = "PATCONFIG_CONFIG_RESP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ENTERPRISE_CONFIG = "ENTERPRISE_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VM_RESYNC = "VM_RESYNC"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_IKE_SUBNET = "IKE_SUBNET"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_CUSTOMER_VRF_SEQUENCENO = "CUSTOMER_VRF_SEQUENCENO"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_APPD_FLOW_SECURITY_POLICY = "APPD_FLOW_SECURITY_POLICY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_RTRD_SEQUENCENO = "RTRD_SEQUENCENO"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VPN_CONNECT = "VPN_CONNECT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EGRESS_ACL = "EGRESS_ACL"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_FLOATING_IP_ACL_TEMPLATE_ENTRY = "FLOATING_IP_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_SECURITY_RESPONSE = "GATEWAY_SECURITY_RESPONSE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_ACL = "INGRESS_ACL"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_STATS_POLICY = "STATS_POLICY"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NSREDUNDANT_GW_GRP = "NSREDUNDANT_GW_GRP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_ACL_TEMPLATE = "INGRESS_ACL_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_RATE_LIMITER = "RATE_LIMITER"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VMWARE_VCENTER_DATACENTER = "VMWARE_VCENTER_DATACENTER"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_AUTO_DISC_GATEWAY = "AUTO_DISC_GATEWAY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_LOCATION = "LOCATION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_PATNATPOOL = "PATNATPOOL"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_MC_CHANNEL_MAP = "MC_CHANNEL_MAP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VSC = "VSC"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NATMAPENTRY = "NATMAPENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_L2DOMAIN_TEMPLATE = "L2DOMAIN_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VSP = "VSP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VSD = "VSD"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VMWARE_RELOAD_CONFIG = "VMWARE_RELOAD_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ENTERPRISE_SECURED_DATA = "ENTERPRISE_SECURED_DATA"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SUBNET_POOL_ENTRY = "SUBNET_POOL_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_BGP_NEIGHBOR_MED_RESPONSE = "BGP_NEIGHBOR_MED_RESPONSE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VLAN_TEMPLATE = "VLAN_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VPORT = "VPORT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_BRIDGEINTERFACE = "BRIDGEINTERFACE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_HOSTINTERFACE = "HOSTINTERFACE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_TEMPLATE = "GATEWAY_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NETWORK_MACRO_GROUP = "NETWORK_MACRO_GROUP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DC_CONFIG = "DC_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VMWARE_VCENTER = "VMWARE_VCENTER"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_MC_RANGE = "MC_RANGE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_IKE_GATEWAY_CONFIG = "IKE_GATEWAY_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_KEYSERVER_MEMBER = "KEYSERVER_MEMBER"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_PORT_VLAN_CONFIG = "PORT_VLAN_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SERVICE_VRF_SEQUENCENO = "SERVICE_VRF_SEQUENCENO"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VM_DESCRIPTION = "VM_DESCRIPTION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VNID_SEQUENCENO = "VNID_SEQUENCENO"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_LIBVIRT_INTERFACE = "LIBVIRT_INTERFACE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_ACL_TEMPLATE_ENTRY = "INGRESS_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NSPORT = "NSPORT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EVPN_BGP_COMMUNITY_TAG_ENTRY = "EVPN_BGP_COMMUNITY_TAG_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SUBNET_ENTRY = "SUBNET_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_USER = "USER"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_CHILD_ENTITY_POLICY_CHANGE = "CHILD_ENTITY_POLICY_CHANGE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SYSTEM_CONFIG_REQ = "SYSTEM_CONFIG_REQ"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_IP_BINDING = "IP_BINDING"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SERVICES_GATEWAY_RESPONSE = "SERVICES_GATEWAY_RESPONSE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NSPORT_VLAN_CONFIG = "NSPORT_VLAN_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GROUP = "GROUP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_EXT_SERVICE_TEMPLATE_ENTRY = "INGRESS_EXT_SERVICE_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ADDRESS_RANGE_STATE = "ADDRESS_RANGE_STATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SERVICE_GATEWAY_RESPONSE = "SERVICE_GATEWAY_RESPONSE"
    
    CONST_TYPE_APPLICATION_EXTENDED_NETWORK = "APPLICATION_EXTENDED_NETWORK"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SITE_RES = "SITE_RES"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INFRASTRUCTURE_GATEWAY_PROFILE = "INFRASTRUCTURE_GATEWAY_PROFILE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_APPD_FLOW = "APPD_FLOW"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_FLOATING_IP_ACL_TEMPLATE = "FLOATING_IP_ACL_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_ADV_FWD_TEMPLATE_ENTRY = "INGRESS_ADV_FWD_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DHCP_OPTION = "DHCP_OPTION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_HSC = "HSC"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_ADV_FWD_ENTRY = "INGRESS_ADV_FWD_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_RD_SEQUENCENO = "RD_SEQUENCENO"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EXTERNAL_SERVICE = "EXTERNAL_SERVICE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_MULTI_NIC_VPORT = "MULTI_NIC_VPORT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_ADV_FWD_TEMPLATE = "INGRESS_ADV_FWD_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_REDUNDANT_GW_GRP = "REDUNDANT_GW_GRP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_BOOTSTRAP_ACTIVATION = "BOOTSTRAP_ACTIVATION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_FLOATINGIP = "FLOATINGIP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SUBNET_TEMPLATE = "SUBNET_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_KEYSERVER_MONITOR_ENCRYPTED_SEED = "KEYSERVER_MONITOR_ENCRYPTED_SEED"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_LICENSE = "LICENSE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NETWORK_LAYOUT = "NETWORK_LAYOUT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NSGATEWAY_TEMPLATE = "NSGATEWAY_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_METADATA = "METADATA"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_SERVICE_CONFIG_RESP = "GATEWAY_SERVICE_CONFIG_RESP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ROUTING_POL_MED_RESPONSE = "ROUTING_POL_MED_RESPONSE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_BGPPEER = "BGPPEER"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DISKSTATS = "DISKSTATS"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_IKE_ENCRYPTION_PROFILE = "IKE_ENCRYPTION_PROFILE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_BGP_PROFILE_MED_RESPONSE = "BGP_PROFILE_MED_RESPONSE"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VMWARE_VCENTER_EAM_CONFIG = "VMWARE_VCENTER_EAM_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DSCP_FORWARDING_CLASS_MAPPING = "DSCP_FORWARDING_CLASS_MAPPING"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NSGATEWAY = "NSGATEWAY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VIRTUAL_IP = "VIRTUAL_IP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_BGP_PROFILE = "BGP_PROFILE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SUBNET = "SUBNET"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_APPD_SERVICE = "APPD_SERVICE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_APPD_FLOW_FORWARDING_POLICY = "APPD_FLOW_FORWARDING_POLICY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INFRASTRUCTURE_CONFIG = "INFRASTRUCTURE_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_APPD_APPLICATION = "APPD_APPLICATION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NS_REDUNDANT_PORT = "NS_REDUNDANT_PORT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INFRASTRUCTURE_PORT_PROFILE = "INFRASTRUCTURE_PORT_PROFILE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SHAPING_POLICY = "SHAPING_POLICY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VSD_COMPONENT = "VSD_COMPONENT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VIRTUAL_MACHINE = "VIRTUAL_MACHINE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SYSTEM_CONFIG = "SYSTEM_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_STATS_COLLECTOR = "STATS_COLLECTOR"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_VPORT_CONFIG = "GATEWAY_VPORT_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VLAN_CONFIG_RESPONSE = "VLAN_CONFIG_RESPONSE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_KEYSERVER_MONITOR_SEED = "KEYSERVER_MONITOR_SEED"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_CLOUD_MGMT_SYSTEM = "CLOUD_MGMT_SYSTEM"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_SECURITY_PROFILE_RESPONSE = "GATEWAY_SECURITY_PROFILE_RESPONSE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_WAN_SERVICE = "WAN_SERVICE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GEO_VM_REQ = "GEO_VM_REQ"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_SECURED_DATA = "GATEWAY_SECURED_DATA"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_APPD_EXTERNAL_APP_SERVICE = "APPD_EXTERNAL_APP_SERVICE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_PERMITTED_ACTION = "PERMITTED_ACTION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_MC_LIST = "MC_LIST"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_POLICY_GROUP_TEMPLATE = "POLICY_GROUP_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GEO_VM_RES = "GEO_VM_RES"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EVPN_BGP_COMMUNITY_TAG_SEQ_NO = "EVPN_BGP_COMMUNITY_TAG_SEQ_NO"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_BGP_DAMPENING_MED_RESPONSE = "BGP_DAMPENING_MED_RESPONSE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_EXT_SERVICE = "INGRESS_EXT_SERVICE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ZONE_TEMPLATE = "ZONE_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NSPORT_STATIC_CONFIG = "NSPORT_STATIC_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VLAN = "VLAN"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NETWORK_POLICY_GROUP = "NETWORK_POLICY_GROUP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_SECURITY_REQUEST = "GATEWAY_SECURITY_REQUEST"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_METADATA_TAG = "METADATA_TAG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY = "DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_SECURITY_PROFILE_REQUEST = "GATEWAY_SECURITY_PROFILE_REQUEST"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_UNSUPPORTED = "UNSUPPORTED"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ENDPOINT = "ENDPOINT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DOMAIN_FLOATING_IP_ACL_TEMPLATE = "DOMAIN_FLOATING_IP_ACL_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_PORT_VLAN_CONFIG_RESPONSE = "PORT_VLAN_CONFIG_RESPONSE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_HEALTH_REQ = "HEALTH_REQ"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_EXT_SERVICE_TEMPLATE = "INGRESS_EXT_SERVICE_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VPORTTAGTEMPLATE = "VPORTTAGTEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ENTERPRISE_CONFIG_RESP = "ENTERPRISE_CONFIG_RESP"
    
    CONST_TYPE_NETWORK_MACRO = "NETWORK_MACRO"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DHCP_ALLOC_MESSAGE = "DHCP_ALLOC_MESSAGE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_IKE_PSK = "IKE_PSK"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_CONTAINER_RESYNC = "CONTAINER_RESYNC"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NSGATEWAY_CONFIG = "NSGATEWAY_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SITE_REQ = "SITE_REQ"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DOMAIN_TEMPLATE = "DOMAIN_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_L2DOMAIN_SHARED = "L2DOMAIN_SHARED"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ALARM = "ALARM"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DOMAIN_CONFIG = "DOMAIN_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SHARED_RESOURCE = "SHARED_RESOURCE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DOMAIN = "DOMAIN"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_STATIC_ROUTE_RESP = "STATIC_ROUTE_RESP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_L2DOMAIN = "L2DOMAIN"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_FLOATINGIP_ACL_ENTRY = "FLOATINGIP_ACL_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_POLICY_GROUP = "POLICY_GROUP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NODE_EXECUTION_ERROR = "NODE_EXECUTION_ERROR"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_PORT_MR = "PORT_MR"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DHCP_CONFIG_RESP = "DHCP_CONFIG_RESP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ROUTING_POLICY = "ROUTING_POLICY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ADDRESS_RANGE = "ADDRESS_RANGE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DOMAIN_CONFIG_RESP = "DOMAIN_CONFIG_RESP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VPORT_MIRROR = "VPORT_MIRROR"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SYSTEM_CONFIG_RESP = "SYSTEM_CONFIG_RESP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VMWARE_VCENTER_CLUSTER = "VMWARE_VCENTER_CLUSTER"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_LDAP_CONFIG = "LDAP_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_PORT = "PORT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_IKE_CERTIFICATE = "IKE_CERTIFICATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_PUBLIC_NETWORK = "PUBLIC_NETWORK"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_FLOATINGIP_ACL = "FLOATINGIP_ACL"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EVENT_LOG = "EVENT_LOG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_STATS_TCA = "STATS_TCA"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY_SERVICE_CONFIG = "GATEWAY_SERVICE_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_BGP_NEIGHBOR = "BGP_NEIGHBOR"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VPORTTAG = "VPORTTAG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_DSCP_FORWARDING_CLASS_TABLE = "DSCP_FORWARDING_CLASS_TABLE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_KEYSERVER_NOTIFICATION = "KEYSERVER_NOTIFICATION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_APPLICATION = "APPLICATION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_STATISTICS = "STATISTICS"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NSG_NOTIFICATION = "NSG_NOTIFICATION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_MONITORING_PORT = "MONITORING_PORT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VMWARE_VCENTER_VRS_BASE_CONFIG = "VMWARE_VCENTER_VRS_BASE_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VPRN_LABEL_SEQUENCENO = "VPRN_LABEL_SEQUENCENO"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_PORT_PUSH = "PORT_PUSH"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VM_INTERFACE = "VM_INTERFACE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_POLICY_DECISION = "POLICY_DECISION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_MIRROR_DESTINATION = "MIRROR_DESTINATION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_SITE = "SITE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VMWARE_VCENTER_VRS_CONFIG = "VMWARE_VCENTER_VRS_CONFIG"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_ACL_ENTRY = "INGRESS_ACL_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VPORT_TAG_BASE = "VPORT_TAG_BASE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_KEYSERVER_MONITOR_SEK = "KEYSERVER_MONITOR_SEK"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EGRESS_QOS_QUEUE_MR = "EGRESS_QOS_QUEUE_MR"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GATEWAY = "GATEWAY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_STATIC_ROUTE = "STATIC_ROUTE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_STATSSERVER = "STATSSERVER"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_EXT_SERVICE_ENTRY = "INGRESS_EXT_SERVICE_ENTRY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VSG_REDUNDANT_PORT = "VSG_REDUNDANT_PORT"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_NEXT_HOP_RESP = "NEXT_HOP_RESP"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_UPLINK_RD = "UPLINK_RD"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_PORT_TEMPLATE = "PORT_TEMPLATE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ENTERPRISE_SECURITY = "ENTERPRISE_SECURITY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_VPORT_MEDIATION_REQUEST = "VPORT_MEDIATION_REQUEST"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_GROUPKEY_ENCRYPTION_PROFILE = "GROUPKEY_ENCRYPTION_PROFILE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_IKE_GATEWAY = "IKE_GATEWAY"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_JOB = "JOB"
    
    CONST_TYPE_STANDARD = "STANDARD"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_INGRESS_ADV_FWD = "INGRESS_ADV_FWD"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_ENTERPRISE_PROFILE = "ENTERPRISE_PROFILE"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EGRESS_QOS_MR = "EGRESS_QOS_MR"
    
    CONST_TYPE_APPLICATION = "APPLICATION"
    
    CONST_ASSOCIATED_NETWORK_OBJECT_TYPE_EGRESS_QOS_PRIMITIVE = "EGRESS_QOS_PRIMITIVE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Tier instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> tier = NUTier(id=u'xxxx-xxx-xxx-xxx', name=u'Tier')
                >>> tier = NUTier(data=my_dict)
        """

        super(NUTier, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._gateway = None
        self._address = None
        self._description = None
        self._metadata = None
        self._netmask = None
        self._entity_scope = None
        self._associated_application_id = None
        self._associated_floating_ip_pool_id = None
        self._associated_network_macro_id = None
        self._associated_network_object_id = None
        self._associated_network_object_type = None
        self._external_id = None
        self._type = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway", remote_name="gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata", remote_name="metadata", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_application_id", remote_name="associatedApplicationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_floating_ip_pool_id", remote_name="associatedFloatingIPPoolID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_network_macro_id", remote_name="associatedNetworkMacroID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_network_object_id", remote_name="associatedNetworkObjectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_network_object_type", remote_name="associatedNetworkObjectType", attribute_type=str, is_required=False, is_unique=False, choices=[u'ACLENTRY_LOCATION', u'ADDRESS_RANGE', u'ADDRESS_RANGE_STATE', u'ALARM', u'APPD_APPLICATION', u'APPD_EXTERNAL_APP_SERVICE', u'APPD_FLOW', u'APPD_FLOW_FORWARDING_POLICY', u'APPD_FLOW_SECURITY_POLICY', u'APPD_SERVICE', u'APPD_TIER', u'APPLICATION', u'AUTO_DISC_GATEWAY', u'BACK_HAUL_SERVICE_RESP', u'BGP_DAMPENING_MED_RESPONSE', u'BGP_NEIGHBOR', u'BGP_NEIGHBOR_MED_RESPONSE', u'BGP_PROFILE', u'BGP_PROFILE_MED_RESPONSE', u'BGPPEER', u'BOOTSTRAP', u'BOOTSTRAP_ACTIVATION', u'BRIDGEINTERFACE', u'CERTIFICATE', u'CHILD_ENTITY_POLICY_CHANGE', u'CLOUD_MGMT_SYSTEM', u'CONTAINER_RESYNC', u'CUSTOMER_VRF_SEQUENCENO', u'DC_CONFIG', u'DHCP_ALLOC_MESSAGE', u'DHCP_CONFIG_RESP', u'DHCP_OPTION', u'DISKSTATS', u'DOMAIN', u'DOMAIN_CONFIG', u'DOMAIN_CONFIG_RESP', u'DOMAIN_FLOATING_IP_ACL_TEMPLATE', u'DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY', u'DOMAIN_TEMPLATE', u'DSCP_FORWARDING_CLASS_MAPPING', u'DSCP_FORWARDING_CLASS_TABLE', u'EGRESS_ACL', u'EGRESS_ACL_ENTRY', u'EGRESS_ACL_TEMPLATE', u'EGRESS_ACL_TEMPLATE_ENTRY', u'EGRESS_QOS_MR', u'EGRESS_QOS_PRIMITIVE', u'EGRESS_QOS_QUEUE_MR', u'ENDPOINT', u'ENTERPRISE', u'ENTERPRISE_CONFIG', u'ENTERPRISE_CONFIG_RESP', u'ENTERPRISE_NETWORK', u'ENTERPRISE_PERMISSION', u'ENTERPRISE_PROFILE', u'ENTERPRISE_SECURED_DATA', u'ENTERPRISE_SECURITY', u'ENTITY_METADATA_BINDING', u'ESI_SEQUENCENO', u'EVENT_LOG', u'EVPN_BGP_COMMUNITY_TAG_ENTRY', u'EVPN_BGP_COMMUNITY_TAG_SEQ_NO', u'EXPORTIMPORT', u'EXTERNAL_SERVICE', u'FLOATING_IP_ACL_TEMPLATE', u'FLOATING_IP_ACL_TEMPLATE_ENTRY', u'FLOATINGIP', u'FLOATINGIP_ACL', u'FLOATINGIP_ACL_ENTRY', u'GATEWAY', u'GATEWAY_CONFIG', u'GATEWAY_CONFIG_RESP', u'GATEWAY_SECURED_DATA', u'GATEWAY_SECURITY', u'GATEWAY_SECURITY_PROFILE_REQUEST', u'GATEWAY_SECURITY_PROFILE_RESPONSE', u'GATEWAY_SECURITY_REQUEST', u'GATEWAY_SECURITY_RESPONSE', u'GATEWAY_SERVICE_CONFIG', u'GATEWAY_SERVICE_CONFIG_RESP', u'GATEWAY_TEMPLATE', u'GATEWAY_VPORT_CONFIG', u'GATEWAY_VPORT_CONFIG_RESP', u'GEO_VM_EVENT', u'GEO_VM_REQ', u'GEO_VM_RES', u'GROUP', u'GROUPKEY_ENCRYPTION_PROFILE', u'HEALTH_REQ', u'HOSTINTERFACE', u'HSC', u'IKE_CERTIFICATE', u'IKE_ENCRYPTION_PROFILE', u'IKE_GATEWAY', u'IKE_GATEWAY_CONFIG', u'IKE_GATEWAY_CONNECTION', u'IKE_GATEWAY_PROFILE', u'IKE_PSK', u'IKE_SUBNET', u'INFRASTRUCTURE_CONFIG', u'INFRASTRUCTURE_GATEWAY_PROFILE', u'INFRASTRUCTURE_PORT_PROFILE', u'INFRASTRUCTURE_VSC_PROFILE', u'INGRESS_ACL', u'INGRESS_ACL_ENTRY', u'INGRESS_ACL_TEMPLATE', u'INGRESS_ACL_TEMPLATE_ENTRY', u'INGRESS_ADV_FWD', u'INGRESS_ADV_FWD_ENTRY', u'INGRESS_ADV_FWD_TEMPLATE', u'INGRESS_ADV_FWD_TEMPLATE_ENTRY', u'INGRESS_EXT_SERVICE', u'INGRESS_EXT_SERVICE_ENTRY', u'INGRESS_EXT_SERVICE_TEMPLATE', u'INGRESS_EXT_SERVICE_TEMPLATE_ENTRY', u'IP_BINDING', u'JOB', u'KEYSERVER_MEMBER', u'KEYSERVER_MONITOR', u'KEYSERVER_MONITOR_ENCRYPTED_SEED', u'KEYSERVER_MONITOR_SEED', u'KEYSERVER_MONITOR_SEK', u'KEYSERVER_NOTIFICATION', u'L2DOMAIN', u'L2DOMAIN_SHARED', u'L2DOMAIN_TEMPLATE', u'LDAP_CONFIG', u'LIBVIRT_INTERFACE', u'LICENSE', u'LOCATION', u'MC_CHANNEL_MAP', u'MC_LIST', u'MC_RANGE', u'METADATA', u'METADATA_TAG', u'MIRROR_DESTINATION', u'MONITORING_PORT', u'MULTI_NIC_VPORT', u'NATMAPENTRY', u'NETWORK_ELEMENT', u'NETWORK_LAYOUT', u'NETWORK_MACRO_GROUP', u'NETWORK_POLICY_GROUP', u'NEXT_HOP_RESP', u'NODE_EXECUTION_ERROR', u'NS_REDUNDANT_PORT', u'NSG_NOTIFICATION', u'NSGATEWAY', u'NSGATEWAY_CONFIG', u'NSGATEWAY_TEMPLATE', u'NSPORT', u'NSPORT_STATIC_CONFIG', u'NSPORT_TEMPLATE', u'NSPORT_VLAN_CONFIG', u'NSREDUNDANT_GW_GRP', u'PATCONFIG_CONFIG_RESP', u'PATNATPOOL', u'PERMISSION', u'PERMITTED_ACTION', u'POLICING_POLICY', u'POLICY_DECISION', u'POLICY_GROUP', u'POLICY_GROUP_TEMPLATE', u'PORT', u'PORT_MR', u'PORT_PUSH', u'PORT_TEMPLATE', u'PORT_VLAN_CONFIG', u'PORT_VLAN_CONFIG_RESPONSE', u'PUBLIC_NETWORK', u'QOS_PRIMITIVE', u'RATE_LIMITER', u'RD_SEQUENCENO', u'REDUNDANT_GW_GRP', u'ROUTING_POL_MED_RESPONSE', u'ROUTING_POLICY', u'RTRD_ENTITY', u'RTRD_SEQUENCENO', u'SERVICE_GATEWAY_RESPONSE', u'SERVICE_VRF_SEQUENCENO', u'SERVICES_GATEWAY_RESPONSE', u'SHAPING_POLICY', u'SHARED_RESOURCE', u'SITE', u'SITE_REQ', u'SITE_RES', u'STATIC_ROUTE', u'STATIC_ROUTE_RESP', u'STATISTICS', u'STATS_COLLECTOR', u'STATS_POLICY', u'STATS_TCA', u'STATSSERVER', u'SUBNET', u'SUBNET_ENTRY', u'SUBNET_MAC_ENTRY', u'SUBNET_POOL_ENTRY', u'SUBNET_TEMPLATE', u'SYSTEM_CONFIG', u'SYSTEM_CONFIG_REQ', u'SYSTEM_CONFIG_RESP', u'SYSTEM_MONITORING', u'UNSUPPORTED', u'UPLINK_RD', u'USER', u'VIRTUAL_IP', u'VIRTUAL_MACHINE', u'VIRTUAL_MACHINE_REPORT', u'VLAN', u'VLAN_CONFIG_RESPONSE', u'VLAN_TEMPLATE', u'VM_DESCRIPTION', u'VM_INTERFACE', u'VM_RESYNC', u'VMWARE_RELOAD_CONFIG', u'VMWARE_VCENTER', u'VMWARE_VCENTER_CLUSTER', u'VMWARE_VCENTER_DATACENTER', u'VMWARE_VCENTER_EAM_CONFIG', u'VMWARE_VCENTER_HYPERVISOR', u'VMWARE_VCENTER_VRS_BASE_CONFIG', u'VMWARE_VCENTER_VRS_CONFIG', u'VMWARE_VRS_ADDRESS_RANGE', u'VNID_SEQUENCENO', u'VPN_CONNECT', u'VPORT', u'VPORT_GATEWAY_RESPONSE', u'VPORT_MEDIATION_REQUEST', u'VPORT_MIRROR', u'VPORT_TAG_BASE', u'VPORTTAG', u'VPORTTAGTEMPLATE', u'VPRN_LABEL_SEQUENCENO', u'VRS', u'VSC', u'VSD', u'VSD_COMPONENT', u'VSG_REDUNDANT_PORT', u'VSP', u'WAN_SERVICE', u'ZONE', u'ZONE_TEMPLATE'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=True, is_unique=False, choices=[u'APPLICATION', u'APPLICATION_EXTENDED_NETWORK', u'NETWORK_MACRO', u'STANDARD'])
        

        # Fetchers
        
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.containers = NUContainersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the application tier.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the application tier.

                
        """
        self._name = value

    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def gateway(self):
        """ Get gateway value.

            Notes:
                The IP address of the gateway for this tier.

                
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """ Set gateway value.

            Notes:
                The IP address of the gateway for this tier.

                
        """
        self._gateway = value

    
    @property
    def address(self):
        """ Get address value.

            Notes:
                IP address of the tier defined.

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                IP address of the tier defined.

                
        """
        self._address = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the application tier.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the application tier.

                
        """
        self._description = value

    
    @property
    def metadata(self):
        """ Get metadata value.

            Notes:
                Metadata field to store tier related data.

                
        """
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        """ Set metadata value.

            Notes:
                Metadata field to store tier related data.

                
        """
        self._metadata = value

    
    @property
    def netmask(self):
        """ Get netmask value.

            Notes:
                Netmask for the tier.

                
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """ Set netmask value.

            Notes:
                Netmask for the tier.

                
        """
        self._netmask = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def associated_application_id(self):
        """ Get associated_application_id value.

            Notes:
                The associated network macro ID.

                
                This attribute is named `associatedApplicationID` in VSD API.
                
        """
        return self._associated_application_id

    @associated_application_id.setter
    def associated_application_id(self, value):
        """ Set associated_application_id value.

            Notes:
                The associated network macro ID.

                
                This attribute is named `associatedApplicationID` in VSD API.
                
        """
        self._associated_application_id = value

    
    @property
    def associated_floating_ip_pool_id(self):
        """ Get associated_floating_ip_pool_id value.

            Notes:
                The associated floating IP Pool ID.

                
                This attribute is named `associatedFloatingIPPoolID` in VSD API.
                
        """
        return self._associated_floating_ip_pool_id

    @associated_floating_ip_pool_id.setter
    def associated_floating_ip_pool_id(self, value):
        """ Set associated_floating_ip_pool_id value.

            Notes:
                The associated floating IP Pool ID.

                
                This attribute is named `associatedFloatingIPPoolID` in VSD API.
                
        """
        self._associated_floating_ip_pool_id = value

    
    @property
    def associated_network_macro_id(self):
        """ Get associated_network_macro_id value.

            Notes:
                The associated network macro ID.

                
                This attribute is named `associatedNetworkMacroID` in VSD API.
                
        """
        return self._associated_network_macro_id

    @associated_network_macro_id.setter
    def associated_network_macro_id(self, value):
        """ Set associated_network_macro_id value.

            Notes:
                The associated network macro ID.

                
                This attribute is named `associatedNetworkMacroID` in VSD API.
                
        """
        self._associated_network_macro_id = value

    
    @property
    def associated_network_object_id(self):
        """ Get associated_network_object_id value.

            Notes:
                The associated network object id.

                
                This attribute is named `associatedNetworkObjectID` in VSD API.
                
        """
        return self._associated_network_object_id

    @associated_network_object_id.setter
    def associated_network_object_id(self, value):
        """ Set associated_network_object_id value.

            Notes:
                The associated network object id.

                
                This attribute is named `associatedNetworkObjectID` in VSD API.
                
        """
        self._associated_network_object_id = value

    
    @property
    def associated_network_object_type(self):
        """ Get associated_network_object_type value.

            Notes:
                The associated network object type. Refer to API section for supported types.

                
                This attribute is named `associatedNetworkObjectType` in VSD API.
                
        """
        return self._associated_network_object_type

    @associated_network_object_type.setter
    def associated_network_object_type(self, value):
        """ Set associated_network_object_type value.

            Notes:
                The associated network object type. Refer to API section for supported types.

                
                This attribute is named `associatedNetworkObjectType` in VSD API.
                
        """
        self._associated_network_object_type = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    
    @property
    def type(self):
        """ Get type value.

            Notes:
                Type of the application tier.

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                Type of the application tier.

                
        """
        self._type = value

    

    