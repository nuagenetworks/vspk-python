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


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUTCA(NURESTObject):
    """ Represents a TCA in the VSD

        Notes:
            Provides the definition of the Threshold Control Alarms.
    """

    __rest_name__ = "tca"
    __resource_name__ = "tcas"

    
    ## Constants
    
    CONST_METRIC_PACKETS_OUT_DROPPED = "PACKETS_OUT_DROPPED"
    
    CONST_PROTOCOL_NONE = "NONE"
    
    CONST_METRIC_FIP_RATE_LIMIT_DROPPED_PACKETS = "FIP_RATE_LIMIT_DROPPED_PACKETS"
    
    CONST_TYPE_BREACH = "BREACH"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_METRIC_TCP_FLAG_RST_IN = "TCP_FLAG_RST_IN"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_METRIC_TCP_FLAG_ACK_OUT = "TCP_FLAG_ACK_OUT"
    
    CONST_METRIC_PORT_SWEEP_IP_COUNT = "PORT_SWEEP_IP_COUNT"
    
    CONST_METRIC_PACKETS_IN_DROPPED = "PACKETS_IN_DROPPED"
    
    CONST_METRIC_L7_BYTES_OUT = "L7_BYTES_OUT"
    
    CONST_TYPE_UNIQUE_COUNT = "UNIQUE_COUNT"
    
    CONST_PROTOCOL_UDP = "UDP"
    
    CONST_METRIC_FIP_RATE_LIMIT_DROPPED_BYTES = "FIP_RATE_LIMIT_DROPPED_BYTES"
    
    CONST_METRIC_DESTINATION_PORT_PROTOCOL_COUNT = "DESTINATION_PORT_PROTOCOL_COUNT"
    
    CONST_METRIC_PACKETS_DROPPED_BY_RATE_LIMIT = "PACKETS_DROPPED_BY_RATE_LIMIT"
    
    CONST_METRIC_PACKETS_IN = "PACKETS_IN"
    
    CONST_METRIC_IDP_EVENT_COUNT = "IDP_EVENT_COUNT"
    
    CONST_METRIC_TCP_FLAG_ACK_IN = "TCP_FLAG_ACK_IN"
    
    CONST_METRIC_ANTI_SPOOF_EVENT_COUNT = "ANTI_SPOOF_EVENT_COUNT"
    
    CONST_METRIC_ACL_DENY_EVENT_COUNT = "ACL_DENY_EVENT_COUNT"
    
    CONST_METRIC_PORT_SCAN_PORT_COUNT = "PORT_SCAN_PORT_COUNT"
    
    CONST_METRIC_TCP_FLAG_NULL_IN = "TCP_FLAG_NULL_IN"
    
    CONST_METRIC_TCP_FLAG_NULL_OUT = "TCP_FLAG_NULL_OUT"
    
    CONST_METRIC_BYTES_IN = "BYTES_IN"
    
    CONST_ACTION_ALERT_ADD_POLICY_GROUP = "Alert_Add_Policy_Group"
    
    CONST_METRIC_FIP_PRE_RATE_LIMIT_BYTES = "FIP_PRE_RATE_LIMIT_BYTES"
    
    CONST_METRIC_TCP_FLAG_RST_OUT = "TCP_FLAG_RST_OUT"
    
    CONST_ACTION_ALERT_POLICYGROUPCHANGE = "Alert_PolicyGroupChange"
    
    CONST_METRIC_PACKETS_IN_ERROR = "PACKETS_IN_ERROR"
    
    CONST_PROTOCOL_TCP = "TCP"
    
    CONST_METRIC_HIGH_RISK_IP_ACCESS_EVENT_COUNT = "HIGH_RISK_IP_ACCESS_EVENT_COUNT"
    
    CONST_METRIC_PACKETS_OUT_ERROR = "PACKETS_OUT_ERROR"
    
    CONST_METRIC_BYTES_OUT = "BYTES_OUT"
    
    CONST_METRIC_L7_PACKETS_OUT = "L7_PACKETS_OUT"
    
    CONST_METRIC_L7_BYTES_IN = "L7_BYTES_IN"
    
    CONST_ACTION_ALERT_ADD_NETWORK_MACRO = "Alert_Add_Network_Macro"
    
    CONST_METRIC_TCP_FLAG_SYN_OUT = "TCP_FLAG_SYN_OUT"
    
    CONST_METRIC_PACKETS_OUT = "PACKETS_OUT"
    
    CONST_TYPE_ROLLING_AVERAGE = "ROLLING_AVERAGE"
    
    CONST_METRIC_FIP_PRE_RATE_LIMIT_PACKETS = "FIP_PRE_RATE_LIMIT_PACKETS"
    
    CONST_METRIC_MEDIUM_RISK_IP_ACCESS_EVENT_COUNT = "MEDIUM_RISK_IP_ACCESS_EVENT_COUNT"
    
    CONST_ACTION_ALERT = "Alert"
    
    CONST_METRIC_TCP_FLAG_SYN_IN = "TCP_FLAG_SYN_IN"
    
    CONST_METRIC_L7_PACKETS_IN = "L7_PACKETS_IN"
    
    

    def __init__(self, **kwargs):
        """ Initializes a TCA instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> tca = NUTCA(id=u'xxxx-xxx-xxx-xxx', name=u'TCA')
                >>> tca = NUTCA(data=my_dict)
        """

        super(NUTCA, self).__init__()

        # Read/Write Attributes
        
        self._url_end_point = None
        self._name = None
        self._target_entity_id = None
        self._target_policy_group_id = None
        self._last_updated_by = None
        self._last_updated_date = None
        self._action = None
        self._period = None
        self._description = None
        self._destination_port = None
        self._metric = None
        self._threshold = None
        self._throttle_time = None
        self._disable = None
        self._display_status = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._count = None
        self._creation_date = None
        self._trigger_interval = None
        self._protocol = None
        self._status = None
        self._owner = None
        self._external_id = None
        self._type = None
        
        self.expose_attribute(local_name="url_end_point", remote_name="URLEndPoint", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="target_entity_id", remote_name="targetEntityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="target_policy_group_id", remote_name="targetPolicyGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="action", remote_name="action", attribute_type=str, is_required=True, is_unique=False, choices=[u'Alert', u'Alert_Add_Network_Macro', u'Alert_Add_Policy_Group', u'Alert_PolicyGroupChange'])
        self.expose_attribute(local_name="period", remote_name="period", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="destination_port", remote_name="destinationPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metric", remote_name="metric", attribute_type=str, is_required=True, is_unique=False, choices=[u'ACL_DENY_EVENT_COUNT', u'ANTI_SPOOF_EVENT_COUNT', u'BYTES_IN', u'BYTES_OUT', u'DESTINATION_PORT_PROTOCOL_COUNT', u'FIP_PRE_RATE_LIMIT_BYTES', u'FIP_PRE_RATE_LIMIT_PACKETS', u'FIP_RATE_LIMIT_DROPPED_BYTES', u'FIP_RATE_LIMIT_DROPPED_PACKETS', u'HIGH_RISK_IP_ACCESS_EVENT_COUNT', u'IDP_EVENT_COUNT', u'L7_BYTES_IN', u'L7_BYTES_OUT', u'L7_PACKETS_IN', u'L7_PACKETS_OUT', u'MEDIUM_RISK_IP_ACCESS_EVENT_COUNT', u'PACKETS_DROPPED_BY_RATE_LIMIT', u'PACKETS_IN', u'PACKETS_IN_DROPPED', u'PACKETS_IN_ERROR', u'PACKETS_OUT', u'PACKETS_OUT_DROPPED', u'PACKETS_OUT_ERROR', u'PORT_SCAN_PORT_COUNT', u'PORT_SWEEP_IP_COUNT', u'TCP_FLAG_ACK_IN', u'TCP_FLAG_ACK_OUT', u'TCP_FLAG_NULL_IN', u'TCP_FLAG_NULL_OUT', u'TCP_FLAG_RST_IN', u'TCP_FLAG_RST_OUT', u'TCP_FLAG_SYN_IN', u'TCP_FLAG_SYN_OUT'])
        self.expose_attribute(local_name="threshold", remote_name="threshold", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="throttle_time", remote_name="throttleTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="disable", remote_name="disable", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="display_status", remote_name="displayStatus", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="count", remote_name="count", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="trigger_interval", remote_name="triggerInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="protocol", remote_name="protocol", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'TCP', u'UDP'])
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=True, is_unique=False, choices=[u'BREACH', u'ROLLING_AVERAGE', u'UNIQUE_COUNT'])
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def url_end_point(self):
        """ Get url_end_point value.

            Notes:
                URL endpoint to post Alarm data to when TCA is triggered

                
                This attribute is named `URLEndPoint` in VSD API.
                
        """
        return self._url_end_point

    @url_end_point.setter
    def url_end_point(self, value):
        """ Set url_end_point value.

            Notes:
                URL endpoint to post Alarm data to when TCA is triggered

                
                This attribute is named `URLEndPoint` in VSD API.
                
        """
        self._url_end_point = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name of the TCA

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name of the TCA

                
        """
        self._name = value

    
    @property
    def target_entity_id(self):
        """ Get target_entity_id value.

            Notes:
                ID of the target VSD entity used by the TCA action

                
                This attribute is named `targetEntityID` in VSD API.
                
        """
        return self._target_entity_id

    @target_entity_id.setter
    def target_entity_id(self, value):
        """ Set target_entity_id value.

            Notes:
                ID of the target VSD entity used by the TCA action

                
                This attribute is named `targetEntityID` in VSD API.
                
        """
        self._target_entity_id = value

    
    @property
    def target_policy_group_id(self):
        """ Get target_policy_group_id value.

            Notes:
                Target policygroup used by the TCA action

                
                This attribute is named `targetPolicyGroupID` in VSD API.
                
        """
        return self._target_policy_group_id

    @target_policy_group_id.setter
    def target_policy_group_id(self, value):
        """ Set target_policy_group_id value.

            Notes:
                Target policygroup used by the TCA action

                
                This attribute is named `targetPolicyGroupID` in VSD API.
                
        """
        self._target_policy_group_id = value

    
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
    def action(self):
        """ Get action value.

            Notes:
                Action to be taken when TCA is fired - Alert or PolicyGroupChange

                
        """
        return self._action

    @action.setter
    def action(self, value):
        """ Set action value.

            Notes:
                Action to be taken when TCA is fired - Alert or PolicyGroupChange

                
        """
        self._action = value

    
    @property
    def period(self):
        """ Get period value.

            Notes:
                The averaging period

                
        """
        return self._period

    @period.setter
    def period(self, value):
        """ Set period value.

            Notes:
                The averaging period

                
        """
        self._period = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the TCA

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the TCA

                
        """
        self._description = value

    
    @property
    def destination_port(self):
        """ Get destination_port value.

            Notes:
                Destination Port Number. Valid range is 1-65535 for the metric DESTINATION_PORT_PROTOCOL_COUNT, 0 for rest of the metrics.

                
                This attribute is named `destinationPort` in VSD API.
                
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, value):
        """ Set destination_port value.

            Notes:
                Destination Port Number. Valid range is 1-65535 for the metric DESTINATION_PORT_PROTOCOL_COUNT, 0 for rest of the metrics.

                
                This attribute is named `destinationPort` in VSD API.
                
        """
        self._destination_port = value

    
    @property
    def metric(self):
        """ Get metric value.

            Notes:
                The metric associated with the TCA.

                
        """
        return self._metric

    @metric.setter
    def metric(self, value):
        """ Set metric value.

            Notes:
                The metric associated with the TCA.

                
        """
        self._metric = value

    
    @property
    def threshold(self):
        """ Get threshold value.

            Notes:
                The threshold that must be exceeded before an alarm is issued

                
        """
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        """ Set threshold value.

            Notes:
                The threshold that must be exceeded before an alarm is issued

                
        """
        self._threshold = value

    
    @property
    def throttle_time(self):
        """ Get throttle_time value.

            Notes:
                Throttle time in seconds

                
                This attribute is named `throttleTime` in VSD API.
                
        """
        return self._throttle_time

    @throttle_time.setter
    def throttle_time(self, value):
        """ Set throttle_time value.

            Notes:
                Throttle time in seconds

                
                This attribute is named `throttleTime` in VSD API.
                
        """
        self._throttle_time = value

    
    @property
    def disable(self):
        """ Get disable value.

            Notes:
                This flag is used to indicate whether the watch(TCA) is enabled/disabled

                
        """
        return self._disable

    @disable.setter
    def disable(self, value):
        """ Set disable value.

            Notes:
                This flag is used to indicate whether the watch(TCA) is enabled/disabled

                
        """
        self._disable = value

    
    @property
    def display_status(self):
        """ Get display_status value.

            Notes:
                Explanation of the TCA status

                
                This attribute is named `displayStatus` in VSD API.
                
        """
        return self._display_status

    @display_status.setter
    def display_status(self, value):
        """ Set display_status value.

            Notes:
                Explanation of the TCA status

                
                This attribute is named `displayStatus` in VSD API.
                
        """
        self._display_status = value

    
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
    def count(self):
        """ Get count value.

            Notes:
                Count of the attempts by maintenanace thread to create/update watcher

                
        """
        return self._count

    @count.setter
    def count(self, value):
        """ Set count value.

            Notes:
                Count of the attempts by maintenanace thread to create/update watcher

                
        """
        self._count = value

    
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
    def trigger_interval(self):
        """ Get trigger_interval value.

            Notes:
                The trigger interval of the ES watch corresponding to this TCA, in seconds

                
                This attribute is named `triggerInterval` in VSD API.
                
        """
        return self._trigger_interval

    @trigger_interval.setter
    def trigger_interval(self, value):
        """ Set trigger_interval value.

            Notes:
                The trigger interval of the ES watch corresponding to this TCA, in seconds

                
                This attribute is named `triggerInterval` in VSD API.
                
        """
        self._trigger_interval = value

    
    @property
    def protocol(self):
        """ Get protocol value.

            Notes:
                L4 service protocol - Possible values TCP, UDP for the metric DESTINATION_PORT_PROTOCOL_COUNT, NONE for rest of the metrics.

                
        """
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        """ Set protocol value.

            Notes:
                L4 service protocol - Possible values TCP, UDP for the metric DESTINATION_PORT_PROTOCOL_COUNT, NONE for rest of the metrics.

                
        """
        self._protocol = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                This flag is used to indicate the status of TCA

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                This flag is used to indicate the status of TCA

                
        """
        self._status = value

    
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
    def type(self):
        """ Get type value.

            Notes:
                The aggregation type for the metric over the selected period - Sum, Average or Unique Count

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                The aggregation type for the metric over the selected period - Sum, Average or Unique Count

                
        """
        self._type = value

    

    