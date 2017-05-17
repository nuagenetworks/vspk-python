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


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVMsFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NUMonitoringPortsFetcher


from .fetchers import NUVPortsFetcher


from .fetchers import NUHSCsFetcher


from .fetchers import NUVSCsFetcher


from .fetchers import NUMultiNICVPortsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUVRS(NURESTObject):
    """ Represents a VRS in the VSD

        Notes:
            System Monitoring details for VRS connected to VSC or HSC
    """

    __rest_name__ = "vrs"
    __resource_name__ = "vrss"

    
    ## Constants
    
    CONST_STATUS_DOWN = "DOWN"
    
    CONST_CLUSTER_NODE_ROLE_NONE = "NONE"
    
    CONST_HYPERVISOR_CONNECTION_STATE_UP = "UP"
    
    CONST_HYPERVISOR_CONNECTION_STATE_ADMIN_DOWN = "ADMIN_DOWN"
    
    CONST_PERSONALITY_NONE = "NONE"
    
    CONST_HYPERVISOR_CONNECTION_STATE_DOWN = "DOWN"
    
    CONST_CLUSTER_NODE_ROLE_SECONDARY = "SECONDARY"
    
    CONST_PERSONALITY_VRS = "VRS"
    
    CONST_PERSONALITY_NSG = "NSG"
    
    CONST_ROLE_MASTER = "MASTER"
    
    CONST_STATUS_ADMIN_DOWN = "ADMIN_DOWN"
    
    CONST_ROLE_SLAVE = "SLAVE"
    
    CONST_PERSONALITY_HARDWARE_VTEP = "HARDWARE_VTEP"
    
    CONST_JSONRPC_CONNECTION_STATE_UP = "UP"
    
    CONST_JSONRPC_CONNECTION_STATE_ADMIN_DOWN = "ADMIN_DOWN"
    
    CONST_STATUS_UP = "UP"
    
    CONST_PERSONALITY_VRSG = "VRSG"
    
    CONST_CLUSTER_NODE_ROLE_PRIMARY = "PRIMARY"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_JSONRPC_CONNECTION_STATE_DOWN = "DOWN"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ROLE_NONE = "NONE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VRS instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vrs = NUVRS(id=u'xxxx-xxx-xxx-xxx', name=u'VRS')
                >>> vrs = NUVRS(data=my_dict)
        """

        super(NUVRS, self).__init__()

        # Read/Write Attributes
        
        self._jsonrpc_connection_state = None
        self._name = None
        self._management_ip = None
        self._parent_ids = None
        self._last_event_name = None
        self._last_event_object = None
        self._last_event_timestamp = None
        self._last_state_change = None
        self._last_updated_by = None
        self._db_synced = None
        self._address = None
        self._peak_cpuusage = None
        self._peak_memory_usage = None
        self._peer = None
        self._personality = None
        self._description = None
        self._messages = None
        self._disks = None
        self._cluster_node_role = None
        self._entity_scope = None
        self._location = None
        self._role = None
        self._uptime = None
        self._product_version = None
        self._is_resilient = None
        self._status = None
        self._multi_nic_vport_enabled = None
        self._number_of_bridge_interfaces = None
        self._number_of_host_interfaces = None
        self._number_of_virtual_machines = None
        self._current_cpuusage = None
        self._current_memory_usage = None
        self._average_cpuusage = None
        self._average_memory_usage = None
        self._external_id = None
        self._dynamic = None
        self._hypervisor_connection_state = None
        self._hypervisor_identifier = None
        self._hypervisor_name = None
        self._hypervisor_type = None
        
        self.expose_attribute(local_name="jsonrpc_connection_state", remote_name="JSONRPCConnectionState", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'UP'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="management_ip", remote_name="managementIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="parent_ids", remote_name="parentIDs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_event_name", remote_name="lastEventName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_event_object", remote_name="lastEventObject", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_event_timestamp", remote_name="lastEventTimestamp", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_state_change", remote_name="lastStateChange", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="db_synced", remote_name="dbSynced", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peak_cpuusage", remote_name="peakCPUUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peak_memory_usage", remote_name="peakMemoryUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer", remote_name="peer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=False, is_unique=False, choices=[u'HARDWARE_VTEP', u'NONE', u'NSG', u'VRS', u'VRSG'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="messages", remote_name="messages", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="disks", remote_name="disks", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cluster_node_role", remote_name="clusterNodeRole", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'PRIMARY', u'SECONDARY'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="location", remote_name="location", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="role", remote_name="role", attribute_type=str, is_required=False, is_unique=False, choices=[u'MASTER', u'NONE', u'SLAVE'])
        self.expose_attribute(local_name="uptime", remote_name="uptime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="product_version", remote_name="productVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="is_resilient", remote_name="isResilient", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'UP'])
        self.expose_attribute(local_name="multi_nic_vport_enabled", remote_name="multiNICVPortEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="number_of_bridge_interfaces", remote_name="numberOfBridgeInterfaces", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="number_of_host_interfaces", remote_name="numberOfHostInterfaces", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="number_of_virtual_machines", remote_name="numberOfVirtualMachines", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="current_cpuusage", remote_name="currentCPUUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="current_memory_usage", remote_name="currentMemoryUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="average_cpuusage", remote_name="averageCPUUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="average_memory_usage", remote_name="averageMemoryUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="dynamic", remote_name="dynamic", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="hypervisor_connection_state", remote_name="hypervisorConnectionState", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'UP'])
        self.expose_attribute(local_name="hypervisor_identifier", remote_name="hypervisorIdentifier", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="hypervisor_name", remote_name="hypervisorName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="hypervisor_type", remote_name="hypervisorType", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.monitoring_ports = NUMonitoringPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.hscs = NUHSCsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vscs = NUVSCsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.multi_nic_vports = NUMultiNICVPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def jsonrpc_connection_state(self):
        """ Get jsonrpc_connection_state value.

            Notes:
                The current JSON RPC connection status.

                
                This attribute is named `JSONRPCConnectionState` in VSD API.
                
        """
        return self._jsonrpc_connection_state

    @jsonrpc_connection_state.setter
    def jsonrpc_connection_state(self, value):
        """ Set jsonrpc_connection_state value.

            Notes:
                The current JSON RPC connection status.

                
                This attribute is named `JSONRPCConnectionState` in VSD API.
                
        """
        self._jsonrpc_connection_state = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Identifies the entity with a name.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Identifies the entity with a name.

                
        """
        self._name = value

    
    @property
    def management_ip(self):
        """ Get management_ip value.

            Notes:
                The management IP of the VRS entity

                
                This attribute is named `managementIP` in VSD API.
                
        """
        return self._management_ip

    @management_ip.setter
    def management_ip(self, value):
        """ Set management_ip value.

            Notes:
                The management IP of the VRS entity

                
                This attribute is named `managementIP` in VSD API.
                
        """
        self._management_ip = value

    
    @property
    def parent_ids(self):
        """ Get parent_ids value.

            Notes:
                Holds VRS controllers ids

                
                This attribute is named `parentIDs` in VSD API.
                
        """
        return self._parent_ids

    @parent_ids.setter
    def parent_ids(self, value):
        """ Set parent_ids value.

            Notes:
                Holds VRS controllers ids

                
                This attribute is named `parentIDs` in VSD API.
                
        """
        self._parent_ids = value

    
    @property
    def last_event_name(self):
        """ Get last_event_name value.

            Notes:
                The last event name from the hypervisor.

                
                This attribute is named `lastEventName` in VSD API.
                
        """
        return self._last_event_name

    @last_event_name.setter
    def last_event_name(self, value):
        """ Set last_event_name value.

            Notes:
                The last event name from the hypervisor.

                
                This attribute is named `lastEventName` in VSD API.
                
        """
        self._last_event_name = value

    
    @property
    def last_event_object(self):
        """ Get last_event_object value.

            Notes:
                The last event object (including metadata) from the hypervisor.

                
                This attribute is named `lastEventObject` in VSD API.
                
        """
        return self._last_event_object

    @last_event_object.setter
    def last_event_object(self, value):
        """ Set last_event_object value.

            Notes:
                The last event object (including metadata) from the hypervisor.

                
                This attribute is named `lastEventObject` in VSD API.
                
        """
        self._last_event_object = value

    
    @property
    def last_event_timestamp(self):
        """ Get last_event_timestamp value.

            Notes:
                The last event timestamp from the hypervisor.

                
                This attribute is named `lastEventTimestamp` in VSD API.
                
        """
        return self._last_event_timestamp

    @last_event_timestamp.setter
    def last_event_timestamp(self, value):
        """ Set last_event_timestamp value.

            Notes:
                The last event timestamp from the hypervisor.

                
                This attribute is named `lastEventTimestamp` in VSD API.
                
        """
        self._last_event_timestamp = value

    
    @property
    def last_state_change(self):
        """ Get last_state_change value.

            Notes:
                Last state change timestamp (in millis).

                
                This attribute is named `lastStateChange` in VSD API.
                
        """
        return self._last_state_change

    @last_state_change.setter
    def last_state_change(self, value):
        """ Set last_state_change value.

            Notes:
                Last state change timestamp (in millis).

                
                This attribute is named `lastStateChange` in VSD API.
                
        """
        self._last_state_change = value

    
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
    def db_synced(self):
        """ Get db_synced value.

            Notes:
                Flag to indicate if the ovs database is synced between the NSG pair part of a redundant group

                
                This attribute is named `dbSynced` in VSD API.
                
        """
        return self._db_synced

    @db_synced.setter
    def db_synced(self, value):
        """ Set db_synced value.

            Notes:
                Flag to indicate if the ovs database is synced between the NSG pair part of a redundant group

                
                This attribute is named `dbSynced` in VSD API.
                
        """
        self._db_synced = value

    
    @property
    def address(self):
        """ Get address value.

            Notes:
                The IP of the VRS entity

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                The IP of the VRS entity

                
        """
        self._address = value

    
    @property
    def peak_cpuusage(self):
        """ Get peak_cpuusage value.

            Notes:
                Peek CPU usage percentage.

                
                This attribute is named `peakCPUUsage` in VSD API.
                
        """
        return self._peak_cpuusage

    @peak_cpuusage.setter
    def peak_cpuusage(self, value):
        """ Set peak_cpuusage value.

            Notes:
                Peek CPU usage percentage.

                
                This attribute is named `peakCPUUsage` in VSD API.
                
        """
        self._peak_cpuusage = value

    
    @property
    def peak_memory_usage(self):
        """ Get peak_memory_usage value.

            Notes:
                Peek memory usage percentage.

                
                This attribute is named `peakMemoryUsage` in VSD API.
                
        """
        return self._peak_memory_usage

    @peak_memory_usage.setter
    def peak_memory_usage(self, value):
        """ Set peak_memory_usage value.

            Notes:
                Peek memory usage percentage.

                
                This attribute is named `peakMemoryUsage` in VSD API.
                
        """
        self._peak_memory_usage = value

    
    @property
    def peer(self):
        """ Get peer value.

            Notes:
                The redundant peer id for the current VRS.

                
        """
        return self._peer

    @peer.setter
    def peer(self, value):
        """ Set peer value.

            Notes:
                The redundant peer id for the current VRS.

                
        """
        self._peer = value

    
    @property
    def personality(self):
        """ Get personality value.

            Notes:
                VRS personality.

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                VRS personality.

                
        """
        self._personality = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the entity.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the entity.

                
        """
        self._description = value

    
    @property
    def messages(self):
        """ Get messages value.

            Notes:
                An array of degraded messages.

                
        """
        return self._messages

    @messages.setter
    def messages(self, value):
        """ Set messages value.

            Notes:
                An array of degraded messages.

                
        """
        self._messages = value

    
    @property
    def disks(self):
        """ Get disks value.

            Notes:
                Set of disk usage details.

                
        """
        return self._disks

    @disks.setter
    def disks(self, value):
        """ Set disks value.

            Notes:
                Set of disk usage details.

                
        """
        self._disks = value

    
    @property
    def cluster_node_role(self):
        """ Get cluster_node_role value.

            Notes:
                Indicate that the controller associated is primary, secondary or unknown.

                
                This attribute is named `clusterNodeRole` in VSD API.
                
        """
        return self._cluster_node_role

    @cluster_node_role.setter
    def cluster_node_role(self, value):
        """ Set cluster_node_role value.

            Notes:
                Indicate that the controller associated is primary, secondary or unknown.

                
                This attribute is named `clusterNodeRole` in VSD API.
                
        """
        self._cluster_node_role = value

    
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
    def location(self):
        """ Get location value.

            Notes:
                Identifies the entity to be associated with a location.

                
        """
        return self._location

    @location.setter
    def location(self, value):
        """ Set location value.

            Notes:
                Identifies the entity to be associated with a location.

                
        """
        self._location = value

    
    @property
    def role(self):
        """ Get role value.

            Notes:
                Flag to indicate that VRS-G redundancy state (active/standby/standalone).  Only applicable for gateways.

                
        """
        return self._role

    @role.setter
    def role(self, value):
        """ Set role value.

            Notes:
                Flag to indicate that VRS-G redundancy state (active/standby/standalone).  Only applicable for gateways.

                
        """
        self._role = value

    
    @property
    def uptime(self):
        """ Get uptime value.

            Notes:
                How long the VRS was up.

                
        """
        return self._uptime

    @uptime.setter
    def uptime(self, value):
        """ Set uptime value.

            Notes:
                How long the VRS was up.

                
        """
        self._uptime = value

    
    @property
    def product_version(self):
        """ Get product_version value.

            Notes:
                Product version supported by this entity.

                
                This attribute is named `productVersion` in VSD API.
                
        """
        return self._product_version

    @product_version.setter
    def product_version(self, value):
        """ Set product_version value.

            Notes:
                Product version supported by this entity.

                
                This attribute is named `productVersion` in VSD API.
                
        """
        self._product_version = value

    
    @property
    def is_resilient(self):
        """ Get is_resilient value.

            Notes:
                Flag to indicate that the VRS is part of a redundant group.

                
                This attribute is named `isResilient` in VSD API.
                
        """
        return self._is_resilient

    @is_resilient.setter
    def is_resilient(self, value):
        """ Set is_resilient value.

            Notes:
                Flag to indicate that the VRS is part of a redundant group.

                
                This attribute is named `isResilient` in VSD API.
                
        """
        self._is_resilient = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                Computed status of the entity.

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                Computed status of the entity.

                
        """
        self._status = value

    
    @property
    def multi_nic_vport_enabled(self):
        """ Get multi_nic_vport_enabled value.

            Notes:
                VRS is in Multi-NIC VPORT Mode

                
                This attribute is named `multiNICVPortEnabled` in VSD API.
                
        """
        return self._multi_nic_vport_enabled

    @multi_nic_vport_enabled.setter
    def multi_nic_vport_enabled(self, value):
        """ Set multi_nic_vport_enabled value.

            Notes:
                VRS is in Multi-NIC VPORT Mode

                
                This attribute is named `multiNICVPortEnabled` in VSD API.
                
        """
        self._multi_nic_vport_enabled = value

    
    @property
    def number_of_bridge_interfaces(self):
        """ Get number_of_bridge_interfaces value.

            Notes:
                Number of bridge interfaces defined in this VRS.

                
                This attribute is named `numberOfBridgeInterfaces` in VSD API.
                
        """
        return self._number_of_bridge_interfaces

    @number_of_bridge_interfaces.setter
    def number_of_bridge_interfaces(self, value):
        """ Set number_of_bridge_interfaces value.

            Notes:
                Number of bridge interfaces defined in this VRS.

                
                This attribute is named `numberOfBridgeInterfaces` in VSD API.
                
        """
        self._number_of_bridge_interfaces = value

    
    @property
    def number_of_host_interfaces(self):
        """ Get number_of_host_interfaces value.

            Notes:
                Number of host interfaces defined in this VRS.

                
                This attribute is named `numberOfHostInterfaces` in VSD API.
                
        """
        return self._number_of_host_interfaces

    @number_of_host_interfaces.setter
    def number_of_host_interfaces(self, value):
        """ Set number_of_host_interfaces value.

            Notes:
                Number of host interfaces defined in this VRS.

                
                This attribute is named `numberOfHostInterfaces` in VSD API.
                
        """
        self._number_of_host_interfaces = value

    
    @property
    def number_of_virtual_machines(self):
        """ Get number_of_virtual_machines value.

            Notes:
                Number of VMs defined in this VRS.

                
                This attribute is named `numberOfVirtualMachines` in VSD API.
                
        """
        return self._number_of_virtual_machines

    @number_of_virtual_machines.setter
    def number_of_virtual_machines(self, value):
        """ Set number_of_virtual_machines value.

            Notes:
                Number of VMs defined in this VRS.

                
                This attribute is named `numberOfVirtualMachines` in VSD API.
                
        """
        self._number_of_virtual_machines = value

    
    @property
    def current_cpuusage(self):
        """ Get current_cpuusage value.

            Notes:
                Current CPU usage percentage.

                
                This attribute is named `currentCPUUsage` in VSD API.
                
        """
        return self._current_cpuusage

    @current_cpuusage.setter
    def current_cpuusage(self, value):
        """ Set current_cpuusage value.

            Notes:
                Current CPU usage percentage.

                
                This attribute is named `currentCPUUsage` in VSD API.
                
        """
        self._current_cpuusage = value

    
    @property
    def current_memory_usage(self):
        """ Get current_memory_usage value.

            Notes:
                Current memory usage percentage.

                
                This attribute is named `currentMemoryUsage` in VSD API.
                
        """
        return self._current_memory_usage

    @current_memory_usage.setter
    def current_memory_usage(self, value):
        """ Set current_memory_usage value.

            Notes:
                Current memory usage percentage.

                
                This attribute is named `currentMemoryUsage` in VSD API.
                
        """
        self._current_memory_usage = value

    
    @property
    def average_cpuusage(self):
        """ Get average_cpuusage value.

            Notes:
                Average CPU usage percentage.

                
                This attribute is named `averageCPUUsage` in VSD API.
                
        """
        return self._average_cpuusage

    @average_cpuusage.setter
    def average_cpuusage(self, value):
        """ Set average_cpuusage value.

            Notes:
                Average CPU usage percentage.

                
                This attribute is named `averageCPUUsage` in VSD API.
                
        """
        self._average_cpuusage = value

    
    @property
    def average_memory_usage(self):
        """ Get average_memory_usage value.

            Notes:
                Average memory usage percentage.

                
                This attribute is named `averageMemoryUsage` in VSD API.
                
        """
        return self._average_memory_usage

    @average_memory_usage.setter
    def average_memory_usage(self, value):
        """ Set average_memory_usage value.

            Notes:
                Average memory usage percentage.

                
                This attribute is named `averageMemoryUsage` in VSD API.
                
        """
        self._average_memory_usage = value

    
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
    def dynamic(self):
        """ Get dynamic value.

            Notes:
                Flag to indicate it is dynamically configured or not.

                
        """
        return self._dynamic

    @dynamic.setter
    def dynamic(self, value):
        """ Set dynamic value.

            Notes:
                Flag to indicate it is dynamically configured or not.

                
        """
        self._dynamic = value

    
    @property
    def hypervisor_connection_state(self):
        """ Get hypervisor_connection_state value.

            Notes:
                The VRS connection state with the hypervisor.

                
                This attribute is named `hypervisorConnectionState` in VSD API.
                
        """
        return self._hypervisor_connection_state

    @hypervisor_connection_state.setter
    def hypervisor_connection_state(self, value):
        """ Set hypervisor_connection_state value.

            Notes:
                The VRS connection state with the hypervisor.

                
                This attribute is named `hypervisorConnectionState` in VSD API.
                
        """
        self._hypervisor_connection_state = value

    
    @property
    def hypervisor_identifier(self):
        """ Get hypervisor_identifier value.

            Notes:
                The hypervisor IP (or name) associated with the VRS.

                
                This attribute is named `hypervisorIdentifier` in VSD API.
                
        """
        return self._hypervisor_identifier

    @hypervisor_identifier.setter
    def hypervisor_identifier(self, value):
        """ Set hypervisor_identifier value.

            Notes:
                The hypervisor IP (or name) associated with the VRS.

                
                This attribute is named `hypervisorIdentifier` in VSD API.
                
        """
        self._hypervisor_identifier = value

    
    @property
    def hypervisor_name(self):
        """ Get hypervisor_name value.

            Notes:
                The hypervisor name associated with the VRS.

                
                This attribute is named `hypervisorName` in VSD API.
                
        """
        return self._hypervisor_name

    @hypervisor_name.setter
    def hypervisor_name(self, value):
        """ Set hypervisor_name value.

            Notes:
                The hypervisor name associated with the VRS.

                
                This attribute is named `hypervisorName` in VSD API.
                
        """
        self._hypervisor_name = value

    
    @property
    def hypervisor_type(self):
        """ Get hypervisor_type value.

            Notes:
                The hypervisor type associated with the VRS.

                
                This attribute is named `hypervisorType` in VSD API.
                
        """
        return self._hypervisor_type

    @hypervisor_type.setter
    def hypervisor_type(self, value):
        """ Set hypervisor_type value.

            Notes:
                The hypervisor type associated with the VRS.

                
                This attribute is named `hypervisorType` in VSD API.
                
        """
        self._hypervisor_type = value

    

    