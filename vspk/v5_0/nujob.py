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


class NUJob(NURESTObject):
    """ Represents a Job in the VSD

        Notes:
            Represents JOB entity. The job API accepts a command and parameters and executes the job and returns the results. Jobs API are typically used for long running tasks.
    """

    __rest_name__ = "job"
    __resource_name__ = "jobs"

    
    ## Constants
    
    CONST_STATUS_SUCCESS = "SUCCESS"
    
    CONST_COMMAND_RETRIEVE_ACTIVE_NSGS = "RETRIEVE_ACTIVE_NSGS"
    
    CONST_COMMAND_UNDEPLOY = "UNDEPLOY"
    
    CONST_COMMAND_RELOAD = "RELOAD"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_COMMAND_REJECT_ZFB_REQUEST = "REJECT_ZFB_REQUEST"
    
    CONST_COMMAND_NSG_NOTIFICATION_TEST = "NSG_NOTIFICATION_TEST"
    
    CONST_COMMAND_VCENTER_REMOVE_COMPUTERESOURCE_INSCOPE = "VCENTER_REMOVE_COMPUTERESOURCE_INSCOPE"
    
    CONST_COMMAND_NETCONF_FORCE_DEPLOY = "NETCONF_FORCE_DEPLOY"
    
    CONST_COMMAND_FORCE_KEYSERVER_UPDATE = "FORCE_KEYSERVER_UPDATE"
    
    CONST_COMMAND_START = "START"
    
    CONST_COMMAND_RELOAD_NSG_CONFIG = "RELOAD_NSG_CONFIG"
    
    CONST_COMMAND_BEGIN_POLICY_CHANGES = "BEGIN_POLICY_CHANGES"
    
    CONST_COMMAND_VCENTER_SYNC = "VCENTER_SYNC"
    
    CONST_COMMAND_CERTIFICATE_NSG_REVOKE = "CERTIFICATE_NSG_REVOKE"
    
    CONST_COMMAND_STATUS = "STATUS"
    
    CONST_COMMAND_EXPORT = "EXPORT"
    
    CONST_COMMAND_GET_ZFB_INFO = "GET_ZFB_INFO"
    
    CONST_COMMAND_FORCE_KEYSERVER_VSD_RESYNC = "FORCE_KEYSERVER_VSD_RESYNC"
    
    CONST_COMMAND_RESTART = "RESTART"
    
    CONST_COMMAND_BATCH_CRUD_REQUEST = "BATCH_CRUD_REQUEST"
    
    CONST_COMMAND_VCENTER_DELETE_AGENCY = "VCENTER_DELETE_AGENCY"
    
    CONST_STATUS_FAILED = "FAILED"
    
    CONST_COMMAND_APPLY_POLICY_CHANGES = "APPLY_POLICY_CHANGES"
    
    CONST_COMMAND_FORCE_KEYSERVER_UPDATE_ACK = "FORCE_KEYSERVER_UPDATE_ACK"
    
    CONST_COMMAND_NOTIFY_NSG_REGISTRATION = "NOTIFY_NSG_REGISTRATION"
    
    CONST_COMMAND_REDEPLOY = "REDEPLOY"
    
    CONST_COMMAND_NETCONF_SYNC = "NETCONF_SYNC"
    
    CONST_COMMAND_VCENTER_ADD_COMPUTERESOURCE_INSCOPE = "VCENTER_ADD_COMPUTERESOURCE_INSCOPE"
    
    CONST_COMMAND_APPLICATION_SIGNATURE_IMPORT = "APPLICATION_SIGNATURE_IMPORT"
    
    CONST_COMMAND_VCENTER_RECONNECT = "VCENTER_RECONNECT"
    
    CONST_COMMAND_CLEAR_MAC_MOVE_ALARMS = "CLEAR_MAC_MOVE_ALARMS"
    
    CONST_COMMAND_VCENTER_RELOAD = "VCENTER_RELOAD"
    
    CONST_COMMAND_NSG_REGISTRATION_INFO = "NSG_REGISTRATION_INFO"
    
    CONST_COMMAND_GATEWAY_AUDIT = "GATEWAY_AUDIT"
    
    CONST_COMMAND_NOTIFY_NSG_REGISTRATION_TEST = "NOTIFY_NSG_REGISTRATION_TEST"
    
    CONST_COMMAND_NOTIFY_NSG_REGISTRATION_ACK = "NOTIFY_NSG_REGISTRATION_ACK"
    
    CONST_COMMAND_STOP = "STOP"
    
    CONST_COMMAND_VCENTER_UPGRADE_VRS = "VCENTER_UPGRADE_VRS"
    
    CONST_COMMAND_IMPORT = "IMPORT"
    
    CONST_COMMAND_CLEAR_IPSEC_DATA = "CLEAR_IPSEC_DATA"
    
    CONST_COMMAND_RELOAD_GEO_REDUNDANT_INFO = "RELOAD_GEO_REDUNDANT_INFO"
    
    CONST_COMMAND_CERTIFICATE_NSG_RENEW = "CERTIFICATE_NSG_RENEW"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_STATUS_RUNNING = "RUNNING"
    
    CONST_COMMAND_VCENTER_SCRIPT_UPGRADE_VRS = "VCENTER_SCRIPT_UPGRADE_VRS"
    
    CONST_COMMAND_DEPLOY = "DEPLOY"
    
    CONST_COMMAND_SYNC = "SYNC"
    
    CONST_COMMAND_KEYSERVER_NOTIFICATION_TEST = "KEYSERVER_NOTIFICATION_TEST"
    
    CONST_COMMAND_DISCARD_POLICY_CHANGES = "DISCARD_POLICY_CHANGES"
    
    CONST_COMMAND_VCENTER_MARK_AGENT_VM_AVAILABLE = "VCENTER_MARK_AGENT_VM_AVAILABLE"
    
    CONST_COMMAND_SAAS_APPLICATION_TYPE = "SAAS_APPLICATION_TYPE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Job instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> job = NUJob(id=u'xxxx-xxx-xxx-xxx', name=u'Job')
                >>> job = NUJob(data=my_dict)
        """

        super(NUJob, self).__init__()

        # Read/Write Attributes
        
        self._parameters = None
        self._last_updated_by = None
        self._result = None
        self._entity_scope = None
        self._command = None
        self._progress = None
        self._assoc_entity_type = None
        self._status = None
        self._external_id = None
        
        self.expose_attribute(local_name="parameters", remote_name="parameters", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="result", remote_name="result", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="command", remote_name="command", attribute_type=str, is_required=True, is_unique=False, choices=[u'APPLICATION_SIGNATURE_IMPORT', u'APPLY_POLICY_CHANGES', u'BATCH_CRUD_REQUEST', u'BEGIN_POLICY_CHANGES', u'CERTIFICATE_NSG_RENEW', u'CERTIFICATE_NSG_REVOKE', u'CLEAR_IPSEC_DATA', u'CLEAR_MAC_MOVE_ALARMS', u'DEPLOY', u'DISCARD_POLICY_CHANGES', u'EXPORT', u'FORCE_KEYSERVER_UPDATE', u'FORCE_KEYSERVER_UPDATE_ACK', u'FORCE_KEYSERVER_VSD_RESYNC', u'GATEWAY_AUDIT', u'GET_ZFB_INFO', u'IMPORT', u'KEYSERVER_NOTIFICATION_TEST', u'NETCONF_FORCE_DEPLOY', u'NETCONF_SYNC', u'NOTIFY_NSG_REGISTRATION', u'NOTIFY_NSG_REGISTRATION_ACK', u'NOTIFY_NSG_REGISTRATION_TEST', u'NSG_NOTIFICATION_TEST', u'NSG_REGISTRATION_INFO', u'REDEPLOY', u'REJECT_ZFB_REQUEST', u'RELOAD', u'RELOAD_GEO_REDUNDANT_INFO', u'RELOAD_NSG_CONFIG', u'RESTART', u'RETRIEVE_ACTIVE_NSGS', u'SAAS_APPLICATION_TYPE', u'START', u'STATUS', u'STOP', u'SYNC', u'UNDEPLOY', u'VCENTER_ADD_COMPUTERESOURCE_INSCOPE', u'VCENTER_DELETE_AGENCY', u'VCENTER_MARK_AGENT_VM_AVAILABLE', u'VCENTER_RECONNECT', u'VCENTER_RELOAD', u'VCENTER_REMOVE_COMPUTERESOURCE_INSCOPE', u'VCENTER_SCRIPT_UPGRADE_VRS', u'VCENTER_SYNC', u'VCENTER_UPGRADE_VRS'])
        self.expose_attribute(local_name="progress", remote_name="progress", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="assoc_entity_type", remote_name="assocEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'FAILED', u'RUNNING', u'SUCCESS'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def parameters(self):
        """ Get parameters value.

            Notes:
                Additional arguments required for the specific command. Differs based on types of command.

                
        """
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        """ Set parameters value.

            Notes:
                Additional arguments required for the specific command. Differs based on types of command.

                
        """
        self._parameters = value

    
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
    def result(self):
        """ Get result value.

            Notes:
                Results from the execution of the job

                
        """
        return self._result

    @result.setter
    def result(self, value):
        """ Set result value.

            Notes:
                Results from the execution of the job

                
        """
        self._result = value

    
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
                Name of the command.

                
        """
        return self._command

    @command.setter
    def command(self, value):
        """ Set command value.

            Notes:
                Name of the command.

                
        """
        self._command = value

    
    @property
    def progress(self):
        """ Get progress value.

            Notes:
                Indicates the progress of the job as a faction. eg : 0.5 means 50% done.

                
        """
        return self._progress

    @progress.setter
    def progress(self, value):
        """ Set progress value.

            Notes:
                Indicates the progress of the job as a faction. eg : 0.5 means 50% done.

                
        """
        self._progress = value

    
    @property
    def assoc_entity_type(self):
        """ Get assoc_entity_type value.

            Notes:
                Entity with which this job is associated Refer to API section for supported types.

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        return self._assoc_entity_type

    @assoc_entity_type.setter
    def assoc_entity_type(self, value):
        """ Set assoc_entity_type value.

            Notes:
                Entity with which this job is associated Refer to API section for supported types.

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        self._assoc_entity_type = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                Current status of the job. Possible values are RUNNING, FAILED, SUCCESS, .

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                Current status of the job. Possible values are RUNNING, FAILED, SUCCESS, .

                
        """
        self._status = value

    
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

    

    