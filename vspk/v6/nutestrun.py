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




from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUTestRun(NURESTObject):
    """ Represents a TestRun in the VSD

        Notes:
            A Test Run object represents the execution of a specific Test as part of a Test Suite Run.
    """

    __rest_name__ = "testrun"
    __resource_name__ = "testruns"

    
    ## Constants
    
    CONST_OPERATION_STATUS_STARTED = "STARTED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_OPERATION_STATUS_UNKNOWN = "UNKNOWN"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_OPERATION_STATUS_FAILED = "FAILED"
    
    CONST_OPERATION_STATUS_COMPLETED = "COMPLETED"
    
    CONST_OPERATION_STATUS_TIMED_OUT = "TIMED_OUT"
    
    

    def __init__(self, **kwargs):
        """ Initializes a TestRun instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> testrun = NUTestRun(id=u'xxxx-xxx-xxx-xxx', name=u'TestRun')
                >>> testrun = NUTestRun(data=my_dict)
        """

        super(NUTestRun, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._command = None
        self._command_exit_code = None
        self._command_output = None
        self._command_output_summary = None
        self._operation_status = None
        self._associated_test_id = None
        self._associated_test_suite_run_id = None
        self._start_date_time = None
        self._stop_date_time = None
        self._duration = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="command", remote_name="command", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="command_exit_code", remote_name="commandExitCode", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="command_output", remote_name="commandOutput", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="command_output_summary", remote_name="commandOutputSummary", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="operation_status", remote_name="operationStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'COMPLETED', u'FAILED', u'STARTED', u'TIMED_OUT', u'UNKNOWN'])
        self.expose_attribute(local_name="associated_test_id", remote_name="associatedTestID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_test_suite_run_id", remote_name="associatedTestSuiteRunID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="start_date_time", remote_name="startDateTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stop_date_time", remote_name="stopDateTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="duration", remote_name="duration", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
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
    def embedded_metadata(self):
        """ Get embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        return self._embedded_metadata

    @embedded_metadata.setter
    def embedded_metadata(self, value):
        """ Set embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        self._embedded_metadata = value

    
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
    def command(self):
        """ Get command value.

            Notes:
                The command, with its arguments, that is to be executed as part of the Test Run.

                
        """
        return self._command

    @command.setter
    def command(self, value):
        """ Set command value.

            Notes:
                The command, with its arguments, that is to be executed as part of the Test Run.

                
        """
        self._command = value

    
    @property
    def command_exit_code(self):
        """ Get command_exit_code value.

            Notes:
                The exit code returned to the OS from the executed test command. Field modified on VSD by the NSG.

                
                This attribute is named `commandExitCode` in VSD API.
                
        """
        return self._command_exit_code

    @command_exit_code.setter
    def command_exit_code(self, value):
        """ Set command_exit_code value.

            Notes:
                The exit code returned to the OS from the executed test command. Field modified on VSD by the NSG.

                
                This attribute is named `commandExitCode` in VSD API.
                
        """
        self._command_exit_code = value

    
    @property
    def command_output(self):
        """ Get command_output value.

            Notes:
                The output of the test command that was executed. Updated on VSD by the NSG.

                
                This attribute is named `commandOutput` in VSD API.
                
        """
        return self._command_output

    @command_output.setter
    def command_output(self, value):
        """ Set command_output value.

            Notes:
                The output of the test command that was executed. Updated on VSD by the NSG.

                
                This attribute is named `commandOutput` in VSD API.
                
        """
        self._command_output = value

    
    @property
    def command_output_summary(self):
        """ Get command_output_summary value.

            Notes:
                A brief summary of the command output received by the NSG.  Only the beginning and the end of the output is displayed.

                
                This attribute is named `commandOutputSummary` in VSD API.
                
        """
        return self._command_output_summary

    @command_output_summary.setter
    def command_output_summary(self, value):
        """ Set command_output_summary value.

            Notes:
                A brief summary of the command output received by the NSG.  Only the beginning and the end of the output is displayed.

                
                This attribute is named `commandOutputSummary` in VSD API.
                
        """
        self._command_output_summary = value

    
    @property
    def operation_status(self):
        """ Get operation_status value.

            Notes:
                The status of the test operation request as received by the NSG Agent. This field is set by the NSG.

                
                This attribute is named `operationStatus` in VSD API.
                
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, value):
        """ Set operation_status value.

            Notes:
                The status of the test operation request as received by the NSG Agent. This field is set by the NSG.

                
                This attribute is named `operationStatus` in VSD API.
                
        """
        self._operation_status = value

    
    @property
    def associated_test_id(self):
        """ Get associated_test_id value.

            Notes:
                The ID of the Test instance to which this Test Run is bound.

                
                This attribute is named `associatedTestID` in VSD API.
                
        """
        return self._associated_test_id

    @associated_test_id.setter
    def associated_test_id(self, value):
        """ Set associated_test_id value.

            Notes:
                The ID of the Test instance to which this Test Run is bound.

                
                This attribute is named `associatedTestID` in VSD API.
                
        """
        self._associated_test_id = value

    
    @property
    def associated_test_suite_run_id(self):
        """ Get associated_test_suite_run_id value.

            Notes:
                Test Run instances are part of a Test Suite Run.  This is the ID of the Test Suite Run object to which this Test Run belongs.

                
                This attribute is named `associatedTestSuiteRunID` in VSD API.
                
        """
        return self._associated_test_suite_run_id

    @associated_test_suite_run_id.setter
    def associated_test_suite_run_id(self, value):
        """ Set associated_test_suite_run_id value.

            Notes:
                Test Run instances are part of a Test Suite Run.  This is the ID of the Test Suite Run object to which this Test Run belongs.

                
                This attribute is named `associatedTestSuiteRunID` in VSD API.
                
        """
        self._associated_test_suite_run_id = value

    
    @property
    def start_date_time(self):
        """ Get start_date_time value.

            Notes:
                The start date and time of the test in milliseconds since Epoch.

                
                This attribute is named `startDateTime` in VSD API.
                
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, value):
        """ Set start_date_time value.

            Notes:
                The start date and time of the test in milliseconds since Epoch.

                
                This attribute is named `startDateTime` in VSD API.
                
        """
        self._start_date_time = value

    
    @property
    def stop_date_time(self):
        """ Get stop_date_time value.

            Notes:
                The stop date and time of the test in milliseconds since Epoch.

                
                This attribute is named `stopDateTime` in VSD API.
                
        """
        return self._stop_date_time

    @stop_date_time.setter
    def stop_date_time(self, value):
        """ Set stop_date_time value.

            Notes:
                The stop date and time of the test in milliseconds since Epoch.

                
                This attribute is named `stopDateTime` in VSD API.
                
        """
        self._stop_date_time = value

    
    @property
    def duration(self):
        """ Get duration value.

            Notes:
                The duration of execution of the Test in milliseconds.

                
        """
        return self._duration

    @duration.setter
    def duration(self, value):
        """ Set duration value.

            Notes:
                The duration of execution of the Test in milliseconds.

                
        """
        self._duration = value

    
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

    

    