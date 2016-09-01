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


from bambou import NURESTObject


class NUVRSMetrics(NURESTObject):
    """ Represents a VRSMetrics in the VSD

        Notes:
            None
    """

    __rest_name__ = "vrsmetrics"
    __resource_name__ = "vrsmetrics"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VRSMetrics instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vrsmetrics = NUVRSMetrics(id=u'xxxx-xxx-xxx-xxx', name=u'VRSMetrics')
                >>> vrsmetrics = NUVRSMetrics(data=my_dict)
        """

        super(NUVRSMetrics, self).__init__()

        # Read/Write Attributes
        
        self._al_ubr0_status = None
        self._cpu_utilization = None
        self._vrs_process = None
        self._vrsvsc_status = None
        self._last_updated_by = None
        self._re_deploy = None
        self._receiving_metrics = None
        self._memory_utilization = None
        self._jesxmon_process = None
        self._agent_name = None
        self._entity_scope = None
        self._associated_vcenter_hypervisor_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="al_ubr0_status", remote_name="ALUbr0Status", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cpu_utilization", remote_name="CPUUtilization", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_process", remote_name="VRSProcess", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrsvsc_status", remote_name="VRSVSCStatus", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="re_deploy", remote_name="reDeploy", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="receiving_metrics", remote_name="receivingMetrics", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="memory_utilization", remote_name="memoryUtilization", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="jesxmon_process", remote_name="jesxmonProcess", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="agent_name", remote_name="agentName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_vcenter_hypervisor_id", remote_name="associatedVCenterHypervisorID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def al_ubr0_status(self):
        """ Get al_ubr0_status value.

            Notes:
                alubr0 status

                
                This attribute is named `ALUbr0Status` in VSD API.
                
        """
        return self._al_ubr0_status

    @al_ubr0_status.setter
    def al_ubr0_status(self, value):
        """ Set al_ubr0_status value.

            Notes:
                alubr0 status

                
                This attribute is named `ALUbr0Status` in VSD API.
                
        """
        self._al_ubr0_status = value

    
    @property
    def cpu_utilization(self):
        """ Get cpu_utilization value.

            Notes:
                cpu utilization

                
                This attribute is named `CPUUtilization` in VSD API.
                
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, value):
        """ Set cpu_utilization value.

            Notes:
                cpu utilization

                
                This attribute is named `CPUUtilization` in VSD API.
                
        """
        self._cpu_utilization = value

    
    @property
    def vrs_process(self):
        """ Get vrs_process value.

            Notes:
                vrs vsc process status

                
                This attribute is named `VRSProcess` in VSD API.
                
        """
        return self._vrs_process

    @vrs_process.setter
    def vrs_process(self, value):
        """ Set vrs_process value.

            Notes:
                vrs vsc process status

                
                This attribute is named `VRSProcess` in VSD API.
                
        """
        self._vrs_process = value

    
    @property
    def vrsvsc_status(self):
        """ Get vrsvsc_status value.

            Notes:
                vrs vrs connection status

                
                This attribute is named `VRSVSCStatus` in VSD API.
                
        """
        return self._vrsvsc_status

    @vrsvsc_status.setter
    def vrsvsc_status(self, value):
        """ Set vrsvsc_status value.

            Notes:
                vrs vrs connection status

                
                This attribute is named `VRSVSCStatus` in VSD API.
                
        """
        self._vrsvsc_status = value

    
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
    def re_deploy(self):
        """ Get re_deploy value.

            Notes:
                re-Deploy

                
                This attribute is named `reDeploy` in VSD API.
                
        """
        return self._re_deploy

    @re_deploy.setter
    def re_deploy(self, value):
        """ Set re_deploy value.

            Notes:
                re-Deploy

                
                This attribute is named `reDeploy` in VSD API.
                
        """
        self._re_deploy = value

    
    @property
    def receiving_metrics(self):
        """ Get receiving_metrics value.

            Notes:
                Is the VRS VM Sending Metrics to the hypervisor on VCIN

                
                This attribute is named `receivingMetrics` in VSD API.
                
        """
        return self._receiving_metrics

    @receiving_metrics.setter
    def receiving_metrics(self, value):
        """ Set receiving_metrics value.

            Notes:
                Is the VRS VM Sending Metrics to the hypervisor on VCIN

                
                This attribute is named `receivingMetrics` in VSD API.
                
        """
        self._receiving_metrics = value

    
    @property
    def memory_utilization(self):
        """ Get memory_utilization value.

            Notes:
                Memory Utilization

                
                This attribute is named `memoryUtilization` in VSD API.
                
        """
        return self._memory_utilization

    @memory_utilization.setter
    def memory_utilization(self, value):
        """ Set memory_utilization value.

            Notes:
                Memory Utilization

                
                This attribute is named `memoryUtilization` in VSD API.
                
        """
        self._memory_utilization = value

    
    @property
    def jesxmon_process(self):
        """ Get jesxmon_process value.

            Notes:
                jesxmon process status

                
                This attribute is named `jesxmonProcess` in VSD API.
                
        """
        return self._jesxmon_process

    @jesxmon_process.setter
    def jesxmon_process(self, value):
        """ Set jesxmon_process value.

            Notes:
                jesxmon process status

                
                This attribute is named `jesxmonProcess` in VSD API.
                
        """
        self._jesxmon_process = value

    
    @property
    def agent_name(self):
        """ Get agent_name value.

            Notes:
                VRS Agent Name

                
                This attribute is named `agentName` in VSD API.
                
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        """ Set agent_name value.

            Notes:
                VRS Agent Name

                
                This attribute is named `agentName` in VSD API.
                
        """
        self._agent_name = value

    
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
    def associated_vcenter_hypervisor_id(self):
        """ Get associated_vcenter_hypervisor_id value.

            Notes:
                None

                
                This attribute is named `associatedVCenterHypervisorID` in VSD API.
                
        """
        return self._associated_vcenter_hypervisor_id

    @associated_vcenter_hypervisor_id.setter
    def associated_vcenter_hypervisor_id(self, value):
        """ Set associated_vcenter_hypervisor_id value.

            Notes:
                None

                
                This attribute is named `associatedVCenterHypervisorID` in VSD API.
                
        """
        self._associated_vcenter_hypervisor_id = value

    
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

    

    