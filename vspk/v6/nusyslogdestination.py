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


class NUSyslogDestination(NURESTObject):
    """ Represents a SyslogDestination in the VSD

        Notes:
            Syslog Destination provides the definition for a Syslog Server Destination
    """

    __rest_name__ = "syslogdestination"
    __resource_name__ = "syslogdestinations"

    
    ## Constants
    
    CONST_IP_TYPE_IPV4 = "IPV4"
    
    CONST_TYPE_UDP = "UDP"
    
    

    def __init__(self, **kwargs):
        """ Initializes a SyslogDestination instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> syslogdestination = NUSyslogDestination(id=u'xxxx-xxx-xxx-xxx', name=u'SyslogDestination')
                >>> syslogdestination = NUSyslogDestination(data=my_dict)
        """

        super(NUSyslogDestination, self).__init__()

        # Read/Write Attributes
        
        self._ip_address = None
        self._ip_type = None
        self._name = None
        self._description = None
        self._port = None
        self._type = None
        
        self.expose_attribute(local_name="ip_address", remote_name="IPAddress", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="ip_type", remote_name="IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="port", remote_name="port", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=False, is_unique=False, choices=[u'UDP'])
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ip_address(self):
        """ Get ip_address value.

            Notes:
                The IP Address of the syslog server

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        """ Set ip_address value.

            Notes:
                The IP Address of the syslog server

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        self._ip_address = value

    
    @property
    def ip_type(self):
        """ Get ip_type value.

            Notes:
                IP Type of the syslog IP Address. Supported values: 'IPV4'

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        """ Set ip_type value.

            Notes:
                IP Type of the syslog IP Address. Supported values: 'IPV4'

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the syslog server

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the syslog server

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A detailed description of the syslog server

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A detailed description of the syslog server

                
        """
        self._description = value

    
    @property
    def port(self):
        """ Get port value.

            Notes:
                The port the syslog server is configured on

                
        """
        return self._port

    @port.setter
    def port(self, value):
        """ Set port value.

            Notes:
                The port the syslog server is configured on

                
        """
        self._port = value

    
    @property
    def type(self):
        """ Get type value.

            Notes:
                The protocol type of the syslog server. Supported values: 'UDP'

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                The protocol type of the syslog server. Supported values: 'UDP'

                
        """
        self._type = value

    

    