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


class NUNSPortInfo(NURESTObject):
    """ Represents a NSPortInfo in the VSD

        Notes:
            This API provides a list of monitoring ports and a list of configured ports for a NSG
    """

    __rest_name__ = "portinfo"
    __resource_name__ = "portinfos"

    

    def __init__(self, **kwargs):
        """ Initializes a NSPortInfo instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsportinfo = NUNSPortInfo(id=u'xxxx-xxx-xxx-xxx', name=u'NSPortInfo')
                >>> nsportinfo = NUNSPortInfo(data=my_dict)
        """

        super(NUNSPortInfo, self).__init__()

        # Read/Write Attributes
        
        self._wireless_ports = None
        self._monitoring_ports = None
        self._ports = None
        
        self.expose_attribute(local_name="wireless_ports", remote_name="wirelessPorts", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="monitoring_ports", remote_name="monitoringPorts", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ports", remote_name="ports", attribute_type=list, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def wireless_ports(self):
        """ Get wireless_ports value.

            Notes:
                List of configured wireless ports for the gateway

                
                This attribute is named `wirelessPorts` in VSD API.
                
        """
        return self._wireless_ports

    @wireless_ports.setter
    def wireless_ports(self, value):
        """ Set wireless_ports value.

            Notes:
                List of configured wireless ports for the gateway

                
                This attribute is named `wirelessPorts` in VSD API.
                
        """
        self._wireless_ports = value

    
    @property
    def monitoring_ports(self):
        """ Get monitoring_ports value.

            Notes:
                List of monitoring ports for the gateway

                
                This attribute is named `monitoringPorts` in VSD API.
                
        """
        return self._monitoring_ports

    @monitoring_ports.setter
    def monitoring_ports(self, value):
        """ Set monitoring_ports value.

            Notes:
                List of monitoring ports for the gateway

                
                This attribute is named `monitoringPorts` in VSD API.
                
        """
        self._monitoring_ports = value

    
    @property
    def ports(self):
        """ Get ports value.

            Notes:
                List of configured ports for the gateway

                
        """
        return self._ports

    @ports.setter
    def ports(self, value):
        """ Set ports value.

            Notes:
                List of configured ports for the gateway

                
        """
        self._ports = value

    

    