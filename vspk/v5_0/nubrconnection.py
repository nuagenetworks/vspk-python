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


from .fetchers import NUBFDSessionsFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUBRConnection(NURESTObject):
    """ Represents a BRConnection in the VSD

        Notes:
            Configuration of VNS Gateway Border Router connection
    """

    __rest_name__ = "brconnection"
    __resource_name__ = "brconnections"

    
    ## Constants
    
    CONST_ADVERTISEMENT_CRITERIA_OPERATIONAL_LINK = "OPERATIONAL_LINK"
    
    CONST_ADVERTISEMENT_CRITERIA_BFD = "BFD"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_MODE_STATIC = "Static"
    
    CONST_ADDRESS_FAMILY_IPV6 = "IPV6"
    
    CONST_ADDRESS_FAMILY_IPV4 = "IPV4"
    
    

    def __init__(self, **kwargs):
        """ Initializes a BRConnection instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> brconnection = NUBRConnection(id=u'xxxx-xxx-xxx-xxx', name=u'BRConnection')
                >>> brconnection = NUBRConnection(data=my_dict)
        """

        super(NUBRConnection, self).__init__()

        # Read/Write Attributes
        
        self._dns_address = None
        self._dns_address_v6 = None
        self._last_updated_by = None
        self._gateway = None
        self._gateway_v6 = None
        self._address = None
        self._address_family = None
        self._address_v6 = None
        self._advertisement_criteria = None
        self._netmask = None
        self._inherited = None
        self._entity_scope = None
        self._mode = None
        self._uplink_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="dns_address", remote_name="DNSAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dns_address_v6", remote_name="DNSAddressV6", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway", remote_name="gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_v6", remote_name="gatewayV6", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address_family", remote_name="addressFamily", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4', u'IPV6'])
        self.expose_attribute(local_name="address_v6", remote_name="addressV6", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="advertisement_criteria", remote_name="advertisementCriteria", attribute_type=str, is_required=False, is_unique=False, choices=[u'BFD', u'OPERATIONAL_LINK'])
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="inherited", remote_name="inherited", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="mode", remote_name="mode", attribute_type=str, is_required=False, is_unique=False, choices=[u'Static'])
        self.expose_attribute(local_name="uplink_id", remote_name="uplinkID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bfd_sessions = NUBFDSessionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def dns_address(self):
        """ Get dns_address value.

            Notes:
                DNS Address for the vlan

                
                This attribute is named `DNSAddress` in VSD API.
                
        """
        return self._dns_address

    @dns_address.setter
    def dns_address(self, value):
        """ Set dns_address value.

            Notes:
                DNS Address for the vlan

                
                This attribute is named `DNSAddress` in VSD API.
                
        """
        self._dns_address = value

    
    @property
    def dns_address_v6(self):
        """ Get dns_address_v6 value.

            Notes:
                DNS IPv6 Address

                
                This attribute is named `DNSAddressV6` in VSD API.
                
        """
        return self._dns_address_v6

    @dns_address_v6.setter
    def dns_address_v6(self, value):
        """ Set dns_address_v6 value.

            Notes:
                DNS IPv6 Address

                
                This attribute is named `DNSAddressV6` in VSD API.
                
        """
        self._dns_address_v6 = value

    
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
    def gateway(self):
        """ Get gateway value.

            Notes:
                IP address of the gateway bound to the VLAN.

                
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """ Set gateway value.

            Notes:
                IP address of the gateway bound to the VLAN.

                
        """
        self._gateway = value

    
    @property
    def gateway_v6(self):
        """ Get gateway_v6 value.

            Notes:
                IPv6 address of the gateway bound to the port.

                
                This attribute is named `gatewayV6` in VSD API.
                
        """
        return self._gateway_v6

    @gateway_v6.setter
    def gateway_v6(self, value):
        """ Set gateway_v6 value.

            Notes:
                IPv6 address of the gateway bound to the port.

                
                This attribute is named `gatewayV6` in VSD API.
                
        """
        self._gateway_v6 = value

    
    @property
    def address(self):
        """ Get address value.

            Notes:
                Static IP address for the VLAN on which the BR Connection is created.

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                Static IP address for the VLAN on which the BR Connection is created.

                
        """
        self._address = value

    
    @property
    def address_family(self):
        """ Get address_family value.

            Notes:
                IP address family of this BRConnection

                
                This attribute is named `addressFamily` in VSD API.
                
        """
        return self._address_family

    @address_family.setter
    def address_family(self, value):
        """ Set address_family value.

            Notes:
                IP address family of this BRConnection

                
                This attribute is named `addressFamily` in VSD API.
                
        """
        self._address_family = value

    
    @property
    def address_v6(self):
        """ Get address_v6 value.

            Notes:
                IPv6 address for static configuration on the BR Connection instance.

                
                This attribute is named `addressV6` in VSD API.
                
        """
        return self._address_v6

    @address_v6.setter
    def address_v6(self, value):
        """ Set address_v6 value.

            Notes:
                IPv6 address for static configuration on the BR Connection instance.

                
                This attribute is named `addressV6` in VSD API.
                
        """
        self._address_v6 = value

    
    @property
    def advertisement_criteria(self):
        """ Get advertisement_criteria value.

            Notes:
                Advertisement Criteria for Traffic Flow on a BR Connection.

                
                This attribute is named `advertisementCriteria` in VSD API.
                
        """
        return self._advertisement_criteria

    @advertisement_criteria.setter
    def advertisement_criteria(self, value):
        """ Set advertisement_criteria value.

            Notes:
                Advertisement Criteria for Traffic Flow on a BR Connection.

                
                This attribute is named `advertisementCriteria` in VSD API.
                
        """
        self._advertisement_criteria = value

    
    @property
    def netmask(self):
        """ Get netmask value.

            Notes:
                network mask

                
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """ Set netmask value.

            Notes:
                network mask

                
        """
        self._netmask = value

    
    @property
    def inherited(self):
        """ Get inherited value.

            Notes:
                This flag will determine if the abstract connection is inherited from the instance template

                
        """
        return self._inherited

    @inherited.setter
    def inherited(self, value):
        """ Set inherited value.

            Notes:
                This flag will determine if the abstract connection is inherited from the instance template

                
        """
        self._inherited = value

    
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
    def mode(self):
        """ Get mode value.

            Notes:
                Connection mode: Only static is allowed on a Bridge Router Connection.

                
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        """ Set mode value.

            Notes:
                Connection mode: Only static is allowed on a Bridge Router Connection.

                
        """
        self._mode = value

    
    @property
    def uplink_id(self):
        """ Get uplink_id value.

            Notes:
                Internally generated ID in the range that idenitifies the uplink within the context of NSG.

                
                This attribute is named `uplinkID` in VSD API.
                
        """
        return self._uplink_id

    @uplink_id.setter
    def uplink_id(self, value):
        """ Set uplink_id value.

            Notes:
                Internally generated ID in the range that idenitifies the uplink within the context of NSG.

                
                This attribute is named `uplinkID` in VSD API.
                
        """
        self._uplink_id = value

    
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

    

    