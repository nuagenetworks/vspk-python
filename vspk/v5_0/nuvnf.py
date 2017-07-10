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



from .fetchers import NUVNFInterfacesFetcher


from .fetchers import NUVNFMetadatasFetcher


from .fetchers import NUJobsFetcher

from bambou import NURESTObject


class NUVNF(NURESTObject):
    """ Represents a VNF in the VSD

        Notes:
            Represent a VNF instance
    """

    __rest_name__ = "vnf"
    __resource_name__ = "vnfs"

    
    ## Constants
    
    CONST_STATUS_SHUTOFF = "SHUTOFF"
    
    CONST_STATUS_IDLE = "IDLE"
    
    CONST_TASK_STATE_NONE = "NONE"
    
    CONST_STATUS_SHUTDOWN = "SHUTDOWN"
    
    CONST_STATUS_PAUSED = "PAUSED"
    
    CONST_STATUS_PMSUSPENDED = "PMSUSPENDED"
    
    CONST_ALLOWED_ACTIONS_STOP = "STOP"
    
    CONST_TASK_STATE_STARTING = "STARTING"
    
    CONST_STATUS_LAST = "LAST"
    
    CONST_STATUS_CRASHED = "CRASHED"
    
    CONST_STATUS_RUNNING = "RUNNING"
    
    CONST_ALLOWED_ACTIONS_UNDEPLOY = "UNDEPLOY"
    
    CONST_STATUS_INIT = "INIT"
    
    CONST_STATUS_DYING = "DYING"
    
    CONST_ALLOWED_ACTIONS_DEPLOY = "DEPLOY"
    
    CONST_TASK_STATE_STOPPING = "STOPPING"
    
    CONST_STATUS_BLOCKED = "BLOCKED"
    
    CONST_TASK_STATE_UNDEPLOYING = "UNDEPLOYING"
    
    CONST_TASK_STATE_DEPLOYING = "DEPLOYING"
    
    CONST_ALLOWED_ACTIONS_START = "START"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VNF instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vnf = NUVNF(id=u'xxxx-xxx-xxx-xxx', name=u'VNF')
                >>> vnf = NUVNF(data=my_dict)
        """

        super(NUVNF, self).__init__()

        # Read/Write Attributes
        
        self._vnf_descriptor_id = None
        self._vnf_descriptor_name = None
        self._cpu_count = None
        self._nsg_name = None
        self._nsg_system_id = None
        self._ns_gateway_id = None
        self._name = None
        self._task_state = None
        self._last_known_error = None
        self._memory_mb = None
        self._vendor = None
        self._description = None
        self._metadata_id = None
        self._allowed_actions = None
        self._enterprise_id = None
        self._status = None
        self._storage_gb = None
        
        self.expose_attribute(local_name="vnf_descriptor_id", remote_name="VNFDescriptorID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="vnf_descriptor_name", remote_name="VNFDescriptorName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cpu_count", remote_name="CPUCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_name", remote_name="NSGName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_system_id", remote_name="NSGSystemID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ns_gateway_id", remote_name="NSGatewayID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="task_state", remote_name="taskState", attribute_type=str, is_required=False, is_unique=False, choices=[u'DEPLOYING', u'NONE', u'STARTING', u'STOPPING', u'UNDEPLOYING'])
        self.expose_attribute(local_name="last_known_error", remote_name="lastKnownError", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="memory_mb", remote_name="memoryMB", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vendor", remote_name="vendor", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_id", remote_name="metadataID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allowed_actions", remote_name="allowedActions", attribute_type=str, is_required=False, is_unique=False, choices=[u'DEPLOY', u'START', u'STOP', u'UNDEPLOY'])
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'BLOCKED', u'CRASHED', u'DYING', u'IDLE', u'INIT', u'LAST', u'PAUSED', u'PMSUSPENDED', u'RUNNING', u'SHUTDOWN', u'SHUTOFF'])
        self.expose_attribute(local_name="storage_gb", remote_name="storageGB", attribute_type=int, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.vnf_interfaces = NUVNFInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vnf_metadatas = NUVNFMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vnf_descriptor_id(self):
        """ Get vnf_descriptor_id value.

            Notes:
                The ID of VNF Descriptor from which VNF to be created.

                
                This attribute is named `VNFDescriptorID` in VSD API.
                
        """
        return self._vnf_descriptor_id

    @vnf_descriptor_id.setter
    def vnf_descriptor_id(self, value):
        """ Set vnf_descriptor_id value.

            Notes:
                The ID of VNF Descriptor from which VNF to be created.

                
                This attribute is named `VNFDescriptorID` in VSD API.
                
        """
        self._vnf_descriptor_id = value

    
    @property
    def vnf_descriptor_name(self):
        """ Get vnf_descriptor_name value.

            Notes:
                The Name of VNF Descriptor from which this VNF instance is created.

                
                This attribute is named `VNFDescriptorName` in VSD API.
                
        """
        return self._vnf_descriptor_name

    @vnf_descriptor_name.setter
    def vnf_descriptor_name(self, value):
        """ Set vnf_descriptor_name value.

            Notes:
                The Name of VNF Descriptor from which this VNF instance is created.

                
                This attribute is named `VNFDescriptorName` in VSD API.
                
        """
        self._vnf_descriptor_name = value

    
    @property
    def cpu_count(self):
        """ Get cpu_count value.

            Notes:
                Number of CPUs to be allocated for this VNF instance

                
                This attribute is named `CPUCount` in VSD API.
                
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, value):
        """ Set cpu_count value.

            Notes:
                Number of CPUs to be allocated for this VNF instance

                
                This attribute is named `CPUCount` in VSD API.
                
        """
        self._cpu_count = value

    
    @property
    def nsg_name(self):
        """ Get nsg_name value.

            Notes:
                The NSG name where VNF is deployed

                
                This attribute is named `NSGName` in VSD API.
                
        """
        return self._nsg_name

    @nsg_name.setter
    def nsg_name(self, value):
        """ Set nsg_name value.

            Notes:
                The NSG name where VNF is deployed

                
                This attribute is named `NSGName` in VSD API.
                
        """
        self._nsg_name = value

    
    @property
    def nsg_system_id(self):
        """ Get nsg_system_id value.

            Notes:
                The NSG system id where VNF is deployed

                
                This attribute is named `NSGSystemID` in VSD API.
                
        """
        return self._nsg_system_id

    @nsg_system_id.setter
    def nsg_system_id(self, value):
        """ Set nsg_system_id value.

            Notes:
                The NSG system id where VNF is deployed

                
                This attribute is named `NSGSystemID` in VSD API.
                
        """
        self._nsg_system_id = value

    
    @property
    def ns_gateway_id(self):
        """ Get ns_gateway_id value.

            Notes:
                The NSG instance id where VNF is deployed

                
                This attribute is named `NSGatewayID` in VSD API.
                
        """
        return self._ns_gateway_id

    @ns_gateway_id.setter
    def ns_gateway_id(self, value):
        """ Set ns_gateway_id value.

            Notes:
                The NSG instance id where VNF is deployed

                
                This attribute is named `NSGatewayID` in VSD API.
                
        """
        self._ns_gateway_id = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the VNF

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the VNF

                
        """
        self._name = value

    
    @property
    def task_state(self):
        """ Get task_state value.

            Notes:
                Current state of operation/task

                
                This attribute is named `taskState` in VSD API.
                
        """
        return self._task_state

    @task_state.setter
    def task_state(self, value):
        """ Set task_state value.

            Notes:
                Current state of operation/task

                
                This attribute is named `taskState` in VSD API.
                
        """
        self._task_state = value

    
    @property
    def last_known_error(self):
        """ Get last_known_error value.

            Notes:
                Last error reported

                
                This attribute is named `lastKnownError` in VSD API.
                
        """
        return self._last_known_error

    @last_known_error.setter
    def last_known_error(self, value):
        """ Set last_known_error value.

            Notes:
                Last error reported

                
                This attribute is named `lastKnownError` in VSD API.
                
        """
        self._last_known_error = value

    
    @property
    def memory_mb(self):
        """ Get memory_mb value.

            Notes:
                Memory (in MB) to be allocated for this VNF instance.

                
                This attribute is named `memoryMB` in VSD API.
                
        """
        return self._memory_mb

    @memory_mb.setter
    def memory_mb(self, value):
        """ Set memory_mb value.

            Notes:
                Memory (in MB) to be allocated for this VNF instance.

                
                This attribute is named `memoryMB` in VSD API.
                
        """
        self._memory_mb = value

    
    @property
    def vendor(self):
        """ Get vendor value.

            Notes:
                The vendor for VNF

                
        """
        return self._vendor

    @vendor.setter
    def vendor(self, value):
        """ Set vendor value.

            Notes:
                The vendor for VNF

                
        """
        self._vendor = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the VNF Instance

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the VNF Instance

                
        """
        self._description = value

    
    @property
    def metadata_id(self):
        """ Get metadata_id value.

            Notes:
                Id of referenced metadata object

                
                This attribute is named `metadataID` in VSD API.
                
        """
        return self._metadata_id

    @metadata_id.setter
    def metadata_id(self, value):
        """ Set metadata_id value.

            Notes:
                Id of referenced metadata object

                
                This attribute is named `metadataID` in VSD API.
                
        """
        self._metadata_id = value

    
    @property
    def allowed_actions(self):
        """ Get allowed_actions value.

            Notes:
                Action allowed to  performed on VNF based on current status and taskState

                
                This attribute is named `allowedActions` in VSD API.
                
        """
        return self._allowed_actions

    @allowed_actions.setter
    def allowed_actions(self, value):
        """ Set allowed_actions value.

            Notes:
                Action allowed to  performed on VNF based on current status and taskState

                
                This attribute is named `allowedActions` in VSD API.
                
        """
        self._allowed_actions = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                ID of the enterprise that this VNF belongs to

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                ID of the enterprise that this VNF belongs to

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                State/Status of the VNF

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                State/Status of the VNF

                
        """
        self._status = value

    
    @property
    def storage_gb(self):
        """ Get storage_gb value.

            Notes:
                Disk storage (in GB) to be allocated for deployed VNF instance

                
                This attribute is named `storageGB` in VSD API.
                
        """
        return self._storage_gb

    @storage_gb.setter
    def storage_gb(self, value):
        """ Set storage_gb value.

            Notes:
                Disk storage (in GB) to be allocated for deployed VNF instance

                
                This attribute is named `storageGB` in VSD API.
                
        """
        self._storage_gb = value

    

    