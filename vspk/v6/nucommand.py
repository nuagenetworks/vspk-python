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


class NUCommand(NURESTObject):
    """ Represents a Command in the VSD

        Notes:
            A Command represents an operation that needs to be executed on an entity (NSG, Gateway, ...) which requires little processing by VSD, but may result in a long activity on the external entity.  An example would be to trigger an action on VSD so that a Gateway download a new image.  VSDs handling of the request is limited to generating a message to be sent to the device on which the download process is expected.  The device then acts on the request and proceeds with the download...  That may be a long process.  The commands API is similar to the Jobs API with regards to triggering operations on objects.
    """

    __rest_name__ = "command"
    __resource_name__ = "commands"

    
    ## Constants
    
    CONST_OVERRIDE_ABANDON = "ABANDON"
    
    CONST_OVERRIDE_UNSPECIFIED = "UNSPECIFIED"
    
    CONST_COMMAND_NSG_APPLY_PATCH = "NSG_APPLY_PATCH"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_STATUS_UNKNOWN = "UNKNOWN"
    
    CONST_STATUS_SKIPPED = "SKIPPED"
    
    CONST_STATUS_STARTED = "STARTED"
    
    CONST_STATUS_RUNNING = "RUNNING"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_COMMAND_UNKNOWN = "UNKNOWN"
    
    CONST_STATUS_COMPLETED = "COMPLETED"
    
    CONST_COMMAND_NSG_DOWNLOAD_OS_IMAGE = "NSG_DOWNLOAD_OS_IMAGE"
    
    CONST_STATUS_FAILED = "FAILED"
    
    CONST_COMMAND_NSG_UPGRADE_TO_IMAGE = "NSG_UPGRADE_TO_IMAGE"
    
    CONST_COMMAND_NSG_DELETE_PATCH = "NSG_DELETE_PATCH"
    
    CONST_STATUS_ABANDONED = "ABANDONED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Command instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> command = NUCommand(id=u'xxxx-xxx-xxx-xxx', name=u'Command')
                >>> command = NUCommand(data=my_dict)
        """

        super(NUCommand, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._detail = None
        self._detailed_status = None
        self._detailed_status_code = None
        self._entity_scope = None
        self._command = None
        self._command_information = None
        self._progress = None
        self._assoc_entity_type = None
        self._associated_param = None
        self._associated_param_type = None
        self._status = None
        self._full_command = None
        self._summary = None
        self._override = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="detail", remote_name="detail", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="detailed_status", remote_name="detailedStatus", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="detailed_status_code", remote_name="detailedStatusCode", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="command", remote_name="command", attribute_type=str, is_required=True, is_unique=False, choices=[u'NSG_APPLY_PATCH', u'NSG_DELETE_PATCH', u'NSG_DOWNLOAD_OS_IMAGE', u'NSG_UPGRADE_TO_IMAGE', u'UNKNOWN'])
        self.expose_attribute(local_name="command_information", remote_name="commandInformation", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="progress", remote_name="progress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="assoc_entity_type", remote_name="assocEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_param", remote_name="associatedParam", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_param_type", remote_name="associatedParamType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'ABANDONED', u'COMPLETED', u'FAILED', u'RUNNING', u'SKIPPED', u'STARTED', u'UNKNOWN'])
        self.expose_attribute(local_name="full_command", remote_name="fullCommand", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="summary", remote_name="summary", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="override", remote_name="override", attribute_type=str, is_required=False, is_unique=False, choices=[u'ABANDON', u'UNSPECIFIED'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

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
    def detail(self):
        """ Get detail value.

            Notes:
                Details about the command execution as reported directly from the NSG independent of status codes.

                
        """
        return self._detail

    @detail.setter
    def detail(self, value):
        """ Set detail value.

            Notes:
                Details about the command execution as reported directly from the NSG independent of status codes.

                
        """
        self._detail = value

    
    @property
    def detailed_status(self):
        """ Get detailed_status value.

            Notes:
                A string representing the detailed status of the operation that was triggered by the execution of the Command instance.

                
                This attribute is named `detailedStatus` in VSD API.
                
        """
        return self._detailed_status

    @detailed_status.setter
    def detailed_status(self, value):
        """ Set detailed_status value.

            Notes:
                A string representing the detailed status of the operation that was triggered by the execution of the Command instance.

                
                This attribute is named `detailedStatus` in VSD API.
                
        """
        self._detailed_status = value

    
    @property
    def detailed_status_code(self):
        """ Get detailed_status_code value.

            Notes:
                A numerical code mapping to a list of detailed statuses that can apply to a Command instance.

                
                This attribute is named `detailedStatusCode` in VSD API.
                
        """
        return self._detailed_status_code

    @detailed_status_code.setter
    def detailed_status_code(self, value):
        """ Set detailed_status_code value.

            Notes:
                A numerical code mapping to a list of detailed statuses that can apply to a Command instance.

                
                This attribute is named `detailedStatusCode` in VSD API.
                
        """
        self._detailed_status_code = value

    
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
                Specifies the type of command that is stated for execution on the system receiving the operation request.  A request for download, a request for upgrade, a request for revocation, ...

                
        """
        return self._command

    @command.setter
    def command(self, value):
        """ Set command value.

            Notes:
                Specifies the type of command that is stated for execution on the system receiving the operation request.  A request for download, a request for upgrade, a request for revocation, ...

                
        """
        self._command = value

    
    @property
    def command_information(self):
        """ Get command_information value.

            Notes:
                Informative details on what command is to be executed.  It complements the commandType attribute.  An example of a value could be a URL, a version number, a UUID of another object, ...

                
                This attribute is named `commandInformation` in VSD API.
                
        """
        return self._command_information

    @command_information.setter
    def command_information(self, value):
        """ Set command_information value.

            Notes:
                Informative details on what command is to be executed.  It complements the commandType attribute.  An example of a value could be a URL, a version number, a UUID of another object, ...

                
                This attribute is named `commandInformation` in VSD API.
                
        """
        self._command_information = value

    
    @property
    def progress(self):
        """ Get progress value.

            Notes:
                JSON string detailing the progress of the command execution on Gateway.

                
        """
        return self._progress

    @progress.setter
    def progress(self, value):
        """ Set progress value.

            Notes:
                JSON string detailing the progress of the command execution on Gateway.

                
        """
        self._progress = value

    
    @property
    def assoc_entity_type(self):
        """ Get assoc_entity_type value.

            Notes:
                Managed Object Type of the entity on which this Command is associated.

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        return self._assoc_entity_type

    @assoc_entity_type.setter
    def assoc_entity_type(self, value):
        """ Set assoc_entity_type value.

            Notes:
                Managed Object Type of the entity on which this Command is associated.

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        self._assoc_entity_type = value

    
    @property
    def associated_param(self):
        """ Get associated_param value.

            Notes:
                Parameters to be supplied for execution of this command. This should be the ID of the object supplying parameters.

                
                This attribute is named `associatedParam` in VSD API.
                
        """
        return self._associated_param

    @associated_param.setter
    def associated_param(self, value):
        """ Set associated_param value.

            Notes:
                Parameters to be supplied for execution of this command. This should be the ID of the object supplying parameters.

                
                This attribute is named `associatedParam` in VSD API.
                
        """
        self._associated_param = value

    
    @property
    def associated_param_type(self):
        """ Get associated_param_type value.

            Notes:
                Type of the object which supplies parameters for this command. For NSG_APPLY_PATCH command this should be NSG_PATCH_PROFILE. For NSG_DELETE_PATCH it should be PATCH

                
                This attribute is named `associatedParamType` in VSD API.
                
        """
        return self._associated_param_type

    @associated_param_type.setter
    def associated_param_type(self, value):
        """ Set associated_param_type value.

            Notes:
                Type of the object which supplies parameters for this command. For NSG_APPLY_PATCH command this should be NSG_PATCH_PROFILE. For NSG_DELETE_PATCH it should be PATCH

                
                This attribute is named `associatedParamType` in VSD API.
                
        """
        self._associated_param_type = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                The status of the Command from a VSD perspective.

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                The status of the Command from a VSD perspective.

                
        """
        self._status = value

    
    @property
    def full_command(self):
        """ Get full_command value.

            Notes:
                Full command including parameters that is to be executed.

                
                This attribute is named `fullCommand` in VSD API.
                
        """
        return self._full_command

    @full_command.setter
    def full_command(self, value):
        """ Set full_command value.

            Notes:
                Full command including parameters that is to be executed.

                
                This attribute is named `fullCommand` in VSD API.
                
        """
        self._full_command = value

    
    @property
    def summary(self):
        """ Get summary value.

            Notes:
                A generated summary for the action giving some general context on the command executed.

                
        """
        return self._summary

    @summary.setter
    def summary(self, value):
        """ Set summary value.

            Notes:
                A generated summary for the action giving some general context on the command executed.

                
        """
        self._summary = value

    
    @property
    def override(self):
        """ Get override value.

            Notes:
                Operator specified action which overrides the normal life cycle of a command.

                
        """
        return self._override

    @override.setter
    def override(self, value):
        """ Set override value.

            Notes:
                Operator specified action which overrides the normal life cycle of a command.

                
        """
        self._override = value

    
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

    

    