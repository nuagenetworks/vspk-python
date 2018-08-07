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


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUShuntLink(NURESTObject):
    """ Represents a ShuntLink in the VSD

        Notes:
            A shunt link represents an alliance of uplink interface resources between two NSGs belonging to a Redundant Group.  An operator specifies which network port-VLAN from each NSG peers to be considered as shunted together so that control uplinks from each NSG may be used by the other.
    """

    __rest_name__ = "shuntlink"
    __resource_name__ = "shuntlinks"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a ShuntLink instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> shuntlink = NUShuntLink(id=u'xxxx-xxx-xxx-xxx', name=u'ShuntLink')
                >>> shuntlink = NUShuntLink(data=my_dict)
        """

        super(NUShuntLink, self).__init__()

        # Read/Write Attributes
        
        self._vlan_peer1_id = None
        self._vlan_peer2_id = None
        self._name = None
        self._last_updated_by = None
        self._gateway_peer1_id = None
        self._gateway_peer2_id = None
        self._peer1_ip_address = None
        self._peer1_subnet = None
        self._peer2_ip_address = None
        self._peer2_subnet = None
        self._description = None
        self._entity_scope = None
        self._external_id = None
        
        self.expose_attribute(local_name="vlan_peer1_id", remote_name="VLANPeer1ID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="vlan_peer2_id", remote_name="VLANPeer2ID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_peer1_id", remote_name="gatewayPeer1ID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_peer2_id", remote_name="gatewayPeer2ID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer1_ip_address", remote_name="peer1IPAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer1_subnet", remote_name="peer1Subnet", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer2_ip_address", remote_name="peer2IPAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer2_subnet", remote_name="peer2Subnet", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vlan_peer1_id(self):
        """ Get vlan_peer1_id value.

            Notes:
                The ID of the shunted VLAN from the first NSG of the redundant gateway group.

                
                This attribute is named `VLANPeer1ID` in VSD API.
                
        """
        return self._vlan_peer1_id

    @vlan_peer1_id.setter
    def vlan_peer1_id(self, value):
        """ Set vlan_peer1_id value.

            Notes:
                The ID of the shunted VLAN from the first NSG of the redundant gateway group.

                
                This attribute is named `VLANPeer1ID` in VSD API.
                
        """
        self._vlan_peer1_id = value

    
    @property
    def vlan_peer2_id(self):
        """ Get vlan_peer2_id value.

            Notes:
                The ID of the shunted VLAN from the second NSG of the redundant gateway group.

                
                This attribute is named `VLANPeer2ID` in VSD API.
                
        """
        return self._vlan_peer2_id

    @vlan_peer2_id.setter
    def vlan_peer2_id(self, value):
        """ Set vlan_peer2_id value.

            Notes:
                The ID of the shunted VLAN from the second NSG of the redundant gateway group.

                
                This attribute is named `VLANPeer2ID` in VSD API.
                
        """
        self._vlan_peer2_id = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name auto-generated by VSD and given to a newly created Shunt Link.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name auto-generated by VSD and given to a newly created Shunt Link.

                
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
    def gateway_peer1_id(self):
        """ Get gateway_peer1_id value.

            Notes:
                The ID of the first NSG of the redundant gateway group part of this Shunt Link.

                
                This attribute is named `gatewayPeer1ID` in VSD API.
                
        """
        return self._gateway_peer1_id

    @gateway_peer1_id.setter
    def gateway_peer1_id(self, value):
        """ Set gateway_peer1_id value.

            Notes:
                The ID of the first NSG of the redundant gateway group part of this Shunt Link.

                
                This attribute is named `gatewayPeer1ID` in VSD API.
                
        """
        self._gateway_peer1_id = value

    
    @property
    def gateway_peer2_id(self):
        """ Get gateway_peer2_id value.

            Notes:
                The ID of the second NSG of the redundant gateway group part of this Shunt Link.

                
                This attribute is named `gatewayPeer2ID` in VSD API.
                
        """
        return self._gateway_peer2_id

    @gateway_peer2_id.setter
    def gateway_peer2_id(self, value):
        """ Set gateway_peer2_id value.

            Notes:
                The ID of the second NSG of the redundant gateway group part of this Shunt Link.

                
                This attribute is named `gatewayPeer2ID` in VSD API.
                
        """
        self._gateway_peer2_id = value

    
    @property
    def peer1_ip_address(self):
        """ Get peer1_ip_address value.

            Notes:
                The IP address of the first peer of the Shunt Link.

                
                This attribute is named `peer1IPAddress` in VSD API.
                
        """
        return self._peer1_ip_address

    @peer1_ip_address.setter
    def peer1_ip_address(self, value):
        """ Set peer1_ip_address value.

            Notes:
                The IP address of the first peer of the Shunt Link.

                
                This attribute is named `peer1IPAddress` in VSD API.
                
        """
        self._peer1_ip_address = value

    
    @property
    def peer1_subnet(self):
        """ Get peer1_subnet value.

            Notes:
                The subnet given to the first peer of the Shunt Link.

                
                This attribute is named `peer1Subnet` in VSD API.
                
        """
        return self._peer1_subnet

    @peer1_subnet.setter
    def peer1_subnet(self, value):
        """ Set peer1_subnet value.

            Notes:
                The subnet given to the first peer of the Shunt Link.

                
                This attribute is named `peer1Subnet` in VSD API.
                
        """
        self._peer1_subnet = value

    
    @property
    def peer2_ip_address(self):
        """ Get peer2_ip_address value.

            Notes:
                The IP address of the second peer of the Shunt Link.

                
                This attribute is named `peer2IPAddress` in VSD API.
                
        """
        return self._peer2_ip_address

    @peer2_ip_address.setter
    def peer2_ip_address(self, value):
        """ Set peer2_ip_address value.

            Notes:
                The IP address of the second peer of the Shunt Link.

                
                This attribute is named `peer2IPAddress` in VSD API.
                
        """
        self._peer2_ip_address = value

    
    @property
    def peer2_subnet(self):
        """ Get peer2_subnet value.

            Notes:
                The subnet on the second peer of the Shunt Link.

                
                This attribute is named `peer2Subnet` in VSD API.
                
        """
        return self._peer2_subnet

    @peer2_subnet.setter
    def peer2_subnet(self, value):
        """ Set peer2_subnet value.

            Notes:
                The subnet on the second peer of the Shunt Link.

                
                This attribute is named `peer2Subnet` in VSD API.
                
        """
        self._peer2_subnet = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Extra information entered by the operator to define the Shunt Link.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Extra information entered by the operator to define the Shunt Link.

                
        """
        self._description = value

    
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

    

    