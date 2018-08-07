# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc, 2017 Nokia
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


class NUDeploymentFailure(NURESTObject):
    """ Represents a DeploymentFailure in the VSD

        Notes:
            A deployment failure represents a deployment operation initiated by the VSD that resulted in a failure.
    """

    __rest_name__ = "deploymentfailure"
    __resource_name__ = "deploymentfailures"

    
    ## Constants
    
    CONST_EVENT_TYPE_DELETE = "DELETE"
    
    CONST_EVENT_TYPE_CREATE = "CREATE"
    
    CONST_EVENT_TYPE_UPDATE = "UPDATE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a DeploymentFailure instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> deploymentfailure = NUDeploymentFailure(id=u'xxxx-xxx-xxx-xxx', name=u'DeploymentFailure')
                >>> deploymentfailure = NUDeploymentFailure(data=my_dict)
        """

        super(NUDeploymentFailure, self).__init__()

        # Read/Write Attributes
        
        self._last_failure_reason = None
        self._last_known_error = None
        self._affected_entity_id = None
        self._affected_entity_type = None
        self._error_condition = None
        self._number_of_occurences = None
        self._event_type = None
        
        self.expose_attribute(local_name="last_failure_reason", remote_name="lastFailureReason", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_known_error", remote_name="lastKnownError", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="affected_entity_id", remote_name="affectedEntityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="affected_entity_type", remote_name="affectedEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="error_condition", remote_name="errorCondition", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="number_of_occurences", remote_name="numberOfOccurences", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="event_type", remote_name="eventType", attribute_type=str, is_required=False, is_unique=False, choices=[u'CREATE', u'DELETE', u'UPDATE'])
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def last_failure_reason(self):
        """ Get last_failure_reason value.

            Notes:
                A detailed description of the last deployment failure.

                
                This attribute is named `lastFailureReason` in VSD API.
                
        """
        return self._last_failure_reason

    @last_failure_reason.setter
    def last_failure_reason(self, value):
        """ Set last_failure_reason value.

            Notes:
                A detailed description of the last deployment failure.

                
                This attribute is named `lastFailureReason` in VSD API.
                
        """
        self._last_failure_reason = value

    
    @property
    def last_known_error(self):
        """ Get last_known_error value.

            Notes:
                A string reporting the last reported deployment error condition.

                
                This attribute is named `lastKnownError` in VSD API.
                
        """
        return self._last_known_error

    @last_known_error.setter
    def last_known_error(self, value):
        """ Set last_known_error value.

            Notes:
                A string reporting the last reported deployment error condition.

                
                This attribute is named `lastKnownError` in VSD API.
                
        """
        self._last_known_error = value

    
    @property
    def affected_entity_id(self):
        """ Get affected_entity_id value.

            Notes:
                UUID of the entity on which deployment failed.

                
                This attribute is named `affectedEntityID` in VSD API.
                
        """
        return self._affected_entity_id

    @affected_entity_id.setter
    def affected_entity_id(self, value):
        """ Set affected_entity_id value.

            Notes:
                UUID of the entity on which deployment failed.

                
                This attribute is named `affectedEntityID` in VSD API.
                
        """
        self._affected_entity_id = value

    
    @property
    def affected_entity_type(self):
        """ Get affected_entity_type value.

            Notes:
                Managed object type corresponding to the entity on which deployment failed.

                
                This attribute is named `affectedEntityType` in VSD API.
                
        """
        return self._affected_entity_type

    @affected_entity_type.setter
    def affected_entity_type(self, value):
        """ Set affected_entity_type value.

            Notes:
                Managed object type corresponding to the entity on which deployment failed.

                
                This attribute is named `affectedEntityType` in VSD API.
                
        """
        self._affected_entity_type = value

    
    @property
    def error_condition(self):
        """ Get error_condition value.

            Notes:
                A numerical code mapping to the deployment error condition.

                
                This attribute is named `errorCondition` in VSD API.
                
        """
        return self._error_condition

    @error_condition.setter
    def error_condition(self, value):
        """ Set error_condition value.

            Notes:
                A numerical code mapping to the deployment error condition.

                
                This attribute is named `errorCondition` in VSD API.
                
        """
        self._error_condition = value

    
    @property
    def number_of_occurences(self):
        """ Get number_of_occurences value.

            Notes:
                A count of failed deployment attempts.

                
                This attribute is named `numberOfOccurences` in VSD API.
                
        """
        return self._number_of_occurences

    @number_of_occurences.setter
    def number_of_occurences(self, value):
        """ Set number_of_occurences value.

            Notes:
                A count of failed deployment attempts.

                
                This attribute is named `numberOfOccurences` in VSD API.
                
        """
        self._number_of_occurences = value

    
    @property
    def event_type(self):
        """ Get event_type value.

            Notes:
                Event type corresponding to the deployment failure

                
                This attribute is named `eventType` in VSD API.
                
        """
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        """ Set event_type value.

            Notes:
                Event type corresponding to the deployment failure

                
                This attribute is named `eventType` in VSD API.
                
        """
        self._event_type = value

    

    