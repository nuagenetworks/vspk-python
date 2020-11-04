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




from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUVMIPReservation(NURESTObject):
    """ Represents a VMIPReservation in the VSD

        Notes:
            VM IP Reservation under Subnet/L2Domain.
    """

    __rest_name__ = "vmipreservation"
    __resource_name__ = "vmipreservations"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_STATE_ASSIGNED = "ASSIGNED"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_IP_TYPE_IPV6 = "IPV6"
    
    CONST_IP_TYPE_IPV4 = "IPV4"
    
    CONST_STATE_ASSIGNED_DELETE_PENDING = "ASSIGNED_DELETE_PENDING"
    
    CONST_STATE_UNASSIGNED = "UNASSIGNED"
    
    CONST_IP_TYPE_DUALSTACK = "DUALSTACK"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VMIPReservation instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vmipreservation = NUVMIPReservation(id=u'xxxx-xxx-xxx-xxx', name=u'VMIPReservation')
                >>> vmipreservation = NUVMIPReservation(data=my_dict)
        """

        super(NUVMIPReservation, self).__init__()

        # Read/Write Attributes
        
        self._ip_type = None
        self._ipv4_address = None
        self._ipv6_address = None
        self._ipv6_allocation_pools = None
        self._last_updated_by = None
        self._last_updated_date = None
        self._allocation_pools = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._creation_date = None
        self._state = None
        self._owner = None
        self._external_id = None
        
        self.expose_attribute(local_name="ip_type", remote_name="IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DUALSTACK', u'IPV4', u'IPV6'])
        self.expose_attribute(local_name="ipv4_address", remote_name="IPV4Address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ipv6_address", remote_name="IPV6Address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ipv6_allocation_pools", remote_name="IPV6AllocationPools", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allocation_pools", remote_name="allocationPools", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="state", remote_name="state", attribute_type=str, is_required=False, is_unique=False, choices=[u'ASSIGNED', u'ASSIGNED_DELETE_PENDING', u'UNASSIGNED'])
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ip_type(self):
        """ Get ip_type value.

            Notes:
                Specify if the VM IP Reservation is of type IPv6, IPv4 or DualStack. If not specified, it is derived from the Subnet/L2Domain

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        """ Set ip_type value.

            Notes:
                Specify if the VM IP Reservation is of type IPv6, IPv4 or DualStack. If not specified, it is derived from the Subnet/L2Domain

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    
    @property
    def ipv4_address(self):
        """ Get ipv4_address value.

            Notes:
                IPv4 Address associated with this VM IP Reservation.

                
                This attribute is named `IPV4Address` in VSD API.
                
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, value):
        """ Set ipv4_address value.

            Notes:
                IPv4 Address associated with this VM IP Reservation.

                
                This attribute is named `IPV4Address` in VSD API.
                
        """
        self._ipv4_address = value

    
    @property
    def ipv6_address(self):
        """ Get ipv6_address value.

            Notes:
                IPv6 Address associated with this VM IP Reservation.

                
                This attribute is named `IPV6Address` in VSD API.
                
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, value):
        """ Set ipv6_address value.

            Notes:
                IPv6 Address associated with this VM IP Reservation.

                
                This attribute is named `IPV6Address` in VSD API.
                
        """
        self._ipv6_address = value

    
    @property
    def ipv6_allocation_pools(self):
        """ Get ipv6_allocation_pools value.

            Notes:
                Collection of IPv6 address ranges to consider for reservation.

                
                This attribute is named `IPV6AllocationPools` in VSD API.
                
        """
        return self._ipv6_allocation_pools

    @ipv6_allocation_pools.setter
    def ipv6_allocation_pools(self, value):
        """ Set ipv6_allocation_pools value.

            Notes:
                Collection of IPv6 address ranges to consider for reservation.

                
                This attribute is named `IPV6AllocationPools` in VSD API.
                
        """
        self._ipv6_allocation_pools = value

    
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
    def last_updated_date(self):
        """ Get last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, value):
        """ Set last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        self._last_updated_date = value

    
    @property
    def allocation_pools(self):
        """ Get allocation_pools value.

            Notes:
                Collection of IPv4 address ranges to consider for reservation.

                
                This attribute is named `allocationPools` in VSD API.
                
        """
        return self._allocation_pools

    @allocation_pools.setter
    def allocation_pools(self, value):
        """ Set allocation_pools value.

            Notes:
                Collection of IPv4 address ranges to consider for reservation.

                
                This attribute is named `allocationPools` in VSD API.
                
        """
        self._allocation_pools = value

    
    @property
    def embedded_metadata(self):
        """ Get embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        return self._embedded_metadata

    @embedded_metadata.setter
    def embedded_metadata(self, value):
        """ Set embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        self._embedded_metadata = value

    
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
    def creation_date(self):
        """ Get creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """ Set creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        self._creation_date = value

    
    @property
    def state(self):
        """ Get state value.

            Notes:
                This indicates the state of this VM IP Reservation. Possible values are 'ASSIGNED', 'ASSIGNED_DELETE_PENDING', 'UNASSIGNED'.

                
        """
        return self._state

    @state.setter
    def state(self, value):
        """ Set state value.

            Notes:
                This indicates the state of this VM IP Reservation. Possible values are 'ASSIGNED', 'ASSIGNED_DELETE_PENDING', 'UNASSIGNED'.

                
        """
        self._state = value

    
    @property
    def owner(self):
        """ Get owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """ Set owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        self._owner = value

    
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

    

    