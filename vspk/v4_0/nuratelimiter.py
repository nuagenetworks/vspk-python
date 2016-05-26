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


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NURateLimiter(NURESTObject):
    """ Represents a RateLimiter in the VSD

        Notes:
            Rate Limiter object that contains peak, burst and cir. It can be associated with Egress QOS policy objects.
    """

    __rest_name__ = "ratelimiter"
    __resource_name__ = "ratelimiters"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a RateLimiter instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ratelimiter = NURateLimiter(id=u'xxxx-xxx-xxx-xxx', name=u'RateLimiter')
                >>> ratelimiter = NURateLimiter(data=my_dict)
        """

        super(NURateLimiter, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._peak_burst_size = None
        self._peak_information_rate = None
        self._description = None
        self._entity_scope = None
        self._committed_information_rate = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peak_burst_size", remote_name="peakBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peak_information_rate", remote_name="peakInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="committed_information_rate", remote_name="committedInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                A unique name of the Rate Limiter object

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                A unique name of the Rate Limiter object

                
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
    def peak_burst_size(self):
        """ Get peak_burst_size value.

            Notes:
                Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bits; only whole values are supported.

                
                This attribute is named `peakBurstSize` in VSD API.
                
        """
        return self._peak_burst_size

    @peak_burst_size.setter
    def peak_burst_size(self, value):
        """ Set peak_burst_size value.

            Notes:
                Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bits; only whole values are supported.

                
                This attribute is named `peakBurstSize` in VSD API.
                
        """
        self._peak_burst_size = value

    
    @property
    def peak_information_rate(self):
        """ Get peak_information_rate value.

            Notes:
                Peak Information Rate :  Peak bandwidth allowed in Mb/s; only whole values supported.

                
                This attribute is named `peakInformationRate` in VSD API.
                
        """
        return self._peak_information_rate

    @peak_information_rate.setter
    def peak_information_rate(self, value):
        """ Set peak_information_rate value.

            Notes:
                Peak Information Rate :  Peak bandwidth allowed in Mb/s; only whole values supported.

                
                This attribute is named `peakInformationRate` in VSD API.
                
        """
        self._peak_information_rate = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the Rate Limiter object

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the Rate Limiter object

                
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
    def committed_information_rate(self):
        """ Get committed_information_rate value.

            Notes:
                Committed Information Rate :  Committed bandwidth that is allowed in Mb/s; only whole values supported.

                
                This attribute is named `committedInformationRate` in VSD API.
                
        """
        return self._committed_information_rate

    @committed_information_rate.setter
    def committed_information_rate(self, value):
        """ Set committed_information_rate value.

            Notes:
                Committed Information Rate :  Committed bandwidth that is allowed in Mb/s; only whole values supported.

                
                This attribute is named `committedInformationRate` in VSD API.
                
        """
        self._committed_information_rate = value

    
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

    

    