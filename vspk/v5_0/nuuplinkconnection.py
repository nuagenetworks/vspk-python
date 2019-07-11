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


from .fetchers import NUCustomPropertiesFetcher

from bambou import NURESTObject


class NUUplinkConnection(NURESTObject):
    """ Represents a UplinkConnection in the VSD

        Notes:
            Configuration of VNS Gateway uplinks
    """

    __rest_name__ = "uplinkconnection"
    __resource_name__ = "uplinkconnections"

    
    ## Constants
    
    CONST_INTERFACE_CONNECTION_TYPE_USB_MODEM = "USB_MODEM"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_MODE_ANY = "Any"
    
    CONST_ADVERTISEMENT_CRITERIA_CONTROL_SESSION = "CONTROL_SESSION"
    
    CONST_ADVERTISEMENT_CRITERIA_BFD = "BFD"
    
    CONST_ROLE_UNKNOWN = "UNKNOWN"
    
    CONST_MODE_DYNAMIC = "Dynamic"
    
    CONST_MODE_LTE = "LTE"
    
    CONST_ADDRESS_FAMILY_IPV6 = "IPV6"
    
    CONST_ADDRESS_FAMILY_IPV4 = "IPV4"
    
    CONST_ADVERTISEMENT_CRITERIA_OPERATIONAL_LINK = "OPERATIONAL_LINK"
    
    CONST_ROLE_SECONDARY = "SECONDARY"
    
    CONST_MODE_PPPOE = "PPPoE"
    
    CONST_INTERFACE_CONNECTION_TYPE_USB_ETHERNET = "USB_ETHERNET"
    
    CONST_INTERFACE_CONNECTION_TYPE_AUTOMATIC = "AUTOMATIC"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ROLE_NONE = "NONE"
    
    CONST_INTERFACE_CONNECTION_TYPE_EMBEDDED = "EMBEDDED"
    
    CONST_ROLE_TERTIARY = "TERTIARY"
    
    CONST_MODE_STATIC = "Static"
    
    CONST_INTERFACE_CONNECTION_TYPE_PCI_EXPRESS = "PCI_EXPRESS"
    
    CONST_ROLE_PRIMARY = "PRIMARY"
    
    

    def __init__(self, **kwargs):
        """ Initializes a UplinkConnection instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> uplinkconnection = NUUplinkConnection(id=u'xxxx-xxx-xxx-xxx', name=u'UplinkConnection')
                >>> uplinkconnection = NUUplinkConnection(data=my_dict)
        """

        super(NUUplinkConnection, self).__init__()

        # Read/Write Attributes
        
        self._pat_enabled = None
        self._dns_address = None
        self._dns_address_v6 = None
        self._password = None
        self._last_updated_by = None
        self._gateway = None
        self._gateway_v6 = None
        self._address = None
        self._address_family = None
        self._address_v6 = None
        self._advertisement_criteria = None
        self._secondary_address = None
        self._netmask = None
        self._vlan = None
        self._underlay_enabled = None
        self._underlay_id = None
        self._inherited = None
        self._installer_managed = None
        self._interface_connection_type = None
        self._entity_scope = None
        self._mode = None
        self._role = None
        self._role_order = None
        self._port_name = None
        self._download_rate_limit = None
        self._uplink_id = None
        self._username = None
        self._assoc_underlay_id = None
        self._associated_bgp_neighbor_id = None
        self._associated_underlay_name = None
        self._auxiliary_link = None
        self._external_id = None
        
        self.expose_attribute(local_name="pat_enabled", remote_name="PATEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dns_address", remote_name="DNSAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dns_address_v6", remote_name="DNSAddressV6", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="password", remote_name="password", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway", remote_name="gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_v6", remote_name="gatewayV6", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address_family", remote_name="addressFamily", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4', u'IPV6'])
        self.expose_attribute(local_name="address_v6", remote_name="addressV6", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="advertisement_criteria", remote_name="advertisementCriteria", attribute_type=str, is_required=False, is_unique=False, choices=[u'BFD', u'CONTROL_SESSION', u'OPERATIONAL_LINK'])
        self.expose_attribute(local_name="secondary_address", remote_name="secondaryAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vlan", remote_name="vlan", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="underlay_enabled", remote_name="underlayEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="underlay_id", remote_name="underlayID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="inherited", remote_name="inherited", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="installer_managed", remote_name="installerManaged", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="interface_connection_type", remote_name="interfaceConnectionType", attribute_type=str, is_required=False, is_unique=False, choices=[u'AUTOMATIC', u'EMBEDDED', u'PCI_EXPRESS', u'USB_ETHERNET', u'USB_MODEM'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="mode", remote_name="mode", attribute_type=str, is_required=False, is_unique=False, choices=[u'Any', u'Dynamic', u'LTE', u'PPPoE', u'Static'])
        self.expose_attribute(local_name="role", remote_name="role", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'PRIMARY', u'SECONDARY', u'TERTIARY', u'UNKNOWN'])
        self.expose_attribute(local_name="role_order", remote_name="roleOrder", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="port_name", remote_name="portName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="download_rate_limit", remote_name="downloadRateLimit", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="uplink_id", remote_name="uplinkID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="username", remote_name="username", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="assoc_underlay_id", remote_name="assocUnderlayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_bgp_neighbor_id", remote_name="associatedBGPNeighborID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_underlay_name", remote_name="associatedUnderlayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="auxiliary_link", remote_name="auxiliaryLink", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bfd_sessions = NUBFDSessionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.custom_properties = NUCustomPropertiesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def pat_enabled(self):
        """ Get pat_enabled value.

            Notes:
                Indicates whether PAT is enabled on the underlay for this uplink connection.

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        return self._pat_enabled

    @pat_enabled.setter
    def pat_enabled(self, value):
        """ Set pat_enabled value.

            Notes:
                Indicates whether PAT is enabled on the underlay for this uplink connection.

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        self._pat_enabled = value

    
    @property
    def dns_address(self):
        """ Get dns_address value.

            Notes:
                DNS server address.

                
                This attribute is named `DNSAddress` in VSD API.
                
        """
        return self._dns_address

    @dns_address.setter
    def dns_address(self, value):
        """ Set dns_address value.

            Notes:
                DNS server address.

                
                This attribute is named `DNSAddress` in VSD API.
                
        """
        self._dns_address = value

    
    @property
    def dns_address_v6(self):
        """ Get dns_address_v6 value.

            Notes:
                IPv6 DNS server address.

                
                This attribute is named `DNSAddressV6` in VSD API.
                
        """
        return self._dns_address_v6

    @dns_address_v6.setter
    def dns_address_v6(self, value):
        """ Set dns_address_v6 value.

            Notes:
                IPv6 DNS server address.

                
                This attribute is named `DNSAddressV6` in VSD API.
                
        """
        self._dns_address_v6 = value

    
    @property
    def password(self):
        """ Get password value.

            Notes:
                PPPoE password.

                
        """
        return self._password

    @password.setter
    def password(self, value):
        """ Set password value.

            Notes:
                PPPoE password.

                
        """
        self._password = value

    
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
                IP address of the gateway bound to the port

                
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """ Set gateway value.

            Notes:
                IP address of the gateway bound to the port

                
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
                IP address for static configuration

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                IP address for static configuration

                
        """
        self._address = value

    
    @property
    def address_family(self):
        """ Get address_family value.

            Notes:
                IP address family of this UplinkConnection

                
                This attribute is named `addressFamily` in VSD API.
                
        """
        return self._address_family

    @address_family.setter
    def address_family(self, value):
        """ Set address_family value.

            Notes:
                IP address family of this UplinkConnection

                
                This attribute is named `addressFamily` in VSD API.
                
        """
        self._address_family = value

    
    @property
    def address_v6(self):
        """ Get address_v6 value.

            Notes:
                IPv6 address for static configuration

                
                This attribute is named `addressV6` in VSD API.
                
        """
        return self._address_v6

    @address_v6.setter
    def address_v6(self, value):
        """ Set address_v6 value.

            Notes:
                IPv6 address for static configuration

                
                This attribute is named `addressV6` in VSD API.
                
        """
        self._address_v6 = value

    
    @property
    def advertisement_criteria(self):
        """ Get advertisement_criteria value.

            Notes:
                Advertisement Criteria for Traffic Flow

                
                This attribute is named `advertisementCriteria` in VSD API.
                
        """
        return self._advertisement_criteria

    @advertisement_criteria.setter
    def advertisement_criteria(self, value):
        """ Set advertisement_criteria value.

            Notes:
                Advertisement Criteria for Traffic Flow

                
                This attribute is named `advertisementCriteria` in VSD API.
                
        """
        self._advertisement_criteria = value

    
    @property
    def secondary_address(self):
        """ Get secondary_address value.

            Notes:
                Secondary IP Address (Control IP Address) for Loopback. 

                
                This attribute is named `secondaryAddress` in VSD API.
                
        """
        return self._secondary_address

    @secondary_address.setter
    def secondary_address(self, value):
        """ Set secondary_address value.

            Notes:
                Secondary IP Address (Control IP Address) for Loopback. 

                
                This attribute is named `secondaryAddress` in VSD API.
                
        """
        self._secondary_address = value

    
    @property
    def netmask(self):
        """ Get netmask value.

            Notes:
                Subnet mask of the uplink connection if mode is set to Static.

                
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """ Set netmask value.

            Notes:
                Subnet mask of the uplink connection if mode is set to Static.

                
        """
        self._netmask = value

    
    @property
    def vlan(self):
        """ Get vlan value.

            Notes:
                VLAN Id of this uplink

                
        """
        return self._vlan

    @vlan.setter
    def vlan(self, value):
        """ Set vlan value.

            Notes:
                VLAN Id of this uplink

                
        """
        self._vlan = value

    
    @property
    def underlay_enabled(self):
        """ Get underlay_enabled value.

            Notes:
                Indicated whether route to underlay is enabled on this uplink connection.

                
                This attribute is named `underlayEnabled` in VSD API.
                
        """
        return self._underlay_enabled

    @underlay_enabled.setter
    def underlay_enabled(self, value):
        """ Set underlay_enabled value.

            Notes:
                Indicated whether route to underlay is enabled on this uplink connection.

                
                This attribute is named `underlayEnabled` in VSD API.
                
        """
        self._underlay_enabled = value

    
    @property
    def underlay_id(self):
        """ Get underlay_id value.

            Notes:
                Underlay Identifier of underlay associated with this uplink.

                
                This attribute is named `underlayID` in VSD API.
                
        """
        return self._underlay_id

    @underlay_id.setter
    def underlay_id(self, value):
        """ Set underlay_id value.

            Notes:
                Underlay Identifier of underlay associated with this uplink.

                
                This attribute is named `underlayID` in VSD API.
                
        """
        self._underlay_id = value

    
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
    def installer_managed(self):
        """ Get installer_managed value.

            Notes:
                Boolean flag to indicate that connection parameters will be configured by the installer onsite. Limited to ConnectionMode: PPPoE

                
                This attribute is named `installerManaged` in VSD API.
                
        """
        return self._installer_managed

    @installer_managed.setter
    def installer_managed(self, value):
        """ Set installer_managed value.

            Notes:
                Boolean flag to indicate that connection parameters will be configured by the installer onsite. Limited to ConnectionMode: PPPoE

                
                This attribute is named `installerManaged` in VSD API.
                
        """
        self._installer_managed = value

    
    @property
    def interface_connection_type(self):
        """ Get interface_connection_type value.

            Notes:
                The way the interface is connected via the NSG.  This value depends on if the interface internal or external to the NSG.

                
                This attribute is named `interfaceConnectionType` in VSD API.
                
        """
        return self._interface_connection_type

    @interface_connection_type.setter
    def interface_connection_type(self, value):
        """ Set interface_connection_type value.

            Notes:
                The way the interface is connected via the NSG.  This value depends on if the interface internal or external to the NSG.

                
                This attribute is named `interfaceConnectionType` in VSD API.
                
        """
        self._interface_connection_type = value

    
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
                Specify how to connect to the network. Possible values: Dynamic (DHCP), Static (static configuration is required), PPPoE (pppoe configuration required), LTE (LTE configuration required). Default: Dynamic

                
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        """ Set mode value.

            Notes:
                Specify how to connect to the network. Possible values: Dynamic (DHCP), Static (static configuration is required), PPPoE (pppoe configuration required), LTE (LTE configuration required). Default: Dynamic

                
        """
        self._mode = value

    
    @property
    def role(self):
        """ Get role value.

            Notes:
                To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, 

                
        """
        return self._role

    @role.setter
    def role(self, value):
        """ Set role value.

            Notes:
                To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, 

                
        """
        self._role = value

    
    @property
    def role_order(self):
        """ Get role_order value.

            Notes:
                Role order: Primary 1, Primary 2, Secondary 3. Note: Order will be calculated when all uplink connections fetched for gateway

                
                This attribute is named `roleOrder` in VSD API.
                
        """
        return self._role_order

    @role_order.setter
    def role_order(self, value):
        """ Set role_order value.

            Notes:
                Role order: Primary 1, Primary 2, Secondary 3. Note: Order will be calculated when all uplink connections fetched for gateway

                
                This attribute is named `roleOrder` in VSD API.
                
        """
        self._role_order = value

    
    @property
    def port_name(self):
        """ Get port_name value.

            Notes:
                Physical port name this uplink belongs to.

                
                This attribute is named `portName` in VSD API.
                
        """
        return self._port_name

    @port_name.setter
    def port_name(self, value):
        """ Set port_name value.

            Notes:
                Physical port name this uplink belongs to.

                
                This attribute is named `portName` in VSD API.
                
        """
        self._port_name = value

    
    @property
    def download_rate_limit(self):
        """ Get download_rate_limit value.

            Notes:
                Download rate limit for this uplink in Mb/s.

                
                This attribute is named `downloadRateLimit` in VSD API.
                
        """
        return self._download_rate_limit

    @download_rate_limit.setter
    def download_rate_limit(self, value):
        """ Set download_rate_limit value.

            Notes:
                Download rate limit for this uplink in Mb/s.

                
                This attribute is named `downloadRateLimit` in VSD API.
                
        """
        self._download_rate_limit = value

    
    @property
    def uplink_id(self):
        """ Get uplink_id value.

            Notes:
                ID that unqiuely identifies the uplink.

                
                This attribute is named `uplinkID` in VSD API.
                
        """
        return self._uplink_id

    @uplink_id.setter
    def uplink_id(self, value):
        """ Set uplink_id value.

            Notes:
                ID that unqiuely identifies the uplink.

                
                This attribute is named `uplinkID` in VSD API.
                
        """
        self._uplink_id = value

    
    @property
    def username(self):
        """ Get username value.

            Notes:
                PPPoE username if uplink mode is set to PPPoE.

                
        """
        return self._username

    @username.setter
    def username(self, value):
        """ Set username value.

            Notes:
                PPPoE username if uplink mode is set to PPPoE.

                
        """
        self._username = value

    
    @property
    def assoc_underlay_id(self):
        """ Get assoc_underlay_id value.

            Notes:
                UUID of the underlay associated to the uplink.

                
                This attribute is named `assocUnderlayID` in VSD API.
                
        """
        return self._assoc_underlay_id

    @assoc_underlay_id.setter
    def assoc_underlay_id(self, value):
        """ Set assoc_underlay_id value.

            Notes:
                UUID of the underlay associated to the uplink.

                
                This attribute is named `assocUnderlayID` in VSD API.
                
        """
        self._assoc_underlay_id = value

    
    @property
    def associated_bgp_neighbor_id(self):
        """ Get associated_bgp_neighbor_id value.

            Notes:
                UUID of BGP Neighbor associated to the Uplink which will be used for Bootstrap. This is mandatory if a secondaryAddress is defined.

                
                This attribute is named `associatedBGPNeighborID` in VSD API.
                
        """
        return self._associated_bgp_neighbor_id

    @associated_bgp_neighbor_id.setter
    def associated_bgp_neighbor_id(self, value):
        """ Set associated_bgp_neighbor_id value.

            Notes:
                UUID of BGP Neighbor associated to the Uplink which will be used for Bootstrap. This is mandatory if a secondaryAddress is defined.

                
                This attribute is named `associatedBGPNeighborID` in VSD API.
                
        """
        self._associated_bgp_neighbor_id = value

    
    @property
    def associated_underlay_name(self):
        """ Get associated_underlay_name value.

            Notes:
                The display name of the Underlay instance associated with this uplink connection.

                
                This attribute is named `associatedUnderlayName` in VSD API.
                
        """
        return self._associated_underlay_name

    @associated_underlay_name.setter
    def associated_underlay_name(self, value):
        """ Set associated_underlay_name value.

            Notes:
                The display name of the Underlay instance associated with this uplink connection.

                
                This attribute is named `associatedUnderlayName` in VSD API.
                
        """
        self._associated_underlay_name = value

    
    @property
    def auxiliary_link(self):
        """ Get auxiliary_link value.

            Notes:
                Make this uplink an auxiliary one that will only come up when all other uplinks are disconnected or can't perform their role.

                
                This attribute is named `auxiliaryLink` in VSD API.
                
        """
        return self._auxiliary_link

    @auxiliary_link.setter
    def auxiliary_link(self, value):
        """ Set auxiliary_link value.

            Notes:
                Make this uplink an auxiliary one that will only come up when all other uplinks are disconnected or can't perform their role.

                
                This attribute is named `auxiliaryLink` in VSD API.
                
        """
        self._auxiliary_link = value

    
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

    

    