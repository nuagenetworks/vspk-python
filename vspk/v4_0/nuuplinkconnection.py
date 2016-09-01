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


from bambou import NURESTObject


class NUUplinkConnection(NURESTObject):
    """ Represents a UplinkConnection in the VSD

        Notes:
            None
    """

    __rest_name__ = "uplinkconnection"
    __resource_name__ = "uplinkconnections"

    
    ## Constants
    
    CONST_ROLE_UNKNOWN = "UNKNOWN"
    
    CONST_ROLE_SECONDARY = "SECONDARY"
    
    CONST_MODE_PPPOE = "PPPoE"
    
    CONST_MODE_DYNAMIC = "Dynamic"
    
    CONST_ROLE_TERTIARY = "TERTIARY"
    
    CONST_MODE_ANY = "Any"
    
    CONST_MODE_STATIC = "Static"
    
    CONST_ADDRESS_IPV4 = "IPv4"
    
    CONST_ROLE_PRIMARY = "PRIMARY"
    
    CONST_ADDRESS_IPV6 = "IPv6"
    
    

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
        self._address = None
        self._netmask = None
        self._mode = None
        self._role = None
        self._username = None
        self._associated_vsc_profile_id = None
        
        self.expose_attribute(local_name="dns_address", remote_name="DNSAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="password", remote_name="password", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPv4', u'IPv6'])
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mode", remote_name="mode", attribute_type=str, is_required=False, is_unique=False, choices=[u'Any', u'Dynamic', u'PPPoE', u'Static'])
        self.expose_attribute(local_name="role", remote_name="role", attribute_type=str, is_required=False, is_unique=False, choices=[u'PRIMARY', u'SECONDARY', u'TERTIARY', u'UNKNOWN'])
        self.expose_attribute(local_name="username", remote_name="username", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_vsc_profile_id", remote_name="associatedVSCProfileID", attribute_type=str, is_required=False, is_unique=False)
        

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
    def mode(self):
        """ Get mode value.

            Notes:
                Specify how to connect to the network. Possible values: Any, Dynamic (DHCP), Static (static configuration is required), PPPoE (pppoe configuration required). Default: Dynamic

                
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        """ Set mode value.

            Notes:
                Specify how to connect to the network. Possible values: Any, Dynamic (DHCP), Static (static configuration is required), PPPoE (pppoe configuration required). Default: Dynamic

                
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

    

    