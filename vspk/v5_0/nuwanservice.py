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


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUEnterprisePermissionsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUWANService(NURESTObject):
    """ Represents a WANService in the VSD

        Notes:
            Represents a WAN Service Object.
    """

    __rest_name__ = "service"
    __resource_name__ = "services"

    
    ## Constants
    
    CONST_TUNNEL_TYPE_DC_DEFAULT = "DC_DEFAULT"
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_SERVICE_TYPE_L2 = "L2"
    
    CONST_SERVICE_TYPE_L3 = "L3"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_TUNNEL_TYPE_VXLAN = "VXLAN"
    
    CONST_CONFIG_TYPE_STATIC = "STATIC"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_CONFIG_TYPE_DYNAMIC = "DYNAMIC"
    
    CONST_TUNNEL_TYPE_GRE = "GRE"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    

    def __init__(self, **kwargs):
        """ Initializes a WANService instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> wanservice = NUWANService(id=u'xxxx-xxx-xxx-xxx', name=u'WANService')
                >>> wanservice = NUWANService(data=my_dict)
        """

        super(NUWANService, self).__init__()

        # Read/Write Attributes
        
        self._wan_service_identifier = None
        self._irb_enabled = None
        self._name = None
        self._last_updated_by = None
        self._permitted_action = None
        self._service_policy = None
        self._service_type = None
        self._description = None
        self._vn_id = None
        self._enterprise_name = None
        self._entity_scope = None
        self._domain_name = None
        self._config_type = None
        self._orphan = None
        self._use_user_mnemonic = None
        self._user_mnemonic = None
        self._associated_domain_id = None
        self._associated_vpn_connect_id = None
        self._tunnel_type = None
        self._external_id = None
        self._external_route_target = None
        
        self.expose_attribute(local_name="wan_service_identifier", remote_name="WANServiceIdentifier", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="irb_enabled", remote_name="IRBEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="service_policy", remote_name="servicePolicy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="service_type", remote_name="serviceType", attribute_type=str, is_required=True, is_unique=False, choices=[u'L2', u'L3'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vn_id", remote_name="vnId", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_name", remote_name="enterpriseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="domain_name", remote_name="domainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="config_type", remote_name="configType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DYNAMIC', u'STATIC'])
        self.expose_attribute(local_name="orphan", remote_name="orphan", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="use_user_mnemonic", remote_name="useUserMnemonic", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="user_mnemonic", remote_name="userMnemonic", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_domain_id", remote_name="associatedDomainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_vpn_connect_id", remote_name="associatedVPNConnectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tunnel_type", remote_name="tunnelType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DC_DEFAULT', u'GRE', u'VXLAN'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="external_route_target", remote_name="externalRouteTarget", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def wan_service_identifier(self):
        """ Get wan_service_identifier value.

            Notes:
                Identifier of the WAN Service

                
                This attribute is named `WANServiceIdentifier` in VSD API.
                
        """
        return self._wan_service_identifier

    @wan_service_identifier.setter
    def wan_service_identifier(self, value):
        """ Set wan_service_identifier value.

            Notes:
                Identifier of the WAN Service

                
                This attribute is named `WANServiceIdentifier` in VSD API.
                
        """
        self._wan_service_identifier = value

    
    @property
    def irb_enabled(self):
        """ Get irb_enabled value.

            Notes:
                Determines whether Integrated Routing and Bridging is enabled on the WAN Service

                
                This attribute is named `IRBEnabled` in VSD API.
                
        """
        return self._irb_enabled

    @irb_enabled.setter
    def irb_enabled(self, value):
        """ Set irb_enabled value.

            Notes:
                Determines whether Integrated Routing and Bridging is enabled on the WAN Service

                
                This attribute is named `IRBEnabled` in VSD API.
                
        """
        self._irb_enabled = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the WAN Service

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the WAN Service

                
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
    def service_policy(self):
        """ Get service_policy value.

            Notes:
                Name of 7X50 Policy associated with the service

                
                This attribute is named `servicePolicy` in VSD API.
                
        """
        return self._service_policy

    @service_policy.setter
    def service_policy(self, value):
        """ Set service_policy value.

            Notes:
                Name of 7X50 Policy associated with the service

                
                This attribute is named `servicePolicy` in VSD API.
                
        """
        self._service_policy = value

    
    @property
    def service_type(self):
        """ Get service_type value.

            Notes:
                Type of the service.

                
                This attribute is named `serviceType` in VSD API.
                
        """
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        """ Set service_type value.

            Notes:
                Type of the service.

                
                This attribute is named `serviceType` in VSD API.
                
        """
        self._service_type = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the WAN Service

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the WAN Service

                
        """
        self._description = value

    
    @property
    def vn_id(self):
        """ Get vn_id value.

            Notes:
                VNID of the BackHaul Subnet of L3Domain /L2Domain to which this WANService is associated

                
                This attribute is named `vnId` in VSD API.
                
        """
        return self._vn_id

    @vn_id.setter
    def vn_id(self, value):
        """ Set vn_id value.

            Notes:
                VNID of the BackHaul Subnet of L3Domain /L2Domain to which this WANService is associated

                
                This attribute is named `vnId` in VSD API.
                
        """
        self._vn_id = value

    
    @property
    def enterprise_name(self):
        """ Get enterprise_name value.

            Notes:
                The associated enterprise name.

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        """ Set enterprise_name value.

            Notes:
                The associated enterprise name.

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        self._enterprise_name = value

    
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
    def domain_name(self):
        """ Get domain_name value.

            Notes:
                The associated domain name.

                
                This attribute is named `domainName` in VSD API.
                
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        """ Set domain_name value.

            Notes:
                The associated domain name.

                
                This attribute is named `domainName` in VSD API.
                
        """
        self._domain_name = value

    
    @property
    def config_type(self):
        """ Get config_type value.

            Notes:
                Type of the CONFIG.

                
                This attribute is named `configType` in VSD API.
                
        """
        return self._config_type

    @config_type.setter
    def config_type(self, value):
        """ Set config_type value.

            Notes:
                Type of the CONFIG.

                
                This attribute is named `configType` in VSD API.
                
        """
        self._config_type = value

    
    @property
    def orphan(self):
        """ Get orphan value.

            Notes:
                Indicates if this WAN Service is orphan or not.

                
        """
        return self._orphan

    @orphan.setter
    def orphan(self, value):
        """ Set orphan value.

            Notes:
                Indicates if this WAN Service is orphan or not.

                
        """
        self._orphan = value

    
    @property
    def use_user_mnemonic(self):
        """ Get use_user_mnemonic value.

            Notes:
                Determines whether to use user mnemonic of the WAN Service

                
                This attribute is named `useUserMnemonic` in VSD API.
                
        """
        return self._use_user_mnemonic

    @use_user_mnemonic.setter
    def use_user_mnemonic(self, value):
        """ Set use_user_mnemonic value.

            Notes:
                Determines whether to use user mnemonic of the WAN Service

                
                This attribute is named `useUserMnemonic` in VSD API.
                
        """
        self._use_user_mnemonic = value

    
    @property
    def user_mnemonic(self):
        """ Get user_mnemonic value.

            Notes:
                user mnemonic of the WAN Service

                
                This attribute is named `userMnemonic` in VSD API.
                
        """
        return self._user_mnemonic

    @user_mnemonic.setter
    def user_mnemonic(self, value):
        """ Set user_mnemonic value.

            Notes:
                user mnemonic of the WAN Service

                
                This attribute is named `userMnemonic` in VSD API.
                
        """
        self._user_mnemonic = value

    
    @property
    def associated_domain_id(self):
        """ Get associated_domain_id value.

            Notes:
                ID of the entity to which the WAN Service is attached to. This could be ID DOMAIN/L2DOMAIN

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        return self._associated_domain_id

    @associated_domain_id.setter
    def associated_domain_id(self, value):
        """ Set associated_domain_id value.

            Notes:
                ID of the entity to which the WAN Service is attached to. This could be ID DOMAIN/L2DOMAIN

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        self._associated_domain_id = value

    
    @property
    def associated_vpn_connect_id(self):
        """ Get associated_vpn_connect_id value.

            Notes:
                The associated vpn connect ID.

                
                This attribute is named `associatedVPNConnectID` in VSD API.
                
        """
        return self._associated_vpn_connect_id

    @associated_vpn_connect_id.setter
    def associated_vpn_connect_id(self, value):
        """ Set associated_vpn_connect_id value.

            Notes:
                The associated vpn connect ID.

                
                This attribute is named `associatedVPNConnectID` in VSD API.
                
        """
        self._associated_vpn_connect_id = value

    
    @property
    def tunnel_type(self):
        """ Get tunnel_type value.

            Notes:
                Type of the tunnel.

                
                This attribute is named `tunnelType` in VSD API.
                
        """
        return self._tunnel_type

    @tunnel_type.setter
    def tunnel_type(self, value):
        """ Set tunnel_type value.

            Notes:
                Type of the tunnel.

                
                This attribute is named `tunnelType` in VSD API.
                
        """
        self._tunnel_type = value

    
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
    def external_route_target(self):
        """ Get external_route_target value.

            Notes:
                Route target associated with the WAN. It is an optional parameterthat can be provided by the user

                
                This attribute is named `externalRouteTarget` in VSD API.
                
        """
        return self._external_route_target

    @external_route_target.setter
    def external_route_target(self, value):
        """ Set external_route_target value.

            Notes:
                Route target associated with the WAN. It is an optional parameterthat can be provided by the user

                
                This attribute is named `externalRouteTarget` in VSD API.
                
        """
        self._external_route_target = value

    

    