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


class NUAlarm(NURESTObject):
    """ Represents a Alarm in the VSD

        Notes:
            The alarm API allows the management of system alarms.
    """

    __rest_name__ = "alarm"
    __resource_name__ = "alarms"

    
    ## Constants
    
    CONST_SEVERITY_WARNING = "WARNING"
    
    CONST_SEVERITY_MAJOR = "MAJOR"
    
    CONST_SEVERITY_CRITICAL = "CRITICAL"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_SEVERITY_INFO = "INFO"
    
    CONST_SEVERITY_MINOR = "MINOR"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Alarm instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> alarm = NUAlarm(id=u'xxxx-xxx-xxx-xxx', name=u'Alarm')
                >>> alarm = NUAlarm(data=my_dict)
        """

        super(NUAlarm, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._target_object = None
        self._last_updated_by = None
        self._acknowledged = None
        self._reason = None
        self._description = None
        self._severity = None
        self._timestamp = None
        self._enterprise_id = None
        self._entity_scope = None
        self._error_condition = None
        self._number_of_occurances = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="target_object", remote_name="targetObject", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="acknowledged", remote_name="acknowledged", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="reason", remote_name="reason", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="severity", remote_name="severity", attribute_type=str, is_required=False, is_unique=False, choices=[u'CRITICAL', u'INFO', u'MAJOR', u'MINOR', u'WARNING'])
        self.expose_attribute(local_name="timestamp", remote_name="timestamp", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="error_condition", remote_name="errorCondition", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="number_of_occurances", remote_name="numberOfOccurances", attribute_type=int, is_required=False, is_unique=False)
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
                The alarm name.  Each type of alarm will generate its own name

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The alarm name.  Each type of alarm will generate its own name

                
        """
        self._name = value

    
    @property
    def target_object(self):
        """ Get target_object value.

            Notes:
                Identifies affected Entity.  Example: Alarm generated by TCA for Domain domain1(Packets towards a VM, Breach)

                
                This attribute is named `targetObject` in VSD API.
                
        """
        return self._target_object

    @target_object.setter
    def target_object(self, value):
        """ Set target_object value.

            Notes:
                Identifies affected Entity.  Example: Alarm generated by TCA for Domain domain1(Packets towards a VM, Breach)

                
                This attribute is named `targetObject` in VSD API.
                
        """
        self._target_object = value

    
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
    def acknowledged(self):
        """ Get acknowledged value.

            Notes:
                Flag to indicate that alarm is already acknowledged or not

                
        """
        return self._acknowledged

    @acknowledged.setter
    def acknowledged(self, value):
        """ Set acknowledged value.

            Notes:
                Flag to indicate that alarm is already acknowledged or not

                
        """
        self._acknowledged = value

    
    @property
    def reason(self):
        """ Get reason value.

            Notes:
                Provides a description of the alarm

                
        """
        return self._reason

    @reason.setter
    def reason(self, value):
        """ Set reason value.

            Notes:
                Provides a description of the alarm

                
        """
        self._reason = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the alarm

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the alarm

                
        """
        self._description = value

    
    @property
    def severity(self):
        """ Get severity value.

            Notes:
                Severity of the alarm.

                
        """
        return self._severity

    @severity.setter
    def severity(self, value):
        """ Set severity value.

            Notes:
                Severity of the alarm.

                
        """
        self._severity = value

    
    @property
    def timestamp(self):
        """ Get timestamp value.

            Notes:
                Indicates the time that the alarm was triggered

                
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        """ Set timestamp value.

            Notes:
                Indicates the time that the alarm was triggered

                
        """
        self._timestamp = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                Enterprise that this alarm belongs to

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                Enterprise that this alarm belongs to

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
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
    def error_condition(self):
        """ Get error_condition value.

            Notes:
                Identifies the error condition

                
                This attribute is named `errorCondition` in VSD API.
                
        """
        return self._error_condition

    @error_condition.setter
    def error_condition(self, value):
        """ Set error_condition value.

            Notes:
                Identifies the error condition

                
                This attribute is named `errorCondition` in VSD API.
                
        """
        self._error_condition = value

    
    @property
    def number_of_occurances(self):
        """ Get number_of_occurances value.

            Notes:
                Number of times that the alarm was triggered

                
                This attribute is named `numberOfOccurances` in VSD API.
                
        """
        return self._number_of_occurances

    @number_of_occurances.setter
    def number_of_occurances(self, value):
        """ Set number_of_occurances value.

            Notes:
                Number of times that the alarm was triggered

                
                This attribute is named `numberOfOccurances` in VSD API.
                
        """
        self._number_of_occurances = value

    
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

    

    