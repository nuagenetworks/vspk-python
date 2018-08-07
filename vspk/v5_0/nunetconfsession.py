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


class NUNetconfSession(NURESTObject):
    """ Represents a NetconfSession in the VSD

        Notes:
            Represents session between gateway and Netconf Manager, This can only be created by netconfmgr user
    """

    __rest_name__ = "netconfsession"
    __resource_name__ = "netconfsessions"

    
    ## Constants
    
    CONST_STATUS_DISCONNECTED = "DISCONNECTED"
    
    CONST_STATUS_CONNECTED = "CONNECTED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NetconfSession instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> netconfsession = NUNetconfSession(id=u'xxxx-xxx-xxx-xxx', name=u'NetconfSession')
                >>> netconfsession = NUNetconfSession(data=my_dict)
        """

        super(NUNetconfSession, self).__init__()

        # Read/Write Attributes
        
        self._associated_gateway_id = None
        self._associated_gateway_name = None
        self._status = None
        
        self.expose_attribute(local_name="associated_gateway_id", remote_name="associatedGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_gateway_name", remote_name="associatedGatewayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'CONNECTED', u'DISCONNECTED'])
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def associated_gateway_id(self):
        """ Get associated_gateway_id value.

            Notes:
                UUID of the gateway associated to this Netconf session.

                
                This attribute is named `associatedGatewayID` in VSD API.
                
        """
        return self._associated_gateway_id

    @associated_gateway_id.setter
    def associated_gateway_id(self, value):
        """ Set associated_gateway_id value.

            Notes:
                UUID of the gateway associated to this Netconf session.

                
                This attribute is named `associatedGatewayID` in VSD API.
                
        """
        self._associated_gateway_id = value

    
    @property
    def associated_gateway_name(self):
        """ Get associated_gateway_name value.

            Notes:
                Name of the gateway associated to this Netconf session.

                
                This attribute is named `associatedGatewayName` in VSD API.
                
        """
        return self._associated_gateway_name

    @associated_gateway_name.setter
    def associated_gateway_name(self, value):
        """ Set associated_gateway_name value.

            Notes:
                Name of the gateway associated to this Netconf session.

                
                This attribute is named `associatedGatewayName` in VSD API.
                
        """
        self._associated_gateway_name = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                The status of the NetConf session to a gateway.

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                The status of the NetConf session to a gateway.

                
        """
        self._status = value

    

    