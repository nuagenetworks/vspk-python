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



from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUVLANsFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUEnterprisePermissionsFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUStatisticsPoliciesFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUNSPort(NURESTObject):
    """ Represents a NSPort in the VSD

        Notes:
            Represents a Port of a particular NS Gateway object.
    """

    __rest_name__ = "nsport"
    __resource_name__ = "nsports"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_SPEED_BASE10 = "BASE10"
    
    CONST_SPEED_BASETX100 = "BASETX100"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_PORT_TYPE_ACCESS = "ACCESS"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_SPEED_BASET1000 = "BASET1000"
    
    CONST_STATUS_INITIALIZED = "INITIALIZED"
    
    CONST_SPEED_BASEX10G = "BASEX10G"
    
    CONST_PORT_TYPE_NETWORK = "NETWORK"
    
    CONST_NAT_TRAVERSAL_FULL_NAT = "FULL_NAT"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_NAT_TRAVERSAL_NONE = "NONE"
    
    CONST_STATUS_MISMATCH = "MISMATCH"
    
    CONST_STATUS_ORPHAN = "ORPHAN"
    
    CONST_SPEED_AUTONEGOTIATE = "AUTONEGOTIATE"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_NAT_TRAVERSAL_ONE_TO_ONE_NAT = "ONE_TO_ONE_NAT"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_STATUS_READY = "READY"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NSPort instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsport = NUNSPort(id=u'xxxx-xxx-xxx-xxx', name=u'NSPort')
                >>> nsport = NUNSPort(data=my_dict)
        """

        super(NUNSPort, self).__init__()

        # Read/Write Attributes
        
        self._nat_traversal = None
        self._vlan_range = None
        self._name = None
        self._last_updated_by = None
        self._template_id = None
        self._permitted_action = None
        self._description = None
        self._physical_name = None
        self._entity_scope = None
        self._port_type = None
        self._speed = None
        self._use_user_mnemonic = None
        self._user_mnemonic = None
        self._associated_egress_qos_policy_id = None
        self._associated_redundant_port_id = None
        self._status = None
        self._mtu = None
        self._external_id = None
        
        self.expose_attribute(local_name="nat_traversal", remote_name="NATTraversal", attribute_type=str, is_required=False, is_unique=False, choices=[u'FULL_NAT', u'NONE', u'ONE_TO_ONE_NAT'])
        self.expose_attribute(local_name="vlan_range", remote_name="VLANRange", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="physical_name", remote_name="physicalName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="port_type", remote_name="portType", attribute_type=str, is_required=True, is_unique=False, choices=[u'ACCESS', u'NETWORK'])
        self.expose_attribute(local_name="speed", remote_name="speed", attribute_type=str, is_required=False, is_unique=False, choices=[u'AUTONEGOTIATE', u'BASE10', u'BASET1000', u'BASETX100', u'BASEX10G'])
        self.expose_attribute(local_name="use_user_mnemonic", remote_name="useUserMnemonic", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="user_mnemonic", remote_name="userMnemonic", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="associated_egress_qos_policy_id", remote_name="associatedEgressQOSPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_redundant_port_id", remote_name="associatedRedundantPortID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'INITIALIZED', u'MISMATCH', u'ORPHAN', u'READY'])
        self.expose_attribute(local_name="mtu", remote_name="mtu", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vlans = NUVLANsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def nat_traversal(self):
        """ Get nat_traversal value.

            Notes:
                Enum value that states the type of NAT Traversal the NSG instance will use to talk to other NSGs and the Internet.

                
                This attribute is named `NATTraversal` in VSD API.
                
        """
        return self._nat_traversal

    @nat_traversal.setter
    def nat_traversal(self, value):
        """ Set nat_traversal value.

            Notes:
                Enum value that states the type of NAT Traversal the NSG instance will use to talk to other NSGs and the Internet.

                
                This attribute is named `NATTraversal` in VSD API.
                
        """
        self._nat_traversal = value

    
    @property
    def vlan_range(self):
        """ Get vlan_range value.

            Notes:
                VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        return self._vlan_range

    @vlan_range.setter
    def vlan_range(self, value):
        """ Set vlan_range value.

            Notes:
                VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        self._vlan_range = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Port

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Port

                
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
    def template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the template that this Port was created from

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the template that this Port was created from

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    
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
                A description of the Port

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the Port

                
        """
        self._description = value

    
    @property
    def physical_name(self):
        """ Get physical_name value.

            Notes:
                Identifier of the Port

                
                This attribute is named `physicalName` in VSD API.
                
        """
        return self._physical_name

    @physical_name.setter
    def physical_name(self, value):
        """ Set physical_name value.

            Notes:
                Identifier of the Port

                
                This attribute is named `physicalName` in VSD API.
                
        """
        self._physical_name = value

    
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
    def port_type(self):
        """ Get port_type value.

            Notes:
                Type of the Port.

                
                This attribute is named `portType` in VSD API.
                
        """
        return self._port_type

    @port_type.setter
    def port_type(self, value):
        """ Set port_type value.

            Notes:
                Type of the Port.

                
                This attribute is named `portType` in VSD API.
                
        """
        self._port_type = value

    
    @property
    def speed(self):
        """ Get speed value.

            Notes:
                Port Speed in Mb/s :  Supported Ethernet speeds are 10 (10Base-T), 100 (Fast-ethernet 100Base-TX), 1000 (Gigabit Ethernet 1000Base-T), 10 000 (10 Gigabit Ethernet 10GBase-X), and Auto-Negotiate.

                
        """
        return self._speed

    @speed.setter
    def speed(self, value):
        """ Set speed value.

            Notes:
                Port Speed in Mb/s :  Supported Ethernet speeds are 10 (10Base-T), 100 (Fast-ethernet 100Base-TX), 1000 (Gigabit Ethernet 1000Base-T), 10 000 (10 Gigabit Ethernet 10GBase-X), and Auto-Negotiate.

                
        """
        self._speed = value

    
    @property
    def use_user_mnemonic(self):
        """ Get use_user_mnemonic value.

            Notes:
                determines whether to use user mnemonic of the Port

                
                This attribute is named `useUserMnemonic` in VSD API.
                
        """
        return self._use_user_mnemonic

    @use_user_mnemonic.setter
    def use_user_mnemonic(self, value):
        """ Set use_user_mnemonic value.

            Notes:
                determines whether to use user mnemonic of the Port

                
                This attribute is named `useUserMnemonic` in VSD API.
                
        """
        self._use_user_mnemonic = value

    
    @property
    def user_mnemonic(self):
        """ Get user_mnemonic value.

            Notes:
                user mnemonic of the Port

                
                This attribute is named `userMnemonic` in VSD API.
                
        """
        return self._user_mnemonic

    @user_mnemonic.setter
    def user_mnemonic(self, value):
        """ Set user_mnemonic value.

            Notes:
                user mnemonic of the Port

                
                This attribute is named `userMnemonic` in VSD API.
                
        """
        self._user_mnemonic = value

    
    @property
    def associated_egress_qos_policy_id(self):
        """ Get associated_egress_qos_policy_id value.

            Notes:
                ID of the Egress QOS Policy associated with this Vlan.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        return self._associated_egress_qos_policy_id

    @associated_egress_qos_policy_id.setter
    def associated_egress_qos_policy_id(self, value):
        """ Set associated_egress_qos_policy_id value.

            Notes:
                ID of the Egress QOS Policy associated with this Vlan.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        self._associated_egress_qos_policy_id = value

    
    @property
    def associated_redundant_port_id(self):
        """ Get associated_redundant_port_id value.

            Notes:
                ID of the redundant port to which the Port is associated to.

                
                This attribute is named `associatedRedundantPortID` in VSD API.
                
        """
        return self._associated_redundant_port_id

    @associated_redundant_port_id.setter
    def associated_redundant_port_id(self, value):
        """ Set associated_redundant_port_id value.

            Notes:
                ID of the redundant port to which the Port is associated to.

                
                This attribute is named `associatedRedundantPortID` in VSD API.
                
        """
        self._associated_redundant_port_id = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                Status of the port.

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                Status of the port.

                
        """
        self._status = value

    
    @property
    def mtu(self):
        """ Get mtu value.

            Notes:
                Port MTU (Maximum Transmission Unit) :  The size in octets of the largest protocol data unit (PDU) that the layer can pass on.  The default value is normally 1500 octets for Ethernet v2 and can go up to 9198 for Jumbo Frames.

                
        """
        return self._mtu

    @mtu.setter
    def mtu(self, value):
        """ Set mtu value.

            Notes:
                Port MTU (Maximum Transmission Unit) :  The size in octets of the largest protocol data unit (PDU) that the layer can pass on.  The default value is normally 1500 octets for Ethernet v2 and can go up to 9198 for Jumbo Frames.

                
        """
        self._mtu = value

    
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

    

    