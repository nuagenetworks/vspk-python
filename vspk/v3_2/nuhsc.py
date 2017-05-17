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


from .fetchers import NUBGPPeersFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NUMonitoringPortsFetcher


from .fetchers import NUVRSsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUHSC(NURESTObject):
    """ Represents a HSC in the VSD

        Notes:
            System Monitoring details for hardware service controllers.
    """

    __rest_name__ = "hsc"
    __resource_name__ = "hscs"

    
    ## Constants
    
    CONST_TYPE_VSG = "VSG"
    
    CONST_STATUS_DOWN = "DOWN"
    
    CONST_TYPE_VSA = "VSA"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_TYPE_NONE = "NONE"
    
    CONST_TYPE_DC7X50 = "DC7X50"
    
    CONST_STATUS_UP = "UP"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_STATUS_ADMIN_DOWN = "ADMIN_DOWN"
    
    

    def __init__(self, **kwargs):
        """ Initializes a HSC instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> hsc = NUHSC(id=u'xxxx-xxx-xxx-xxx', name=u'HSC')
                >>> hsc = NUHSC(data=my_dict)
        """

        super(NUHSC, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._management_ip = None
        self._last_state_change = None
        self._last_updated_by = None
        self._address = None
        self._peak_cpuusage = None
        self._peak_memory_usage = None
        self._description = None
        self._messages = None
        self._disks = None
        self._already_marked_for_unavailable = None
        self._unavailable_timestamp = None
        self._entity_scope = None
        self._location = None
        self._model = None
        self._product_version = None
        self._vsds = None
        self._status = None
        self._current_cpuusage = None
        self._current_memory_usage = None
        self._average_cpuusage = None
        self._average_memory_usage = None
        self._external_id = None
        self._type = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="management_ip", remote_name="managementIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_state_change", remote_name="lastStateChange", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peak_cpuusage", remote_name="peakCPUUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peak_memory_usage", remote_name="peakMemoryUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="messages", remote_name="messages", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="disks", remote_name="disks", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="already_marked_for_unavailable", remote_name="alreadyMarkedForUnavailable", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="unavailable_timestamp", remote_name="unavailableTimestamp", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="location", remote_name="location", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="model", remote_name="model", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="product_version", remote_name="productVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vsds", remote_name="vsds", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'UP'])
        self.expose_attribute(local_name="current_cpuusage", remote_name="currentCPUUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="current_memory_usage", remote_name="currentMemoryUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="average_cpuusage", remote_name="averageCPUUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="average_memory_usage", remote_name="averageMemoryUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=False, is_unique=False, choices=[u'DC7X50', u'NONE', u'VSA', u'VSG'])
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bgp_peers = NUBGPPeersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.monitoring_ports = NUMonitoringPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vrss = NUVRSsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
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
                The management IP of the VSC/HSC entity

                
                This attribute is named `managementIP` in VSD API.
                
        """
        return self._management_ip

    @management_ip.setter
    def management_ip(self, value):
        """ Set management_ip value.

            Notes:
                The management IP of the VSC/HSC entity

                
                This attribute is named `managementIP` in VSD API.
                
        """
        self._management_ip = value

    
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
    def already_marked_for_unavailable(self):
        """ Get already_marked_for_unavailable value.

            Notes:
                Flag to indicate that it is already marked a unavailable.

                
                This attribute is named `alreadyMarkedForUnavailable` in VSD API.
                
        """
        return self._already_marked_for_unavailable

    @already_marked_for_unavailable.setter
    def already_marked_for_unavailable(self, value):
        """ Set already_marked_for_unavailable value.

            Notes:
                Flag to indicate that it is already marked a unavailable.

                
                This attribute is named `alreadyMarkedForUnavailable` in VSD API.
                
        """
        self._already_marked_for_unavailable = value

    
    @property
    def unavailable_timestamp(self):
        """ Get unavailable_timestamp value.

            Notes:
                The duration the controller is unavailable (in millis).

                
                This attribute is named `unavailableTimestamp` in VSD API.
                
        """
        return self._unavailable_timestamp

    @unavailable_timestamp.setter
    def unavailable_timestamp(self, value):
        """ Set unavailable_timestamp value.

            Notes:
                The duration the controller is unavailable (in millis).

                
                This attribute is named `unavailableTimestamp` in VSD API.
                
        """
        self._unavailable_timestamp = value

    
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
    def model(self):
        """ Get model value.

            Notes:
                The model of the hardware service controller

                
        """
        return self._model

    @model.setter
    def model(self, value):
        """ Set model value.

            Notes:
                The model of the hardware service controller

                
        """
        self._model = value

    
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
    def vsds(self):
        """ Get vsds value.

            Notes:
                A collection of VSD id(s) which are identified by this controller.

                
        """
        return self._vsds

    @vsds.setter
    def vsds(self, value):
        """ Set vsds value.

            Notes:
                A collection of VSD id(s) which are identified by this controller.

                
        """
        self._vsds = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                Computed status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                Computed status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .

                
        """
        self._status = value

    
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
    def type(self):
        """ Get type value.

            Notes:
                The type of the hardware service controller.

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                The type of the hardware service controller.

                
        """
        self._type = value

    

    