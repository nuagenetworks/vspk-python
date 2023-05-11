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




from .fetchers import NUFlowstatisticsaggregationrulesFetcher


from .fetchers import NUEnterprisesFetcher


from .fetchers import NUNSGatewaysFetcher

from bambou import NURESTObject


class NUStatisticsprofile(NURESTObject):
    """ Represents a Statisticsprofile in the VSD

        Notes:
            Provides the definition of the Statistics Profile
    """

    __rest_name__ = "statisticsprofile"
    __resource_name__ = "statisticsprofiles"

    

    def __init__(self, **kwargs):
        """ Initializes a Statisticsprofile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> statisticsprofile = NUStatisticsprofile(id=u'xxxx-xxx-xxx-xxx', name=u'Statisticsprofile')
                >>> statisticsprofile = NUStatisticsprofile(data=my_dict)
        """

        super(NUStatisticsprofile, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._description = None
        self._flow_stats_aggregation_enabled = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="flow_stats_aggregation_enabled", remote_name="flowStatsAggregationEnabled", attribute_type=bool, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.flowstatisticsaggregationrules = NUFlowstatisticsaggregationrulesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprises = NUEnterprisesFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.ns_gateways = NUNSGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="member")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name of the Statistics Profile.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name of the Statistics Profile.

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Desription of the Statistics Profile.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Desription of the Statistics Profile.

                
        """
        self._description = value

    
    @property
    def flow_stats_aggregation_enabled(self):
        """ Get flow_stats_aggregation_enabled value.

            Notes:
                Indicates if flow statistics aggregation is enabled.

                
                This attribute is named `flowStatsAggregationEnabled` in VSD API.
                
        """
        return self._flow_stats_aggregation_enabled

    @flow_stats_aggregation_enabled.setter
    def flow_stats_aggregation_enabled(self, value):
        """ Set flow_stats_aggregation_enabled value.

            Notes:
                Indicates if flow statistics aggregation is enabled.

                
                This attribute is named `flowStatsAggregationEnabled` in VSD API.
                
        """
        self._flow_stats_aggregation_enabled = value

    

    