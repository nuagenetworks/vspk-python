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



from .fetchers import NUBFDSessionsFetcher


from .fetchers import NUUnderlaysFetcher


from .fetchers import NUCustomPropertiesFetcher

from bambou import NURESTObject


class NUUplinkConnection(NURESTObject):
    """ Represents a UplinkConnection in the VSD

        Notes:
            None
    """

    __rest_name__ = "uplinkconnection"
    __resource_name__ = "uplinkconnections"

    
    ## Constants
    
    CONST_INTERFACE_CONNECTION_TYPE_AUTOMATIC = "AUTOMATIC"
    
    CONST_ADVERTISEMENT_CRITERIA_BFD = "BFD"
    
    CONST_ROLE_UNKNOWN = "UNKNOWN"
    
    CONST_INTERFACE_CONNECTION_TYPE_PCI_EXPRESS = "PCI_EXPRESS"
    
    CONST_ROLE_NONE = "NONE"
    
    CONST_ROLE_SECONDARY = "SECONDARY"
    
    CONST_INTERFACE_CONNECTION_TYPE_EMBEDDED = "EMBEDDED"
    
    CONST_ADVERTISEMENT_CRITERIA_OPERATIONAL_LINK = "OPERATIONAL_LINK"
    
    CONST_INTERFACE_CONNECTION_TYPE_USB_MODEM = "USB_MODEM"
    
    CONST_MODE_PPPOE = "PPPoE"
    
    CONST_MODE_DYNAMIC = "Dynamic"
    
    CONST_MODE_LTE = "LTE"
    
    CONST_ROLE_TERTIARY = "TERTIARY"
    
    CONST_MODE_ANY = "Any"
    
    CONST_ADVERTISEMENT_CRITERIA_CONTROL_SESSION = "CONTROL_SESSION"
    
    CONST_MODE_STATIC = "Static"
    
    CONST_ADDRESS_IPV4 = "IPv4"
    
    CONST_INTERFACE_CONNECTION_TYPE_USB_ETHERNET = "USB_ETHERNET"
    
    CONST_ADDRESS_IPV6 = "IPv6"
    
    CONST_ROLE_PRIMARY = "PRIMARY"
    
    

    def __init__(self, **kwargs):
        """ Initializes a UplinkConnection instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> uplinkconnection = NUUplinkConnection(id=u'xxxx-xxx-xxx-xxx', name=u'UplinkConnection')
                >>> uplinkconnection = NUUplinkConnection(data=my_dict)
        """

        super(NUUplinkConnection, self).__init__()

        # Read/Write Attributes
        
        self._dns_address = None
        self._password = None
        self._gateway = None
        self._address = None
        self._advertisement_criteria = None
        self._netmask = None
        self._interface_connection_type = None
        self._mode = None
        self._role = None
        self._uplink_id = None
        self._username = None
        self._assoc_underlay_id = None
        self._associated_underlay_name = None
        self._associated_vsc_profile_id = None
        self._auxiliary_link = None
        
        self.expose_attribute(local_name="dns_address", remote_name="DNSAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="password", remote_name="password", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway", remote_name="gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPv4', u'IPv6'])
        self.expose_attribute(local_name="advertisement_criteria", remote_name="advertisementCriteria", attribute_type=str, is_required=False, is_unique=False, choices=[u'BFD', u'CONTROL_SESSION', u'OPERATIONAL_LINK'])
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="interface_connection_type", remote_name="interfaceConnectionType", attribute_type=str, is_required=False, is_unique=False, choices=[u'AUTOMATIC', u'EMBEDDED', u'PCI_EXPRESS', u'USB_ETHERNET', u'USB_MODEM'])
        self.expose_attribute(local_name="mode", remote_name="mode", attribute_type=str, is_required=False, is_unique=False, choices=[u'Any', u'Dynamic', u'LTE', u'PPPoE', u'Static'])
        self.expose_attribute(local_name="role", remote_name="role", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'PRIMARY', u'SECONDARY', u'TERTIARY', u'UNKNOWN'])
        self.expose_attribute(local_name="uplink_id", remote_name="uplinkID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="username", remote_name="username", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="assoc_underlay_id", remote_name="assocUnderlayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_underlay_name", remote_name="associatedUnderlayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_vsc_profile_id", remote_name="associatedVSCProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="auxiliary_link", remote_name="auxiliaryLink", attribute_type=bool, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.bfd_sessions = NUBFDSessionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.underlays = NUUnderlaysFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.custom_properties = NUCustomPropertiesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def dns_address(self):
        """ Get dns_address value.

            Notes:
                DNS server address

                
                This attribute is named `DNSAddress` in VSD API.
                
        """
        return self._dns_address

    @dns_address.setter
    def dns_address(self, value):
        """ Set dns_address value.

            Notes:
                DNS server address

                
                This attribute is named `DNSAddress` in VSD API.
                
        """
        self._dns_address = value

    
    @property
    def password(self):
        """ Get password value.

            Notes:
                PPPoE password.

                
        """
        return self._password

    @password.setter
    def password(self, value):
        """ Set password value.

            Notes:
                PPPoE password.

                
        """
        self._password = value

    
    @property
    def gateway(self):
        """ Get gateway value.

            Notes:
                IP address of the gateway bound to the port

                
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """ Set gateway value.

            Notes:
                IP address of the gateway bound to the port

                
        """
        self._gateway = value

    
    @property
    def address(self):
        """ Get address value.

            Notes:
                IP address for static configuration

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                IP address for static configuration

                
        """
        self._address = value

    
    @property
    def advertisement_criteria(self):
        """ Get advertisement_criteria value.

            Notes:
                Advertisement Criteria for Traffic Flow

                
                This attribute is named `advertisementCriteria` in VSD API.
                
        """
        return self._advertisement_criteria

    @advertisement_criteria.setter
    def advertisement_criteria(self, value):
        """ Set advertisement_criteria value.

            Notes:
                Advertisement Criteria for Traffic Flow

                
                This attribute is named `advertisementCriteria` in VSD API.
                
        """
        self._advertisement_criteria = value

    
    @property
    def netmask(self):
        """ Get netmask value.

            Notes:
                Subnet mask

                
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """ Set netmask value.

            Notes:
                Subnet mask

                
        """
        self._netmask = value

    
    @property
    def interface_connection_type(self):
        """ Get interface_connection_type value.

            Notes:
                The way the interface is connected via the NSG.  This value depends on if the interface internal or external to the NSG.

                
                This attribute is named `interfaceConnectionType` in VSD API.
                
        """
        return self._interface_connection_type

    @interface_connection_type.setter
    def interface_connection_type(self, value):
        """ Set interface_connection_type value.

            Notes:
                The way the interface is connected via the NSG.  This value depends on if the interface internal or external to the NSG.

                
                This attribute is named `interfaceConnectionType` in VSD API.
                
        """
        self._interface_connection_type = value

    
    @property
    def mode(self):
        """ Get mode value.

            Notes:
                Specify how to connect to the network. Possible values: Any, Dynamic (DHCP), Static (static configuration is required), PPPoE (pppoe configuration required), LTE (LTE configuration required). Default: Dynamic

                
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        """ Set mode value.

            Notes:
                Specify how to connect to the network. Possible values: Any, Dynamic (DHCP), Static (static configuration is required), PPPoE (pppoe configuration required), LTE (LTE configuration required). Default: Dynamic

                
        """
        self._mode = value

    
    @property
    def role(self):
        """ Get role value.

            Notes:
                To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, 

                
        """
        return self._role

    @role.setter
    def role(self, value):
        """ Set role value.

            Notes:
                To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, 

                
        """
        self._role = value

    
    @property
    def uplink_id(self):
        """ Get uplink_id value.

            Notes:
                ID that unqiuely identifies the uplink. 

                
                This attribute is named `uplinkID` in VSD API.
                
        """
        return self._uplink_id

    @uplink_id.setter
    def uplink_id(self, value):
        """ Set uplink_id value.

            Notes:
                ID that unqiuely identifies the uplink. 

                
                This attribute is named `uplinkID` in VSD API.
                
        """
        self._uplink_id = value

    
    @property
    def username(self):
        """ Get username value.

            Notes:
                PPPoE username

                
        """
        return self._username

    @username.setter
    def username(self, value):
        """ Set username value.

            Notes:
                PPPoE username

                
        """
        self._username = value

    
    @property
    def assoc_underlay_id(self):
        """ Get assoc_underlay_id value.

            Notes:
                UUID of the underlay associated to the uplink.

                
                This attribute is named `assocUnderlayID` in VSD API.
                
        """
        return self._assoc_underlay_id

    @assoc_underlay_id.setter
    def assoc_underlay_id(self, value):
        """ Set assoc_underlay_id value.

            Notes:
                UUID of the underlay associated to the uplink.

                
                This attribute is named `assocUnderlayID` in VSD API.
                
        """
        self._assoc_underlay_id = value

    
    @property
    def associated_underlay_name(self):
        """ Get associated_underlay_name value.

            Notes:
                The display name of the Underlay instance associated with this uplink connection.

                
                This attribute is named `associatedUnderlayName` in VSD API.
                
        """
        return self._associated_underlay_name

    @associated_underlay_name.setter
    def associated_underlay_name(self, value):
        """ Set associated_underlay_name value.

            Notes:
                The display name of the Underlay instance associated with this uplink connection.

                
                This attribute is named `associatedUnderlayName` in VSD API.
                
        """
        self._associated_underlay_name = value

    
    @property
    def associated_vsc_profile_id(self):
        """ Get associated_vsc_profile_id value.

            Notes:
                The ID of the infrastructure VSC profile this is associated with this instance of a vlan or vlan template.

                
                This attribute is named `associatedVSCProfileID` in VSD API.
                
        """
        return self._associated_vsc_profile_id

    @associated_vsc_profile_id.setter
    def associated_vsc_profile_id(self, value):
        """ Set associated_vsc_profile_id value.

            Notes:
                The ID of the infrastructure VSC profile this is associated with this instance of a vlan or vlan template.

                
                This attribute is named `associatedVSCProfileID` in VSD API.
                
        """
        self._associated_vsc_profile_id = value

    
    @property
    def auxiliary_link(self):
        """ Get auxiliary_link value.

            Notes:
                Make this uplink an auxiliary one that will only come up when all other uplinks are disconnected or can't perform their role.

                
                This attribute is named `auxiliaryLink` in VSD API.
                
        """
        return self._auxiliary_link

    @auxiliary_link.setter
    def auxiliary_link(self, value):
        """ Set auxiliary_link value.

            Notes:
                Make this uplink an auxiliary one that will only come up when all other uplinks are disconnected or can't perform their role.

                
                This attribute is named `auxiliaryLink` in VSD API.
                
        """
        self._auxiliary_link = value

    

    