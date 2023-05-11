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



from bambou import NURESTObject


class NUFlowstatisticsaggregationrule(NURESTObject):
    """ Represents a Flowstatisticsaggregationrule in the VSD

        Notes:
            Provides the definition of the flow statistics Aggregation Rule.
    """

    __rest_name__ = "flowstatisticsaggregationrule"
    __resource_name__ = "flowstatisticsaggregationrules"

    
    ## Constants
    
    CONST_MATCHING_CRITERIA_L4_SERVICE_GROUP = "L4_SERVICE_GROUP"
    
    CONST_MATCHING_CRITERIA_L4_SERVICE = "L4_SERVICE"
    
    CONST_AGGREGATION_CRITERIA_FORWARD_AND_REVERSE_TRAFFIC_PORT_AGG = "FORWARD_AND_REVERSE_TRAFFIC_PORT_AGG"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Flowstatisticsaggregationrule instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> flowstatisticsaggregationrule = NUFlowstatisticsaggregationrule(id=u'xxxx-xxx-xxx-xxx', name=u'Flowstatisticsaggregationrule')
                >>> flowstatisticsaggregationrule = NUFlowstatisticsaggregationrule(data=my_dict)
        """

        super(NUFlowstatisticsaggregationrule, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._matching_criteria = None
        self._description = None
        self._aggregation_criteria = None
        self._associated_traffic_type_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="matching_criteria", remote_name="matchingCriteria", attribute_type=str, is_required=True, is_unique=False, choices=[u'L4_SERVICE', u'L4_SERVICE_GROUP'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aggregation_criteria", remote_name="aggregationCriteria", attribute_type=str, is_required=True, is_unique=False, choices=[u'FORWARD_AND_REVERSE_TRAFFIC_PORT_AGG'])
        self.expose_attribute(local_name="associated_traffic_type_id", remote_name="associatedTrafficTypeID", attribute_type=str, is_required=True, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name of the flow statistics aggregation rule.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name of the flow statistics aggregation rule.

                
        """
        self._name = value

    
    @property
    def matching_criteria(self):
        """ Get matching_criteria value.

            Notes:
                This property reflects the type of traffic associated to flow statistics aggregation rule. Supported values are L4_SERVICE, L4_SERVICE_GROUP.

                
                This attribute is named `matchingCriteria` in VSD API.
                
        """
        return self._matching_criteria

    @matching_criteria.setter
    def matching_criteria(self, value):
        """ Set matching_criteria value.

            Notes:
                This property reflects the type of traffic associated to flow statistics aggregation rule. Supported values are L4_SERVICE, L4_SERVICE_GROUP.

                
                This attribute is named `matchingCriteria` in VSD API.
                
        """
        self._matching_criteria = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Desription of the flow statistics aggregation rule.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Desription of the flow statistics aggregation rule.

                
        """
        self._description = value

    
    @property
    def aggregation_criteria(self):
        """ Get aggregation_criteria value.

            Notes:
                Indicates the criteria for statistics aggregation.

                
                This attribute is named `aggregationCriteria` in VSD API.
                
        """
        return self._aggregation_criteria

    @aggregation_criteria.setter
    def aggregation_criteria(self, value):
        """ Set aggregation_criteria value.

            Notes:
                Indicates the criteria for statistics aggregation.

                
                This attribute is named `aggregationCriteria` in VSD API.
                
        """
        self._aggregation_criteria = value

    
    @property
    def associated_traffic_type_id(self):
        """ Get associated_traffic_type_id value.

            Notes:
                Associated Service/Service Group ID.

                
                This attribute is named `associatedTrafficTypeID` in VSD API.
                
        """
        return self._associated_traffic_type_id

    @associated_traffic_type_id.setter
    def associated_traffic_type_id(self, value):
        """ Set associated_traffic_type_id value.

            Notes:
                Associated Service/Service Group ID.

                
                This attribute is named `associatedTrafficTypeID` in VSD API.
                
        """
        self._associated_traffic_type_id = value

    

    