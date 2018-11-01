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




from .fetchers import NUDestinationurlsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUTier(NURESTObject):
    """ Represents a Tier in the VSD

        Notes:
            When the customer creates an HTTP probe, VSD will automatically create Tier1 and Tier2 under it with default properties.
    """

    __rest_name__ = "tier"
    __resource_name__ = "tiers"

    
    ## Constants
    
    CONST_TIER_TYPE_TIER2 = "TIER2"
    
    CONST_TIER_TYPE_TIER1 = "TIER1"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Tier instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> tier = NUTier(id=u'xxxx-xxx-xxx-xxx', name=u'Tier')
                >>> tier = NUTier(data=my_dict)
        """

        super(NUTier, self).__init__()

        # Read/Write Attributes
        
        self._packet_count = None
        self._last_updated_by = None
        self._description = None
        self._tier_type = None
        self._timeout = None
        self._entity_scope = None
        self._down_threshold_count = None
        self._probe_interval = None
        self._external_id = None
        
        self.expose_attribute(local_name="packet_count", remote_name="packetCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tier_type", remote_name="tierType", attribute_type=str, is_required=True, is_unique=False, choices=[u'TIER1', u'TIER2'])
        self.expose_attribute(local_name="timeout", remote_name="timeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="down_threshold_count", remote_name="downThresholdCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="probe_interval", remote_name="probeInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.destinationurls = NUDestinationurlsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def packet_count(self):
        """ Get packet_count value.

            Notes:
                packet count (part of rate along with probeInterval). Applicable to Tier2 type.

                
                This attribute is named `packetCount` in VSD API.
                
        """
        return self._packet_count

    @packet_count.setter
    def packet_count(self, value):
        """ Set packet_count value.

            Notes:
                packet count (part of rate along with probeInterval). Applicable to Tier2 type.

                
                This attribute is named `packetCount` in VSD API.
                
        """
        self._packet_count = value

    
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
                Descrtiption of the Tier

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Descrtiption of the Tier

                
        """
        self._description = value

    
    @property
    def tier_type(self):
        """ Get tier_type value.

            Notes:
                Tier type

                
                This attribute is named `tierType` in VSD API.
                
        """
        return self._tier_type

    @tier_type.setter
    def tier_type(self, value):
        """ Set tier_type value.

            Notes:
                Tier type

                
                This attribute is named `tierType` in VSD API.
                
        """
        self._tier_type = value

    
    @property
    def timeout(self):
        """ Get timeout value.

            Notes:
                number of milliseconds to wait until the probe is timed out. Applicable to Tier2 type.

                
        """
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        """ Set timeout value.

            Notes:
                number of milliseconds to wait until the probe is timed out. Applicable to Tier2 type.

                
        """
        self._timeout = value

    
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
    def down_threshold_count(self):
        """ Get down_threshold_count value.

            Notes:
                Number of times the probe is allowed to retry on successive timeouts. Applicable only for TIER2

                
                This attribute is named `downThresholdCount` in VSD API.
                
        """
        return self._down_threshold_count

    @down_threshold_count.setter
    def down_threshold_count(self, value):
        """ Set down_threshold_count value.

            Notes:
                Number of times the probe is allowed to retry on successive timeouts. Applicable only for TIER2

                
                This attribute is named `downThresholdCount` in VSD API.
                
        """
        self._down_threshold_count = value

    
    @property
    def probe_interval(self):
        """ Get probe_interval value.

            Notes:
                probe interval (part of rate along with packetCount). Applicable to Tier2 type.

                
                This attribute is named `probeInterval` in VSD API.
                
        """
        return self._probe_interval

    @probe_interval.setter
    def probe_interval(self, value):
        """ Set probe_interval value.

            Notes:
                probe interval (part of rate along with packetCount). Applicable to Tier2 type.

                
                This attribute is named `probeInterval` in VSD API.
                
        """
        self._probe_interval = value

    
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

    

    