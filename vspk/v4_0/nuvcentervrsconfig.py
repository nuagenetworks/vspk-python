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



from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVRSAddressRangesFetcher


from .fetchers import NUVRSRedeploymentpoliciesFetcher

from bambou import NURESTObject


class NUVCenterVRSConfig(NURESTObject):
    """ Represents a VCenterVRSConfig in the VSD

        Notes:
            Default VRS Configuration parameters
    """

    __rest_name__ = "vrsconfig"
    __resource_name__ = "vrsconfigs"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VCenterVRSConfig instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vcentervrsconfig = NUVCenterVRSConfig(id=u'xxxx-xxx-xxx-xxx', name=u'VCenterVRSConfig')
                >>> vcentervrsconfig = NUVCenterVRSConfig(data=my_dict)
        """

        super(NUVCenterVRSConfig, self).__init__()

        # Read/Write Attributes
        
        self._v_require_nuage_metadata = None
        self._last_updated_by = None
        self._data_dns1 = None
        self._data_dns2 = None
        self._data_gateway = None
        self._data_network_portgroup = None
        self._datapath_sync_timeout = None
        self._secondary_nuage_controller = None
        self._generic_split_activation = None
        self._separate_data_network = None
        self._personality = None
        self._metadata_server_ip = None
        self._metadata_server_listen_port = None
        self._metadata_server_port = None
        self._metadata_service_enabled = None
        self._network_uplink_interface = None
        self._network_uplink_interface_gateway = None
        self._network_uplink_interface_ip = None
        self._network_uplink_interface_netmask = None
        self._nfs_log_server = None
        self._nfs_mount_path = None
        self._mgmt_dns1 = None
        self._mgmt_dns2 = None
        self._mgmt_gateway = None
        self._mgmt_network_portgroup = None
        self._dhcp_relay_server = None
        self._site_id = None
        self._allow_data_dhcp = None
        self._allow_mgmt_dhcp = None
        self._flow_eviction_threshold = None
        self._vm_network_portgroup = None
        self._entity_scope = None
        self._portgroup_metadata = None
        self._nova_client_version = None
        self._nova_metadata_service_auth_url = None
        self._nova_metadata_service_endpoint = None
        self._nova_metadata_service_password = None
        self._nova_metadata_service_tenant = None
        self._nova_metadata_service_username = None
        self._nova_metadata_shared_secret = None
        self._nova_region_name = None
        self._primary_nuage_controller = None
        self._vrs_password = None
        self._vrs_user_name = None
        self._static_route = None
        self._static_route_gateway = None
        self._static_route_netmask = None
        self._ntp_server1 = None
        self._ntp_server2 = None
        self._mtu = None
        self._multi_vmssupport = None
        self._multicast_receive_interface = None
        self._multicast_receive_interface_ip = None
        self._multicast_receive_interface_netmask = None
        self._multicast_receive_range = None
        self._multicast_send_interface = None
        self._multicast_send_interface_ip = None
        self._multicast_send_interface_netmask = None
        self._multicast_source_portgroup = None
        self._customized_script_url = None
        self._external_id = None
        
        self.expose_attribute(local_name="v_require_nuage_metadata", remote_name="vRequireNuageMetadata", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="data_dns1", remote_name="dataDNS1", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="data_dns2", remote_name="dataDNS2", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="data_gateway", remote_name="dataGateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="data_network_portgroup", remote_name="dataNetworkPortgroup", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="datapath_sync_timeout", remote_name="datapathSyncTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_nuage_controller", remote_name="secondaryNuageController", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="generic_split_activation", remote_name="genericSplitActivation", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="separate_data_network", remote_name="separateDataNetwork", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_server_ip", remote_name="metadataServerIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_server_listen_port", remote_name="metadataServerListenPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_server_port", remote_name="metadataServerPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_service_enabled", remote_name="metadataServiceEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_uplink_interface", remote_name="networkUplinkInterface", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_uplink_interface_gateway", remote_name="networkUplinkInterfaceGateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_uplink_interface_ip", remote_name="networkUplinkInterfaceIp", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_uplink_interface_netmask", remote_name="networkUplinkInterfaceNetmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nfs_log_server", remote_name="nfsLogServer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nfs_mount_path", remote_name="nfsMountPath", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mgmt_dns1", remote_name="mgmtDNS1", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mgmt_dns2", remote_name="mgmtDNS2", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mgmt_gateway", remote_name="mgmtGateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mgmt_network_portgroup", remote_name="mgmtNetworkPortgroup", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dhcp_relay_server", remote_name="dhcpRelayServer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="site_id", remote_name="siteId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allow_data_dhcp", remote_name="allowDataDHCP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allow_mgmt_dhcp", remote_name="allowMgmtDHCP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="flow_eviction_threshold", remote_name="flowEvictionThreshold", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vm_network_portgroup", remote_name="vmNetworkPortgroup", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="portgroup_metadata", remote_name="portgroupMetadata", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_client_version", remote_name="novaClientVersion", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_service_auth_url", remote_name="novaMetadataServiceAuthUrl", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_service_endpoint", remote_name="novaMetadataServiceEndpoint", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_service_password", remote_name="novaMetadataServicePassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_service_tenant", remote_name="novaMetadataServiceTenant", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_service_username", remote_name="novaMetadataServiceUsername", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_metadata_shared_secret", remote_name="novaMetadataSharedSecret", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nova_region_name", remote_name="novaRegionName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="primary_nuage_controller", remote_name="primaryNuageController", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_password", remote_name="vrsPassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_user_name", remote_name="vrsUserName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="static_route", remote_name="staticRoute", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="static_route_gateway", remote_name="staticRouteGateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="static_route_netmask", remote_name="staticRouteNetmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ntp_server1", remote_name="ntpServer1", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ntp_server2", remote_name="ntpServer2", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mtu", remote_name="mtu", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multi_vmssupport", remote_name="multiVMSsupport", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_receive_interface", remote_name="multicastReceiveInterface", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_receive_interface_ip", remote_name="multicastReceiveInterfaceIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_receive_interface_netmask", remote_name="multicastReceiveInterfaceNetmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_receive_range", remote_name="multicastReceiveRange", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_send_interface", remote_name="multicastSendInterface", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_send_interface_ip", remote_name="multicastSendInterfaceIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_send_interface_netmask", remote_name="multicastSendInterfaceNetmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast_source_portgroup", remote_name="multicastSourcePortgroup", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="customized_script_url", remote_name="customizedScriptURL", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vrs_address_ranges = NUVRSAddressRangesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vrs_redeploymentpolicies = NUVRSRedeploymentpoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def v_require_nuage_metadata(self):
        """ Get v_require_nuage_metadata value.

            Notes:
                Whether split-activation or not (Openstack/CloudStack)

                
                This attribute is named `vRequireNuageMetadata` in VSD API.
                
        """
        return self._v_require_nuage_metadata

    @v_require_nuage_metadata.setter
    def v_require_nuage_metadata(self, value):
        """ Set v_require_nuage_metadata value.

            Notes:
                Whether split-activation or not (Openstack/CloudStack)

                
                This attribute is named `vRequireNuageMetadata` in VSD API.
                
        """
        self._v_require_nuage_metadata = value

    
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
    def data_dns1(self):
        """ Get data_dns1 value.

            Notes:
                Data DNS 1

                
                This attribute is named `dataDNS1` in VSD API.
                
        """
        return self._data_dns1

    @data_dns1.setter
    def data_dns1(self, value):
        """ Set data_dns1 value.

            Notes:
                Data DNS 1

                
                This attribute is named `dataDNS1` in VSD API.
                
        """
        self._data_dns1 = value

    
    @property
    def data_dns2(self):
        """ Get data_dns2 value.

            Notes:
                Data DNS 2

                
                This attribute is named `dataDNS2` in VSD API.
                
        """
        return self._data_dns2

    @data_dns2.setter
    def data_dns2(self, value):
        """ Set data_dns2 value.

            Notes:
                Data DNS 2

                
                This attribute is named `dataDNS2` in VSD API.
                
        """
        self._data_dns2 = value

    
    @property
    def data_gateway(self):
        """ Get data_gateway value.

            Notes:
                Data Gateway

                
                This attribute is named `dataGateway` in VSD API.
                
        """
        return self._data_gateway

    @data_gateway.setter
    def data_gateway(self, value):
        """ Set data_gateway value.

            Notes:
                Data Gateway

                
                This attribute is named `dataGateway` in VSD API.
                
        """
        self._data_gateway = value

    
    @property
    def data_network_portgroup(self):
        """ Get data_network_portgroup value.

            Notes:
                Data Network Port Group

                
                This attribute is named `dataNetworkPortgroup` in VSD API.
                
        """
        return self._data_network_portgroup

    @data_network_portgroup.setter
    def data_network_portgroup(self, value):
        """ Set data_network_portgroup value.

            Notes:
                Data Network Port Group

                
                This attribute is named `dataNetworkPortgroup` in VSD API.
                
        """
        self._data_network_portgroup = value

    
    @property
    def datapath_sync_timeout(self):
        """ Get datapath_sync_timeout value.

            Notes:
                Datapath Sync Timeout

                
                This attribute is named `datapathSyncTimeout` in VSD API.
                
        """
        return self._datapath_sync_timeout

    @datapath_sync_timeout.setter
    def datapath_sync_timeout(self, value):
        """ Set datapath_sync_timeout value.

            Notes:
                Datapath Sync Timeout

                
                This attribute is named `datapathSyncTimeout` in VSD API.
                
        """
        self._datapath_sync_timeout = value

    
    @property
    def secondary_nuage_controller(self):
        """ Get secondary_nuage_controller value.

            Notes:
                IP address of the secondary Controller (VSC)

                
                This attribute is named `secondaryNuageController` in VSD API.
                
        """
        return self._secondary_nuage_controller

    @secondary_nuage_controller.setter
    def secondary_nuage_controller(self, value):
        """ Set secondary_nuage_controller value.

            Notes:
                IP address of the secondary Controller (VSC)

                
                This attribute is named `secondaryNuageController` in VSD API.
                
        """
        self._secondary_nuage_controller = value

    
    @property
    def generic_split_activation(self):
        """ Get generic_split_activation value.

            Notes:
                Whether split-activation is needed from VRO

                
                This attribute is named `genericSplitActivation` in VSD API.
                
        """
        return self._generic_split_activation

    @generic_split_activation.setter
    def generic_split_activation(self, value):
        """ Set generic_split_activation value.

            Notes:
                Whether split-activation is needed from VRO

                
                This attribute is named `genericSplitActivation` in VSD API.
                
        """
        self._generic_split_activation = value

    
    @property
    def separate_data_network(self):
        """ Get separate_data_network value.

            Notes:
                Whether Data will use the management network or not

                
                This attribute is named `separateDataNetwork` in VSD API.
                
        """
        return self._separate_data_network

    @separate_data_network.setter
    def separate_data_network(self, value):
        """ Set separate_data_network value.

            Notes:
                Whether Data will use the management network or not

                
                This attribute is named `separateDataNetwork` in VSD API.
                
        """
        self._separate_data_network = value

    
    @property
    def personality(self):
        """ Get personality value.

            Notes:
                VRS/VRS-G

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                VRS/VRS-G

                
        """
        self._personality = value

    
    @property
    def metadata_server_ip(self):
        """ Get metadata_server_ip value.

            Notes:
                Metadata Server IP

                
                This attribute is named `metadataServerIP` in VSD API.
                
        """
        return self._metadata_server_ip

    @metadata_server_ip.setter
    def metadata_server_ip(self, value):
        """ Set metadata_server_ip value.

            Notes:
                Metadata Server IP

                
                This attribute is named `metadataServerIP` in VSD API.
                
        """
        self._metadata_server_ip = value

    
    @property
    def metadata_server_listen_port(self):
        """ Get metadata_server_listen_port value.

            Notes:
                Metadata Server Listen Port

                
                This attribute is named `metadataServerListenPort` in VSD API.
                
        """
        return self._metadata_server_listen_port

    @metadata_server_listen_port.setter
    def metadata_server_listen_port(self, value):
        """ Set metadata_server_listen_port value.

            Notes:
                Metadata Server Listen Port

                
                This attribute is named `metadataServerListenPort` in VSD API.
                
        """
        self._metadata_server_listen_port = value

    
    @property
    def metadata_server_port(self):
        """ Get metadata_server_port value.

            Notes:
                Metadata Server Port

                
                This attribute is named `metadataServerPort` in VSD API.
                
        """
        return self._metadata_server_port

    @metadata_server_port.setter
    def metadata_server_port(self, value):
        """ Set metadata_server_port value.

            Notes:
                Metadata Server Port

                
                This attribute is named `metadataServerPort` in VSD API.
                
        """
        self._metadata_server_port = value

    
    @property
    def metadata_service_enabled(self):
        """ Get metadata_service_enabled value.

            Notes:
                Metadata Service Enabled

                
                This attribute is named `metadataServiceEnabled` in VSD API.
                
        """
        return self._metadata_service_enabled

    @metadata_service_enabled.setter
    def metadata_service_enabled(self, value):
        """ Set metadata_service_enabled value.

            Notes:
                Metadata Service Enabled

                
                This attribute is named `metadataServiceEnabled` in VSD API.
                
        """
        self._metadata_service_enabled = value

    
    @property
    def network_uplink_interface(self):
        """ Get network_uplink_interface value.

            Notes:
                Network Upling Interface to support PAT/NAT with no tunnels on VRS-VM

                
                This attribute is named `networkUplinkInterface` in VSD API.
                
        """
        return self._network_uplink_interface

    @network_uplink_interface.setter
    def network_uplink_interface(self, value):
        """ Set network_uplink_interface value.

            Notes:
                Network Upling Interface to support PAT/NAT with no tunnels on VRS-VM

                
                This attribute is named `networkUplinkInterface` in VSD API.
                
        """
        self._network_uplink_interface = value

    
    @property
    def network_uplink_interface_gateway(self):
        """ Get network_uplink_interface_gateway value.

            Notes:
                Network Uplink Interface Gateway

                
                This attribute is named `networkUplinkInterfaceGateway` in VSD API.
                
        """
        return self._network_uplink_interface_gateway

    @network_uplink_interface_gateway.setter
    def network_uplink_interface_gateway(self, value):
        """ Set network_uplink_interface_gateway value.

            Notes:
                Network Uplink Interface Gateway

                
                This attribute is named `networkUplinkInterfaceGateway` in VSD API.
                
        """
        self._network_uplink_interface_gateway = value

    
    @property
    def network_uplink_interface_ip(self):
        """ Get network_uplink_interface_ip value.

            Notes:
                Ip Address to support PAT/NAT with no tunnels on VRS-VM

                
                This attribute is named `networkUplinkInterfaceIp` in VSD API.
                
        """
        return self._network_uplink_interface_ip

    @network_uplink_interface_ip.setter
    def network_uplink_interface_ip(self, value):
        """ Set network_uplink_interface_ip value.

            Notes:
                Ip Address to support PAT/NAT with no tunnels on VRS-VM

                
                This attribute is named `networkUplinkInterfaceIp` in VSD API.
                
        """
        self._network_uplink_interface_ip = value

    
    @property
    def network_uplink_interface_netmask(self):
        """ Get network_uplink_interface_netmask value.

            Notes:
                Network Uplink Interface Netmask

                
                This attribute is named `networkUplinkInterfaceNetmask` in VSD API.
                
        """
        return self._network_uplink_interface_netmask

    @network_uplink_interface_netmask.setter
    def network_uplink_interface_netmask(self, value):
        """ Set network_uplink_interface_netmask value.

            Notes:
                Network Uplink Interface Netmask

                
                This attribute is named `networkUplinkInterfaceNetmask` in VSD API.
                
        """
        self._network_uplink_interface_netmask = value

    
    @property
    def nfs_log_server(self):
        """ Get nfs_log_server value.

            Notes:
                IP address of NFS server to send the VRS log

                
                This attribute is named `nfsLogServer` in VSD API.
                
        """
        return self._nfs_log_server

    @nfs_log_server.setter
    def nfs_log_server(self, value):
        """ Set nfs_log_server value.

            Notes:
                IP address of NFS server to send the VRS log

                
                This attribute is named `nfsLogServer` in VSD API.
                
        """
        self._nfs_log_server = value

    
    @property
    def nfs_mount_path(self):
        """ Get nfs_mount_path value.

            Notes:
                Location to mount the NFS server

                
                This attribute is named `nfsMountPath` in VSD API.
                
        """
        return self._nfs_mount_path

    @nfs_mount_path.setter
    def nfs_mount_path(self, value):
        """ Set nfs_mount_path value.

            Notes:
                Location to mount the NFS server

                
                This attribute is named `nfsMountPath` in VSD API.
                
        """
        self._nfs_mount_path = value

    
    @property
    def mgmt_dns1(self):
        """ Get mgmt_dns1 value.

            Notes:
                DNS server 1

                
                This attribute is named `mgmtDNS1` in VSD API.
                
        """
        return self._mgmt_dns1

    @mgmt_dns1.setter
    def mgmt_dns1(self, value):
        """ Set mgmt_dns1 value.

            Notes:
                DNS server 1

                
                This attribute is named `mgmtDNS1` in VSD API.
                
        """
        self._mgmt_dns1 = value

    
    @property
    def mgmt_dns2(self):
        """ Get mgmt_dns2 value.

            Notes:
                DNS server 2

                
                This attribute is named `mgmtDNS2` in VSD API.
                
        """
        return self._mgmt_dns2

    @mgmt_dns2.setter
    def mgmt_dns2(self, value):
        """ Set mgmt_dns2 value.

            Notes:
                DNS server 2

                
                This attribute is named `mgmtDNS2` in VSD API.
                
        """
        self._mgmt_dns2 = value

    
    @property
    def mgmt_gateway(self):
        """ Get mgmt_gateway value.

            Notes:
                Gateway for the IP address

                
                This attribute is named `mgmtGateway` in VSD API.
                
        """
        return self._mgmt_gateway

    @mgmt_gateway.setter
    def mgmt_gateway(self, value):
        """ Set mgmt_gateway value.

            Notes:
                Gateway for the IP address

                
                This attribute is named `mgmtGateway` in VSD API.
                
        """
        self._mgmt_gateway = value

    
    @property
    def mgmt_network_portgroup(self):
        """ Get mgmt_network_portgroup value.

            Notes:
                Management Network Port group

                
                This attribute is named `mgmtNetworkPortgroup` in VSD API.
                
        """
        return self._mgmt_network_portgroup

    @mgmt_network_portgroup.setter
    def mgmt_network_portgroup(self, value):
        """ Set mgmt_network_portgroup value.

            Notes:
                Management Network Port group

                
                This attribute is named `mgmtNetworkPortgroup` in VSD API.
                
        """
        self._mgmt_network_portgroup = value

    
    @property
    def dhcp_relay_server(self):
        """ Get dhcp_relay_server value.

            Notes:
                To provide IP address of the interface from which you will connect to the DHCP relay server

                
                This attribute is named `dhcpRelayServer` in VSD API.
                
        """
        return self._dhcp_relay_server

    @dhcp_relay_server.setter
    def dhcp_relay_server(self, value):
        """ Set dhcp_relay_server value.

            Notes:
                To provide IP address of the interface from which you will connect to the DHCP relay server

                
                This attribute is named `dhcpRelayServer` in VSD API.
                
        """
        self._dhcp_relay_server = value

    
    @property
    def site_id(self):
        """ Get site_id value.

            Notes:
                Site ID field for object profiles to support VSD Geo-redundancy

                
                This attribute is named `siteId` in VSD API.
                
        """
        return self._site_id

    @site_id.setter
    def site_id(self, value):
        """ Set site_id value.

            Notes:
                Site ID field for object profiles to support VSD Geo-redundancy

                
                This attribute is named `siteId` in VSD API.
                
        """
        self._site_id = value

    
    @property
    def allow_data_dhcp(self):
        """ Get allow_data_dhcp value.

            Notes:
                Whether to get the Data IP for the VRS VM from DHCP or statically

                
                This attribute is named `allowDataDHCP` in VSD API.
                
        """
        return self._allow_data_dhcp

    @allow_data_dhcp.setter
    def allow_data_dhcp(self, value):
        """ Set allow_data_dhcp value.

            Notes:
                Whether to get the Data IP for the VRS VM from DHCP or statically

                
                This attribute is named `allowDataDHCP` in VSD API.
                
        """
        self._allow_data_dhcp = value

    
    @property
    def allow_mgmt_dhcp(self):
        """ Get allow_mgmt_dhcp value.

            Notes:
                Whether to get the management IP for the VRS VM from DHCP or statically

                
                This attribute is named `allowMgmtDHCP` in VSD API.
                
        """
        return self._allow_mgmt_dhcp

    @allow_mgmt_dhcp.setter
    def allow_mgmt_dhcp(self, value):
        """ Set allow_mgmt_dhcp value.

            Notes:
                Whether to get the management IP for the VRS VM from DHCP or statically

                
                This attribute is named `allowMgmtDHCP` in VSD API.
                
        """
        self._allow_mgmt_dhcp = value

    
    @property
    def flow_eviction_threshold(self):
        """ Get flow_eviction_threshold value.

            Notes:
                Flow Eviction Threshold

                
                This attribute is named `flowEvictionThreshold` in VSD API.
                
        """
        return self._flow_eviction_threshold

    @flow_eviction_threshold.setter
    def flow_eviction_threshold(self, value):
        """ Set flow_eviction_threshold value.

            Notes:
                Flow Eviction Threshold

                
                This attribute is named `flowEvictionThreshold` in VSD API.
                
        """
        self._flow_eviction_threshold = value

    
    @property
    def vm_network_portgroup(self):
        """ Get vm_network_portgroup value.

            Notes:
                VM Network Port Group Name

                
                This attribute is named `vmNetworkPortgroup` in VSD API.
                
        """
        return self._vm_network_portgroup

    @vm_network_portgroup.setter
    def vm_network_portgroup(self, value):
        """ Set vm_network_portgroup value.

            Notes:
                VM Network Port Group Name

                
                This attribute is named `vmNetworkPortgroup` in VSD API.
                
        """
        self._vm_network_portgroup = value

    
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
    def portgroup_metadata(self):
        """ Get portgroup_metadata value.

            Notes:
                Port Group Meta data

                
                This attribute is named `portgroupMetadata` in VSD API.
                
        """
        return self._portgroup_metadata

    @portgroup_metadata.setter
    def portgroup_metadata(self, value):
        """ Set portgroup_metadata value.

            Notes:
                Port Group Meta data

                
                This attribute is named `portgroupMetadata` in VSD API.
                
        """
        self._portgroup_metadata = value

    
    @property
    def nova_client_version(self):
        """ Get nova_client_version value.

            Notes:
                Nova client Version 

                
                This attribute is named `novaClientVersion` in VSD API.
                
        """
        return self._nova_client_version

    @nova_client_version.setter
    def nova_client_version(self, value):
        """ Set nova_client_version value.

            Notes:
                Nova client Version 

                
                This attribute is named `novaClientVersion` in VSD API.
                
        """
        self._nova_client_version = value

    
    @property
    def nova_metadata_service_auth_url(self):
        """ Get nova_metadata_service_auth_url value.

            Notes:
                Nova metadata service auth url

                
                This attribute is named `novaMetadataServiceAuthUrl` in VSD API.
                
        """
        return self._nova_metadata_service_auth_url

    @nova_metadata_service_auth_url.setter
    def nova_metadata_service_auth_url(self, value):
        """ Set nova_metadata_service_auth_url value.

            Notes:
                Nova metadata service auth url

                
                This attribute is named `novaMetadataServiceAuthUrl` in VSD API.
                
        """
        self._nova_metadata_service_auth_url = value

    
    @property
    def nova_metadata_service_endpoint(self):
        """ Get nova_metadata_service_endpoint value.

            Notes:
                Nova metadata service endpoint

                
                This attribute is named `novaMetadataServiceEndpoint` in VSD API.
                
        """
        return self._nova_metadata_service_endpoint

    @nova_metadata_service_endpoint.setter
    def nova_metadata_service_endpoint(self, value):
        """ Set nova_metadata_service_endpoint value.

            Notes:
                Nova metadata service endpoint

                
                This attribute is named `novaMetadataServiceEndpoint` in VSD API.
                
        """
        self._nova_metadata_service_endpoint = value

    
    @property
    def nova_metadata_service_password(self):
        """ Get nova_metadata_service_password value.

            Notes:
                Nova metadata service password

                
                This attribute is named `novaMetadataServicePassword` in VSD API.
                
        """
        return self._nova_metadata_service_password

    @nova_metadata_service_password.setter
    def nova_metadata_service_password(self, value):
        """ Set nova_metadata_service_password value.

            Notes:
                Nova metadata service password

                
                This attribute is named `novaMetadataServicePassword` in VSD API.
                
        """
        self._nova_metadata_service_password = value

    
    @property
    def nova_metadata_service_tenant(self):
        """ Get nova_metadata_service_tenant value.

            Notes:
                Nova metadata service tenant

                
                This attribute is named `novaMetadataServiceTenant` in VSD API.
                
        """
        return self._nova_metadata_service_tenant

    @nova_metadata_service_tenant.setter
    def nova_metadata_service_tenant(self, value):
        """ Set nova_metadata_service_tenant value.

            Notes:
                Nova metadata service tenant

                
                This attribute is named `novaMetadataServiceTenant` in VSD API.
                
        """
        self._nova_metadata_service_tenant = value

    
    @property
    def nova_metadata_service_username(self):
        """ Get nova_metadata_service_username value.

            Notes:
                Nova metadata service username

                
                This attribute is named `novaMetadataServiceUsername` in VSD API.
                
        """
        return self._nova_metadata_service_username

    @nova_metadata_service_username.setter
    def nova_metadata_service_username(self, value):
        """ Set nova_metadata_service_username value.

            Notes:
                Nova metadata service username

                
                This attribute is named `novaMetadataServiceUsername` in VSD API.
                
        """
        self._nova_metadata_service_username = value

    
    @property
    def nova_metadata_shared_secret(self):
        """ Get nova_metadata_shared_secret value.

            Notes:
                Nova metadata shared secret

                
                This attribute is named `novaMetadataSharedSecret` in VSD API.
                
        """
        return self._nova_metadata_shared_secret

    @nova_metadata_shared_secret.setter
    def nova_metadata_shared_secret(self, value):
        """ Set nova_metadata_shared_secret value.

            Notes:
                Nova metadata shared secret

                
                This attribute is named `novaMetadataSharedSecret` in VSD API.
                
        """
        self._nova_metadata_shared_secret = value

    
    @property
    def nova_region_name(self):
        """ Get nova_region_name value.

            Notes:
                Nova region name

                
                This attribute is named `novaRegionName` in VSD API.
                
        """
        return self._nova_region_name

    @nova_region_name.setter
    def nova_region_name(self, value):
        """ Set nova_region_name value.

            Notes:
                Nova region name

                
                This attribute is named `novaRegionName` in VSD API.
                
        """
        self._nova_region_name = value

    
    @property
    def primary_nuage_controller(self):
        """ Get primary_nuage_controller value.

            Notes:
                IP address of the primary Controller (VSC)

                
                This attribute is named `primaryNuageController` in VSD API.
                
        """
        return self._primary_nuage_controller

    @primary_nuage_controller.setter
    def primary_nuage_controller(self, value):
        """ Set primary_nuage_controller value.

            Notes:
                IP address of the primary Controller (VSC)

                
                This attribute is named `primaryNuageController` in VSD API.
                
        """
        self._primary_nuage_controller = value

    
    @property
    def vrs_password(self):
        """ Get vrs_password value.

            Notes:
                VRS password to be used by toolbox to communicate with VRS

                
                This attribute is named `vrsPassword` in VSD API.
                
        """
        return self._vrs_password

    @vrs_password.setter
    def vrs_password(self, value):
        """ Set vrs_password value.

            Notes:
                VRS password to be used by toolbox to communicate with VRS

                
                This attribute is named `vrsPassword` in VSD API.
                
        """
        self._vrs_password = value

    
    @property
    def vrs_user_name(self):
        """ Get vrs_user_name value.

            Notes:
                VRS user name to be used by toolbox to communicate with VRS

                
                This attribute is named `vrsUserName` in VSD API.
                
        """
        return self._vrs_user_name

    @vrs_user_name.setter
    def vrs_user_name(self, value):
        """ Set vrs_user_name value.

            Notes:
                VRS user name to be used by toolbox to communicate with VRS

                
                This attribute is named `vrsUserName` in VSD API.
                
        """
        self._vrs_user_name = value

    
    @property
    def static_route(self):
        """ Get static_route value.

            Notes:
                static route to be configured in the VRS

                
                This attribute is named `staticRoute` in VSD API.
                
        """
        return self._static_route

    @static_route.setter
    def static_route(self, value):
        """ Set static_route value.

            Notes:
                static route to be configured in the VRS

                
                This attribute is named `staticRoute` in VSD API.
                
        """
        self._static_route = value

    
    @property
    def static_route_gateway(self):
        """ Get static_route_gateway value.

            Notes:
                Gateway for the static route given above

                
                This attribute is named `staticRouteGateway` in VSD API.
                
        """
        return self._static_route_gateway

    @static_route_gateway.setter
    def static_route_gateway(self, value):
        """ Set static_route_gateway value.

            Notes:
                Gateway for the static route given above

                
                This attribute is named `staticRouteGateway` in VSD API.
                
        """
        self._static_route_gateway = value

    
    @property
    def static_route_netmask(self):
        """ Get static_route_netmask value.

            Notes:
                Nova region name

                
                This attribute is named `staticRouteNetmask` in VSD API.
                
        """
        return self._static_route_netmask

    @static_route_netmask.setter
    def static_route_netmask(self, value):
        """ Set static_route_netmask value.

            Notes:
                Nova region name

                
                This attribute is named `staticRouteNetmask` in VSD API.
                
        """
        self._static_route_netmask = value

    
    @property
    def ntp_server1(self):
        """ Get ntp_server1 value.

            Notes:
                IP of the NTP server 1

                
                This attribute is named `ntpServer1` in VSD API.
                
        """
        return self._ntp_server1

    @ntp_server1.setter
    def ntp_server1(self, value):
        """ Set ntp_server1 value.

            Notes:
                IP of the NTP server 1

                
                This attribute is named `ntpServer1` in VSD API.
                
        """
        self._ntp_server1 = value

    
    @property
    def ntp_server2(self):
        """ Get ntp_server2 value.

            Notes:
                IP of the NTP server 1

                
                This attribute is named `ntpServer2` in VSD API.
                
        """
        return self._ntp_server2

    @ntp_server2.setter
    def ntp_server2(self, value):
        """ Set ntp_server2 value.

            Notes:
                IP of the NTP server 1

                
                This attribute is named `ntpServer2` in VSD API.
                
        """
        self._ntp_server2 = value

    
    @property
    def mtu(self):
        """ Get mtu value.

            Notes:
                Maximum Transmission Unit for eth2 interface

                
        """
        return self._mtu

    @mtu.setter
    def mtu(self, value):
        """ Set mtu value.

            Notes:
                Maximum Transmission Unit for eth2 interface

                
        """
        self._mtu = value

    
    @property
    def multi_vmssupport(self):
        """ Get multi_vmssupport value.

            Notes:
                Whether Multi VM is to be used or not

                
                This attribute is named `multiVMSsupport` in VSD API.
                
        """
        return self._multi_vmssupport

    @multi_vmssupport.setter
    def multi_vmssupport(self, value):
        """ Set multi_vmssupport value.

            Notes:
                Whether Multi VM is to be used or not

                
                This attribute is named `multiVMSsupport` in VSD API.
                
        """
        self._multi_vmssupport = value

    
    @property
    def multicast_receive_interface(self):
        """ Get multicast_receive_interface value.

            Notes:
                Multicast Receive Interface

                
                This attribute is named `multicastReceiveInterface` in VSD API.
                
        """
        return self._multicast_receive_interface

    @multicast_receive_interface.setter
    def multicast_receive_interface(self, value):
        """ Set multicast_receive_interface value.

            Notes:
                Multicast Receive Interface

                
                This attribute is named `multicastReceiveInterface` in VSD API.
                
        """
        self._multicast_receive_interface = value

    
    @property
    def multicast_receive_interface_ip(self):
        """ Get multicast_receive_interface_ip value.

            Notes:
                IP address for eth3 interface

                
                This attribute is named `multicastReceiveInterfaceIP` in VSD API.
                
        """
        return self._multicast_receive_interface_ip

    @multicast_receive_interface_ip.setter
    def multicast_receive_interface_ip(self, value):
        """ Set multicast_receive_interface_ip value.

            Notes:
                IP address for eth3 interface

                
                This attribute is named `multicastReceiveInterfaceIP` in VSD API.
                
        """
        self._multicast_receive_interface_ip = value

    
    @property
    def multicast_receive_interface_netmask(self):
        """ Get multicast_receive_interface_netmask value.

            Notes:
                Multicast Interface netmask

                
                This attribute is named `multicastReceiveInterfaceNetmask` in VSD API.
                
        """
        return self._multicast_receive_interface_netmask

    @multicast_receive_interface_netmask.setter
    def multicast_receive_interface_netmask(self, value):
        """ Set multicast_receive_interface_netmask value.

            Notes:
                Multicast Interface netmask

                
                This attribute is named `multicastReceiveInterfaceNetmask` in VSD API.
                
        """
        self._multicast_receive_interface_netmask = value

    
    @property
    def multicast_receive_range(self):
        """ Get multicast_receive_range value.

            Notes:
                Allowed Range to receive the Multicast traffic from

                
                This attribute is named `multicastReceiveRange` in VSD API.
                
        """
        return self._multicast_receive_range

    @multicast_receive_range.setter
    def multicast_receive_range(self, value):
        """ Set multicast_receive_range value.

            Notes:
                Allowed Range to receive the Multicast traffic from

                
                This attribute is named `multicastReceiveRange` in VSD API.
                
        """
        self._multicast_receive_range = value

    
    @property
    def multicast_send_interface(self):
        """ Get multicast_send_interface value.

            Notes:
                Multicast Send Interface

                
                This attribute is named `multicastSendInterface` in VSD API.
                
        """
        return self._multicast_send_interface

    @multicast_send_interface.setter
    def multicast_send_interface(self, value):
        """ Set multicast_send_interface value.

            Notes:
                Multicast Send Interface

                
                This attribute is named `multicastSendInterface` in VSD API.
                
        """
        self._multicast_send_interface = value

    
    @property
    def multicast_send_interface_ip(self):
        """ Get multicast_send_interface_ip value.

            Notes:
                IP address for eth3 interface

                
                This attribute is named `multicastSendInterfaceIP` in VSD API.
                
        """
        return self._multicast_send_interface_ip

    @multicast_send_interface_ip.setter
    def multicast_send_interface_ip(self, value):
        """ Set multicast_send_interface_ip value.

            Notes:
                IP address for eth3 interface

                
                This attribute is named `multicastSendInterfaceIP` in VSD API.
                
        """
        self._multicast_send_interface_ip = value

    
    @property
    def multicast_send_interface_netmask(self):
        """ Get multicast_send_interface_netmask value.

            Notes:
                Multicast Interface netmask

                
                This attribute is named `multicastSendInterfaceNetmask` in VSD API.
                
        """
        return self._multicast_send_interface_netmask

    @multicast_send_interface_netmask.setter
    def multicast_send_interface_netmask(self, value):
        """ Set multicast_send_interface_netmask value.

            Notes:
                Multicast Interface netmask

                
                This attribute is named `multicastSendInterfaceNetmask` in VSD API.
                
        """
        self._multicast_send_interface_netmask = value

    
    @property
    def multicast_source_portgroup(self):
        """ Get multicast_source_portgroup value.

            Notes:
                Multi Cast Source Port Group Name

                
                This attribute is named `multicastSourcePortgroup` in VSD API.
                
        """
        return self._multicast_source_portgroup

    @multicast_source_portgroup.setter
    def multicast_source_portgroup(self, value):
        """ Set multicast_source_portgroup value.

            Notes:
                Multi Cast Source Port Group Name

                
                This attribute is named `multicastSourcePortgroup` in VSD API.
                
        """
        self._multicast_source_portgroup = value

    
    @property
    def customized_script_url(self):
        """ Get customized_script_url value.

            Notes:
                To provide a URL to install a custom app on VRS

                
                This attribute is named `customizedScriptURL` in VSD API.
                
        """
        return self._customized_script_url

    @customized_script_url.setter
    def customized_script_url(self, value):
        """ Set customized_script_url value.

            Notes:
                To provide a URL to install a custom app on VRS

                
                This attribute is named `customizedScriptURL` in VSD API.
                
        """
        self._customized_script_url = value

    
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

    

    