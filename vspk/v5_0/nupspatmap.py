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


class NUPSPATMap(NURESTObject):
    """ Represents a PSPATMap in the VSD

        Notes:
            None
    """

    __rest_name__ = "pspatmap"
    __resource_name__ = "pspatmaps"

    

    def __init__(self, **kwargs):
        """ Initializes a PSPATMap instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> pspatmap = NUPSPATMap(id=u'xxxx-xxx-xxx-xxx', name=u'PSPATMap')
                >>> pspatmap = NUPSPATMap(data=my_dict)
        """

        super(NUPSPATMap, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._reserved_spatips = None
        self._associated_spat_sources_pool_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="reserved_spatips", remote_name="reservedSPATIPs", attribute_type=list, is_required=True, is_unique=False)
        self.expose_attribute(local_name="associated_spat_sources_pool_id", remote_name="associatedSPATSourcesPoolID", attribute_type=str, is_required=True, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name for this Bi-Directional mapping object

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name for this Bi-Directional mapping object

                
        """
        self._name = value

    
    @property
    def reserved_spatips(self):
        """ Get reserved_spatips value.

            Notes:
                Reserved provider SPAT IPs to be used to SPAT a collection of provider private IPs in customer domain.

                
                This attribute is named `reservedSPATIPs` in VSD API.
                
        """
        return self._reserved_spatips

    @reserved_spatips.setter
    def reserved_spatips(self, value):
        """ Set reserved_spatips value.

            Notes:
                Reserved provider SPAT IPs to be used to SPAT a collection of provider private IPs in customer domain.

                
                This attribute is named `reservedSPATIPs` in VSD API.
                
        """
        self._reserved_spatips = value

    
    @property
    def associated_spat_sources_pool_id(self):
        """ Get associated_spat_sources_pool_id value.

            Notes:
                The ID of the associated SPAT sources defined in the provider domain.

                
                This attribute is named `associatedSPATSourcesPoolID` in VSD API.
                
        """
        return self._associated_spat_sources_pool_id

    @associated_spat_sources_pool_id.setter
    def associated_spat_sources_pool_id(self, value):
        """ Set associated_spat_sources_pool_id value.

            Notes:
                The ID of the associated SPAT sources defined in the provider domain.

                
                This attribute is named `associatedSPATSourcesPoolID` in VSD API.
                
        """
        self._associated_spat_sources_pool_id = value

    

    