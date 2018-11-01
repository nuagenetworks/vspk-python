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


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUUplinkConnectionsFetcher


from .fetchers import NUBRConnectionsFetcher

from bambou import NURESTObject


class NUVLANTemplate(NURESTObject):
    """ Represents a VLANTemplate in the VSD

        Notes:
            Represents VLAN Template under a Port Template object.
    """

    __rest_name__ = "vlantemplate"
    __resource_name__ = "vlantemplates"

    
    ## Constants
    
    CONST_ASSOCIATED_CONNECTION_TYPE_UPLINK_CONNECTION = "UPLINK_CONNECTION"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ASSOCIATED_CONNECTION_TYPE_BR_CONNECTION = "BR_CONNECTION"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_TYPE_DUC = "DUC"
    
    CONST_TYPE_ACCESS = "ACCESS"
    
    CONST_TYPE_BR = "BR"
    
    CONST_TYPE_UPLINK = "UPLINK"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VLANTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vlantemplate = NUVLANTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'VLANTemplate')
                >>> vlantemplate = NUVLANTemplate(data=my_dict)
        """

        super(NUVLANTemplate, self).__init__()

        # Read/Write Attributes
        
        self._value = None
        self._last_updated_by = None
        self._description = None
        self._entity_scope = None
        self._is_uplink = None
        self._associated_connection_type = None
        self._associated_egress_qos_policy_id = None
        self._associated_ingress_overlay_qo_s_policer_id = None
        self._associated_ingress_qos_policy_id = None
        self._associated_ingress_underlay_qo_s_policer_id = None
        self._associated_uplink_connection_id = None
        self._associated_vsc_profile_id = None
        self._duc_vlan = None
        self._external_id = None
        self._type = None
        
        self.expose_attribute(local_name="value", remote_name="value", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="is_uplink", remote_name="isUplink", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_connection_type", remote_name="associatedConnectionType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BR_CONNECTION', u'UPLINK_CONNECTION'])
        self.expose_attribute(local_name="associated_egress_qos_policy_id", remote_name="associatedEgressQOSPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ingress_overlay_qo_s_policer_id", remote_name="associatedIngressOverlayQoSPolicerID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ingress_qos_policy_id", remote_name="associatedIngressQOSPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ingress_underlay_qo_s_policer_id", remote_name="associatedIngressUnderlayQoSPolicerID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_uplink_connection_id", remote_name="associatedUplinkConnectionID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_vsc_profile_id", remote_name="associatedVSCProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="duc_vlan", remote_name="ducVlan", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=False, is_unique=False, choices=[u'ACCESS', u'BR', u'DUC', u'UPLINK'])
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.uplink_connections = NUUplinkConnectionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.br_connections = NUBRConnectionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def value(self):
        """ Get value value.

            Notes:
                Value or ID of VLAN instances to be created from this template.

                
        """
        return self._value

    @value.setter
    def value(self, value):
        """ Set value value.

            Notes:
                Value or ID of VLAN instances to be created from this template.

                
        """
        self._value = value

    
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
    def is_uplink(self):
        """ Get is_uplink value.

            Notes:
                Indicates that this VLAN Template should be considered as being used for uplink connection.

                
                This attribute is named `isUplink` in VSD API.
                
        """
        return self._is_uplink

    @is_uplink.setter
    def is_uplink(self, value):
        """ Set is_uplink value.

            Notes:
                Indicates that this VLAN Template should be considered as being used for uplink connection.

                
                This attribute is named `isUplink` in VSD API.
                
        """
        self._is_uplink = value

    
    @property
    def associated_connection_type(self):
        """ Get associated_connection_type value.

            Notes:
                States the managed object type of the uplink connection associated to this VLAN Template instance.

                
                This attribute is named `associatedConnectionType` in VSD API.
                
        """
        return self._associated_connection_type

    @associated_connection_type.setter
    def associated_connection_type(self, value):
        """ Set associated_connection_type value.

            Notes:
                States the managed object type of the uplink connection associated to this VLAN Template instance.

                
                This attribute is named `associatedConnectionType` in VSD API.
                
        """
        self._associated_connection_type = value

    
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
    def associated_ingress_overlay_qo_s_policer_id(self):
        """ Get associated_ingress_overlay_qo_s_policer_id value.

            Notes:
                ID of the Ingress Overlay QoS Policer associated with a VLAN.

                
                This attribute is named `associatedIngressOverlayQoSPolicerID` in VSD API.
                
        """
        return self._associated_ingress_overlay_qo_s_policer_id

    @associated_ingress_overlay_qo_s_policer_id.setter
    def associated_ingress_overlay_qo_s_policer_id(self, value):
        """ Set associated_ingress_overlay_qo_s_policer_id value.

            Notes:
                ID of the Ingress Overlay QoS Policer associated with a VLAN.

                
                This attribute is named `associatedIngressOverlayQoSPolicerID` in VSD API.
                
        """
        self._associated_ingress_overlay_qo_s_policer_id = value

    
    @property
    def associated_ingress_qos_policy_id(self):
        """ Get associated_ingress_qos_policy_id value.

            Notes:
                ID of the Ingress QoS Policy associated with this VLAN Template.

                
                This attribute is named `associatedIngressQOSPolicyID` in VSD API.
                
        """
        return self._associated_ingress_qos_policy_id

    @associated_ingress_qos_policy_id.setter
    def associated_ingress_qos_policy_id(self, value):
        """ Set associated_ingress_qos_policy_id value.

            Notes:
                ID of the Ingress QoS Policy associated with this VLAN Template.

                
                This attribute is named `associatedIngressQOSPolicyID` in VSD API.
                
        """
        self._associated_ingress_qos_policy_id = value

    
    @property
    def associated_ingress_underlay_qo_s_policer_id(self):
        """ Get associated_ingress_underlay_qo_s_policer_id value.

            Notes:
                ID of the Ingress Underlay QoS Policer associated with a VLAN.

                
                This attribute is named `associatedIngressUnderlayQoSPolicerID` in VSD API.
                
        """
        return self._associated_ingress_underlay_qo_s_policer_id

    @associated_ingress_underlay_qo_s_policer_id.setter
    def associated_ingress_underlay_qo_s_policer_id(self, value):
        """ Set associated_ingress_underlay_qo_s_policer_id value.

            Notes:
                ID of the Ingress Underlay QoS Policer associated with a VLAN.

                
                This attribute is named `associatedIngressUnderlayQoSPolicerID` in VSD API.
                
        """
        self._associated_ingress_underlay_qo_s_policer_id = value

    
    @property
    def associated_uplink_connection_id(self):
        """ Get associated_uplink_connection_id value.

            Notes:
                ID of the uplink connection making use of this VLAN Template instance.

                
                This attribute is named `associatedUplinkConnectionID` in VSD API.
                
        """
        return self._associated_uplink_connection_id

    @associated_uplink_connection_id.setter
    def associated_uplink_connection_id(self, value):
        """ Set associated_uplink_connection_id value.

            Notes:
                ID of the uplink connection making use of this VLAN Template instance.

                
                This attribute is named `associatedUplinkConnectionID` in VSD API.
                
        """
        self._associated_uplink_connection_id = value

    
    @property
    def associated_vsc_profile_id(self):
        """ Get associated_vsc_profile_id value.

            Notes:
                The ID of the infrastructure VSC profile this is associated with this instance of a vlan or vlan template.

                
                This attribute is named `associatedVSCProfileID` in VSD API.
                
        """
        return self._associated_vsc_profile_id

    @associated_vsc_profile_id.setter
    def associated_vsc_profile_id(self, value):
        """ Set associated_vsc_profile_id value.

            Notes:
                The ID of the infrastructure VSC profile this is associated with this instance of a vlan or vlan template.

                
                This attribute is named `associatedVSCProfileID` in VSD API.
                
        """
        self._associated_vsc_profile_id = value

    
    @property
    def duc_vlan(self):
        """ Get duc_vlan value.

            Notes:
                When set to true, this specifies that this VLAN template instance serves as an underlay connection endpoint on an NSG-UBR gateway.

                
                This attribute is named `ducVlan` in VSD API.
                
        """
        return self._duc_vlan

    @duc_vlan.setter
    def duc_vlan(self, value):
        """ Set duc_vlan value.

            Notes:
                When set to true, this specifies that this VLAN template instance serves as an underlay connection endpoint on an NSG-UBR gateway.

                
                This attribute is named `ducVlan` in VSD API.
                
        """
        self._duc_vlan = value

    
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
                This type marks a VLAN for its utility.

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                This type marks a VLAN for its utility.

                
        """
        self._type = value

    

    
    ## Custom methods
    def is_template(self):
        """ Verify that the object is a template
    
            Returns:
                (bool): True if the object is a template
        """
        return True
    
    def is_from_template(self):
        """ Verify if the object has been instantiated from a template
    
            Note:
                The object has to be fetched. Otherwise, it does not
                have information from its parent
    
            Returns:
                (bool): True if the object is a template
        """
        return False
    