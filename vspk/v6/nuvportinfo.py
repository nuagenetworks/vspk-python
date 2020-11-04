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


class NUVPortInfo(NURESTObject):
    """ Represents a VPortInfo in the VSD

        Notes:
            Represents the vport status info at individual gateway for ethernet segment group
    """

    __rest_name__ = "None"
    __resource_name__ = "None"

    
    ## Constants
    
    CONST_V_PORT_OPERATIONAL_STATE_UP = "UP"
    
    CONST_V_PORT_OPERATIONAL_STATE_DOWN = "DOWN"
    
    CONST_V_PORT_OPERATIONAL_STATE_DEGRADED = "DEGRADED"
    
    CONST_V_PORT_OPERATIONAL_STATE_INIT = "INIT"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VPortInfo instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vportinfo = NUVPortInfo(id=u'xxxx-xxx-xxx-xxx', name=u'VPortInfo')
                >>> vportinfo = NUVPortInfo(data=my_dict)
        """

        super(NUVPortInfo, self).__init__()

        # Read/Write Attributes
        
        self._v_port_operational_state = None
        self._gateway_id = None
        self._gateway_name = None
        
        self.expose_attribute(local_name="v_port_operational_state", remote_name="vPortOperationalState", attribute_type=str, is_required=False, is_unique=False, choices=[u'DEGRADED', u'DOWN', u'INIT', u'UP'])
        self.expose_attribute(local_name="gateway_id", remote_name="gatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_name", remote_name="gatewayName", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def v_port_operational_state(self):
        """ Get v_port_operational_state value.

            Notes:
                VPort operational state at this Gateway

                
                This attribute is named `vPortOperationalState` in VSD API.
                
        """
        return self._v_port_operational_state

    @v_port_operational_state.setter
    def v_port_operational_state(self, value):
        """ Set v_port_operational_state value.

            Notes:
                VPort operational state at this Gateway

                
                This attribute is named `vPortOperationalState` in VSD API.
                
        """
        self._v_port_operational_state = value

    
    @property
    def gateway_id(self):
        """ Get gateway_id value.

            Notes:
                UUID of the Gateway

                
                This attribute is named `gatewayID` in VSD API.
                
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, value):
        """ Set gateway_id value.

            Notes:
                UUID of the Gateway

                
                This attribute is named `gatewayID` in VSD API.
                
        """
        self._gateway_id = value

    
    @property
    def gateway_name(self):
        """ Get gateway_name value.

            Notes:
                Name of the Gateway

                
                This attribute is named `gatewayName` in VSD API.
                
        """
        return self._gateway_name

    @gateway_name.setter
    def gateway_name(self, value):
        """ Set gateway_name value.

            Notes:
                Name of the Gateway

                
                This attribute is named `gatewayName` in VSD API.
                
        """
        self._gateway_name = value

    

    