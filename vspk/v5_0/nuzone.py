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




from .fetchers import NUTCAsFetcher


from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUDHCPOptionsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVMsFetcher


from .fetchers import NUVMInterfacesFetcher


from .fetchers import NUContainersFetcher


from .fetchers import NUContainerInterfacesFetcher


from .fetchers import NUQOSsFetcher


from .fetchers import NUVPortsFetcher


from .fetchers import NUGroupsFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUStatisticsPoliciesFetcher


from .fetchers import NUSubnetsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUZone(NURESTObject):
    """ Represents a Zone in the VSD

        Notes:
            The zone is a collection of subnets attached to a domain. The zone concept enables the definition of policies for collections of subnets.
    """

    __rest_name__ = "zone"
    __resource_name__ = "zones"

    
    ## Constants
    
    CONST_MAINTENANCE_MODE_ENABLED_INHERITED = "ENABLED_INHERITED"
    
    CONST_MAINTENANCE_MODE_ENABLED = "ENABLED"
    
    CONST_ENCRYPTION_ENABLED = "ENABLED"
    
    CONST_ENCRYPTION_DISABLED = "DISABLED"
    
    CONST_DPI_ENABLED = "ENABLED"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_IP_TYPE_IPV6 = "IPV6"
    
    CONST_DPI_INHERITED = "INHERITED"
    
    CONST_IP_TYPE_IPV4 = "IPV4"
    
    CONST_MULTICAST_ENABLED = "ENABLED"
    
    CONST_MULTICAST_INHERITED = "INHERITED"
    
    CONST_DPI_DISABLED = "DISABLED"
    
    CONST_MAINTENANCE_MODE_DISABLED = "DISABLED"
    
    CONST_ENCRYPTION_INHERITED = "INHERITED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_MULTICAST_DISABLED = "DISABLED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Zone instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> zone = NUZone(id=u'xxxx-xxx-xxx-xxx', name=u'Zone')
                >>> zone = NUZone(data=my_dict)
        """

        super(NUZone, self).__init__()

        # Read/Write Attributes
        
        self._dpi = None
        self._ip_type = None
        self._ipv6_address = None
        self._maintenance_mode = None
        self._name = None
        self._last_updated_by = None
        self._address = None
        self._template_id = None
        self._description = None
        self._netmask = None
        self._encryption = None
        self._entity_scope = None
        self._policy_group_id = None
        self._associated_multicast_channel_map_id = None
        self._public_zone = None
        self._multicast = None
        self._number_of_hosts_in_subnets = None
        self._external_id = None
        self._dynamic_ipv6_address = None
        
        self.expose_attribute(local_name="dpi", remote_name="DPI", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="ip_type", remote_name="IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4', u'IPV6'])
        self.expose_attribute(local_name="ipv6_address", remote_name="IPv6Address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="maintenance_mode", remote_name="maintenanceMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'ENABLED_INHERITED'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="encryption", remote_name="encryption", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="policy_group_id", remote_name="policyGroupID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_multicast_channel_map_id", remote_name="associatedMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="public_zone", remote_name="publicZone", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="multicast", remote_name="multicast", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="number_of_hosts_in_subnets", remote_name="numberOfHostsInSubnets", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="dynamic_ipv6_address", remote_name="dynamicIpv6Address", attribute_type=bool, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.dhcp_options = NUDHCPOptionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.containers = NUContainersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.container_interfaces = NUContainerInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.groups = NUGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.subnets = NUSubnetsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def dpi(self):
        """ Get dpi value.

            Notes:
                determines whether or not Deep packet inspection is enabled

                
                This attribute is named `DPI` in VSD API.
                
        """
        return self._dpi

    @dpi.setter
    def dpi(self, value):
        """ Set dpi value.

            Notes:
                determines whether or not Deep packet inspection is enabled

                
                This attribute is named `DPI` in VSD API.
                
        """
        self._dpi = value

    
    @property
    def ip_type(self):
        """ Get ip_type value.

            Notes:
                IPv4 or IPv6

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        """ Set ip_type value.

            Notes:
                IPv4 or IPv6

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    
    @property
    def ipv6_address(self):
        """ Get ipv6_address value.

            Notes:
                IPv6 address range of the zone. This is an optional field that allows users to allocate an address range to a zone. The VSD will auto-assign IP ranges to subnets from this range if an IP range is not defined for a subnet.

                
                This attribute is named `IPv6Address` in VSD API.
                
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, value):
        """ Set ipv6_address value.

            Notes:
                IPv6 address range of the zone. This is an optional field that allows users to allocate an address range to a zone. The VSD will auto-assign IP ranges to subnets from this range if an IP range is not defined for a subnet.

                
                This attribute is named `IPv6Address` in VSD API.
                
        """
        self._ipv6_address = value

    
    @property
    def maintenance_mode(self):
        """ Get maintenance_mode value.

            Notes:
                Indicates if the Zone is accepting VM activation requests.

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        return self._maintenance_mode

    @maintenance_mode.setter
    def maintenance_mode(self, value):
        """ Set maintenance_mode value.

            Notes:
                Indicates if the Zone is accepting VM activation requests.

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        self._maintenance_mode = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

                
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
    def address(self):
        """ Get address value.

            Notes:
                IPv4 address range of the zone. This is an optional field that allows users to allocate an address range to a zone. The VSD will auto-assign IP ranges to subnets from this range if an IP range is not defined for a subnet.

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                IPv4 address range of the zone. This is an optional field that allows users to allocate an address range to a zone. The VSD will auto-assign IP ranges to subnets from this range if an IP range is not defined for a subnet.

                
        """
        self._address = value

    
    @property
    def template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the template that this zone was derived from

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the template that this zone was derived from

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the zone

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the zone

                
        """
        self._description = value

    
    @property
    def netmask(self):
        """ Get netmask value.

            Notes:
                Netmask of the subnet defined

                
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """ Set netmask value.

            Notes:
                Netmask of the subnet defined

                
        """
        self._netmask = value

    
    @property
    def encryption(self):
        """ Get encryption value.

            Notes:
                Determines whether or not IPSEC is enabled.

                
        """
        return self._encryption

    @encryption.setter
    def encryption(self, value):
        """ Set encryption value.

            Notes:
                Determines whether or not IPSEC is enabled.

                
        """
        self._encryption = value

    
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
    def policy_group_id(self):
        """ Get policy_group_id value.

            Notes:
                PG ID for the subnet. This is unique per domain and will be in the range 1-4095

                
                This attribute is named `policyGroupID` in VSD API.
                
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, value):
        """ Set policy_group_id value.

            Notes:
                PG ID for the subnet. This is unique per domain and will be in the range 1-4095

                
                This attribute is named `policyGroupID` in VSD API.
                
        """
        self._policy_group_id = value

    
    @property
    def associated_multicast_channel_map_id(self):
        """ Get associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this zone/zone template is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_multicast_channel_map_id

    @associated_multicast_channel_map_id.setter
    def associated_multicast_channel_map_id(self, value):
        """ Set associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this zone/zone template is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        self._associated_multicast_channel_map_id = value

    
    @property
    def public_zone(self):
        """ Get public_zone value.

            Notes:
                If a zone is marked as public, then it is lined to the public network associated with this data center

                
                This attribute is named `publicZone` in VSD API.
                
        """
        return self._public_zone

    @public_zone.setter
    def public_zone(self, value):
        """ Set public_zone value.

            Notes:
                If a zone is marked as public, then it is lined to the public network associated with this data center

                
                This attribute is named `publicZone` in VSD API.
                
        """
        self._public_zone = value

    
    @property
    def multicast(self):
        """ Get multicast value.

            Notes:
                Indicates multicast policy on zone.

                
        """
        return self._multicast

    @multicast.setter
    def multicast(self, value):
        """ Set multicast value.

            Notes:
                Indicates multicast policy on zone.

                
        """
        self._multicast = value

    
    @property
    def number_of_hosts_in_subnets(self):
        """ Get number_of_hosts_in_subnets value.

            Notes:
                Number of hosts in each of the subnets that can be created under a zone and are auto-assigned IP addresses

                
                This attribute is named `numberOfHostsInSubnets` in VSD API.
                
        """
        return self._number_of_hosts_in_subnets

    @number_of_hosts_in_subnets.setter
    def number_of_hosts_in_subnets(self, value):
        """ Set number_of_hosts_in_subnets value.

            Notes:
                Number of hosts in each of the subnets that can be created under a zone and are auto-assigned IP addresses

                
                This attribute is named `numberOfHostsInSubnets` in VSD API.
                
        """
        self._number_of_hosts_in_subnets = value

    
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
    def dynamic_ipv6_address(self):
        """ Get dynamic_ipv6_address value.

            Notes:
                Turn on or off dynamic allocation of IPV6 address

                
                This attribute is named `dynamicIpv6Address` in VSD API.
                
        """
        return self._dynamic_ipv6_address

    @dynamic_ipv6_address.setter
    def dynamic_ipv6_address(self, value):
        """ Set dynamic_ipv6_address value.

            Notes:
                Turn on or off dynamic allocation of IPV6 address

                
                This attribute is named `dynamicIpv6Address` in VSD API.
                
        """
        self._dynamic_ipv6_address = value

    

    
    ## Custom methods
    def is_template(self):
        """ Verify that the object is a template
    
            Returns:
                (bool): True if the object is a template
        """
        return False
    
    def is_from_template(self):
        """ Verify if the object has been instantiated from a template
    
            Note:
                The object has to be fetched. Otherwise, it does not
                have information from its parent
    
            Returns:
                (bool): True if the object is a template
        """
        return self.template_id
    