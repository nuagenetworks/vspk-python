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




from .fetchers import NUDeploymentFailuresFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVPortsFetcher

from bambou import NURESTObject


class NUIngressProfile(NURESTObject):
    """ Represents a IngressProfile in the VSD

        Notes:
            An Ingress Profile represents an aggregation of IP, MAC and ingress QoS profiles that are applied on a VPort instance.
    """

    __rest_name__ = "ingressprofile"
    __resource_name__ = "ingressprofiles"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a IngressProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ingressprofile = NUIngressProfile(id=u'xxxx-xxx-xxx-xxx', name=u'IngressProfile')
                >>> ingressprofile = NUIngressProfile(data=my_dict)
        """

        super(NUIngressProfile, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._description = None
        self._entity_scope = None
        self._assoc_entity_type = None
        self._associated_ip_filter_profile_id = None
        self._associated_ip_filter_profile_name = None
        self._associated_ipv6_filter_profile_id = None
        self._associated_ipv6_filter_profile_name = None
        self._associated_mac_filter_profile_id = None
        self._associated_mac_filter_profile_name = None
        self._associated_sap_ingress_qo_s_profile_id = None
        self._associated_sap_ingress_qo_s_profile_name = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="assoc_entity_type", remote_name="assocEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ip_filter_profile_id", remote_name="associatedIPFilterProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ip_filter_profile_name", remote_name="associatedIPFilterProfileName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ipv6_filter_profile_id", remote_name="associatedIPv6FilterProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ipv6_filter_profile_name", remote_name="associatedIPv6FilterProfileName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_mac_filter_profile_id", remote_name="associatedMACFilterProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_mac_filter_profile_name", remote_name="associatedMACFilterProfileName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_sap_ingress_qo_s_profile_id", remote_name="associatedSAPIngressQoSProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_sap_ingress_qo_s_profile_name", remote_name="associatedSAPIngressQoSProfileName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.deployment_failures = NUDeploymentFailuresFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                A customer friendly name for the Ingress Profile entity.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                A customer friendly name for the Ingress Profile entity.

                
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
    def description(self):
        """ Get description value.

            Notes:
                A customer friendly description of the Ingress Profile entity.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A customer friendly description of the Ingress Profile entity.

                
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
    def assoc_entity_type(self):
        """ Get assoc_entity_type value.

            Notes:
                Type of parent entity

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        return self._assoc_entity_type

    @assoc_entity_type.setter
    def assoc_entity_type(self, value):
        """ Set assoc_entity_type value.

            Notes:
                Type of parent entity

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        self._assoc_entity_type = value

    
    @property
    def associated_ip_filter_profile_id(self):
        """ Get associated_ip_filter_profile_id value.

            Notes:
                UUID of the associated IP Filter Profile entity.

                
                This attribute is named `associatedIPFilterProfileID` in VSD API.
                
        """
        return self._associated_ip_filter_profile_id

    @associated_ip_filter_profile_id.setter
    def associated_ip_filter_profile_id(self, value):
        """ Set associated_ip_filter_profile_id value.

            Notes:
                UUID of the associated IP Filter Profile entity.

                
                This attribute is named `associatedIPFilterProfileID` in VSD API.
                
        """
        self._associated_ip_filter_profile_id = value

    
    @property
    def associated_ip_filter_profile_name(self):
        """ Get associated_ip_filter_profile_name value.

            Notes:
                Name of the associated IP Filter Profile entity.

                
                This attribute is named `associatedIPFilterProfileName` in VSD API.
                
        """
        return self._associated_ip_filter_profile_name

    @associated_ip_filter_profile_name.setter
    def associated_ip_filter_profile_name(self, value):
        """ Set associated_ip_filter_profile_name value.

            Notes:
                Name of the associated IP Filter Profile entity.

                
                This attribute is named `associatedIPFilterProfileName` in VSD API.
                
        """
        self._associated_ip_filter_profile_name = value

    
    @property
    def associated_ipv6_filter_profile_id(self):
        """ Get associated_ipv6_filter_profile_id value.

            Notes:
                UUID of the associated IPv6 Filter Profile entity.

                
                This attribute is named `associatedIPv6FilterProfileID` in VSD API.
                
        """
        return self._associated_ipv6_filter_profile_id

    @associated_ipv6_filter_profile_id.setter
    def associated_ipv6_filter_profile_id(self, value):
        """ Set associated_ipv6_filter_profile_id value.

            Notes:
                UUID of the associated IPv6 Filter Profile entity.

                
                This attribute is named `associatedIPv6FilterProfileID` in VSD API.
                
        """
        self._associated_ipv6_filter_profile_id = value

    
    @property
    def associated_ipv6_filter_profile_name(self):
        """ Get associated_ipv6_filter_profile_name value.

            Notes:
                Name of the associated IPv6 Filter Profile entity.

                
                This attribute is named `associatedIPv6FilterProfileName` in VSD API.
                
        """
        return self._associated_ipv6_filter_profile_name

    @associated_ipv6_filter_profile_name.setter
    def associated_ipv6_filter_profile_name(self, value):
        """ Set associated_ipv6_filter_profile_name value.

            Notes:
                Name of the associated IPv6 Filter Profile entity.

                
                This attribute is named `associatedIPv6FilterProfileName` in VSD API.
                
        """
        self._associated_ipv6_filter_profile_name = value

    
    @property
    def associated_mac_filter_profile_id(self):
        """ Get associated_mac_filter_profile_id value.

            Notes:
                UUID of the associated MAC Filter Profile entity.

                
                This attribute is named `associatedMACFilterProfileID` in VSD API.
                
        """
        return self._associated_mac_filter_profile_id

    @associated_mac_filter_profile_id.setter
    def associated_mac_filter_profile_id(self, value):
        """ Set associated_mac_filter_profile_id value.

            Notes:
                UUID of the associated MAC Filter Profile entity.

                
                This attribute is named `associatedMACFilterProfileID` in VSD API.
                
        """
        self._associated_mac_filter_profile_id = value

    
    @property
    def associated_mac_filter_profile_name(self):
        """ Get associated_mac_filter_profile_name value.

            Notes:
                Name of the associated MAC Filter Profile entity.

                
                This attribute is named `associatedMACFilterProfileName` in VSD API.
                
        """
        return self._associated_mac_filter_profile_name

    @associated_mac_filter_profile_name.setter
    def associated_mac_filter_profile_name(self, value):
        """ Set associated_mac_filter_profile_name value.

            Notes:
                Name of the associated MAC Filter Profile entity.

                
                This attribute is named `associatedMACFilterProfileName` in VSD API.
                
        """
        self._associated_mac_filter_profile_name = value

    
    @property
    def associated_sap_ingress_qo_s_profile_id(self):
        """ Get associated_sap_ingress_qo_s_profile_id value.

            Notes:
                UUID of the associated SAP Ingress QoS Profile entity.

                
                This attribute is named `associatedSAPIngressQoSProfileID` in VSD API.
                
        """
        return self._associated_sap_ingress_qo_s_profile_id

    @associated_sap_ingress_qo_s_profile_id.setter
    def associated_sap_ingress_qo_s_profile_id(self, value):
        """ Set associated_sap_ingress_qo_s_profile_id value.

            Notes:
                UUID of the associated SAP Ingress QoS Profile entity.

                
                This attribute is named `associatedSAPIngressQoSProfileID` in VSD API.
                
        """
        self._associated_sap_ingress_qo_s_profile_id = value

    
    @property
    def associated_sap_ingress_qo_s_profile_name(self):
        """ Get associated_sap_ingress_qo_s_profile_name value.

            Notes:
                Name of the associated SAP Ingress QoS Profile entity.

                
                This attribute is named `associatedSAPIngressQoSProfileName` in VSD API.
                
        """
        return self._associated_sap_ingress_qo_s_profile_name

    @associated_sap_ingress_qo_s_profile_name.setter
    def associated_sap_ingress_qo_s_profile_name(self, value):
        """ Set associated_sap_ingress_qo_s_profile_name value.

            Notes:
                Name of the associated SAP Ingress QoS Profile entity.

                
                This attribute is named `associatedSAPIngressQoSProfileName` in VSD API.
                
        """
        self._associated_sap_ingress_qo_s_profile_name = value

    
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

    

    