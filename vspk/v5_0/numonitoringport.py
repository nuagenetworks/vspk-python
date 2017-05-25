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

from bambou import NURESTObject


class NUMonitoringPort(NURESTObject):
    """ Represents a MonitoringPort in the VSD

        Notes:
            Encapsulates the port information for system monitoring entity.
    """

    __rest_name__ = "monitoringport"
    __resource_name__ = "monitoringports"

    
    ## Constants
    
    CONST_RESILIENCY_STATE_BACKUP = "backup"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_RESILIENCY_STATE_NONE = "none"
    
    CONST_RESILIENCY_STATE_MASTER = "master"
    
    CONST_STATE_DOWN = "DOWN"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_STATE_ADMIN_DOWN = "ADMIN_DOWN"
    
    CONST_STATE_UP = "UP"
    
    

    def __init__(self, **kwargs):
        """ Initializes a MonitoringPort instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> monitoringport = NUMonitoringPort(id=u'xxxx-xxx-xxx-xxx', name=u'MonitoringPort')
                >>> monitoringport = NUMonitoringPort(data=my_dict)
        """

        super(NUMonitoringPort, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_state_change = None
        self._access = None
        self._description = None
        self._resiliency_state = None
        self._resilient = None
        self._entity_scope = None
        self._uplink = None
        self._state = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_state_change", remote_name="lastStateChange", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="access", remote_name="access", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="resiliency_state", remote_name="resiliencyState", attribute_type=str, is_required=False, is_unique=False, choices=[u'backup', u'master', u'none'])
        self.expose_attribute(local_name="resilient", remote_name="resilient", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="uplink", remote_name="uplink", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="state", remote_name="state", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'UP'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name for the port.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name for the port.

                
        """
        self._name = value

    
    @property
    def last_state_change(self):
        """ Get last_state_change value.

            Notes:
                Last port state change timestamp.

                
                This attribute is named `lastStateChange` in VSD API.
                
        """
        return self._last_state_change

    @last_state_change.setter
    def last_state_change(self, value):
        """ Set last_state_change value.

            Notes:
                Last port state change timestamp.

                
                This attribute is named `lastStateChange` in VSD API.
                
        """
        self._last_state_change = value

    
    @property
    def access(self):
        """ Get access value.

            Notes:
                Flag to indicate that it is a access port or network port.

                
        """
        return self._access

    @access.setter
    def access(self, value):
        """ Set access value.

            Notes:
                Flag to indicate that it is a access port or network port.

                
        """
        self._access = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Optional port description.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Optional port description.

                
        """
        self._description = value

    
    @property
    def resiliency_state(self):
        """ Get resiliency_state value.

            Notes:
                

                
                This attribute is named `resiliencyState` in VSD API.
                
        """
        return self._resiliency_state

    @resiliency_state.setter
    def resiliency_state(self, value):
        """ Set resiliency_state value.

            Notes:
                

                
                This attribute is named `resiliencyState` in VSD API.
                
        """
        self._resiliency_state = value

    
    @property
    def resilient(self):
        """ Get resilient value.

            Notes:
                Flag to indicate if an ACCESS port is resilient or not.

                
        """
        return self._resilient

    @resilient.setter
    def resilient(self, value):
        """ Set resilient value.

            Notes:
                Flag to indicate if an ACCESS port is resilient or not.

                
        """
        self._resilient = value

    
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
    def uplink(self):
        """ Get uplink value.

            Notes:
                Flag to indicate that is an uplink or downlink port.

                
        """
        return self._uplink

    @uplink.setter
    def uplink(self, value):
        """ Set uplink value.

            Notes:
                Flag to indicate that is an uplink or downlink port.

                
        """
        self._uplink = value

    
    @property
    def state(self):
        """ Get state value.

            Notes:
                The current state of the port.

                
        """
        return self._state

    @state.setter
    def state(self, value):
        """ Set state value.

            Notes:
                The current state of the port.

                
        """
        self._state = value

    
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

    

    