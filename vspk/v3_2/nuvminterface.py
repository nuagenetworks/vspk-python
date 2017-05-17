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



from .fetchers import NUTCAsFetcher


from .fetchers import NURedirectionTargetsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUDHCPOptionsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUPolicyDecisionsFetcher


from .fetchers import NUPolicyGroupsFetcher


from .fetchers import NUStaticRoutesFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUMultiCastChannelMapsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUVMInterface(NURESTObject):
    """ Represents a VMInterface in the VSD

        Notes:
            Read only API that can retrieve the VM interface associated with a domain, zone or subnet for mediation created VM's for REST created  VM interfaces you need to set the additional proxy header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example :bob@Alcatel Lucent), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header.
    """

    __rest_name__ = "vminterface"
    __resource_name__ = "vminterfaces"

    
    ## Constants
    
    CONST_ATTACHED_NETWORK_TYPE_L2DOMAIN = "L2DOMAIN"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ATTACHED_NETWORK_TYPE_SUBNET = "SUBNET"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VMInterface instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vminterface = NUVMInterface(id=u'xxxx-xxx-xxx-xxx', name=u'VMInterface')
                >>> vminterface = NUVMInterface(data=my_dict)
        """

        super(NUVMInterface, self).__init__()

        # Read/Write Attributes
        
        self._mac = None
        self._vmuuid = None
        self._ip_address = None
        self._vport_id = None
        self._vport_name = None
        self._name = None
        self._last_updated_by = None
        self._gateway = None
        self._netmask = None
        self._network_name = None
        self._tier_id = None
        self._entity_scope = None
        self._policy_decision_id = None
        self._domain_id = None
        self._domain_name = None
        self._zone_id = None
        self._zone_name = None
        self._associated_floating_ip_address = None
        self._attached_network_id = None
        self._attached_network_type = None
        self._multi_nic_vport_name = None
        self._external_id = None
        
        self.expose_attribute(local_name="mac", remote_name="MAC", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vmuuid", remote_name="VMUUID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ip_address", remote_name="IPAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vport_id", remote_name="VPortID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vport_name", remote_name="VPortName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway", remote_name="gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_name", remote_name="networkName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tier_id", remote_name="tierID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="policy_decision_id", remote_name="policyDecisionID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="domain_id", remote_name="domainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="domain_name", remote_name="domainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zone_id", remote_name="zoneID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zone_name", remote_name="zoneName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_floating_ip_address", remote_name="associatedFloatingIPAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="attached_network_id", remote_name="attachedNetworkID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="attached_network_type", remote_name="attachedNetworkType", attribute_type=str, is_required=False, is_unique=False, choices=[u'L2DOMAIN', u'SUBNET'])
        self.expose_attribute(local_name="multi_nic_vport_name", remote_name="multiNICVPortName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.redirection_targets = NURedirectionTargetsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.dhcp_options = NUDHCPOptionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.policy_decisions = NUPolicyDecisionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.policy_groups = NUPolicyGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.static_routes = NUStaticRoutesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.multi_cast_channel_maps = NUMultiCastChannelMapsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def mac(self):
        """ Get mac value.

            Notes:
                MAC address of the  interface

                
                This attribute is named `MAC` in VSD API.
                
        """
        return self._mac

    @mac.setter
    def mac(self, value):
        """ Set mac value.

            Notes:
                MAC address of the  interface

                
                This attribute is named `MAC` in VSD API.
                
        """
        self._mac = value

    
    @property
    def vmuuid(self):
        """ Get vmuuid value.

            Notes:
                UUID of the associated virtual machine

                
                This attribute is named `VMUUID` in VSD API.
                
        """
        return self._vmuuid

    @vmuuid.setter
    def vmuuid(self, value):
        """ Set vmuuid value.

            Notes:
                UUID of the associated virtual machine

                
                This attribute is named `VMUUID` in VSD API.
                
        """
        self._vmuuid = value

    
    @property
    def ip_address(self):
        """ Get ip_address value.

            Notes:
                IP address of the  interface

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        """ Set ip_address value.

            Notes:
                IP address of the  interface

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        self._ip_address = value

    
    @property
    def vport_id(self):
        """ Get vport_id value.

            Notes:
                ID of the vport that the interface is attached to

                
                This attribute is named `VPortID` in VSD API.
                
        """
        return self._vport_id

    @vport_id.setter
    def vport_id(self, value):
        """ Set vport_id value.

            Notes:
                ID of the vport that the interface is attached to

                
                This attribute is named `VPortID` in VSD API.
                
        """
        self._vport_id = value

    
    @property
    def vport_name(self):
        """ Get vport_name value.

            Notes:
                Name of the vport that the VM is attached to

                
                This attribute is named `VPortName` in VSD API.
                
        """
        return self._vport_name

    @vport_name.setter
    def vport_name(self, value):
        """ Set vport_name value.

            Notes:
                Name of the vport that the VM is attached to

                
                This attribute is named `VPortName` in VSD API.
                
        """
        self._vport_name = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Device name associated with this interface

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Device name associated with this interface

                
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
    def gateway(self):
        """ Get gateway value.

            Notes:
                Gateway of the subnet that the VM is connected to

                
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """ Set gateway value.

            Notes:
                Gateway of the subnet that the VM is connected to

                
        """
        self._gateway = value

    
    @property
    def netmask(self):
        """ Get netmask value.

            Notes:
                Netmask of the subnet that the VM is attached to

                
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """ Set netmask value.

            Notes:
                Netmask of the subnet that the VM is attached to

                
        """
        self._netmask = value

    
    @property
    def network_name(self):
        """ Get network_name value.

            Notes:
                Name of the network that the VM is attached to

                
                This attribute is named `networkName` in VSD API.
                
        """
        return self._network_name

    @network_name.setter
    def network_name(self, value):
        """ Set network_name value.

            Notes:
                Name of the network that the VM is attached to

                
                This attribute is named `networkName` in VSD API.
                
        """
        self._network_name = value

    
    @property
    def tier_id(self):
        """ Get tier_id value.

            Notes:
                ID of the tier that the interface is attached to.

                
                This attribute is named `tierID` in VSD API.
                
        """
        return self._tier_id

    @tier_id.setter
    def tier_id(self, value):
        """ Set tier_id value.

            Notes:
                ID of the tier that the interface is attached to.

                
                This attribute is named `tierID` in VSD API.
                
        """
        self._tier_id = value

    
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
    def policy_decision_id(self):
        """ Get policy_decision_id value.

            Notes:
                The policy decision ID for this particular  interface

                
                This attribute is named `policyDecisionID` in VSD API.
                
        """
        return self._policy_decision_id

    @policy_decision_id.setter
    def policy_decision_id(self, value):
        """ Set policy_decision_id value.

            Notes:
                The policy decision ID for this particular  interface

                
                This attribute is named `policyDecisionID` in VSD API.
                
        """
        self._policy_decision_id = value

    
    @property
    def domain_id(self):
        """ Get domain_id value.

            Notes:
                ID of the domain that the VM is attached to

                
                This attribute is named `domainID` in VSD API.
                
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, value):
        """ Set domain_id value.

            Notes:
                ID of the domain that the VM is attached to

                
                This attribute is named `domainID` in VSD API.
                
        """
        self._domain_id = value

    
    @property
    def domain_name(self):
        """ Get domain_name value.

            Notes:
                Name of the domain that the VM is attached to

                
                This attribute is named `domainName` in VSD API.
                
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        """ Set domain_name value.

            Notes:
                Name of the domain that the VM is attached to

                
                This attribute is named `domainName` in VSD API.
                
        """
        self._domain_name = value

    
    @property
    def zone_id(self):
        """ Get zone_id value.

            Notes:
                ID of the zone that the interface is attached to

                
                This attribute is named `zoneID` in VSD API.
                
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, value):
        """ Set zone_id value.

            Notes:
                ID of the zone that the interface is attached to

                
                This attribute is named `zoneID` in VSD API.
                
        """
        self._zone_id = value

    
    @property
    def zone_name(self):
        """ Get zone_name value.

            Notes:
                Name of the zone that the VM is attached to

                
                This attribute is named `zoneName` in VSD API.
                
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value):
        """ Set zone_name value.

            Notes:
                Name of the zone that the VM is attached to

                
                This attribute is named `zoneName` in VSD API.
                
        """
        self._zone_name = value

    
    @property
    def associated_floating_ip_address(self):
        """ Get associated_floating_ip_address value.

            Notes:
                Floating Ip Address of this network interface eg: 10.1.2.1

                
                This attribute is named `associatedFloatingIPAddress` in VSD API.
                
        """
        return self._associated_floating_ip_address

    @associated_floating_ip_address.setter
    def associated_floating_ip_address(self, value):
        """ Set associated_floating_ip_address value.

            Notes:
                Floating Ip Address of this network interface eg: 10.1.2.1

                
                This attribute is named `associatedFloatingIPAddress` in VSD API.
                
        """
        self._associated_floating_ip_address = value

    
    @property
    def attached_network_id(self):
        """ Get attached_network_id value.

            Notes:
                ID of the l2 domain or Subnet that the VM is attached to

                
                This attribute is named `attachedNetworkID` in VSD API.
                
        """
        return self._attached_network_id

    @attached_network_id.setter
    def attached_network_id(self, value):
        """ Set attached_network_id value.

            Notes:
                ID of the l2 domain or Subnet that the VM is attached to

                
                This attribute is named `attachedNetworkID` in VSD API.
                
        """
        self._attached_network_id = value

    
    @property
    def attached_network_type(self):
        """ Get attached_network_type value.

            Notes:
                l2 domain or Subnet that the interface is attached to

                
                This attribute is named `attachedNetworkType` in VSD API.
                
        """
        return self._attached_network_type

    @attached_network_type.setter
    def attached_network_type(self, value):
        """ Set attached_network_type value.

            Notes:
                l2 domain or Subnet that the interface is attached to

                
                This attribute is named `attachedNetworkType` in VSD API.
                
        """
        self._attached_network_type = value

    
    @property
    def multi_nic_vport_name(self):
        """ Get multi_nic_vport_name value.

            Notes:
                Name of the Multi NIC VPort associated with this VM Interface

                
                This attribute is named `multiNICVPortName` in VSD API.
                
        """
        return self._multi_nic_vport_name

    @multi_nic_vport_name.setter
    def multi_nic_vport_name(self, value):
        """ Set multi_nic_vport_name value.

            Notes:
                Name of the Multi NIC VPort associated with this VM Interface

                
                This attribute is named `multiNICVPortName` in VSD API.
                
        """
        self._multi_nic_vport_name = value

    
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

    

    