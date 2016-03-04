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



from .fetchers import NUEventLogsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUMetadatasFetcher

from bambou import NURESTObject


class NUAddressRange(NURESTObject):
    """ Represents a AddressRange in the VSD

        Notes:
            This is the definition of a Address Range associated with a Network.
    """

    __rest_name__ = "addressrange"
    __resource_name__ = "addressranges"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_DHCP_POOL_TYPE_BRIDGE = "BRIDGE"
    
    CONST_DHCP_POOL_TYPE_HOST = "HOST"
    
    

    def __init__(self, **kwargs):
        """ Initializes a AddressRange instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> addressrange = NUAddressRange(id=u'xxxx-xxx-xxx-xxx', name=u'AddressRange')
                >>> addressrange = NUAddressRange(data=my_dict)
        """

        super(NUAddressRange, self).__init__()

        # Read/Write Attributes
        
        self._dhcp_pool_type = None
        self._entity_scope = None
        self._external_id = None
        self._last_updated_by = None
        self._max_address = None
        self._min_address = None
        
        self.expose_attribute(local_name="dhcp_pool_type", remote_name="DHCPPoolType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BRIDGE', u'HOST'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="max_address", remote_name="maxAddress", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="min_address", remote_name="minAddress", attribute_type=str, is_required=True, is_unique=False)
        

        # Fetchers
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def dhcp_pool_type(self):
        """ Get dhcp_pool_type value.

            Notes:
                DHCPPoolType is an enum that indicates if the DHCP Pool is for HOST/BRIDGE.

                
                This attribute is named `DHCPPoolType` in VSD API.
                
        """
        return self._dhcp_pool_type

    @dhcp_pool_type.setter
    def dhcp_pool_type(self, value):
        """ Set dhcp_pool_type value.

            Notes:
                DHCPPoolType is an enum that indicates if the DHCP Pool is for HOST/BRIDGE.

                
                This attribute is named `DHCPPoolType` in VSD API.
                
        """
        self._dhcp_pool_type = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def max_address(self):
        """ Get max_address value.

            Notes:
                Higest address in the address range

                
                This attribute is named `maxAddress` in VSD API.
                
        """
        return self._max_address

    @max_address.setter
    def max_address(self, value):
        """ Set max_address value.

            Notes:
                Higest address in the address range

                
                This attribute is named `maxAddress` in VSD API.
                
        """
        self._max_address = value

    
    @property
    def min_address(self):
        """ Get min_address value.

            Notes:
                Lowest address in the address range

                
                This attribute is named `minAddress` in VSD API.
                
        """
        return self._min_address

    @min_address.setter
    def min_address(self, value):
        """ Set min_address value.

            Notes:
                Lowest address in the address range

                
                This attribute is named `minAddress` in VSD API.
                
        """
        self._min_address = value

    

    