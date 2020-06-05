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


class NUAllocationPool(NURESTObject):
    """ Represents a AllocationPool in the VSD

        Notes:
            IP Address range requested for a VM IP Reservation.
    """

    __rest_name__ = "None"
    __resource_name__ = "None"

    

    def __init__(self, **kwargs):
        """ Initializes a AllocationPool instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> allocationpool = NUAllocationPool(id=u'xxxx-xxx-xxx-xxx', name=u'AllocationPool')
                >>> allocationpool = NUAllocationPool(data=my_dict)
        """

        super(NUAllocationPool, self).__init__()

        # Read/Write Attributes
        
        self._max_address = None
        self._min_address = None
        
        self.expose_attribute(local_name="max_address", remote_name="maxAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="min_address", remote_name="minAddress", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def max_address(self):
        """ Get max_address value.

            Notes:
                End IPV4/IPV6 address.

                
                This attribute is named `maxAddress` in VSD API.
                
        """
        return self._max_address

    @max_address.setter
    def max_address(self, value):
        """ Set max_address value.

            Notes:
                End IPV4/IPV6 address.

                
                This attribute is named `maxAddress` in VSD API.
                
        """
        self._max_address = value

    
    @property
    def min_address(self):
        """ Get min_address value.

            Notes:
                Start IPV4/IPV6 address.

                
                This attribute is named `minAddress` in VSD API.
                
        """
        return self._min_address

    @min_address.setter
    def min_address(self, value):
        """ Set min_address value.

            Notes:
                Start IPV4/IPV6 address.

                
                This attribute is named `minAddress` in VSD API.
                
        """
        self._min_address = value

    

    