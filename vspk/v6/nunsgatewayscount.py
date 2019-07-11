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


class NUNSGatewaysCount(NURESTObject):
    """ Represents a NSGatewaysCount in the VSD

        Notes:
            NSGateway count is a summary object per enterprise which contains the counts of inactive and NSGs by alarm severity. This object is used in Application Aware Routing (AAR) visualization
    """

    __rest_name__ = "nsgatewayscount"
    __resource_name__ = "nsgatewayscounts"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NSGatewaysCount instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsgatewayscount = NUNSGatewaysCount(id=u'xxxx-xxx-xxx-xxx', name=u'NSGatewaysCount')
                >>> nsgatewayscount = NUNSGatewaysCount(data=my_dict)
        """

        super(NUNSGatewaysCount, self).__init__()

        # Read/Write Attributes
        
        self._active_nsg_count = None
        self._alarmed_nsg_count = None
        self._embedded_metadata = None
        self._inactive_nsg_count = None
        self._entity_scope = None
        self._external_id = None
        
        self.expose_attribute(local_name="active_nsg_count", remote_name="activeNSGCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="alarmed_nsg_count", remote_name="alarmedNSGCount", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="inactive_nsg_count", remote_name="inactiveNSGCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def active_nsg_count(self):
        """ Get active_nsg_count value.

            Notes:
                Number of Network Service Gateways in an enterprise whose bootstrap status is ACTIVE

                
                This attribute is named `activeNSGCount` in VSD API.
                
        """
        return self._active_nsg_count

    @active_nsg_count.setter
    def active_nsg_count(self, value):
        """ Set active_nsg_count value.

            Notes:
                Number of Network Service Gateways in an enterprise whose bootstrap status is ACTIVE

                
                This attribute is named `activeNSGCount` in VSD API.
                
        """
        self._active_nsg_count = value

    
    @property
    def alarmed_nsg_count(self):
        """ Get alarmed_nsg_count value.

            Notes:
                An embedded object containing three attributes: critical, major, healthy - number of NSGs with CRITICAL alarm severity, manumber of NSGs with MAJOR alarm severity, number of NSGs that have no CRITICAL or MAJOR alarms

                
                This attribute is named `alarmedNSGCount` in VSD API.
                
        """
        return self._alarmed_nsg_count

    @alarmed_nsg_count.setter
    def alarmed_nsg_count(self, value):
        """ Set alarmed_nsg_count value.

            Notes:
                An embedded object containing three attributes: critical, major, healthy - number of NSGs with CRITICAL alarm severity, manumber of NSGs with MAJOR alarm severity, number of NSGs that have no CRITICAL or MAJOR alarms

                
                This attribute is named `alarmedNSGCount` in VSD API.
                
        """
        self._alarmed_nsg_count = value

    
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
    def inactive_nsg_count(self):
        """ Get inactive_nsg_count value.

            Notes:
                Number of Network Service Gateways in an enterprise whose bootstrap status is not ACTIVE

                
                This attribute is named `inactiveNSGCount` in VSD API.
                
        """
        return self._inactive_nsg_count

    @inactive_nsg_count.setter
    def inactive_nsg_count(self, value):
        """ Set inactive_nsg_count value.

            Notes:
                Number of Network Service Gateways in an enterprise whose bootstrap status is not ACTIVE

                
                This attribute is named `inactiveNSGCount` in VSD API.
                
        """
        self._inactive_nsg_count = value

    
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

    

    