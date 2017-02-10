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


class NUVia(NURESTObject):
    """ Represents a Via in the VSD

        Notes:
            None
    """

    __rest_name__ = "via"
    __resource_name__ = "vias"

    

    def __init__(self, **kwargs):
        """ Initializes a Via instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> via = NUVia(id=u'xxxx-xxx-xxx-xxx', name=u'Via')
                >>> via = NUVia(data=my_dict)
        """

        super(NUVia, self).__init__()

        # Read/Write Attributes
        
        self._next_hops = None
        
        self.expose_attribute(local_name="next_hops", remote_name="nextHops", attribute_type=list, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def next_hops(self):
        """ Get next_hops value.

            Notes:
                A set of NextHop objects. A NextHop can be either an InetAddress (IPv4 or IPV6) address or a VLAN ID (for NSGBR)

                
                This attribute is named `nextHops` in VSD API.
                
        """
        return self._next_hops

    @next_hops.setter
    def next_hops(self, value):
        """ Set next_hops value.

            Notes:
                A set of NextHop objects. A NextHop can be either an InetAddress (IPv4 or IPV6) address or a VLAN ID (for NSGBR)

                
                This attribute is named `nextHops` in VSD API.
                
        """
        self._next_hops = value

    

    