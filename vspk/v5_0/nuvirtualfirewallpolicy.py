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


from .fetchers import NUVirtualFirewallRulesFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUVirtualFirewallPolicy(NURESTObject):
    """ Represents a VirtualFirewallPolicy in the VSD

        Notes:
            Defines the template for a Virtual Firewall Policy that helps to group a set of rules either based on functions or actions 
    """

    __rest_name__ = "virtualfirewallpolicy"
    __resource_name__ = "virtualfirewallpolicies"

    
    ## Constants
    
    CONST_POLICY_STATE_DRAFT = "DRAFT"
    
    CONST_POLICY_STATE_LIVE = "LIVE"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_PRIORITY_TYPE_TOP = "TOP"
    
    CONST_PRIORITY_TYPE_BOTTOM = "BOTTOM"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VirtualFirewallPolicy instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> virtualfirewallpolicy = NUVirtualFirewallPolicy(id=u'xxxx-xxx-xxx-xxx', name=u'VirtualFirewallPolicy')
                >>> virtualfirewallpolicy = NUVirtualFirewallPolicy(data=my_dict)
        """

        super(NUVirtualFirewallPolicy, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._active = None
        self._default_allow_ip = None
        self._default_allow_non_ip = None
        self._default_install_acl_implicit_rules = None
        self._description = None
        self._allow_address_spoof = None
        self._entity_scope = None
        self._policy_state = None
        self._priority = None
        self._priority_type = None
        self._associated_egress_template_id = None
        self._associated_ingress_template_id = None
        self._associated_live_entity_id = None
        self._auto_generate_priority = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="active", remote_name="active", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="default_allow_ip", remote_name="defaultAllowIP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="default_allow_non_ip", remote_name="defaultAllowNonIP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="default_install_acl_implicit_rules", remote_name="defaultInstallACLImplicitRules", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allow_address_spoof", remote_name="allowAddressSpoof", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="policy_state", remote_name="policyState", attribute_type=str, is_required=False, is_unique=False, choices=[u'DRAFT', u'LIVE'])
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="priority_type", remote_name="priorityType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BOTTOM', u'TOP'])
        self.expose_attribute(local_name="associated_egress_template_id", remote_name="associatedEgressTemplateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ingress_template_id", remote_name="associatedIngressTemplateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_live_entity_id", remote_name="associatedLiveEntityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="auto_generate_priority", remote_name="autoGeneratePriority", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.virtual_firewall_rules = NUVirtualFirewallRulesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                A unique name set by an operator identifying the Virtual Firewall Rule Template.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                A unique name set by an operator identifying the Virtual Firewall Rule Template.

                
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
    def active(self):
        """ Get active value.

            Notes:
                If enabled, it means that this rule is active

                
        """
        return self._active

    @active.setter
    def active(self, value):
        """ Set active value.

            Notes:
                If enabled, it means that this rule is active

                
        """
        self._active = value

    
    @property
    def default_allow_ip(self):
        """ Get default_allow_ip value.

            Notes:
                If enabled a default RUle of Allow All is added as the last entry in the list of rule entries

                
                This attribute is named `defaultAllowIP` in VSD API.
                
        """
        return self._default_allow_ip

    @default_allow_ip.setter
    def default_allow_ip(self, value):
        """ Set default_allow_ip value.

            Notes:
                If enabled a default RUle of Allow All is added as the last entry in the list of rule entries

                
                This attribute is named `defaultAllowIP` in VSD API.
                
        """
        self._default_allow_ip = value

    
    @property
    def default_allow_non_ip(self):
        """ Get default_allow_non_ip value.

            Notes:
                If enabled, non ip traffic will be dropped

                
                This attribute is named `defaultAllowNonIP` in VSD API.
                
        """
        return self._default_allow_non_ip

    @default_allow_non_ip.setter
    def default_allow_non_ip(self, value):
        """ Set default_allow_non_ip value.

            Notes:
                If enabled, non ip traffic will be dropped

                
                This attribute is named `defaultAllowNonIP` in VSD API.
                
        """
        self._default_allow_non_ip = value

    
    @property
    def default_install_acl_implicit_rules(self):
        """ Get default_install_acl_implicit_rules value.

            Notes:
                If enabled, implicit rule will allow intra domain traffic by default

                
                This attribute is named `defaultInstallACLImplicitRules` in VSD API.
                
        """
        return self._default_install_acl_implicit_rules

    @default_install_acl_implicit_rules.setter
    def default_install_acl_implicit_rules(self, value):
        """ Set default_install_acl_implicit_rules value.

            Notes:
                If enabled, implicit rule will allow intra domain traffic by default

                
                This attribute is named `defaultInstallACLImplicitRules` in VSD API.
                
        """
        self._default_install_acl_implicit_rules = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A concise description of the Virtual Firewall Rule Template that gives a small preview of its use.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A concise description of the Virtual Firewall Rule Template that gives a small preview of its use.

                
        """
        self._description = value

    
    @property
    def allow_address_spoof(self):
        """ Get allow_address_spoof value.

            Notes:
                If enabled, it will disable the default anti-spoof Rule for this domain that essentially prevents any VM to send packets that do not originate from that particular VM

                
                This attribute is named `allowAddressSpoof` in VSD API.
                
        """
        return self._allow_address_spoof

    @allow_address_spoof.setter
    def allow_address_spoof(self, value):
        """ Set allow_address_spoof value.

            Notes:
                If enabled, it will disable the default anti-spoof Rule for this domain that essentially prevents any VM to send packets that do not originate from that particular VM

                
                This attribute is named `allowAddressSpoof` in VSD API.
                
        """
        self._allow_address_spoof = value

    
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
    def policy_state(self):
        """ Get policy_state value.

            Notes:
                States if the policy is Live or Draft

                
                This attribute is named `policyState` in VSD API.
                
        """
        return self._policy_state

    @policy_state.setter
    def policy_state(self, value):
        """ Set policy_state value.

            Notes:
                States if the policy is Live or Draft

                
                This attribute is named `policyState` in VSD API.
                
        """
        self._policy_state = value

    
    @property
    def priority(self):
        """ Get priority value.

            Notes:
                The priority of the rule entry that determines the order of entries

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                The priority of the rule entry that determines the order of entries

                
        """
        self._priority = value

    
    @property
    def priority_type(self):
        """ Get priority_type value.

            Notes:
                Possible values: TOP or BOTTOM. TOP and BOTTOM ACL policies can only be defined and managed on the template level. These allow for careful control of Rule priority handling.

                
                This attribute is named `priorityType` in VSD API.
                
        """
        return self._priority_type

    @priority_type.setter
    def priority_type(self, value):
        """ Set priority_type value.

            Notes:
                Possible values: TOP or BOTTOM. TOP and BOTTOM ACL policies can only be defined and managed on the template level. These allow for careful control of Rule priority handling.

                
                This attribute is named `priorityType` in VSD API.
                
        """
        self._priority_type = value

    
    @property
    def associated_egress_template_id(self):
        """ Get associated_egress_template_id value.

            Notes:
                The read only id of the auto generated Egress Template

                
                This attribute is named `associatedEgressTemplateID` in VSD API.
                
        """
        return self._associated_egress_template_id

    @associated_egress_template_id.setter
    def associated_egress_template_id(self, value):
        """ Set associated_egress_template_id value.

            Notes:
                The read only id of the auto generated Egress Template

                
                This attribute is named `associatedEgressTemplateID` in VSD API.
                
        """
        self._associated_egress_template_id = value

    
    @property
    def associated_ingress_template_id(self):
        """ Get associated_ingress_template_id value.

            Notes:
                The read only id of the auto generated Ingress Template

                
                This attribute is named `associatedIngressTemplateID` in VSD API.
                
        """
        return self._associated_ingress_template_id

    @associated_ingress_template_id.setter
    def associated_ingress_template_id(self, value):
        """ Set associated_ingress_template_id value.

            Notes:
                The read only id of the auto generated Ingress Template

                
                This attribute is named `associatedIngressTemplateID` in VSD API.
                
        """
        self._associated_ingress_template_id = value

    
    @property
    def associated_live_entity_id(self):
        """ Get associated_live_entity_id value.

            Notes:
                In the draft mode, the rule entry refers to this LiveEntity. In non-drafted mode, this is null.

                
                This attribute is named `associatedLiveEntityID` in VSD API.
                
        """
        return self._associated_live_entity_id

    @associated_live_entity_id.setter
    def associated_live_entity_id(self, value):
        """ Set associated_live_entity_id value.

            Notes:
                In the draft mode, the rule entry refers to this LiveEntity. In non-drafted mode, this is null.

                
                This attribute is named `associatedLiveEntityID` in VSD API.
                
        """
        self._associated_live_entity_id = value

    
    @property
    def auto_generate_priority(self):
        """ Get auto_generate_priority value.

            Notes:
                This option affects how Rule entry priorities are generated when not specified. If 'false', the priority is generated by incrementing the current highest priority by 100. If 'true', a random priority will be generated, which is advised when creating many entries concurrently without specifying the priority. This will cause the ACL entry to be randomly placed in the existing list of ACL entries. Therefore it is advised to only enable this when allow rules are being created.

                
                This attribute is named `autoGeneratePriority` in VSD API.
                
        """
        return self._auto_generate_priority

    @auto_generate_priority.setter
    def auto_generate_priority(self, value):
        """ Set auto_generate_priority value.

            Notes:
                This option affects how Rule entry priorities are generated when not specified. If 'false', the priority is generated by incrementing the current highest priority by 100. If 'true', a random priority will be generated, which is advised when creating many entries concurrently without specifying the priority. This will cause the ACL entry to be randomly placed in the existing list of ACL entries. Therefore it is advised to only enable this when allow rules are being created.

                
                This attribute is named `autoGeneratePriority` in VSD API.
                
        """
        self._auto_generate_priority = value

    
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

    

    