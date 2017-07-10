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



from .fetchers import NUAlarmsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUSSIDConnection(NURESTObject):
    """ Represents a SSIDConnection in the VSD

        Notes:
            An SSID Connection instance represents an SSID defined on a WiFi interface.  One SSID Connection is required per SSID created on a WiFi Card/Port.
    """

    __rest_name__ = "ssidconnection"
    __resource_name__ = "ssidconnections"

    
    ## Constants
    
    CONST_AUTHENTICATION_MODE_WEP = "WEP"
    
    CONST_AUTHENTICATION_MODE_WPA = "WPA"
    
    CONST_AUTHENTICATION_MODE_WPA_OTP = "WPA_OTP"
    
    CONST_AUTHENTICATION_MODE_OPEN = "OPEN"
    
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
        self._generic_config = None
        self._description = None
        self._white_list = None
        self._black_list = None
        self._interface_name = None
        self._broadcast_ssid = None
        self._associated_egress_qos_policy_id = None
        self._authentication_mode = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="passphrase", remote_name="passphrase", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="generic_config", remote_name="genericConfig", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="white_list", remote_name="whiteList", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="black_list", remote_name="blackList", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="interface_name", remote_name="interfaceName", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="broadcast_ssid", remote_name="broadcastSSID", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_egress_qos_policy_id", remote_name="associatedEgressQOSPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="authentication_mode", remote_name="authenticationMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'OPEN', u'WEP', u'WPA', u'WPA2', u'WPA_OTP', u'WPA_WPA2'])
        

        # Fetchers
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name associated to the SSID instance.  Has to be unique within an NSG.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name associated to the SSID instance.  Has to be unique within an NSG.

                
        """
        self._name = value

    
    @property
    def passphrase(self):
        """ Get passphrase value.

            Notes:
                Password or passphrase associated to an SSID instance.  Based on the authenticationMode selected.

                
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, value):
        """ Set passphrase value.

            Notes:
                Password or passphrase associated to an SSID instance.  Based on the authenticationMode selected.

                
        """
        self._passphrase = value

    
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

    

    