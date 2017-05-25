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



from .fetchers import NUPSPATMapsFetcher


from .fetchers import NUPTranslationMapsFetcher

from bambou import NURESTObject


class NUPSNATPool(NURESTObject):
    """ Represents a PSNATPool in the VSD

        Notes:
            Provider alias IP range to map provider private IPs from provider domain to provider public IPs in the customer domain.
    """

    __rest_name__ = "psnatpool"
    __resource_name__ = "psnatpools"

    

    def __init__(self, **kwargs):
        """ Initializes a PSNATPool instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> psnatpool = NUPSNATPool(id=u'xxxx-xxx-xxx-xxx', name=u'PSNATPool')
                >>> psnatpool = NUPSNATPool(data=my_dict)
        """

        super(NUPSNATPool, self).__init__()

        # Read/Write Attributes
        
        self._end_address = None
        self._start_address = None
        
        self.expose_attribute(local_name="end_address", remote_name="endAddress", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="start_address", remote_name="startAddress", attribute_type=str, is_required=True, is_unique=False)
        

        # Fetchers
        
        
        self.pspat_maps = NUPSPATMapsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.p_translation_maps = NUPTranslationMapsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def end_address(self):
        """ Get end_address value.

            Notes:
                The last IP address in the range.

                
                This attribute is named `endAddress` in VSD API.
                
        """
        return self._end_address

    @end_address.setter
    def end_address(self, value):
        """ Set end_address value.

            Notes:
                The last IP address in the range.

                
                This attribute is named `endAddress` in VSD API.
                
        """
        self._end_address = value

    
    @property
    def start_address(self):
        """ Get start_address value.

            Notes:
                The first IP address in the range.

                
                This attribute is named `startAddress` in VSD API.
                
        """
        return self._start_address

    @start_address.setter
    def start_address(self, value):
        """ Set start_address value.

            Notes:
                The first IP address in the range.

                
                This attribute is named `startAddress` in VSD API.
                
        """
        self._start_address = value

    

    