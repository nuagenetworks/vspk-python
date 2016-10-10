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



from .fetchers import NUGatewaySecuritiesFetcher


from .fetchers import NUPATNATPoolsFetcher


from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUInfrastructureConfigsFetcher


from .fetchers import NUEnterprisePermissionsFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NULocationsFetcher


from .fetchers import NUMonitorscopesFetcher


from .fetchers import NUBootstrapsFetcher


from .fetchers import NUBootstrapActivationsFetcher


from .fetchers import NUNSGInfosFetcher


from .fetchers import NUNSPortsFetcher


from .fetchers import NUSubnetsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUNSGateway(NURESTObject):
    """ Represents a NSGateway in the VSD

        Notes:
            Represents a Network Service Gateway.
    """

    __rest_name__ = "nsgateway"
    __resource_name__ = "nsgateways"

    
    ## Constants
    
    CONST_FAMILY_NSG_E = "NSG_E"
    
    CONST_INHERITED_SSH_SERVICE_STATE_ENABLED = "ENABLED"
    
    CONST_CONFIGURATION_STATUS_FAILURE = "FAILURE"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_FAMILY_NSG_V = "NSG_V"
    
    CONST_BOOTSTRAP_STATUS_ACTIVE = "ACTIVE"
    
    CONST_CONFIGURATION_RELOAD_STATE_PENDING = "PENDING"
    
    CONST_SSH_SERVICE_DISABLED = "DISABLED"
    
    CONST_PERSONALITY_OTHER = "OTHER"
    
    CONST_SSH_SERVICE_ENABLED = "ENABLED"
    
    CONST_BOOTSTRAP_STATUS_NOTIFICATION_APP_REQ_ACK = "NOTIFICATION_APP_REQ_ACK"
    
    CONST_PERSONALITY_NSG = "NSG"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_CONFIGURATION_STATUS_SUCCESS = "SUCCESS"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_CONFIGURATION_RELOAD_STATE_UNKNOWN = "UNKNOWN"
    
    CONST_PERSONALITY_DC7X50 = "DC7X50"
    
    CONST_BOOTSTRAP_STATUS_CERTIFICATE_SIGNED = "CERTIFICATE_SIGNED"
    
    CONST_FAMILY_ANY = "ANY"
    
    CONST_TPM_STATUS_DISABLED = "DISABLED"
    
    CONST_CONFIGURATION_RELOAD_STATE_APPLIED = "APPLIED"
    
    CONST_PERSONALITY_HARDWARE_VTEP = "HARDWARE_VTEP"
    
    CONST_PERSONALITY_VSA = "VSA"
    
    CONST_PERSONALITY_VSG = "VSG"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_TPM_STATUS_ENABLED_NOT_OPERATIONAL = "ENABLED_NOT_OPERATIONAL"
    
    CONST_TPM_STATUS_UNKNOWN = "UNKNOWN"
    
    CONST_PERSONALITY_VRSG = "VRSG"
    
    CONST_BOOTSTRAP_STATUS_NOTIFICATION_APP_REQ_SENT = "NOTIFICATION_APP_REQ_SENT"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_INHERITED_SSH_SERVICE_STATE_DISABLED = "DISABLED"
    
    CONST_TPM_STATUS_ENABLED_OPERATIONAL = "ENABLED_OPERATIONAL"
    
    CONST_SSH_SERVICE_INHERITED = "INHERITED"
    
    CONST_CONFIGURATION_STATUS_UNKNOWN = "UNKNOWN"
    
    CONST_CONFIGURATION_RELOAD_STATE_SENT = "SENT"
    
    CONST_BOOTSTRAP_STATUS_INACTIVE = "INACTIVE"
    
    CONST_PERSONALITY_NSGBR = "NSGBR"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NSGateway instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsgateway = NUNSGateway(id=u'xxxx-xxx-xxx-xxx', name=u'NSGateway')
                >>> nsgateway = NUNSGateway(data=my_dict)
        """

        super(NUNSGateway, self).__init__()

        # Read/Write Attributes
        
        self._mac_address = None
        self._nat_traversal_enabled = None
        self._sku = None
        self._tpm_status = None
        self._cpu_type = None
        self._nsg_version = None
        self._ssh_service = None
        self._uuid = None
        self._name = None
        self._family = None
        self._last_configuration_reload_timestamp = None
        self._last_updated_by = None
        self._datapath_id = None
        self._redundancy_group_id = None
        self._template_id = None
        self._pending = None
        self._serial_number = None
        self._permitted_action = None
        self._personality = None
        self._description = None
        self._libraries = None
        self._inherited_ssh_service_state = None
        self._enterprise_id = None
        self._entity_scope = None
        self._location_id = None
        self._configuration_reload_state = None
        self._configuration_status = None
        self._bootstrap_id = None
        self._bootstrap_status = None
        self._associated_gateway_security_id = None
        self._associated_gateway_security_profile_id = None
        self._associated_nsg_info_id = None
        self._auto_disc_gateway_id = None
        self._external_id = None
        self._system_id = None
        
        self.expose_attribute(local_name="mac_address", remote_name="MACAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nat_traversal_enabled", remote_name="NATTraversalEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sku", remote_name="SKU", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tpm_status", remote_name="TPMStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED_NOT_OPERATIONAL', u'ENABLED_OPERATIONAL', u'UNKNOWN'])
        self.expose_attribute(local_name="cpu_type", remote_name="CPUType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_version", remote_name="NSGVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ssh_service", remote_name="SSHService", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="uuid", remote_name="UUID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="family", remote_name="family", attribute_type=str, is_required=False, is_unique=False, choices=[u'ANY', u'NSG_E', u'NSG_V'])
        self.expose_attribute(local_name="last_configuration_reload_timestamp", remote_name="lastConfigurationReloadTimestamp", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="datapath_id", remote_name="datapathID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redundancy_group_id", remote_name="redundancyGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="pending", remote_name="pending", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="serial_number", remote_name="serialNumber", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=False, is_unique=False, choices=[u'DC7X50', u'HARDWARE_VTEP', u'NSG', u'NSGBR', u'OTHER', u'VRSG', u'VSA', u'VSG'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="libraries", remote_name="libraries", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="inherited_ssh_service_state", remote_name="inheritedSSHServiceState", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED'])
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="location_id", remote_name="locationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="configuration_reload_state", remote_name="configurationReloadState", attribute_type=str, is_required=False, is_unique=False, choices=[u'APPLIED', u'PENDING', u'SENT', u'UNKNOWN'])
        self.expose_attribute(local_name="configuration_status", remote_name="configurationStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'FAILURE', u'SUCCESS', u'UNKNOWN'])
        self.expose_attribute(local_name="bootstrap_id", remote_name="bootstrapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bootstrap_status", remote_name="bootstrapStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'ACTIVE', u'CERTIFICATE_SIGNED', u'INACTIVE', u'NOTIFICATION_APP_REQ_ACK', u'NOTIFICATION_APP_REQ_SENT'])
        self.expose_attribute(local_name="associated_gateway_security_id", remote_name="associatedGatewaySecurityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_gateway_security_profile_id", remote_name="associatedGatewaySecurityProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_nsg_info_id", remote_name="associatedNSGInfoID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="auto_disc_gateway_id", remote_name="autoDiscGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="system_id", remote_name="systemID", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.gateway_securities = NUGatewaySecuritiesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.patnat_pools = NUPATNATPoolsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.infrastructure_configs = NUInfrastructureConfigsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.locations = NULocationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.monitorscopes = NUMonitorscopesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bootstraps = NUBootstrapsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bootstrap_activations = NUBootstrapActivationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.nsg_infos = NUNSGInfosFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_ports = NUNSPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.subnets = NUSubnetsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def mac_address(self):
        """ Get mac_address value.

            Notes:
                MAC Address of the NSG

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        """ Set mac_address value.

            Notes:
                MAC Address of the NSG

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        self._mac_address = value

    
    @property
    def nat_traversal_enabled(self):
        """ Get nat_traversal_enabled value.

            Notes:
                This attribute is deprecated in version 4.0.

                
                This attribute is named `NATTraversalEnabled` in VSD API.
                
        """
        return self._nat_traversal_enabled

    @nat_traversal_enabled.setter
    def nat_traversal_enabled(self, value):
        """ Set nat_traversal_enabled value.

            Notes:
                This attribute is deprecated in version 4.0.

                
                This attribute is named `NATTraversalEnabled` in VSD API.
                
        """
        self._nat_traversal_enabled = value

    
    @property
    def sku(self):
        """ Get sku value.

            Notes:
                The part number of the NSG

                
                This attribute is named `SKU` in VSD API.
                
        """
        return self._sku

    @sku.setter
    def sku(self, value):
        """ Set sku value.

            Notes:
                The part number of the NSG

                
                This attribute is named `SKU` in VSD API.
                
        """
        self._sku = value

    
    @property
    def tpm_status(self):
        """ Get tpm_status value.

            Notes:
                TPM Status of the NSG based on the information received by the device during bootstrapping or upgrade.

                
                This attribute is named `TPMStatus` in VSD API.
                
        """
        return self._tpm_status

    @tpm_status.setter
    def tpm_status(self, value):
        """ Set tpm_status value.

            Notes:
                TPM Status of the NSG based on the information received by the device during bootstrapping or upgrade.

                
                This attribute is named `TPMStatus` in VSD API.
                
        """
        self._tpm_status = value

    
    @property
    def cpu_type(self):
        """ Get cpu_type value.

            Notes:
                The NSG Processor Type

                
                This attribute is named `CPUType` in VSD API.
                
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, value):
        """ Set cpu_type value.

            Notes:
                The NSG Processor Type

                
                This attribute is named `CPUType` in VSD API.
                
        """
        self._cpu_type = value

    
    @property
    def nsg_version(self):
        """ Get nsg_version value.

            Notes:
                The NSG Version

                
                This attribute is named `NSGVersion` in VSD API.
                
        """
        return self._nsg_version

    @nsg_version.setter
    def nsg_version(self, value):
        """ Set nsg_version value.

            Notes:
                The NSG Version

                
                This attribute is named `NSGVersion` in VSD API.
                
        """
        self._nsg_version = value

    
    @property
    def ssh_service(self):
        """ Get ssh_service value.

            Notes:
                Indicates if SSH Service is enabled/disabled on a NSG. The value configured for this attribute is used only when instanceSSHOverride is allowed on the associated Gateway Template.

                
                This attribute is named `SSHService` in VSD API.
                
        """
        return self._ssh_service

    @ssh_service.setter
    def ssh_service(self, value):
        """ Set ssh_service value.

            Notes:
                Indicates if SSH Service is enabled/disabled on a NSG. The value configured for this attribute is used only when instanceSSHOverride is allowed on the associated Gateway Template.

                
                This attribute is named `SSHService` in VSD API.
                
        """
        self._ssh_service = value

    
    @property
    def uuid(self):
        """ Get uuid value.

            Notes:
                The Redhat UUID of the NSG

                
                This attribute is named `UUID` in VSD API.
                
        """
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """ Set uuid value.

            Notes:
                The Redhat UUID of the NSG

                
                This attribute is named `UUID` in VSD API.
                
        """
        self._uuid = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Gateway

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Gateway

                
        """
        self._name = value

    
    @property
    def family(self):
        """ Get family value.

            Notes:
                The NSG Type

                
        """
        return self._family

    @family.setter
    def family(self, value):
        """ Set family value.

            Notes:
                The NSG Type

                
        """
        self._family = value

    
    @property
    def last_configuration_reload_timestamp(self):
        """ Get last_configuration_reload_timestamp value.

            Notes:
                Time stamp of the last known configuration update of the NSG.  This timestamp gets updated when a bootstrap is successful or when a configuration reload request triggered by VSD is successful.

                
                This attribute is named `lastConfigurationReloadTimestamp` in VSD API.
                
        """
        return self._last_configuration_reload_timestamp

    @last_configuration_reload_timestamp.setter
    def last_configuration_reload_timestamp(self, value):
        """ Set last_configuration_reload_timestamp value.

            Notes:
                Time stamp of the last known configuration update of the NSG.  This timestamp gets updated when a bootstrap is successful or when a configuration reload request triggered by VSD is successful.

                
                This attribute is named `lastConfigurationReloadTimestamp` in VSD API.
                
        """
        self._last_configuration_reload_timestamp = value

    
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
    def datapath_id(self):
        """ Get datapath_id value.

            Notes:
                Identifier of the Gateway, based on the systemId

                
                This attribute is named `datapathID` in VSD API.
                
        """
        return self._datapath_id

    @datapath_id.setter
    def datapath_id(self, value):
        """ Set datapath_id value.

            Notes:
                Identifier of the Gateway, based on the systemId

                
                This attribute is named `datapathID` in VSD API.
                
        """
        self._datapath_id = value

    
    @property
    def redundancy_group_id(self):
        """ Get redundancy_group_id value.

            Notes:
                The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute

                
                This attribute is named `redundancyGroupID` in VSD API.
                
        """
        return self._redundancy_group_id

    @redundancy_group_id.setter
    def redundancy_group_id(self, value):
        """ Set redundancy_group_id value.

            Notes:
                The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute

                
                This attribute is named `redundancyGroupID` in VSD API.
                
        """
        self._redundancy_group_id = value

    
    @property
    def template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    
    @property
    def pending(self):
        """ Get pending value.

            Notes:
                Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.

                
        """
        return self._pending

    @pending.setter
    def pending(self, value):
        """ Set pending value.

            Notes:
                Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.

                
        """
        self._pending = value

    
    @property
    def serial_number(self):
        """ Get serial_number value.

            Notes:
                The NSG's serial number

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        """ Set serial_number value.

            Notes:
                The NSG's serial number

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        self._serial_number = value

    
    @property
    def permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway.

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    @permitted_action.setter
    def permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway.

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    
    @property
    def personality(self):
        """ Get personality value.

            Notes:
                Personality of the Gateway - NSG, cannot be changed after creation.

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                Personality of the Gateway - NSG, cannot be changed after creation.

                
        """
        self._personality = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the Gateway

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the Gateway

                
        """
        self._description = value

    
    @property
    def libraries(self):
        """ Get libraries value.

            Notes:
                Transient representation of the same property on NSGInfo.

                
        """
        return self._libraries

    @libraries.setter
    def libraries(self, value):
        """ Set libraries value.

            Notes:
                Transient representation of the same property on NSGInfo.

                
        """
        self._libraries = value

    
    @property
    def inherited_ssh_service_state(self):
        """ Get inherited_ssh_service_state value.

            Notes:
                Indicates the SSH Service state which is configured on the associated template instance.

                
                This attribute is named `inheritedSSHServiceState` in VSD API.
                
        """
        return self._inherited_ssh_service_state

    @inherited_ssh_service_state.setter
    def inherited_ssh_service_state(self, value):
        """ Set inherited_ssh_service_state value.

            Notes:
                Indicates the SSH Service state which is configured on the associated template instance.

                
                This attribute is named `inheritedSSHServiceState` in VSD API.
                
        """
        self._inherited_ssh_service_state = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                The enterprise associated with this Gateway. This is a read only attribute

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                The enterprise associated with this Gateway. This is a read only attribute

                
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
    def location_id(self):
        """ Get location_id value.

            Notes:
                The NSGateway's Location. NOTE: this is a read only property, it can only be set through the location object

                
                This attribute is named `locationID` in VSD API.
                
        """
        return self._location_id

    @location_id.setter
    def location_id(self, value):
        """ Set location_id value.

            Notes:
                The NSGateway's Location. NOTE: this is a read only property, it can only be set through the location object

                
                This attribute is named `locationID` in VSD API.
                
        """
        self._location_id = value

    
    @property
    def configuration_reload_state(self):
        """ Get configuration_reload_state value.

            Notes:
                None

                
                This attribute is named `configurationReloadState` in VSD API.
                
        """
        return self._configuration_reload_state

    @configuration_reload_state.setter
    def configuration_reload_state(self, value):
        """ Set configuration_reload_state value.

            Notes:
                None

                
                This attribute is named `configurationReloadState` in VSD API.
                
        """
        self._configuration_reload_state = value

    
    @property
    def configuration_status(self):
        """ Get configuration_status value.

            Notes:
                None

                
                This attribute is named `configurationStatus` in VSD API.
                
        """
        return self._configuration_status

    @configuration_status.setter
    def configuration_status(self, value):
        """ Set configuration_status value.

            Notes:
                None

                
                This attribute is named `configurationStatus` in VSD API.
                
        """
        self._configuration_status = value

    
    @property
    def bootstrap_id(self):
        """ Get bootstrap_id value.

            Notes:
                The bootstrap details associated with this NSGateway. NOTE: this is a read only property, it can only be set during creation of an NSG

                
                This attribute is named `bootstrapID` in VSD API.
                
        """
        return self._bootstrap_id

    @bootstrap_id.setter
    def bootstrap_id(self, value):
        """ Set bootstrap_id value.

            Notes:
                The bootstrap details associated with this NSGateway. NOTE: this is a read only property, it can only be set during creation of an NSG

                
                This attribute is named `bootstrapID` in VSD API.
                
        """
        self._bootstrap_id = value

    
    @property
    def bootstrap_status(self):
        """ Get bootstrap_status value.

            Notes:
                The bootstrap status of this NSGateway. NOTE: this is a read only property

                
                This attribute is named `bootstrapStatus` in VSD API.
                
        """
        return self._bootstrap_status

    @bootstrap_status.setter
    def bootstrap_status(self, value):
        """ Set bootstrap_status value.

            Notes:
                The bootstrap status of this NSGateway. NOTE: this is a read only property

                
                This attribute is named `bootstrapStatus` in VSD API.
                
        """
        self._bootstrap_status = value

    
    @property
    def associated_gateway_security_id(self):
        """ Get associated_gateway_security_id value.

            Notes:
                Readonly Id of the associated gateway security object

                
                This attribute is named `associatedGatewaySecurityID` in VSD API.
                
        """
        return self._associated_gateway_security_id

    @associated_gateway_security_id.setter
    def associated_gateway_security_id(self, value):
        """ Set associated_gateway_security_id value.

            Notes:
                Readonly Id of the associated gateway security object

                
                This attribute is named `associatedGatewaySecurityID` in VSD API.
                
        """
        self._associated_gateway_security_id = value

    
    @property
    def associated_gateway_security_profile_id(self):
        """ Get associated_gateway_security_profile_id value.

            Notes:
                Readonly Id of the associated gateway security profile object

                
                This attribute is named `associatedGatewaySecurityProfileID` in VSD API.
                
        """
        return self._associated_gateway_security_profile_id

    @associated_gateway_security_profile_id.setter
    def associated_gateway_security_profile_id(self, value):
        """ Set associated_gateway_security_profile_id value.

            Notes:
                Readonly Id of the associated gateway security profile object

                
                This attribute is named `associatedGatewaySecurityProfileID` in VSD API.
                
        """
        self._associated_gateway_security_profile_id = value

    
    @property
    def associated_nsg_info_id(self):
        """ Get associated_nsg_info_id value.

            Notes:
                Readonly Id of the associated nsg info object

                
                This attribute is named `associatedNSGInfoID` in VSD API.
                
        """
        return self._associated_nsg_info_id

    @associated_nsg_info_id.setter
    def associated_nsg_info_id(self, value):
        """ Set associated_nsg_info_id value.

            Notes:
                Readonly Id of the associated nsg info object

                
                This attribute is named `associatedNSGInfoID` in VSD API.
                
        """
        self._associated_nsg_info_id = value

    
    @property
    def auto_disc_gateway_id(self):
        """ Get auto_disc_gateway_id value.

            Notes:
                The Auto Discovered Gateway associated with this Gateway Instance

                
                This attribute is named `autoDiscGatewayID` in VSD API.
                
        """
        return self._auto_disc_gateway_id

    @auto_disc_gateway_id.setter
    def auto_disc_gateway_id(self, value):
        """ Set auto_disc_gateway_id value.

            Notes:
                The Auto Discovered Gateway associated with this Gateway Instance

                
                This attribute is named `autoDiscGatewayID` in VSD API.
                
        """
        self._auto_disc_gateway_id = value

    
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
    def system_id(self):
        """ Get system_id value.

            Notes:
                Identifier of the Gateway, cannot be modified after creation

                
                This attribute is named `systemID` in VSD API.
                
        """
        return self._system_id

    @system_id.setter
    def system_id(self, value):
        """ Set system_id value.

            Notes:
                Identifier of the Gateway, cannot be modified after creation

                
                This attribute is named `systemID` in VSD API.
                
        """
        self._system_id = value

    

    
    ## Custom methods
    def is_template(self):
        """ Verify that the object is a template
    
            Returns:
                (bool): True if the object is a template
        """
        return False
    
    def is_from_template(self):
        """ Verify if the object has been instantiated from a template
    
            Note:
                The object has to be fetched. Otherwise, it does not
                have information from its parent
    
            Returns:
                (bool): True if the object is a template
        """
        return self.template_id
    