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
    
    CONST_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_METRIC_PACKETS_IN_DROPPED = "PACKETS_IN_DROPPED"
    
    CONST_TYPE_BREACH = "BREACH"
    
    CONST_METRIC_PACKETS_OUT_ERROR = "PACKETS_OUT_ERROR"
    
    CONST_METRIC_BYTES_OUT = "BYTES_OUT"
    
    CONST_TYPE_ROLLING_AVERAGE = "ROLLING_AVERAGE"
    
    CONST_METRIC_PACKETS_DROPPED_BY_RATE_LIMIT = "PACKETS_DROPPED_BY_RATE_LIMIT"
    
    CONST_METRIC_BYTES_IN = "BYTES_IN"
    
    CONST_METRIC_INGRESS_PACKET_COUNT = "INGRESS_PACKET_COUNT"
    
    CONST_METRIC_EGRESS_BYTE_COUNT = "EGRESS_BYTE_COUNT"
    
    CONST_SCOPE_LOCAL = "LOCAL"
    
    CONST_METRIC_INGRESS_BYTE_COUNT = "INGRESS_BYTE_COUNT"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_METRIC_PACKETS_OUT_DROPPED = "PACKETS_OUT_DROPPED"
    
    CONST_METRIC_PACKETS_IN = "PACKETS_IN"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_METRIC_PACKETS_OUT = "PACKETS_OUT"
    
    CONST_METRIC_EGRESS_PACKET_COUNT = "EGRESS_PACKET_COUNT"
    
    CONST_METRIC_PACKETS_IN_ERROR = "PACKETS_IN_ERROR"
    
    

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
        self._last_updated_by = None
        self._scope = None
        self._period = None
        self._description = None
        self._metric = None
        self._threshold = None
        self._entity_scope = None
        self._external_id = None
        self._type = None
        
        self.expose_attribute(local_name="url_end_point", remote_name="URLEndPoint", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="scope", remote_name="scope", attribute_type=str, is_required=True, is_unique=False, choices=[u'GLOBAL', u'LOCAL'])
        self.expose_attribute(local_name="period", remote_name="period", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metric", remote_name="metric", attribute_type=str, is_required=True, is_unique=False, choices=[u'BYTES_IN', u'BYTES_OUT', u'EGRESS_BYTE_COUNT', u'EGRESS_PACKET_COUNT', u'INGRESS_BYTE_COUNT', u'INGRESS_PACKET_COUNT', u'PACKETS_DROPPED_BY_RATE_LIMIT', u'PACKETS_IN', u'PACKETS_IN_DROPPED', u'PACKETS_IN_ERROR', u'PACKETS_OUT', u'PACKETS_OUT_DROPPED', u'PACKETS_OUT_ERROR'])
        self.expose_attribute(local_name="threshold", remote_name="threshold", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=True, is_unique=False, choices=[u'BREACH', u'ROLLING_AVERAGE'])
        

        # Fetchers
        
        
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
    def scope(self):
        """ Get scope value.

            Notes:
                GLOBAL or LOCAL scope. Global refers to aggregate values across subnets, zones or domains. Local refers to traffic from/to individual VMs.

                
        """
        return self._scope

    @scope.setter
    def scope(self, value):
        """ Set scope value.

            Notes:
                GLOBAL or LOCAL scope. Global refers to aggregate values across subnets, zones or domains. Local refers to traffic from/to individual VMs.

                
        """
        self._scope = value

    
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
                Desription of the TCA

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Desription of the TCA

                
        """
        self._description = value

    
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
                Rolling average or sequence of samples over the averaging period.

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                Rolling average or sequence of samples over the averaging period.

                
        """
        self._type = value

    

    