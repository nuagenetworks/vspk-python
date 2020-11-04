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


class NUInfrastructureGatewayProfile(NURESTObject):
    """ Represents a InfrastructureGatewayProfile in the VSD

        Notes:
            Infrastructure Gateway Profiles are gateway-level platform attributes inherited by gateways as they are instantiated, connecting them to Nuage management infrastructure.
    """

    __rest_name__ = "infrastructuregatewayprofile"
    __resource_name__ = "infrastructuregatewayprofiles"

    
    ## Constants
    
    CONST_UPGRADE_ACTION_DOWNLOAD_AND_UPGRADE_NOW = "DOWNLOAD_AND_UPGRADE_NOW"
    
    CONST_CONTROLLER_LESS_FORWARDING_MODE_LOCAL_AND_REMOTE = "LOCAL_AND_REMOTE"
    
    CONST_UPGRADE_ACTION_NONE = "NONE"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_REMOTE_LOG_MODE_RSYSLOG = "RSYSLOG"
    
    CONST_UPGRADE_ACTION_UPGRADE_AT_BOOTSTRAPPING = "UPGRADE_AT_BOOTSTRAPPING"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_UNDERLAY_TEST_UPLINK_MODE_ALL_UPLINKS = "ALL_UPLINKS"
    
    CONST_REMOTE_LOG_MODE_DISABLED = "DISABLED"
    
    CONST_CONTROLLER_LESS_FORWARDING_MODE_DISABLED = "DISABLED"
    
    CONST_UNDERLAY_TEST_UPLINK_MODE_BOOTSTRAP_UPLINK = "BOOTSTRAP_UPLINK"
    
    CONST_UPGRADE_ACTION_DOWNLOAD_ONLY = "DOWNLOAD_ONLY"
    
    CONST_UPGRADE_ACTION_UPGRADE_NOW = "UPGRADE_NOW"
    
    CONST_UPGRADE_ACTION_DOWNLOAD_AND_UPGRADE_AT_WINDOW = "DOWNLOAD_AND_UPGRADE_AT_WINDOW"
    
    CONST_CONTROLLER_LESS_FORWARDING_MODE_LOCAL_ONLY = "LOCAL_ONLY"
    
    

    def __init__(self, **kwargs):
        """ Initializes a InfrastructureGatewayProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> infrastructuregatewayprofile = NUInfrastructureGatewayProfile(id=u'xxxx-xxx-xxx-xxx', name=u'InfrastructureGatewayProfile')
                >>> infrastructuregatewayprofile = NUInfrastructureGatewayProfile(data=my_dict)
        """

        super(NUInfrastructureGatewayProfile, self).__init__()

        # Read/Write Attributes
        
        self._ntp_server_key = None
        self._ntp_server_key_id = None
        self._name = None
        self._last_updated_by = None
        self._last_updated_date = None
        self._datapath_sync_timeout = None
        self._dead_timer = None
        self._dead_timer_enabled = None
        self._web_filter_download_port = None
        self._web_filter_query_port = None
        self._remote_log_mode = None
        self._remote_log_server_address = None
        self._remote_log_server_port = None
        self._description = None
        self._metadata_upgrade_path = None
        self._flow_eviction_threshold = None
        self._embedded_metadata = None
        self._enable_underlay_tests_during_activation = None
        self._underlay_test_server = None
        self._underlay_test_uplink_mode = None
        self._enterprise_id = None
        self._entity_scope = None
        self._controller_less_duration = None
        self._controller_less_enabled = None
        self._controller_less_forwarding_mode = None
        self._controller_less_remote_duration = None
        self._force_immediate_system_sync = None
        self._open_flow_audit_timer = None
        self._upgrade_action = None
        self._creation_date = None
        self._proxy_dns_name = None
        self._use_two_factor = None
        self._stats_collector_port = None
        self._run_underlay_bandwidth_test = None
        self._run_underlay_connectivity_test = None
        self._run_underlay_mtu_discovery_test = None
        self._owner = None
        self._external_id = None
        self._system_sync_scheduler = None
        
        self.expose_attribute(local_name="ntp_server_key", remote_name="NTPServerKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ntp_server_key_id", remote_name="NTPServerKeyID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="datapath_sync_timeout", remote_name="datapathSyncTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dead_timer", remote_name="deadTimer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dead_timer_enabled", remote_name="deadTimerEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="web_filter_download_port", remote_name="webFilterDownloadPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="web_filter_query_port", remote_name="webFilterQueryPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="remote_log_mode", remote_name="remoteLogMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'RSYSLOG'])
        self.expose_attribute(local_name="remote_log_server_address", remote_name="remoteLogServerAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="remote_log_server_port", remote_name="remoteLogServerPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_upgrade_path", remote_name="metadataUpgradePath", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="flow_eviction_threshold", remote_name="flowEvictionThreshold", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enable_underlay_tests_during_activation", remote_name="enableUnderlayTestsDuringActivation", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="underlay_test_server", remote_name="underlayTestServer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="underlay_test_uplink_mode", remote_name="underlayTestUplinkMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL_UPLINKS', u'BOOTSTRAP_UPLINK'])
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="controller_less_duration", remote_name="controllerLessDuration", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="controller_less_enabled", remote_name="controllerLessEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="controller_less_forwarding_mode", remote_name="controllerLessForwardingMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'LOCAL_AND_REMOTE', u'LOCAL_ONLY'])
        self.expose_attribute(local_name="controller_less_remote_duration", remote_name="controllerLessRemoteDuration", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="force_immediate_system_sync", remote_name="forceImmediateSystemSync", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="open_flow_audit_timer", remote_name="openFlowAuditTimer", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="upgrade_action", remote_name="upgradeAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'DOWNLOAD_AND_UPGRADE_AT_WINDOW', u'DOWNLOAD_AND_UPGRADE_NOW', u'DOWNLOAD_ONLY', u'NONE', u'UPGRADE_AT_BOOTSTRAPPING', u'UPGRADE_NOW'])
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="proxy_dns_name", remote_name="proxyDNSName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="use_two_factor", remote_name="useTwoFactor", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_collector_port", remote_name="statsCollectorPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="run_underlay_bandwidth_test", remote_name="runUnderlayBandwidthTest", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="run_underlay_connectivity_test", remote_name="runUnderlayConnectivityTest", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="run_underlay_mtu_discovery_test", remote_name="runUnderlayMTUDiscoveryTest", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="system_sync_scheduler", remote_name="systemSyncScheduler", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ntp_server_key(self):
        """ Get ntp_server_key value.

            Notes:
                If set, this represents the security key for the Gateway to communicate with the NTP server (a VSC).

                
                This attribute is named `NTPServerKey` in VSD API.
                
        """
        return self._ntp_server_key

    @ntp_server_key.setter
    def ntp_server_key(self, value):
        """ Set ntp_server_key value.

            Notes:
                If set, this represents the security key for the Gateway to communicate with the NTP server (a VSC).

                
                This attribute is named `NTPServerKey` in VSD API.
                
        """
        self._ntp_server_key = value

    
    @property
    def ntp_server_key_id(self):
        """ Get ntp_server_key_id value.

            Notes:
                Corresponds to the key ID on the NTP server that matches the NTPServerKey value.  Valid values are from 1 to 255 as specified by SR-OS and when value 0 is entered, it means that the NTP Key is not used (VSD/NSG only).

                
                This attribute is named `NTPServerKeyID` in VSD API.
                
        """
        return self._ntp_server_key_id

    @ntp_server_key_id.setter
    def ntp_server_key_id(self, value):
        """ Set ntp_server_key_id value.

            Notes:
                Corresponds to the key ID on the NTP server that matches the NTPServerKey value.  Valid values are from 1 to 255 as specified by SR-OS and when value 0 is entered, it means that the NTP Key is not used (VSD/NSG only).

                
                This attribute is named `NTPServerKeyID` in VSD API.
                
        """
        self._ntp_server_key_id = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Infrastructure Profile

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Infrastructure Profile

                
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
    def datapath_sync_timeout(self):
        """ Get datapath_sync_timeout value.

            Notes:
                Datapath flows sync-time-interval specified in milliseconds

                
                This attribute is named `datapathSyncTimeout` in VSD API.
                
        """
        return self._datapath_sync_timeout

    @datapath_sync_timeout.setter
    def datapath_sync_timeout(self, value):
        """ Set datapath_sync_timeout value.

            Notes:
                Datapath flows sync-time-interval specified in milliseconds

                
                This attribute is named `datapathSyncTimeout` in VSD API.
                
        """
        self._datapath_sync_timeout = value

    
    @property
    def dead_timer(self):
        """ Get dead_timer value.

            Notes:
                ISO 8601 format duration: **PnYnMnD T nHnMnS**. **P** represents the period field and **T** the time field. Period field: **Y** = year, **M** = month, **D** = day. Time field: **H** = hours, **M** = minutes, **S** = seconds. **n** is the value of each field. Because the years and month are units that vary in length, for the time being those are not supported yet.

                
                This attribute is named `deadTimer` in VSD API.
                
        """
        return self._dead_timer

    @dead_timer.setter
    def dead_timer(self, value):
        """ Set dead_timer value.

            Notes:
                ISO 8601 format duration: **PnYnMnD T nHnMnS**. **P** represents the period field and **T** the time field. Period field: **Y** = year, **M** = month, **D** = day. Time field: **H** = hours, **M** = minutes, **S** = seconds. **n** is the value of each field. Because the years and month are units that vary in length, for the time being those are not supported yet.

                
                This attribute is named `deadTimer` in VSD API.
                
        """
        self._dead_timer = value

    
    @property
    def dead_timer_enabled(self):
        """ Get dead_timer_enabled value.

            Notes:
                Flag to enable the functionlity where VSD will automatically place an NSG into a quarantine state if it is no longer being reported by VSC nodes for a specified period.

                
                This attribute is named `deadTimerEnabled` in VSD API.
                
        """
        return self._dead_timer_enabled

    @dead_timer_enabled.setter
    def dead_timer_enabled(self, value):
        """ Set dead_timer_enabled value.

            Notes:
                Flag to enable the functionlity where VSD will automatically place an NSG into a quarantine state if it is no longer being reported by VSC nodes for a specified period.

                
                This attribute is named `deadTimerEnabled` in VSD API.
                
        """
        self._dead_timer_enabled = value

    
    @property
    def web_filter_download_port(self):
        """ Get web_filter_download_port value.

            Notes:
                The port to be opened by the proxy for webfilter update database

                
                This attribute is named `webFilterDownloadPort` in VSD API.
                
        """
        return self._web_filter_download_port

    @web_filter_download_port.setter
    def web_filter_download_port(self, value):
        """ Set web_filter_download_port value.

            Notes:
                The port to be opened by the proxy for webfilter update database

                
                This attribute is named `webFilterDownloadPort` in VSD API.
                
        """
        self._web_filter_download_port = value

    
    @property
    def web_filter_query_port(self):
        """ Get web_filter_query_port value.

            Notes:
                The port to be opened by the proxy for webfilter category query request

                
                This attribute is named `webFilterQueryPort` in VSD API.
                
        """
        return self._web_filter_query_port

    @web_filter_query_port.setter
    def web_filter_query_port(self, value):
        """ Set web_filter_query_port value.

            Notes:
                The port to be opened by the proxy for webfilter category query request

                
                This attribute is named `webFilterQueryPort` in VSD API.
                
        """
        self._web_filter_query_port = value

    
    @property
    def remote_log_mode(self):
        """ Get remote_log_mode value.

            Notes:
                Type of Log Server for system logs generated by Gateways associated with this Infrastructure Profile.

                
                This attribute is named `remoteLogMode` in VSD API.
                
        """
        return self._remote_log_mode

    @remote_log_mode.setter
    def remote_log_mode(self, value):
        """ Set remote_log_mode value.

            Notes:
                Type of Log Server for system logs generated by Gateways associated with this Infrastructure Profile.

                
                This attribute is named `remoteLogMode` in VSD API.
                
        """
        self._remote_log_mode = value

    
    @property
    def remote_log_server_address(self):
        """ Get remote_log_server_address value.

            Notes:
                Primary Log Server for system logs generated by Gateways associated with this Infrastructure Profile.  Can be an IP address or a URL.  This field is optional.

                
                This attribute is named `remoteLogServerAddress` in VSD API.
                
        """
        return self._remote_log_server_address

    @remote_log_server_address.setter
    def remote_log_server_address(self, value):
        """ Set remote_log_server_address value.

            Notes:
                Primary Log Server for system logs generated by Gateways associated with this Infrastructure Profile.  Can be an IP address or a URL.  This field is optional.

                
                This attribute is named `remoteLogServerAddress` in VSD API.
                
        """
        self._remote_log_server_address = value

    
    @property
    def remote_log_server_port(self):
        """ Get remote_log_server_port value.

            Notes:
                Port to be used to access the Remote Syslog server.  By default, this is port 514.

                
                This attribute is named `remoteLogServerPort` in VSD API.
                
        """
        return self._remote_log_server_port

    @remote_log_server_port.setter
    def remote_log_server_port(self, value):
        """ Set remote_log_server_port value.

            Notes:
                Port to be used to access the Remote Syslog server.  By default, this is port 514.

                
                This attribute is named `remoteLogServerPort` in VSD API.
                
        """
        self._remote_log_server_port = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the Profile instance created.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the Profile instance created.

                
        """
        self._description = value

    
    @property
    def metadata_upgrade_path(self):
        """ Get metadata_upgrade_path value.

            Notes:
                Path/URL to retrieve the NSG Upgrade information meta data files.  From that meta data, the NSG will be able to retrieve the upgrade package files and perform some validations.  It is expected that the meta data file is in JSON format.  RFC 2616 states that there are no 'official' maximum length for a URL but different browsers and servers have limits.  Our friendly Internet Explorer has a maximum of 'around' 2048 characters, we shall use this as a limit here.

                
                This attribute is named `metadataUpgradePath` in VSD API.
                
        """
        return self._metadata_upgrade_path

    @metadata_upgrade_path.setter
    def metadata_upgrade_path(self, value):
        """ Set metadata_upgrade_path value.

            Notes:
                Path/URL to retrieve the NSG Upgrade information meta data files.  From that meta data, the NSG will be able to retrieve the upgrade package files and perform some validations.  It is expected that the meta data file is in JSON format.  RFC 2616 states that there are no 'official' maximum length for a URL but different browsers and servers have limits.  Our friendly Internet Explorer has a maximum of 'around' 2048 characters, we shall use this as a limit here.

                
                This attribute is named `metadataUpgradePath` in VSD API.
                
        """
        self._metadata_upgrade_path = value

    
    @property
    def flow_eviction_threshold(self):
        """ Get flow_eviction_threshold value.

            Notes:
                Number of flows at which eviction from kernel flow table will be triggered (default: 2500)

                
                This attribute is named `flowEvictionThreshold` in VSD API.
                
        """
        return self._flow_eviction_threshold

    @flow_eviction_threshold.setter
    def flow_eviction_threshold(self, value):
        """ Set flow_eviction_threshold value.

            Notes:
                Number of flows at which eviction from kernel flow table will be triggered (default: 2500)

                
                This attribute is named `flowEvictionThreshold` in VSD API.
                
        """
        self._flow_eviction_threshold = value

    
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
    def enable_underlay_tests_during_activation(self):
        """ Get enable_underlay_tests_during_activation value.

            Notes:
                Enables underlay tests during gateway activation. Underlay tests will cause the bootstrapping operation to be about two minutes longer.

                
                This attribute is named `enableUnderlayTestsDuringActivation` in VSD API.
                
        """
        return self._enable_underlay_tests_during_activation

    @enable_underlay_tests_during_activation.setter
    def enable_underlay_tests_during_activation(self, value):
        """ Set enable_underlay_tests_during_activation value.

            Notes:
                Enables underlay tests during gateway activation. Underlay tests will cause the bootstrapping operation to be about two minutes longer.

                
                This attribute is named `enableUnderlayTestsDuringActivation` in VSD API.
                
        """
        self._enable_underlay_tests_during_activation = value

    
    @property
    def underlay_test_server(self):
        """ Get underlay_test_server value.

            Notes:
                Underlay Test Server (FQDN or IP Address). Required when the Underlay test at bootstrap feature is enabled or to allow On-Demand tests to be run.

                
                This attribute is named `underlayTestServer` in VSD API.
                
        """
        return self._underlay_test_server

    @underlay_test_server.setter
    def underlay_test_server(self, value):
        """ Set underlay_test_server value.

            Notes:
                Underlay Test Server (FQDN or IP Address). Required when the Underlay test at bootstrap feature is enabled or to allow On-Demand tests to be run.

                
                This attribute is named `underlayTestServer` in VSD API.
                
        """
        self._underlay_test_server = value

    
    @property
    def underlay_test_uplink_mode(self):
        """ Get underlay_test_uplink_mode value.

            Notes:
                Enumerator to describe which uplinks to run underlay tests on during bootstrap

                
                This attribute is named `underlayTestUplinkMode` in VSD API.
                
        """
        return self._underlay_test_uplink_mode

    @underlay_test_uplink_mode.setter
    def underlay_test_uplink_mode(self, value):
        """ Set underlay_test_uplink_mode value.

            Notes:
                Enumerator to describe which uplinks to run underlay tests on during bootstrap

                
                This attribute is named `underlayTestUplinkMode` in VSD API.
                
        """
        self._underlay_test_uplink_mode = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                Enterprise/Organisation associated with this Profile instance.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                Enterprise/Organisation associated with this Profile instance.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
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
    def controller_less_duration(self):
        """ Get controller_less_duration value.

            Notes:
                Duration for a controller-less local operation (in ISO-duration format).

                
                This attribute is named `controllerLessDuration` in VSD API.
                
        """
        return self._controller_less_duration

    @controller_less_duration.setter
    def controller_less_duration(self, value):
        """ Set controller_less_duration value.

            Notes:
                Duration for a controller-less local operation (in ISO-duration format).

                
                This attribute is named `controllerLessDuration` in VSD API.
                
        """
        self._controller_less_duration = value

    
    @property
    def controller_less_enabled(self):
        """ Get controller_less_enabled value.

            Notes:
                Flag to enable controller-less operations

                
                This attribute is named `controllerLessEnabled` in VSD API.
                
        """
        return self._controller_less_enabled

    @controller_less_enabled.setter
    def controller_less_enabled(self, value):
        """ Set controller_less_enabled value.

            Notes:
                Flag to enable controller-less operations

                
                This attribute is named `controllerLessEnabled` in VSD API.
                
        """
        self._controller_less_enabled = value

    
    @property
    def controller_less_forwarding_mode(self):
        """ Get controller_less_forwarding_mode value.

            Notes:
                The forwarding mode to use for controllerLess operations

                
                This attribute is named `controllerLessForwardingMode` in VSD API.
                
        """
        return self._controller_less_forwarding_mode

    @controller_less_forwarding_mode.setter
    def controller_less_forwarding_mode(self, value):
        """ Set controller_less_forwarding_mode value.

            Notes:
                The forwarding mode to use for controllerLess operations

                
                This attribute is named `controllerLessForwardingMode` in VSD API.
                
        """
        self._controller_less_forwarding_mode = value

    
    @property
    def controller_less_remote_duration(self):
        """ Get controller_less_remote_duration value.

            Notes:
                Duration for a controller-less remote operation (in ISO-duration format).

                
                This attribute is named `controllerLessRemoteDuration` in VSD API.
                
        """
        return self._controller_less_remote_duration

    @controller_less_remote_duration.setter
    def controller_less_remote_duration(self, value):
        """ Set controller_less_remote_duration value.

            Notes:
                Duration for a controller-less remote operation (in ISO-duration format).

                
                This attribute is named `controllerLessRemoteDuration` in VSD API.
                
        """
        self._controller_less_remote_duration = value

    
    @property
    def force_immediate_system_sync(self):
        """ Get force_immediate_system_sync value.

            Notes:
                Usually the synchronization will span across 1 hour window after the defined synchronization time. Forcing an immediate synchronization can overload the system and can have a negative impact on the system.

                
                This attribute is named `forceImmediateSystemSync` in VSD API.
                
        """
        return self._force_immediate_system_sync

    @force_immediate_system_sync.setter
    def force_immediate_system_sync(self, value):
        """ Set force_immediate_system_sync value.

            Notes:
                Usually the synchronization will span across 1 hour window after the defined synchronization time. Forcing an immediate synchronization can overload the system and can have a negative impact on the system.

                
                This attribute is named `forceImmediateSystemSync` in VSD API.
                
        """
        self._force_immediate_system_sync = value

    
    @property
    def open_flow_audit_timer(self):
        """ Get open_flow_audit_timer value.

            Notes:
                Openflow audit timer in seconds. Upon the expiry of this timer a set of cleanup operations will be performed

                
                This attribute is named `openFlowAuditTimer` in VSD API.
                
        """
        return self._open_flow_audit_timer

    @open_flow_audit_timer.setter
    def open_flow_audit_timer(self, value):
        """ Set open_flow_audit_timer value.

            Notes:
                Openflow audit timer in seconds. Upon the expiry of this timer a set of cleanup operations will be performed

                
                This attribute is named `openFlowAuditTimer` in VSD API.
                
        """
        self._open_flow_audit_timer = value

    
    @property
    def upgrade_action(self):
        """ Get upgrade_action value.

            Notes:
                Upgrade action for NSG associated with this Infrastructure Gateway Profile instance.

                
                This attribute is named `upgradeAction` in VSD API.
                
        """
        return self._upgrade_action

    @upgrade_action.setter
    def upgrade_action(self, value):
        """ Set upgrade_action value.

            Notes:
                Upgrade action for NSG associated with this Infrastructure Gateway Profile instance.

                
                This attribute is named `upgradeAction` in VSD API.
                
        """
        self._upgrade_action = value

    
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
    def proxy_dns_name(self):
        """ Get proxy_dns_name value.

            Notes:
                Proxy DNS Name :  DNS Name of the system acting as a proxy between the NSG instances and the VSD.

                
                This attribute is named `proxyDNSName` in VSD API.
                
        """
        return self._proxy_dns_name

    @proxy_dns_name.setter
    def proxy_dns_name(self, value):
        """ Set proxy_dns_name value.

            Notes:
                Proxy DNS Name :  DNS Name of the system acting as a proxy between the NSG instances and the VSD.

                
                This attribute is named `proxyDNSName` in VSD API.
                
        """
        self._proxy_dns_name = value

    
    @property
    def use_two_factor(self):
        """ Get use_two_factor value.

            Notes:
                Use Two Factor :  When set to true, the use of two independent authentication factors will be used to secure the installed NSG.  When set to false, there is an assumption that the NSG is being installed in a secure environment and the installer is also trusted.  The defaut value is true, using 2-factor.

                
                This attribute is named `useTwoFactor` in VSD API.
                
        """
        return self._use_two_factor

    @use_two_factor.setter
    def use_two_factor(self, value):
        """ Set use_two_factor value.

            Notes:
                Use Two Factor :  When set to true, the use of two independent authentication factors will be used to secure the installed NSG.  When set to false, there is an assumption that the NSG is being installed in a secure environment and the installer is also trusted.  The defaut value is true, using 2-factor.

                
                This attribute is named `useTwoFactor` in VSD API.
                
        """
        self._use_two_factor = value

    
    @property
    def stats_collector_port(self):
        """ Get stats_collector_port value.

            Notes:
                The port to open by the proxy for the statistics collector to use.

                
                This attribute is named `statsCollectorPort` in VSD API.
                
        """
        return self._stats_collector_port

    @stats_collector_port.setter
    def stats_collector_port(self, value):
        """ Set stats_collector_port value.

            Notes:
                The port to open by the proxy for the statistics collector to use.

                
                This attribute is named `statsCollectorPort` in VSD API.
                
        """
        self._stats_collector_port = value

    
    @property
    def run_underlay_bandwidth_test(self):
        """ Get run_underlay_bandwidth_test value.

            Notes:
                Run the underlay bandwidth test during activation. Will only have an effect if the Underlay tests at bootstrap are enabled.

                
                This attribute is named `runUnderlayBandwidthTest` in VSD API.
                
        """
        return self._run_underlay_bandwidth_test

    @run_underlay_bandwidth_test.setter
    def run_underlay_bandwidth_test(self, value):
        """ Set run_underlay_bandwidth_test value.

            Notes:
                Run the underlay bandwidth test during activation. Will only have an effect if the Underlay tests at bootstrap are enabled.

                
                This attribute is named `runUnderlayBandwidthTest` in VSD API.
                
        """
        self._run_underlay_bandwidth_test = value

    
    @property
    def run_underlay_connectivity_test(self):
        """ Get run_underlay_connectivity_test value.

            Notes:
                Run the underlay connectivity test during activation. Will only have an effect if the Underlay tests at bootstrap are enabled.

                
                This attribute is named `runUnderlayConnectivityTest` in VSD API.
                
        """
        return self._run_underlay_connectivity_test

    @run_underlay_connectivity_test.setter
    def run_underlay_connectivity_test(self, value):
        """ Set run_underlay_connectivity_test value.

            Notes:
                Run the underlay connectivity test during activation. Will only have an effect if the Underlay tests at bootstrap are enabled.

                
                This attribute is named `runUnderlayConnectivityTest` in VSD API.
                
        """
        self._run_underlay_connectivity_test = value

    
    @property
    def run_underlay_mtu_discovery_test(self):
        """ Get run_underlay_mtu_discovery_test value.

            Notes:
                Run the underlay MTU discovery test during activation. Will only have an effect if the Underlay tests at bootstrap are enabled.

                
                This attribute is named `runUnderlayMTUDiscoveryTest` in VSD API.
                
        """
        return self._run_underlay_mtu_discovery_test

    @run_underlay_mtu_discovery_test.setter
    def run_underlay_mtu_discovery_test(self, value):
        """ Set run_underlay_mtu_discovery_test value.

            Notes:
                Run the underlay MTU discovery test during activation. Will only have an effect if the Underlay tests at bootstrap are enabled.

                
                This attribute is named `runUnderlayMTUDiscoveryTest` in VSD API.
                
        """
        self._run_underlay_mtu_discovery_test = value

    
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
    def system_sync_scheduler(self):
        """ Get system_sync_scheduler value.

            Notes:
                Time, in a Cron format, when configuration updates are being applied on the Gateway (NSG).  This property is linked to systemSyncWindow.  Default value is every midnight (0 0 * * *).  Format:  Minutes Hours DayOfMonth Month DayOfWeek

                
                This attribute is named `systemSyncScheduler` in VSD API.
                
        """
        return self._system_sync_scheduler

    @system_sync_scheduler.setter
    def system_sync_scheduler(self, value):
        """ Set system_sync_scheduler value.

            Notes:
                Time, in a Cron format, when configuration updates are being applied on the Gateway (NSG).  This property is linked to systemSyncWindow.  Default value is every midnight (0 0 * * *).  Format:  Minutes Hours DayOfMonth Month DayOfWeek

                
                This attribute is named `systemSyncScheduler` in VSD API.
                
        """
        self._system_sync_scheduler = value

    

    