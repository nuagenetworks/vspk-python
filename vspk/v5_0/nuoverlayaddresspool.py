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



from .fetchers import NUOverlayPATNATEntriesFetcher

from bambou import NURESTObject


class NUOverlayAddressPool(NURESTObject):
    """ Represents a OverlayAddressPool in the VSD

        Notes:
            The address pool the public IP of the PAT/NAT entries belong too.
    """

    __rest_name__ = "overlayaddresspool"
    __resource_name__ = "overlayaddresspools"

    

    def __init__(self, **kwargs):
        """ Initializes a OverlayAddressPool instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> overlayaddresspool = NUOverlayAddressPool(id=u'xxxx-xxx-xxx-xxx', name=u'OverlayAddressPool')
                >>> overlayaddresspool = NUOverlayAddressPool(data=my_dict)
        """

        super(NUOverlayAddressPool, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._description = None
        self._end_address_range = None
        self._associated_domain_id = None
        self._start_address_range = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="end_address_range", remote_name="endAddressRange", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_domain_id", remote_name="associatedDomainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="start_address_range", remote_name="startAddressRange", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.overlay_patnat_entries = NUOverlayPATNATEntriesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name for the PAT NAT pool

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name for the PAT NAT pool

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                addresspool description

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                addresspool description

                
        """
        self._description = value

    
    @property
    def end_address_range(self):
        """ Get end_address_range value.

            Notes:
                The end address for the pool range.

                
                This attribute is named `endAddressRange` in VSD API.
                
        """
        return self._end_address_range

    @end_address_range.setter
    def end_address_range(self, value):
        """ Set end_address_range value.

            Notes:
                The end address for the pool range.

                
                This attribute is named `endAddressRange` in VSD API.
                
        """
        self._end_address_range = value

    
    @property
    def associated_domain_id(self):
        """ Get associated_domain_id value.

            Notes:
                The ID of the associated l3-domain.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        return self._associated_domain_id

    @associated_domain_id.setter
    def associated_domain_id(self, value):
        """ Set associated_domain_id value.

            Notes:
                The ID of the associated l3-domain.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        self._associated_domain_id = value

    
    @property
    def start_address_range(self):
        """ Get start_address_range value.

            Notes:
                Start address for the pool range

                
                This attribute is named `startAddressRange` in VSD API.
                
        """
        return self._start_address_range

    @start_address_range.setter
    def start_address_range(self, value):
        """ Set start_address_range value.

            Notes:
                Start address for the pool range

                
                This attribute is named `startAddressRange` in VSD API.
                
        """
        self._start_address_range = value

    

    