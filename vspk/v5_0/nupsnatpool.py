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




from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher


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

    
    ## Constants
    
    CONST_IP_TYPE_IPV6 = "IPV6"
    
    CONST_IP_TYPE_IPV4 = "IPV4"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_IP_TYPE_DUALSTACK = "DUALSTACK"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

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
        
        self._ip_type = None
        self._name = None
        self._last_updated_by = None
        self._description = None
        self._end_address = None
        self._entity_scope = None
        self._start_address = None
        self._external_id = None
        
        self.expose_attribute(local_name="ip_type", remote_name="IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DUALSTACK', u'IPV4', u'IPV6'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="end_address", remote_name="endAddress", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="start_address", remote_name="startAddress", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.pspat_maps = NUPSPATMapsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.p_translation_maps = NUPTranslationMapsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ip_type(self):
        """ Get ip_type value.

            Notes:
                The IP Type of this provider alias IP, possible values are IPV4, IPV6 or DUALSTACK.

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        """ Set ip_type value.

            Notes:
                The IP Type of this provider alias IP, possible values are IPV4, IPV6 or DUALSTACK.

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The Provider to Customer NAT Pool

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The Provider to Customer NAT Pool

                
        """
        self._name = value

    
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
    def description(self):
        """ Get description value.

            Notes:
                A description of the PATNATPool instance

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the PATNATPool instance

                
        """
        self._description = value

    
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

    

    