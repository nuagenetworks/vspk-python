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




from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUUserContext(NURESTObject):
    """ Represents a UserContext in the VSD

        Notes:
            This defines a proxy class to expose some of the configuration parameters which are required by UI
    """

    __rest_name__ = "usercontext"
    __resource_name__ = "usercontexts"

    
    ## Constants
    
    CONST_SYSTEM_AVATAR_TYPE_BASE64 = "BASE64"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_SYSTEM_AVATAR_TYPE_COMPUTEDURL = "COMPUTEDURL"
    
    CONST_SYSTEM_AVATAR_TYPE_URL = "URL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a UserContext instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> usercontext = NUUserContext(id=u'xxxx-xxx-xxx-xxx', name=u'UserContext')
                >>> usercontext = NUUserContext(data=my_dict)
        """

        super(NUUserContext, self).__init__()

        # Read/Write Attributes
        
        self._aar_flow_stats_interval = None
        self._aar_probe_stats_interval = None
        self._vss_feature_enabled = None
        self._vss_stats_interval = None
        self._page_size = None
        self._maintenance_mode_enabled = None
        self._last_updated_by = None
        self._last_updated_date = None
        self._rbac_enabled = None
        self._denied_flow_collection_enabled = None
        self._threat_intelligence_enabled = None
        self._allow_enterprise_avatar_on_nsg = None
        self._flow_collection_enabled = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._google_maps_api_key = None
        self._creation_date = None
        self._statistics_enabled = None
        self._stats_database_proxy = None
        self._stats_tsdb_server_address = None
        self._owner = None
        self._explicit_acl_matching_enabled = None
        self._external_id = None
        self._system_avatar_data = None
        self._system_avatar_type = None
        
        self.expose_attribute(local_name="aar_flow_stats_interval", remote_name="AARFlowStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aar_probe_stats_interval", remote_name="AARProbeStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vss_feature_enabled", remote_name="VSSFeatureEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vss_stats_interval", remote_name="VSSStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="page_size", remote_name="pageSize", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="maintenance_mode_enabled", remote_name="maintenanceModeEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rbac_enabled", remote_name="rbacEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="denied_flow_collection_enabled", remote_name="deniedFlowCollectionEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="threat_intelligence_enabled", remote_name="threatIntelligenceEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allow_enterprise_avatar_on_nsg", remote_name="allowEnterpriseAvatarOnNSG", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="flow_collection_enabled", remote_name="flowCollectionEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="google_maps_api_key", remote_name="googleMapsAPIKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="statistics_enabled", remote_name="statisticsEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_database_proxy", remote_name="statsDatabaseProxy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_tsdb_server_address", remote_name="statsTSDBServerAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="explicit_acl_matching_enabled", remote_name="explicitACLMatchingEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="system_avatar_data", remote_name="systemAvatarData", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="system_avatar_type", remote_name="systemAvatarType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BASE64', u'COMPUTEDURL', u'URL'])
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def aar_flow_stats_interval(self):
        """ Get aar_flow_stats_interval value.

            Notes:
                Interval for AAR flow stats

                
                This attribute is named `AARFlowStatsInterval` in VSD API.
                
        """
        return self._aar_flow_stats_interval

    @aar_flow_stats_interval.setter
    def aar_flow_stats_interval(self, value):
        """ Set aar_flow_stats_interval value.

            Notes:
                Interval for AAR flow stats

                
                This attribute is named `AARFlowStatsInterval` in VSD API.
                
        """
        self._aar_flow_stats_interval = value

    
    @property
    def aar_probe_stats_interval(self):
        """ Get aar_probe_stats_interval value.

            Notes:
                Interval for AAR probe stats

                
                This attribute is named `AARProbeStatsInterval` in VSD API.
                
        """
        return self._aar_probe_stats_interval

    @aar_probe_stats_interval.setter
    def aar_probe_stats_interval(self, value):
        """ Set aar_probe_stats_interval value.

            Notes:
                Interval for AAR probe stats

                
                This attribute is named `AARProbeStatsInterval` in VSD API.
                
        """
        self._aar_probe_stats_interval = value

    
    @property
    def vss_feature_enabled(self):
        """ Get vss_feature_enabled value.

            Notes:
                Flag to indicate if VSS feature is enabled.

                
                This attribute is named `VSSFeatureEnabled` in VSD API.
                
        """
        return self._vss_feature_enabled

    @vss_feature_enabled.setter
    def vss_feature_enabled(self, value):
        """ Set vss_feature_enabled value.

            Notes:
                Flag to indicate if VSS feature is enabled.

                
                This attribute is named `VSSFeatureEnabled` in VSD API.
                
        """
        self._vss_feature_enabled = value

    
    @property
    def vss_stats_interval(self):
        """ Get vss_stats_interval value.

            Notes:
                Interval for VSS stats

                
                This attribute is named `VSSStatsInterval` in VSD API.
                
        """
        return self._vss_stats_interval

    @vss_stats_interval.setter
    def vss_stats_interval(self, value):
        """ Set vss_stats_interval value.

            Notes:
                Interval for VSS stats

                
                This attribute is named `VSSStatsInterval` in VSD API.
                
        """
        self._vss_stats_interval = value

    
    @property
    def page_size(self):
        """ Get page_size value.

            Notes:
                Result size for queries

                
                This attribute is named `pageSize` in VSD API.
                
        """
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        """ Set page_size value.

            Notes:
                Result size for queries

                
                This attribute is named `pageSize` in VSD API.
                
        """
        self._page_size = value

    
    @property
    def maintenance_mode_enabled(self):
        """ Get maintenance_mode_enabled value.

            Notes:
                Indicates if this VSD is configured in maintenance mode. This is typically enabled during the VSD upgrade window and when enabled VSD supports only a subset of functionality.

                
                This attribute is named `maintenanceModeEnabled` in VSD API.
                
        """
        return self._maintenance_mode_enabled

    @maintenance_mode_enabled.setter
    def maintenance_mode_enabled(self, value):
        """ Set maintenance_mode_enabled value.

            Notes:
                Indicates if this VSD is configured in maintenance mode. This is typically enabled during the VSD upgrade window and when enabled VSD supports only a subset of functionality.

                
                This attribute is named `maintenanceModeEnabled` in VSD API.
                
        """
        self._maintenance_mode_enabled = value

    
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
    def last_updated_date(self):
        """ Get last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, value):
        """ Set last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        self._last_updated_date = value

    
    @property
    def rbac_enabled(self):
        """ Get rbac_enabled value.

            Notes:
                Indicates wether the new RBAC feature is enabled

                
                This attribute is named `rbacEnabled` in VSD API.
                
        """
        return self._rbac_enabled

    @rbac_enabled.setter
    def rbac_enabled(self, value):
        """ Set rbac_enabled value.

            Notes:
                Indicates wether the new RBAC feature is enabled

                
                This attribute is named `rbacEnabled` in VSD API.
                
        """
        self._rbac_enabled = value

    
    @property
    def denied_flow_collection_enabled(self):
        """ Get denied_flow_collection_enabled value.

            Notes:
                When this option is selected, VSS will only store flows that are denied by security policy (implicit or explicit ACLs). This requires a valid VSS license and Flow Collection enabled.

                
                This attribute is named `deniedFlowCollectionEnabled` in VSD API.
                
        """
        return self._denied_flow_collection_enabled

    @denied_flow_collection_enabled.setter
    def denied_flow_collection_enabled(self, value):
        """ Set denied_flow_collection_enabled value.

            Notes:
                When this option is selected, VSS will only store flows that are denied by security policy (implicit or explicit ACLs). This requires a valid VSS license and Flow Collection enabled.

                
                This attribute is named `deniedFlowCollectionEnabled` in VSD API.
                
        """
        self._denied_flow_collection_enabled = value

    
    @property
    def threat_intelligence_enabled(self):
        """ Get threat_intelligence_enabled value.

            Notes:
                Enables IP based threat intelligence. This requires Flow Collection to be enabled

                
                This attribute is named `threatIntelligenceEnabled` in VSD API.
                
        """
        return self._threat_intelligence_enabled

    @threat_intelligence_enabled.setter
    def threat_intelligence_enabled(self, value):
        """ Set threat_intelligence_enabled value.

            Notes:
                Enables IP based threat intelligence. This requires Flow Collection to be enabled

                
                This attribute is named `threatIntelligenceEnabled` in VSD API.
                
        """
        self._threat_intelligence_enabled = value

    
    @property
    def allow_enterprise_avatar_on_nsg(self):
        """ Get allow_enterprise_avatar_on_nsg value.

            Notes:
                When enabled, it allows Enterprise Avatar (image) to be populated on the NSGateway bootstrapping portal and blocked page notification.

                
                This attribute is named `allowEnterpriseAvatarOnNSG` in VSD API.
                
        """
        return self._allow_enterprise_avatar_on_nsg

    @allow_enterprise_avatar_on_nsg.setter
    def allow_enterprise_avatar_on_nsg(self, value):
        """ Set allow_enterprise_avatar_on_nsg value.

            Notes:
                When enabled, it allows Enterprise Avatar (image) to be populated on the NSGateway bootstrapping portal and blocked page notification.

                
                This attribute is named `allowEnterpriseAvatarOnNSG` in VSD API.
                
        """
        self._allow_enterprise_avatar_on_nsg = value

    
    @property
    def flow_collection_enabled(self):
        """ Get flow_collection_enabled value.

            Notes:
                Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires 'statisticsEnabled'.

                
                This attribute is named `flowCollectionEnabled` in VSD API.
                
        """
        return self._flow_collection_enabled

    @flow_collection_enabled.setter
    def flow_collection_enabled(self, value):
        """ Set flow_collection_enabled value.

            Notes:
                Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires 'statisticsEnabled'.

                
                This attribute is named `flowCollectionEnabled` in VSD API.
                
        """
        self._flow_collection_enabled = value

    
    @property
    def embedded_metadata(self):
        """ Get embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        return self._embedded_metadata

    @embedded_metadata.setter
    def embedded_metadata(self, value):
        """ Set embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        self._embedded_metadata = value

    
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
    def google_maps_api_key(self):
        """ Get google_maps_api_key value.

            Notes:
                Google Maps API Key used to display maps on Nuage UI applications

                
                This attribute is named `googleMapsAPIKey` in VSD API.
                
        """
        return self._google_maps_api_key

    @google_maps_api_key.setter
    def google_maps_api_key(self, value):
        """ Set google_maps_api_key value.

            Notes:
                Google Maps API Key used to display maps on Nuage UI applications

                
                This attribute is named `googleMapsAPIKey` in VSD API.
                
        """
        self._google_maps_api_key = value

    
    @property
    def creation_date(self):
        """ Get creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """ Set creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        self._creation_date = value

    
    @property
    def statistics_enabled(self):
        """ Get statistics_enabled value.

            Notes:
                This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

                
                This attribute is named `statisticsEnabled` in VSD API.
                
        """
        return self._statistics_enabled

    @statistics_enabled.setter
    def statistics_enabled(self, value):
        """ Set statistics_enabled value.

            Notes:
                This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

                
                This attribute is named `statisticsEnabled` in VSD API.
                
        """
        self._statistics_enabled = value

    
    @property
    def stats_database_proxy(self):
        """ Get stats_database_proxy value.

            Notes:
                The location of a public proxy to statistics database server in <FQDN>:<PORT> format.

                
                This attribute is named `statsDatabaseProxy` in VSD API.
                
        """
        return self._stats_database_proxy

    @stats_database_proxy.setter
    def stats_database_proxy(self, value):
        """ Set stats_database_proxy value.

            Notes:
                The location of a public proxy to statistics database server in <FQDN>:<PORT> format.

                
                This attribute is named `statsDatabaseProxy` in VSD API.
                
        """
        self._stats_database_proxy = value

    
    @property
    def stats_tsdb_server_address(self):
        """ Get stats_tsdb_server_address value.

            Notes:
                IP address(es) of the elastic machine

                
                This attribute is named `statsTSDBServerAddress` in VSD API.
                
        """
        return self._stats_tsdb_server_address

    @stats_tsdb_server_address.setter
    def stats_tsdb_server_address(self, value):
        """ Set stats_tsdb_server_address value.

            Notes:
                IP address(es) of the elastic machine

                
                This attribute is named `statsTSDBServerAddress` in VSD API.
                
        """
        self._stats_tsdb_server_address = value

    
    @property
    def owner(self):
        """ Get owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """ Set owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        self._owner = value

    
    @property
    def explicit_acl_matching_enabled(self):
        """ Get explicit_acl_matching_enabled value.

            Notes:
                When this option is selected, VSS will only store allow/denied flows that matches explicit ingress/egress security ACL. This requires a valid VSS license and Flow Collection enabled.

                
                This attribute is named `explicitACLMatchingEnabled` in VSD API.
                
        """
        return self._explicit_acl_matching_enabled

    @explicit_acl_matching_enabled.setter
    def explicit_acl_matching_enabled(self, value):
        """ Set explicit_acl_matching_enabled value.

            Notes:
                When this option is selected, VSS will only store allow/denied flows that matches explicit ingress/egress security ACL. This requires a valid VSS license and Flow Collection enabled.

                
                This attribute is named `explicitACLMatchingEnabled` in VSD API.
                
        """
        self._explicit_acl_matching_enabled = value

    
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
    def system_avatar_data(self):
        """ Get system_avatar_data value.

            Notes:
                URL to the avatar data configured at System Configuration. If the avatarType is URL then value of avatarData should be URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image.

                
                This attribute is named `systemAvatarData` in VSD API.
                
        """
        return self._system_avatar_data

    @system_avatar_data.setter
    def system_avatar_data(self, value):
        """ Set system_avatar_data value.

            Notes:
                URL to the avatar data configured at System Configuration. If the avatarType is URL then value of avatarData should be URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image.

                
                This attribute is named `systemAvatarData` in VSD API.
                
        """
        self._system_avatar_data = value

    
    @property
    def system_avatar_type(self):
        """ Get system_avatar_type value.

            Notes:
                The type of avatar data.

                
                This attribute is named `systemAvatarType` in VSD API.
                
        """
        return self._system_avatar_type

    @system_avatar_type.setter
    def system_avatar_type(self, value):
        """ Set system_avatar_type value.

            Notes:
                The type of avatar data.

                
                This attribute is named `systemAvatarType` in VSD API.
                
        """
        self._system_avatar_type = value

    

    