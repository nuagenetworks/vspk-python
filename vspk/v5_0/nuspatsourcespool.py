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


class NUSPATSourcesPool(NURESTObject):
    """ Represents a SPATSourcesPool in the VSD

        Notes:
            The list of source IPs from the provider domain to be SPATed.
    """

    __rest_name__ = "spatsourcespool"
    __resource_name__ = "spatsourcespools"

    
    ## Constants
    
    CONST_FAMILY_IPV4 = "IPV4"
    
    

    def __init__(self, **kwargs):
        """ Initializes a SPATSourcesPool instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> spatsourcespool = NUSPATSourcesPool(id=u'xxxx-xxx-xxx-xxx', name=u'SPATSourcesPool')
                >>> spatsourcespool = NUSPATSourcesPool(data=my_dict)
        """

        super(NUSPATSourcesPool, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._family = None
        self._address_list = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="family", remote_name="family", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4'])
        self.expose_attribute(local_name="address_list", remote_name="addressList", attribute_type=list, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name for this address pool

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name for this address pool

                
        """
        self._name = value

    
    @property
    def family(self):
        """ Get family value.

            Notes:
                The IP address family. Supported IPV4 for the time being.

                
        """
        return self._family

    @family.setter
    def family(self, value):
        """ Set family value.

            Notes:
                The IP address family. Supported IPV4 for the time being.

                
        """
        self._family = value

    
    @property
    def address_list(self):
        """ Get address_list value.

            Notes:
                The collection of IP addresses that will SPATed in the customer domain.

                
                This attribute is named `addressList` in VSD API.
                
        """
        return self._address_list

    @address_list.setter
    def address_list(self, value):
        """ Set address_list value.

            Notes:
                The collection of IP addresses that will SPATed in the customer domain.

                
                This attribute is named `addressList` in VSD API.
                
        """
        self._address_list = value

    

    