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



from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUStatisticsPoliciesFetcher

from bambou import NURESTObject


class NUAddressMap(NURESTObject):
    """ Represents a AddressMap in the VSD

        Notes:
            Defines an address mapping between a private IP and a port with a public IP address and port.
    """

    __rest_name__ = "addressmap"
    __resource_name__ = "addressmaps"

    
    ## Constants
    
    CONST_TYPE_ONE_TO_ONE_NAT = "ONE_TO_ONE_NAT"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_TYPE_MANY_TO_ONE_PAT = "MANY_TO_ONE_PAT"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a AddressMap instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> addressmap = NUAddressMap(id=u'xxxx-xxx-xxx-xxx', name=u'AddressMap')
                >>> addressmap = NUAddressMap(data=my_dict)
        """

        super(NUAddressMap, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._entity_scope = None
        self._private_ip = None
        self._private_port = None
        self._associated_patnat_pool_id = None
        self._public_ip = None
        self._public_port = None
        self._external_id = None
        self._type = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="private_ip", remote_name="privateIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="private_port", remote_name="privatePort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_patnat_pool_id", remote_name="associatedPATNATPoolID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="public_ip", remote_name="publicIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="public_port", remote_name="publicPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=False, is_unique=False, choices=[u'MANY_TO_ONE_PAT', u'ONE_TO_ONE_NAT'])
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
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
    def private_ip(self):
        """ Get private_ip value.

            Notes:
                Private IP address of the interface

                
                This attribute is named `privateIP` in VSD API.
                
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, value):
        """ Set private_ip value.

            Notes:
                Private IP address of the interface

                
                This attribute is named `privateIP` in VSD API.
                
        """
        self._private_ip = value

    
    @property
    def private_port(self):
        """ Get private_port value.

            Notes:
                None

                
                This attribute is named `privatePort` in VSD API.
                
        """
        return self._private_port

    @private_port.setter
    def private_port(self, value):
        """ Set private_port value.

            Notes:
                None

                
                This attribute is named `privatePort` in VSD API.
                
        """
        self._private_port = value

    
    @property
    def associated_patnat_pool_id(self):
        """ Get associated_patnat_pool_id value.

            Notes:
                Read Only - Indicates which PATNATPool this entry belongs to

                
                This attribute is named `associatedPATNATPoolID` in VSD API.
                
        """
        return self._associated_patnat_pool_id

    @associated_patnat_pool_id.setter
    def associated_patnat_pool_id(self, value):
        """ Set associated_patnat_pool_id value.

            Notes:
                Read Only - Indicates which PATNATPool this entry belongs to

                
                This attribute is named `associatedPATNATPoolID` in VSD API.
                
        """
        self._associated_patnat_pool_id = value

    
    @property
    def public_ip(self):
        """ Get public_ip value.

            Notes:
                Public IP address of the interface

                
                This attribute is named `publicIP` in VSD API.
                
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, value):
        """ Set public_ip value.

            Notes:
                Public IP address of the interface

                
                This attribute is named `publicIP` in VSD API.
                
        """
        self._public_ip = value

    
    @property
    def public_port(self):
        """ Get public_port value.

            Notes:
                None

                
                This attribute is named `publicPort` in VSD API.
                
        """
        return self._public_port

    @public_port.setter
    def public_port(self, value):
        """ Set public_port value.

            Notes:
                None

                
                This attribute is named `publicPort` in VSD API.
                
        """
        self._public_port = value

    
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
    def type(self):
        """ Get type value.

            Notes:
                Identifies the type of address mapping

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                Identifies the type of address mapping

                
        """
        self._type = value

    

    