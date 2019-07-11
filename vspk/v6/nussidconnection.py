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


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUSSIDConnection(NURESTObject):
    """ Represents a SSIDConnection in the VSD

        Notes:
            An SSID Connection instance represents an SSID defined on a WiFi interface. One SSID Connection is required per SSID created on a WiFi Card/Port.
    """

    __rest_name__ = "ssidconnection"
    __resource_name__ = "ssidconnections"

    
    ## Constants
    
    CONST_AUTHENTICATION_MODE_WEP = "WEP"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_REDIRECT_OPTION_CONFIGURED_URL = "CONFIGURED_URL"
    
    CONST_AUTHENTICATION_MODE_WPA = "WPA"
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_REDIRECT_OPTION_ORIGINAL_REQUEST = "ORIGINAL_REQUEST"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_AUTHENTICATION_MODE_CAPTIVE_PORTAL = "CAPTIVE_PORTAL"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_STATUS_INITIALIZED = "INITIALIZED"
    
    CONST_AUTHENTICATION_MODE_OPEN = "OPEN"
    
    CONST_STATUS_MISMATCH = "MISMATCH"
    
    CONST_STATUS_READY = "READY"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_STATUS_ORPHAN = "ORPHAN"
    
    CONST_AUTHENTICATION_MODE_WPA_OTP = "WPA_OTP"
    
    CONST_AUTHENTICATION_MODE_WPA_WPA2 = "WPA_WPA2"
    
    CONST_AUTHENTICATION_MODE_WPA2 = "WPA2"
    
    

    def __init__(self, **kwargs):
        """ Initializes a SSIDConnection instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ssidconnection = NUSSIDConnection(id=u'xxxx-xxx-xxx-xxx', name=u'SSIDConnection')
                >>> ssidconnection = NUSSIDConnection(data=my_dict)
        """

        super(NUSSIDConnection, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._passphrase = None
        self._last_updated_by = None
        self._gateway_id = None
        self._readonly = None
        self._redirect_option = None
        self._redirect_url = None
        self._generic_config = None
        self._permitted_action = None
        self._description = None
        self._restricted = None
        self._white_list = None
        self._black_list = None
        self._vlan_id = None
        self._embedded_metadata = None
        self._interface_name = None
        self._entity_scope = None
        self._vport_id = None
        self._broadcast_ssid = None
        self._associated_captive_portal_profile_id = None
        self._associated_egress_qos_policy_id = None
        self._status = None
        self._authentication_mode = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="passphrase", remote_name="passphrase", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_id", remote_name="gatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="readonly", remote_name="readonly", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redirect_option", remote_name="redirectOption", attribute_type=str, is_required=False, is_unique=False, choices=[u'CONFIGURED_URL', u'ORIGINAL_REQUEST'])
        self.expose_attribute(local_name="redirect_url", remote_name="redirectURL", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="generic_config", remote_name="genericConfig", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="restricted", remote_name="restricted", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="white_list", remote_name="whiteList", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="black_list", remote_name="blackList", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vlan_id", remote_name="vlanID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="interface_name", remote_name="interfaceName", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="vport_id", remote_name="vportID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="broadcast_ssid", remote_name="broadcastSSID", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_captive_portal_profile_id", remote_name="associatedCaptivePortalProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_egress_qos_policy_id", remote_name="associatedEgressQOSPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'INITIALIZED', u'MISMATCH', u'ORPHAN', u'READY'])
        self.expose_attribute(local_name="authentication_mode", remote_name="authenticationMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'CAPTIVE_PORTAL', u'OPEN', u'WEP', u'WPA', u'WPA2', u'WPA_OTP', u'WPA_WPA2'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name associated to the SSID instance. Has to be unique within an NSG.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name associated to the SSID instance. Has to be unique within an NSG.

                
        """
        self._name = value

    
    @property
    def passphrase(self):
        """ Get passphrase value.

            Notes:
                Password or passphrase associated to an SSID instance. Based on the authenticationMode selected.

                
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, value):
        """ Set passphrase value.

            Notes:
                Password or passphrase associated to an SSID instance. Based on the authenticationMode selected.

                
        """
        self._passphrase = value

    
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
    def gateway_id(self):
        """ Get gateway_id value.

            Notes:
                The Gateway (NSG) associated with this SSID. This is a read only attribute

                
                This attribute is named `gatewayID` in VSD API.
                
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, value):
        """ Set gateway_id value.

            Notes:
                The Gateway (NSG) associated with this SSID. This is a read only attribute

                
                This attribute is named `gatewayID` in VSD API.
                
        """
        self._gateway_id = value

    
    @property
    def readonly(self):
        """ Get readonly value.

            Notes:
                Determines whether this entity is read only. Read only objects cannot be modified or deleted.

                
        """
        return self._readonly

    @readonly.setter
    def readonly(self, value):
        """ Set readonly value.

            Notes:
                Determines whether this entity is read only. Read only objects cannot be modified or deleted.

                
        """
        self._readonly = value

    
    @property
    def redirect_option(self):
        """ Get redirect_option value.

            Notes:
                Redirection action to exercise once the connecting user has accepted the use policy presented on the Wireless Captive Portal.

                
                This attribute is named `redirectOption` in VSD API.
                
        """
        return self._redirect_option

    @redirect_option.setter
    def redirect_option(self, value):
        """ Set redirect_option value.

            Notes:
                Redirection action to exercise once the connecting user has accepted the use policy presented on the Wireless Captive Portal.

                
                This attribute is named `redirectOption` in VSD API.
                
        """
        self._redirect_option = value

    
    @property
    def redirect_url(self):
        """ Get redirect_url value.

            Notes:
                URL to have a newly connected user redirected to once the use policy defined on the Wireless Captive Portal has been accepted by the user.

                
                This attribute is named `redirectURL` in VSD API.
                
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        """ Set redirect_url value.

            Notes:
                URL to have a newly connected user redirected to once the use policy defined on the Wireless Captive Portal has been accepted by the user.

                
                This attribute is named `redirectURL` in VSD API.
                
        """
        self._redirect_url = value

    
    @property
    def generic_config(self):
        """ Get generic_config value.

            Notes:
                Blob type attribute that serves to define non-mandatory properties that can be defined in the WiFi Card configuration file.

                
                This attribute is named `genericConfig` in VSD API.
                
        """
        return self._generic_config

    @generic_config.setter
    def generic_config(self, value):
        """ Set generic_config value.

            Notes:
                Blob type attribute that serves to define non-mandatory properties that can be defined in the WiFi Card configuration file.

                
                This attribute is named `genericConfig` in VSD API.
                
        """
        self._generic_config = value

    
    @property
    def permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted action to USE/EXTEND this SSID Connection

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    @permitted_action.setter
    def permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted action to USE/EXTEND this SSID Connection

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Brief description of the SSID.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Brief description of the SSID.

                
        """
        self._description = value

    
    @property
    def restricted(self):
        """ Get restricted value.

            Notes:
                Determines whether this entity can be used in associations with other properties.

                
        """
        return self._restricted

    @restricted.setter
    def restricted(self, value):
        """ Set restricted value.

            Notes:
                Determines whether this entity can be used in associations with other properties.

                
        """
        self._restricted = value

    
    @property
    def white_list(self):
        """ Get white_list value.

            Notes:
                List of all white listed MAC Addresses for a particular SSID.

                
                This attribute is named `whiteList` in VSD API.
                
        """
        return self._white_list

    @white_list.setter
    def white_list(self, value):
        """ Set white_list value.

            Notes:
                List of all white listed MAC Addresses for a particular SSID.

                
                This attribute is named `whiteList` in VSD API.
                
        """
        self._white_list = value

    
    @property
    def black_list(self):
        """ Get black_list value.

            Notes:
                List of all the black listed MAC Addresses for a particular SSID.

                
                This attribute is named `blackList` in VSD API.
                
        """
        return self._black_list

    @black_list.setter
    def black_list(self, value):
        """ Set black_list value.

            Notes:
                List of all the black listed MAC Addresses for a particular SSID.

                
                This attribute is named `blackList` in VSD API.
                
        """
        self._black_list = value

    
    @property
    def vlan_id(self):
        """ Get vlan_id value.

            Notes:
                A VLAN representation of the SSID ordering on a Wireless Card/Port.

                
                This attribute is named `vlanID` in VSD API.
                
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, value):
        """ Set vlan_id value.

            Notes:
                A VLAN representation of the SSID ordering on a Wireless Card/Port.

                
                This attribute is named `vlanID` in VSD API.
                
        """
        self._vlan_id = value

    
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
    def interface_name(self):
        """ Get interface_name value.

            Notes:
                A read-only attribute that represents the generated interface name for the SSID connection to be provisioned on the NSG.

                
                This attribute is named `interfaceName` in VSD API.
                
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, value):
        """ Set interface_name value.

            Notes:
                A read-only attribute that represents the generated interface name for the SSID connection to be provisioned on the NSG.

                
                This attribute is named `interfaceName` in VSD API.
                
        """
        self._interface_name = value

    
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
    def vport_id(self):
        """ Get vport_id value.

            Notes:
                The Vport associated with this SSID connection. The attribute can't be modified directly from the SSID Connection.

                
                This attribute is named `vportID` in VSD API.
                
        """
        return self._vport_id

    @vport_id.setter
    def vport_id(self, value):
        """ Set vport_id value.

            Notes:
                The Vport associated with this SSID connection. The attribute can't be modified directly from the SSID Connection.

                
                This attribute is named `vportID` in VSD API.
                
        """
        self._vport_id = value

    
    @property
    def broadcast_ssid(self):
        """ Get broadcast_ssid value.

            Notes:
                Boolean that defines if the SSID name is to be broadcasted or not.

                
                This attribute is named `broadcastSSID` in VSD API.
                
        """
        return self._broadcast_ssid

    @broadcast_ssid.setter
    def broadcast_ssid(self, value):
        """ Set broadcast_ssid value.

            Notes:
                Boolean that defines if the SSID name is to be broadcasted or not.

                
                This attribute is named `broadcastSSID` in VSD API.
                
        """
        self._broadcast_ssid = value

    
    @property
    def associated_captive_portal_profile_id(self):
        """ Get associated_captive_portal_profile_id value.

            Notes:
                Identification of the Captive Portal Profile that is associated with this instance of SSID connection.

                
                This attribute is named `associatedCaptivePortalProfileID` in VSD API.
                
        """
        return self._associated_captive_portal_profile_id

    @associated_captive_portal_profile_id.setter
    def associated_captive_portal_profile_id(self, value):
        """ Set associated_captive_portal_profile_id value.

            Notes:
                Identification of the Captive Portal Profile that is associated with this instance of SSID connection.

                
                This attribute is named `associatedCaptivePortalProfileID` in VSD API.
                
        """
        self._associated_captive_portal_profile_id = value

    
    @property
    def associated_egress_qos_policy_id(self):
        """ Get associated_egress_qos_policy_id value.

            Notes:
                Identification of the Egress QoS policy that is associated with this instance of an SSID Connection.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        return self._associated_egress_qos_policy_id

    @associated_egress_qos_policy_id.setter
    def associated_egress_qos_policy_id(self, value):
        """ Set associated_egress_qos_policy_id value.

            Notes:
                Identification of the Egress QoS policy that is associated with this instance of an SSID Connection.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        self._associated_egress_qos_policy_id = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                Status of the SSID/VLAN. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                Status of the SSID/VLAN. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH

                
        """
        self._status = value

    
    @property
    def authentication_mode(self):
        """ Get authentication_mode value.

            Notes:
                Which mode of authentication is defined for a particular SSID Connection instance.

                
                This attribute is named `authenticationMode` in VSD API.
                
        """
        return self._authentication_mode

    @authentication_mode.setter
    def authentication_mode(self, value):
        """ Set authentication_mode value.

            Notes:
                Which mode of authentication is defined for a particular SSID Connection instance.

                
                This attribute is named `authenticationMode` in VSD API.
                
        """
        self._authentication_mode = value

    
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

    

    