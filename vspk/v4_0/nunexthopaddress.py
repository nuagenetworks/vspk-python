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


class NUNextHopAddress(NURESTObject):
    """ Represents a NextHopAddress in the VSD

        Notes:
            None
    """

    __rest_name__ = "nexthopaddress"
    __resource_name__ = "nexthopaddress"

    

    def __init__(self, **kwargs):
        """ Initializes a NextHopAddress instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nexthopaddress = NUNextHopAddress(id=u'xxxx-xxx-xxx-xxx', name=u'NextHopAddress')
                >>> nexthopaddress = NUNextHopAddress(data=my_dict)
        """

        super(NUNextHopAddress, self).__init__()

        # Read/Write Attributes
        
        self._address = None
        self._route_distinguisher = None
        self._type = None
        
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="route_distinguisher", remote_name="routeDistinguisher", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def address(self):
        """ Get address value.

            Notes:
                IP address for the next hop.

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                IP address for the next hop.

                
        """
        self._address = value

    
    @property
    def route_distinguisher(self):
        """ Get route_distinguisher value.

            Notes:
                A unique route distinguisher associated with the nexthop. If one is not provided the system generated one automatically. 

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        return self._route_distinguisher

    @route_distinguisher.setter
    def route_distinguisher(self, value):
        """ Set route_distinguisher value.

            Notes:
                A unique route distinguisher associated with the nexthop. If one is not provided the system generated one automatically. 

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        self._route_distinguisher = value

    
    @property
    def type(self):
        """ Get type value.

            Notes:
                Next hop type: IP only supported for service chaining

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                Next hop type: IP only supported for service chaining

                
        """
        self._type = value

    

    