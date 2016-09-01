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


class NUDemarcationService(NURESTObject):
    """ Represents a DemarcationService in the VSD

        Notes:
            None
    """

    __rest_name__ = "demarcationservice"
    __resource_name__ = "demarcationservices"

    
    ## Constants
    
    CONST_TYPE_BR_PORT = "BR_PORT"
    
    CONST_TYPE_GATEWAY = "GATEWAY"
    
    

    def __init__(self, **kwargs):
        """ Initializes a DemarcationService instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> demarcationservice = NUDemarcationService(id=u'xxxx-xxx-xxx-xxx', name=u'DemarcationService')
                >>> demarcationservice = NUDemarcationService(data=my_dict)
        """

        super(NUDemarcationService, self).__init__()

        # Read/Write Attributes
        
        self._route_distinguisher = None
        self._priority = None
        self._associated_gateway_id = None
        self._associated_vlanid = None
        self._type = None
        
        self.expose_attribute(local_name="route_distinguisher", remote_name="routeDistinguisher", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_gateway_id", remote_name="associatedGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_vlanid", remote_name="associatedVLANID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=False, is_unique=False, choices=[u'BR_PORT', u'GATEWAY'])
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def route_distinguisher(self):
        """ Get route_distinguisher value.

            Notes:
                The route distinguisher associated with the next hop. This is a read only property automatically created by VSD.

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        return self._route_distinguisher

    @route_distinguisher.setter
    def route_distinguisher(self, value):
        """ Set route_distinguisher value.

            Notes:
                The route distinguisher associated with the next hop. This is a read only property automatically created by VSD.

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        self._route_distinguisher = value

    
    @property
    def priority(self):
        """ Get priority value.

            Notes:
                Next hop priority assigned by the user.

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                Next hop priority assigned by the user.

                
        """
        self._priority = value

    
    @property
    def associated_gateway_id(self):
        """ Get associated_gateway_id value.

            Notes:
                The ID of the NSGBR Gateway used as next hop in the untrusted domain.

                
                This attribute is named `associatedGatewayID` in VSD API.
                
        """
        return self._associated_gateway_id

    @associated_gateway_id.setter
    def associated_gateway_id(self, value):
        """ Set associated_gateway_id value.

            Notes:
                The ID of the NSGBR Gateway used as next hop in the untrusted domain.

                
                This attribute is named `associatedGatewayID` in VSD API.
                
        """
        self._associated_gateway_id = value

    
    @property
    def associated_vlanid(self):
        """ Get associated_vlanid value.

            Notes:
                The VLAN ID of the BR VLAN used as next hop in the trusted domain.

                
                This attribute is named `associatedVLANID` in VSD API.
                
        """
        return self._associated_vlanid

    @associated_vlanid.setter
    def associated_vlanid(self, value):
        """ Set associated_vlanid value.

            Notes:
                The VLAN ID of the BR VLAN used as next hop in the trusted domain.

                
                This attribute is named `associatedVLANID` in VSD API.
                
        """
        self._associated_vlanid = value

    
    @property
    def type(self):
        """ Get type value.

            Notes:
                The type of next hop determines linking direction for a demarcation service, possible values: BR_PORT, GATEWAY 

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                The type of next hop determines linking direction for a demarcation service, possible values: BR_PORT, GATEWAY 

                
        """
        self._type = value

    

    