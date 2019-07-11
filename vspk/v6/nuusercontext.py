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

from bambou import NURESTObject


class NUUserContext(NURESTObject):
    """ Represents a UserContext in the VSD

        Notes:
            This defines a proxy class to expose some of the configuration parameters which are required by UI
    """

    __rest_name__ = "usercontext"
    __resource_name__ = "usercontexts"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
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
        self._last_updated_by = None
        self._flow_collection_enabled = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._google_maps_api_key = None
        self._statistics_enabled = None
        self._stats_database_proxy = None
        self._stats_tsdb_server_address = None
        self._external_id = None
        
        self.expose_attribute(local_name="aar_flow_stats_interval", remote_name="AARFlowStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aar_probe_stats_interval", remote_name="AARProbeStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vss_feature_enabled", remote_name="VSSFeatureEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vss_stats_interval", remote_name="VSSStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="page_size", remote_name="pageSize", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="flow_collection_enabled", remote_name="flowCollectionEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="google_maps_api_key", remote_name="googleMapsAPIKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="statistics_enabled", remote_name="statisticsEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_database_proxy", remote_name="statsDatabaseProxy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_tsdb_server_address", remote_name="statsTSDBServerAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
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

    

    