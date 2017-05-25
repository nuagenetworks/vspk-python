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



from .fetchers import NUNATMapEntriesFetcher


from .fetchers import NUAddressMapsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUEnterprisePermissionsFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUStatisticsPoliciesFetcher


from .fetchers import NUBulkStatisticsFetcher

from bambou import NURESTObject


class NUPATNATPool(NURESTObject):
    """ Represents a PATNATPool in the VSD

        Notes:
            Represents a PAT NAT Pool object.
    """

    __rest_name__ = "patnatpool"
    __resource_name__ = "patnatpools"

    
    ## Constants
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_ASSOCIATED_GATEWAY_TYPE_GATEWAY = "GATEWAY"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_ASSOCIATED_GATEWAY_TYPE_IKE_GATEWAY = "IKE_GATEWAY"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_ASSOCIATED_GATEWAY_TYPE_NSGATEWAY = "NSGATEWAY"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ASSOCIATED_GATEWAY_TYPE_AUTO_DISC_GATEWAY = "AUTO_DISC_GATEWAY"
    
    

    def __init__(self, **kwargs):
        """ Initializes a PATNATPool instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> patnatpool = NUPATNATPool(id=u'xxxx-xxx-xxx-xxx', name=u'PATNATPool')
                >>> patnatpool = NUPATNATPool(data=my_dict)
        """

        super(NUPATNATPool, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._address_range = None
        self._default_patip = None
        self._permitted_action = None
        self._description = None
        self._end_address_range = None
        self._end_source_address = None
        self._entity_scope = None
        self._associated_gateway_id = None
        self._associated_gateway_type = None
        self._associated_subnet_id = None
        self._associated_vlan_id = None
        self._start_address_range = None
        self._start_source_address = None
        self._external_id = None
        self._dynamic_source_enabled = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address_range", remote_name="addressRange", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="default_patip", remote_name="defaultPATIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="end_address_range", remote_name="endAddressRange", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="end_source_address", remote_name="endSourceAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_gateway_id", remote_name="associatedGatewayId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_gateway_type", remote_name="associatedGatewayType", attribute_type=str, is_required=False, is_unique=False, choices=[u'AUTO_DISC_GATEWAY', u'GATEWAY', u'IKE_GATEWAY', u'NSGATEWAY'])
        self.expose_attribute(local_name="associated_subnet_id", remote_name="associatedSubnetId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_vlan_id", remote_name="associatedVlanId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="start_address_range", remote_name="startAddressRange", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="start_source_address", remote_name="startSourceAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="dynamic_source_enabled", remote_name="dynamicSourceEnabled", attribute_type=bool, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.nat_map_entries = NUNATMapEntriesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.address_maps = NUAddressMapsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bulk_statistics = NUBulkStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the PATNATPool

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the PATNATPool

                
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
    def address_range(self):
        """ Get address_range value.

            Notes:
                Default PAT IP Address, must belong to the pool above

                
                This attribute is named `addressRange` in VSD API.
                
        """
        return self._address_range

    @address_range.setter
    def address_range(self, value):
        """ Set address_range value.

            Notes:
                Default PAT IP Address, must belong to the pool above

                
                This attribute is named `addressRange` in VSD API.
                
        """
        self._address_range = value

    
    @property
    def default_patip(self):
        """ Get default_patip value.

            Notes:
                Default PAT IP Address, must belong to the pool above

                
                This attribute is named `defaultPATIP` in VSD API.
                
        """
        return self._default_patip

    @default_patip.setter
    def default_patip(self, value):
        """ Set default_patip value.

            Notes:
                Default PAT IP Address, must belong to the pool above

                
                This attribute is named `defaultPATIP` in VSD API.
                
        """
        self._default_patip = value

    
    @property
    def permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway.

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    @permitted_action.setter
    def permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway.

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the PATNATPool

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the PATNATPool

                
        """
        self._description = value

    
    @property
    def end_address_range(self):
        """ Get end_address_range value.

            Notes:
                Ending IP Address for the pool of available addresses for use

                
                This attribute is named `endAddressRange` in VSD API.
                
        """
        return self._end_address_range

    @end_address_range.setter
    def end_address_range(self, value):
        """ Set end_address_range value.

            Notes:
                Ending IP Address for the pool of available addresses for use

                
                This attribute is named `endAddressRange` in VSD API.
                
        """
        self._end_address_range = value

    
    @property
    def end_source_address(self):
        """ Get end_source_address value.

            Notes:
                Ending Source IP Address for the pool. (Dynamic Source NAT)

                
                This attribute is named `endSourceAddress` in VSD API.
                
        """
        return self._end_source_address

    @end_source_address.setter
    def end_source_address(self, value):
        """ Set end_source_address value.

            Notes:
                Ending Source IP Address for the pool. (Dynamic Source NAT)

                
                This attribute is named `endSourceAddress` in VSD API.
                
        """
        self._end_source_address = value

    
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
    def associated_gateway_id(self):
        """ Get associated_gateway_id value.

            Notes:
                UUID of the NSG instance this Pool is assocated with. This attribute may be auto-populated when the pool is assigned to a Network VLAN instance.

                
                This attribute is named `associatedGatewayId` in VSD API.
                
        """
        return self._associated_gateway_id

    @associated_gateway_id.setter
    def associated_gateway_id(self, value):
        """ Set associated_gateway_id value.

            Notes:
                UUID of the NSG instance this Pool is assocated with. This attribute may be auto-populated when the pool is assigned to a Network VLAN instance.

                
                This attribute is named `associatedGatewayId` in VSD API.
                
        """
        self._associated_gateway_id = value

    
    @property
    def associated_gateway_type(self):
        """ Get associated_gateway_type value.

            Notes:
                None

                
                This attribute is named `associatedGatewayType` in VSD API.
                
        """
        return self._associated_gateway_type

    @associated_gateway_type.setter
    def associated_gateway_type(self, value):
        """ Set associated_gateway_type value.

            Notes:
                None

                
                This attribute is named `associatedGatewayType` in VSD API.
                
        """
        self._associated_gateway_type = value

    
    @property
    def associated_subnet_id(self):
        """ Get associated_subnet_id value.

            Notes:
                ID of the Subnet for which the information will be used to populate Source Address Range (Dynamic Source NAT).

                
                This attribute is named `associatedSubnetId` in VSD API.
                
        """
        return self._associated_subnet_id

    @associated_subnet_id.setter
    def associated_subnet_id(self, value):
        """ Set associated_subnet_id value.

            Notes:
                ID of the Subnet for which the information will be used to populate Source Address Range (Dynamic Source NAT).

                
                This attribute is named `associatedSubnetId` in VSD API.
                
        """
        self._associated_subnet_id = value

    
    @property
    def associated_vlan_id(self):
        """ Get associated_vlan_id value.

            Notes:
                ID of the network port VLAN on which the pool is associated.

                
                This attribute is named `associatedVlanId` in VSD API.
                
        """
        return self._associated_vlan_id

    @associated_vlan_id.setter
    def associated_vlan_id(self, value):
        """ Set associated_vlan_id value.

            Notes:
                ID of the network port VLAN on which the pool is associated.

                
                This attribute is named `associatedVlanId` in VSD API.
                
        """
        self._associated_vlan_id = value

    
    @property
    def start_address_range(self):
        """ Get start_address_range value.

            Notes:
                Starting IP Address for the pool of available addresses for use

                
                This attribute is named `startAddressRange` in VSD API.
                
        """
        return self._start_address_range

    @start_address_range.setter
    def start_address_range(self, value):
        """ Set start_address_range value.

            Notes:
                Starting IP Address for the pool of available addresses for use

                
                This attribute is named `startAddressRange` in VSD API.
                
        """
        self._start_address_range = value

    
    @property
    def start_source_address(self):
        """ Get start_source_address value.

            Notes:
                Starting Source IP Address for the pool. (Dynamic Source NAT)

                
                This attribute is named `startSourceAddress` in VSD API.
                
        """
        return self._start_source_address

    @start_source_address.setter
    def start_source_address(self, value):
        """ Set start_source_address value.

            Notes:
                Starting Source IP Address for the pool. (Dynamic Source NAT)

                
                This attribute is named `startSourceAddress` in VSD API.
                
        """
        self._start_source_address = value

    
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
    def dynamic_source_enabled(self):
        """ Get dynamic_source_enabled value.

            Notes:
                Set to True if the address translation pool at the address translation pool definition level

                
                This attribute is named `dynamicSourceEnabled` in VSD API.
                
        """
        return self._dynamic_source_enabled

    @dynamic_source_enabled.setter
    def dynamic_source_enabled(self, value):
        """ Set dynamic_source_enabled value.

            Notes:
                Set to True if the address translation pool at the address translation pool definition level

                
                This attribute is named `dynamicSourceEnabled` in VSD API.
                
        """
        self._dynamic_source_enabled = value

    

    