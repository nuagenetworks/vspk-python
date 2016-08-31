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



from .fetchers import NUVMResyncsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVMInterfacesFetcher


from .fetchers import NUVRSsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUVM(NURESTObject):
    """ Represents a VM in the VSD

        Notes:
            Read only API that can retrieve the VMs associated with a domain, zone or subnet for mediation created VM's for REST created  VM's you need to set the additional proxy user header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example : Alcatel Lucent@bob), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header.
    """

    __rest_name__ = "vm"
    __resource_name__ = "vms"

    
    ## Constants
    
    CONST_REASON_TYPE_SHUTDOWN_UNKNOWN = "SHUTDOWN_UNKNOWN"
    
    CONST_REASON_TYPE_CRASHED_UNKNOWN = "CRASHED_UNKNOWN"
    
    CONST_REASON_TYPE_PAUSED_IOERROR = "PAUSED_IOERROR"
    
    CONST_STATUS_SHUTDOWN = "SHUTDOWN"
    
    CONST_REASON_TYPE_SHUTDOWN_LAST = "SHUTDOWN_LAST"
    
    CONST_STATUS_DELETE_PENDING = "DELETE_PENDING"
    
    CONST_REASON_TYPE_RUNNING_UNKNOWN = "RUNNING_UNKNOWN"
    
    CONST_STATUS_RUNNING = "RUNNING"
    
    CONST_REASON_TYPE_RUNNING_LAST = "RUNNING_LAST"
    
    CONST_REASON_TYPE_RUNNING_UNPAUSED = "RUNNING_UNPAUSED"
    
    CONST_REASON_TYPE_PAUSED_FROM_SNAPSHOT = "PAUSED_FROM_SNAPSHOT"
    
    CONST_REASON_TYPE_PAUSED_MIGRATION = "PAUSED_MIGRATION"
    
    CONST_REASON_TYPE_RUNNING_BOOTED = "RUNNING_BOOTED"
    
    CONST_REASON_TYPE_UNKNOWN = "UNKNOWN"
    
    CONST_STATUS_UNREACHABLE = "UNREACHABLE"
    
    CONST_STATUS_BLOCKED = "BLOCKED"
    
    CONST_REASON_TYPE_SHUTOFF_DESTROYED = "SHUTOFF_DESTROYED"
    
    CONST_REASON_TYPE_SHUTOFF_FROM_SNAPSHOT = "SHUTOFF_FROM_SNAPSHOT"
    
    CONST_REASON_TYPE_SHUTOFF_UNKNOWN = "SHUTOFF_UNKNOWN"
    
    CONST_STATUS_NOSTATE = "NOSTATE"
    
    CONST_REASON_TYPE_PAUSED_DUMP = "PAUSED_DUMP"
    
    CONST_REASON_TYPE_CRASHED_LAST = "CRASHED_LAST"
    
    CONST_STATUS_CRASHED = "CRASHED"
    
    CONST_REASON_TYPE_PAUSED_LAST = "PAUSED_LAST"
    
    CONST_REASON_TYPE_BLOCKED_LAST = "BLOCKED_LAST"
    
    CONST_REASON_TYPE_SHUTOFF_LAST = "SHUTOFF_LAST"
    
    CONST_STATUS_SHUTOFF = "SHUTOFF"
    
    CONST_REASON_TYPE_SHUTOFF_SHUTDOWN = "SHUTOFF_SHUTDOWN"
    
    CONST_REASON_TYPE_NOSTATE_UNKNOWN = "NOSTATE_UNKNOWN"
    
    CONST_REASON_TYPE_PAUSED_SAVE = "PAUSED_SAVE"
    
    CONST_REASON_TYPE_RUNNING_FROM_SNAPSHOT = "RUNNING_FROM_SNAPSHOT"
    
    CONST_STATUS_UNKNOWN = "UNKNOWN"
    
    CONST_REASON_TYPE_PAUSED_UNKNOWN = "PAUSED_UNKNOWN"
    
    CONST_REASON_TYPE_SHUTOFF_FAILED = "SHUTOFF_FAILED"
    
    CONST_REASON_TYPE_SHUTOFF_SAVED = "SHUTOFF_SAVED"
    
    CONST_REASON_TYPE_SHUTOFF_MIGRATED = "SHUTOFF_MIGRATED"
    
    CONST_STATUS_LAST = "LAST"
    
    CONST_REASON_TYPE_RUNNING_MIGRATED = "RUNNING_MIGRATED"
    
    CONST_REASON_TYPE_RUNNING_SAVE_CANCELED = "RUNNING_SAVE_CANCELED"
    
    CONST_REASON_TYPE_SHUTDOWN_USER = "SHUTDOWN_USER"
    
    CONST_REASON_TYPE_RUNNING_MIGRATION_CANCELED = "RUNNING_MIGRATION_CANCELED"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_STATUS_PAUSED = "PAUSED"
    
    CONST_STATUS_INIT = "INIT"
    
    CONST_REASON_TYPE_BLOCKED_UNKNOWN = "BLOCKED_UNKNOWN"
    
    CONST_REASON_TYPE_NOSTATE_LAST = "NOSTATE_LAST"
    
    CONST_REASON_TYPE_RUNNING_RESTORED = "RUNNING_RESTORED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_REASON_TYPE_SHUTOFF_CRASHED = "SHUTOFF_CRASHED"
    
    CONST_REASON_TYPE_PAUSED_USER = "PAUSED_USER"
    
    CONST_DELETE_MODE_TIMER = "TIMER"
    
    CONST_REASON_TYPE_PAUSED_WATCHDOG = "PAUSED_WATCHDOG"
    
    CONST_REASON_TYPE_PAUSED_SHUTTING_DOWN = "PAUSED_SHUTTING_DOWN"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VM instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vm = NUVM(id=u'xxxx-xxx-xxx-xxx', name=u'VM')
                >>> vm = NUVM(data=my_dict)
        """

        super(NUVM, self).__init__()

        # Read/Write Attributes
        
        self._l2_domain_ids = None
        self._vrsid = None
        self._uuid = None
        self._name = None
        self._last_updated_by = None
        self._reason_type = None
        self._delete_expiry = None
        self._delete_mode = None
        self._resync_info = None
        self._site_identifier = None
        self._interfaces = None
        self._enterprise_id = None
        self._enterprise_name = None
        self._entity_scope = None
        self._domain_ids = None
        self._zone_ids = None
        self._orchestration_id = None
        self._user_id = None
        self._user_name = None
        self._status = None
        self._subnet_ids = None
        self._external_id = None
        self._hypervisor_ip = None
        
        self.expose_attribute(local_name="l2_domain_ids", remote_name="l2DomainIDs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrsid", remote_name="VRSID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="uuid", remote_name="UUID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="reason_type", remote_name="reasonType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BLOCKED_LAST', u'BLOCKED_UNKNOWN', u'CRASHED_LAST', u'CRASHED_UNKNOWN', u'NOSTATE_LAST', u'NOSTATE_UNKNOWN', u'PAUSED_DUMP', u'PAUSED_FROM_SNAPSHOT', u'PAUSED_IOERROR', u'PAUSED_LAST', u'PAUSED_MIGRATION', u'PAUSED_SAVE', u'PAUSED_SHUTTING_DOWN', u'PAUSED_UNKNOWN', u'PAUSED_USER', u'PAUSED_WATCHDOG', u'RUNNING_BOOTED', u'RUNNING_FROM_SNAPSHOT', u'RUNNING_LAST', u'RUNNING_MIGRATED', u'RUNNING_MIGRATION_CANCELED', u'RUNNING_RESTORED', u'RUNNING_SAVE_CANCELED', u'RUNNING_UNKNOWN', u'RUNNING_UNPAUSED', u'SHUTDOWN_LAST', u'SHUTDOWN_UNKNOWN', u'SHUTDOWN_USER', u'SHUTOFF_CRASHED', u'SHUTOFF_DESTROYED', u'SHUTOFF_FAILED', u'SHUTOFF_FROM_SNAPSHOT', u'SHUTOFF_LAST', u'SHUTOFF_MIGRATED', u'SHUTOFF_SAVED', u'SHUTOFF_SHUTDOWN', u'SHUTOFF_UNKNOWN', u'UNKNOWN'])
        self.expose_attribute(local_name="delete_expiry", remote_name="deleteExpiry", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="delete_mode", remote_name="deleteMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'TIMER'])
        self.expose_attribute(local_name="resync_info", remote_name="resyncInfo", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="site_identifier", remote_name="siteIdentifier", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="interfaces", remote_name="interfaces", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_name", remote_name="enterpriseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="domain_ids", remote_name="domainIDs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zone_ids", remote_name="zoneIDs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="orchestration_id", remote_name="orchestrationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="user_id", remote_name="userID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="user_name", remote_name="userName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'BLOCKED', u'CRASHED', u'DELETE_PENDING', u'INIT', u'LAST', u'NOSTATE', u'PAUSED', u'RUNNING', u'SHUTDOWN', u'SHUTOFF', u'UNKNOWN', u'UNREACHABLE'])
        self.expose_attribute(local_name="subnet_ids", remote_name="subnetIDs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="hypervisor_ip", remote_name="hypervisorIP", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.vm_resyncs = NUVMResyncsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vrss = NUVRSsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def l2_domain_ids(self):
        """ Get l2_domain_ids value.

            Notes:
                Array of IDs of the l2 domain that the VM is connected to

                
                This attribute is named `l2DomainIDs` in VSD API.
                
        """
        return self._l2_domain_ids

    @l2_domain_ids.setter
    def l2_domain_ids(self, value):
        """ Set l2_domain_ids value.

            Notes:
                Array of IDs of the l2 domain that the VM is connected to

                
                This attribute is named `l2DomainIDs` in VSD API.
                
        """
        self._l2_domain_ids = value

    
    @property
    def vrsid(self):
        """ Get vrsid value.

            Notes:
                Id of the VRS that this VM is attached to.

                
                This attribute is named `VRSID` in VSD API.
                
        """
        return self._vrsid

    @vrsid.setter
    def vrsid(self, value):
        """ Set vrsid value.

            Notes:
                Id of the VRS that this VM is attached to.

                
                This attribute is named `VRSID` in VSD API.
                
        """
        self._vrsid = value

    
    @property
    def uuid(self):
        """ Get uuid value.

            Notes:
                UUID of the VM

                
                This attribute is named `UUID` in VSD API.
                
        """
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """ Set uuid value.

            Notes:
                UUID of the VM

                
                This attribute is named `UUID` in VSD API.
                
        """
        self._uuid = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the VM

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the VM

                
        """
        self._name = value

    
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
    def reason_type(self):
        """ Get reason_type value.

            Notes:
                Reason of the event associated with the VM.

                
                This attribute is named `reasonType` in VSD API.
                
        """
        return self._reason_type

    @reason_type.setter
    def reason_type(self, value):
        """ Set reason_type value.

            Notes:
                Reason of the event associated with the VM.

                
                This attribute is named `reasonType` in VSD API.
                
        """
        self._reason_type = value

    
    @property
    def delete_expiry(self):
        """ Get delete_expiry value.

            Notes:
                reflects the  VM Deletion expiry timer in secs , deleteMode needs to be non-null value for deleteExpiry to be taken in to effect. CMS created VM's will always have deleteMode set to TIMER

                
                This attribute is named `deleteExpiry` in VSD API.
                
        """
        return self._delete_expiry

    @delete_expiry.setter
    def delete_expiry(self, value):
        """ Set delete_expiry value.

            Notes:
                reflects the  VM Deletion expiry timer in secs , deleteMode needs to be non-null value for deleteExpiry to be taken in to effect. CMS created VM's will always have deleteMode set to TIMER

                
                This attribute is named `deleteExpiry` in VSD API.
                
        """
        self._delete_expiry = value

    
    @property
    def delete_mode(self):
        """ Get delete_mode value.

            Notes:
                reflects the mode of VM Deletion -  TIMER  Possible values are TIMER, .

                
                This attribute is named `deleteMode` in VSD API.
                
        """
        return self._delete_mode

    @delete_mode.setter
    def delete_mode(self, value):
        """ Set delete_mode value.

            Notes:
                reflects the mode of VM Deletion -  TIMER  Possible values are TIMER, .

                
                This attribute is named `deleteMode` in VSD API.
                
        """
        self._delete_mode = value

    
    @property
    def resync_info(self):
        """ Get resync_info value.

            Notes:
                Information of the status of the resync operation of a VM

                
                This attribute is named `resyncInfo` in VSD API.
                
        """
        return self._resync_info

    @resync_info.setter
    def resync_info(self, value):
        """ Set resync_info value.

            Notes:
                Information of the status of the resync operation of a VM

                
                This attribute is named `resyncInfo` in VSD API.
                
        """
        self._resync_info = value

    
    @property
    def site_identifier(self):
        """ Get site_identifier value.

            Notes:
                This property specifies the site the VM belongs to, for Geo-redundancy.

                
                This attribute is named `siteIdentifier` in VSD API.
                
        """
        return self._site_identifier

    @site_identifier.setter
    def site_identifier(self, value):
        """ Set site_identifier value.

            Notes:
                This property specifies the site the VM belongs to, for Geo-redundancy.

                
                This attribute is named `siteIdentifier` in VSD API.
                
        """
        self._site_identifier = value

    
    @property
    def interfaces(self):
        """ Get interfaces value.

            Notes:
                List of VM interfaces associated with the VM

                
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, value):
        """ Set interfaces value.

            Notes:
                List of VM interfaces associated with the VM

                
        """
        self._interfaces = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                ID of the enterprise that this VM belongs to

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                ID of the enterprise that this VM belongs to

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
    @property
    def enterprise_name(self):
        """ Get enterprise_name value.

            Notes:
                Name of the enterprise that this VM belongs to

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        """ Set enterprise_name value.

            Notes:
                Name of the enterprise that this VM belongs to

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        self._enterprise_name = value

    
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
    def domain_ids(self):
        """ Get domain_ids value.

            Notes:
                Array of IDs of the domain that the VM is connected to

                
                This attribute is named `domainIDs` in VSD API.
                
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, value):
        """ Set domain_ids value.

            Notes:
                Array of IDs of the domain that the VM is connected to

                
                This attribute is named `domainIDs` in VSD API.
                
        """
        self._domain_ids = value

    
    @property
    def zone_ids(self):
        """ Get zone_ids value.

            Notes:
                Array of IDs of the zone that this VM is attached to

                
                This attribute is named `zoneIDs` in VSD API.
                
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, value):
        """ Set zone_ids value.

            Notes:
                Array of IDs of the zone that this VM is attached to

                
                This attribute is named `zoneIDs` in VSD API.
                
        """
        self._zone_ids = value

    
    @property
    def orchestration_id(self):
        """ Get orchestration_id value.

            Notes:
                Orchestration ID

                
                This attribute is named `orchestrationID` in VSD API.
                
        """
        return self._orchestration_id

    @orchestration_id.setter
    def orchestration_id(self, value):
        """ Set orchestration_id value.

            Notes:
                Orchestration ID

                
                This attribute is named `orchestrationID` in VSD API.
                
        """
        self._orchestration_id = value

    
    @property
    def user_id(self):
        """ Get user_id value.

            Notes:
                ID of the user that created this VM

                
                This attribute is named `userID` in VSD API.
                
        """
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """ Set user_id value.

            Notes:
                ID of the user that created this VM

                
                This attribute is named `userID` in VSD API.
                
        """
        self._user_id = value

    
    @property
    def user_name(self):
        """ Get user_name value.

            Notes:
                Username of the user that created this VM

                
                This attribute is named `userName` in VSD API.
                
        """
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        """ Set user_name value.

            Notes:
                Username of the user that created this VM

                
                This attribute is named `userName` in VSD API.
                
        """
        self._user_name = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                Status of the VM.

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                Status of the VM.

                
        """
        self._status = value

    
    @property
    def subnet_ids(self):
        """ Get subnet_ids value.

            Notes:
                Array of IDs of the subnets that the VM is connected to

                
                This attribute is named `subnetIDs` in VSD API.
                
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, value):
        """ Set subnet_ids value.

            Notes:
                Array of IDs of the subnets that the VM is connected to

                
                This attribute is named `subnetIDs` in VSD API.
                
        """
        self._subnet_ids = value

    
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
    def hypervisor_ip(self):
        """ Get hypervisor_ip value.

            Notes:
                IP address of the hypervisor that this VM is currently running in

                
                This attribute is named `hypervisorIP` in VSD API.
                
        """
        return self._hypervisor_ip

    @hypervisor_ip.setter
    def hypervisor_ip(self, value):
        """ Set hypervisor_ip value.

            Notes:
                IP address of the hypervisor that this VM is currently running in

                
                This attribute is named `hypervisorIP` in VSD API.
                
        """
        self._hypervisor_ip = value

    

    