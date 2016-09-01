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


class NUVRSRedeploymentpolicy(NURESTObject):
    """ Represents a VRSRedeploymentpolicy in the VSD

        Notes:
            None
    """

    __rest_name__ = "vrsredeploymentpolicy"
    __resource_name__ = "vrsredeploymentpolicies"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VRSRedeploymentpolicy instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vrsredeploymentpolicy = NUVRSRedeploymentpolicy(id=u'xxxx-xxx-xxx-xxx', name=u'VRSRedeploymentpolicy')
                >>> vrsredeploymentpolicy = NUVRSRedeploymentpolicy(data=my_dict)
        """

        super(NUVRSRedeploymentpolicy, self).__init__()

        # Read/Write Attributes
        
        self._al_ubr0_status_redeployment_enabled = None
        self._cpu_utilization_redeployment_enabled = None
        self._cpu_utilization_threshold = None
        self._vrs_corrective_action_delay = None
        self._vrs_process_redeployment_enabled = None
        self._vrsvsc_status_redeployment_enabled = None
        self._last_updated_by = None
        self._redeployment_delay = None
        self._memory_utilization_redeployment_enabled = None
        self._memory_utilization_threshold = None
        self._deployment_count_threshold = None
        self._jesxmon_process_redeployment_enabled = None
        self._entity_scope = None
        self._external_id = None
        
        self.expose_attribute(local_name="al_ubr0_status_redeployment_enabled", remote_name="ALUbr0StatusRedeploymentEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cpu_utilization_redeployment_enabled", remote_name="CPUUtilizationRedeploymentEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cpu_utilization_threshold", remote_name="CPUUtilizationThreshold", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_corrective_action_delay", remote_name="VRSCorrectiveActionDelay", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_process_redeployment_enabled", remote_name="VRSProcessRedeploymentEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrsvsc_status_redeployment_enabled", remote_name="VRSVSCStatusRedeploymentEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redeployment_delay", remote_name="redeploymentDelay", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="memory_utilization_redeployment_enabled", remote_name="memoryUtilizationRedeploymentEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="memory_utilization_threshold", remote_name="memoryUtilizationThreshold", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="deployment_count_threshold", remote_name="deploymentCountThreshold", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="jesxmon_process_redeployment_enabled", remote_name="jesxmonProcessRedeploymentEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def al_ubr0_status_redeployment_enabled(self):
        """ Get al_ubr0_status_redeployment_enabled value.

            Notes:
                ALU br0 Status Redeployment Enabled

                
                This attribute is named `ALUbr0StatusRedeploymentEnabled` in VSD API.
                
        """
        return self._al_ubr0_status_redeployment_enabled

    @al_ubr0_status_redeployment_enabled.setter
    def al_ubr0_status_redeployment_enabled(self, value):
        """ Set al_ubr0_status_redeployment_enabled value.

            Notes:
                ALU br0 Status Redeployment Enabled

                
                This attribute is named `ALUbr0StatusRedeploymentEnabled` in VSD API.
                
        """
        self._al_ubr0_status_redeployment_enabled = value

    
    @property
    def cpu_utilization_redeployment_enabled(self):
        """ Get cpu_utilization_redeployment_enabled value.

            Notes:
                CPU Utilization Redeployment Enabled

                
                This attribute is named `CPUUtilizationRedeploymentEnabled` in VSD API.
                
        """
        return self._cpu_utilization_redeployment_enabled

    @cpu_utilization_redeployment_enabled.setter
    def cpu_utilization_redeployment_enabled(self, value):
        """ Set cpu_utilization_redeployment_enabled value.

            Notes:
                CPU Utilization Redeployment Enabled

                
                This attribute is named `CPUUtilizationRedeploymentEnabled` in VSD API.
                
        """
        self._cpu_utilization_redeployment_enabled = value

    
    @property
    def cpu_utilization_threshold(self):
        """ Get cpu_utilization_threshold value.

            Notes:
                CPU Utilization Threshold

                
                This attribute is named `CPUUtilizationThreshold` in VSD API.
                
        """
        return self._cpu_utilization_threshold

    @cpu_utilization_threshold.setter
    def cpu_utilization_threshold(self, value):
        """ Set cpu_utilization_threshold value.

            Notes:
                CPU Utilization Threshold

                
                This attribute is named `CPUUtilizationThreshold` in VSD API.
                
        """
        self._cpu_utilization_threshold = value

    
    @property
    def vrs_corrective_action_delay(self):
        """ Get vrs_corrective_action_delay value.

            Notes:
                VRS Corrective Action Delay in seconds

                
                This attribute is named `VRSCorrectiveActionDelay` in VSD API.
                
        """
        return self._vrs_corrective_action_delay

    @vrs_corrective_action_delay.setter
    def vrs_corrective_action_delay(self, value):
        """ Set vrs_corrective_action_delay value.

            Notes:
                VRS Corrective Action Delay in seconds

                
                This attribute is named `VRSCorrectiveActionDelay` in VSD API.
                
        """
        self._vrs_corrective_action_delay = value

    
    @property
    def vrs_process_redeployment_enabled(self):
        """ Get vrs_process_redeployment_enabled value.

            Notes:
                VRS Process Redeployment Enabled

                
                This attribute is named `VRSProcessRedeploymentEnabled` in VSD API.
                
        """
        return self._vrs_process_redeployment_enabled

    @vrs_process_redeployment_enabled.setter
    def vrs_process_redeployment_enabled(self, value):
        """ Set vrs_process_redeployment_enabled value.

            Notes:
                VRS Process Redeployment Enabled

                
                This attribute is named `VRSProcessRedeploymentEnabled` in VSD API.
                
        """
        self._vrs_process_redeployment_enabled = value

    
    @property
    def vrsvsc_status_redeployment_enabled(self):
        """ Get vrsvsc_status_redeployment_enabled value.

            Notes:
                VRSVSC Status Redeployment Enabled

                
                This attribute is named `VRSVSCStatusRedeploymentEnabled` in VSD API.
                
        """
        return self._vrsvsc_status_redeployment_enabled

    @vrsvsc_status_redeployment_enabled.setter
    def vrsvsc_status_redeployment_enabled(self, value):
        """ Set vrsvsc_status_redeployment_enabled value.

            Notes:
                VRSVSC Status Redeployment Enabled

                
                This attribute is named `VRSVSCStatusRedeploymentEnabled` in VSD API.
                
        """
        self._vrsvsc_status_redeployment_enabled = value

    
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
    def redeployment_delay(self):
        """ Get redeployment_delay value.

            Notes:
                redeployment Delay

                
                This attribute is named `redeploymentDelay` in VSD API.
                
        """
        return self._redeployment_delay

    @redeployment_delay.setter
    def redeployment_delay(self, value):
        """ Set redeployment_delay value.

            Notes:
                redeployment Delay

                
                This attribute is named `redeploymentDelay` in VSD API.
                
        """
        self._redeployment_delay = value

    
    @property
    def memory_utilization_redeployment_enabled(self):
        """ Get memory_utilization_redeployment_enabled value.

            Notes:
                memory Utilization Redeployment Enabled

                
                This attribute is named `memoryUtilizationRedeploymentEnabled` in VSD API.
                
        """
        return self._memory_utilization_redeployment_enabled

    @memory_utilization_redeployment_enabled.setter
    def memory_utilization_redeployment_enabled(self, value):
        """ Set memory_utilization_redeployment_enabled value.

            Notes:
                memory Utilization Redeployment Enabled

                
                This attribute is named `memoryUtilizationRedeploymentEnabled` in VSD API.
                
        """
        self._memory_utilization_redeployment_enabled = value

    
    @property
    def memory_utilization_threshold(self):
        """ Get memory_utilization_threshold value.

            Notes:
                memory Utilization Threshold

                
                This attribute is named `memoryUtilizationThreshold` in VSD API.
                
        """
        return self._memory_utilization_threshold

    @memory_utilization_threshold.setter
    def memory_utilization_threshold(self, value):
        """ Set memory_utilization_threshold value.

            Notes:
                memory Utilization Threshold

                
                This attribute is named `memoryUtilizationThreshold` in VSD API.
                
        """
        self._memory_utilization_threshold = value

    
    @property
    def deployment_count_threshold(self):
        """ Get deployment_count_threshold value.

            Notes:
                deployment count threshold

                
                This attribute is named `deploymentCountThreshold` in VSD API.
                
        """
        return self._deployment_count_threshold

    @deployment_count_threshold.setter
    def deployment_count_threshold(self, value):
        """ Set deployment_count_threshold value.

            Notes:
                deployment count threshold

                
                This attribute is named `deploymentCountThreshold` in VSD API.
                
        """
        self._deployment_count_threshold = value

    
    @property
    def jesxmon_process_redeployment_enabled(self):
        """ Get jesxmon_process_redeployment_enabled value.

            Notes:
                jesxmon Process Redeployment Enabled

                
                This attribute is named `jesxmonProcessRedeploymentEnabled` in VSD API.
                
        """
        return self._jesxmon_process_redeployment_enabled

    @jesxmon_process_redeployment_enabled.setter
    def jesxmon_process_redeployment_enabled(self, value):
        """ Set jesxmon_process_redeployment_enabled value.

            Notes:
                jesxmon Process Redeployment Enabled

                
                This attribute is named `jesxmonProcessRedeploymentEnabled` in VSD API.
                
        """
        self._jesxmon_process_redeployment_enabled = value

    
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

    

    