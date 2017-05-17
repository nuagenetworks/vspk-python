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



from .fetchers import NUWANServicesFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUPortsFetcher


from .fetchers import NUNSPortsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUAutoDiscoveredGateway(NURESTObject):
    """ Represents a AutoDiscoveredGateway in the VSD

        Notes:
            Represents Auto discovered Gateway.
    """

    __rest_name__ = "autodiscoveredgateway"
    __resource_name__ = "autodiscoveredgateways"

    
    ## Constants
    
    CONST_PERSONALITY_HARDWARE_VTEP = "HARDWARE_VTEP"
    
    CONST_PERSONALITY_VSA = "VSA"
    
    CONST_PERSONALITY_VSG = "VSG"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_PERSONALITY_OTHER = "OTHER"
    
    CONST_PERSONALITY_NSG = "NSG"
    
    CONST_PERSONALITY_VRSG = "VRSG"
    
    CONST_PERSONALITY_DC7X50 = "DC7X50"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a AutoDiscoveredGateway instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> autodiscoveredgateway = NUAutoDiscoveredGateway(id=u'xxxx-xxx-xxx-xxx', name=u'AutoDiscoveredGateway')
                >>> autodiscoveredgateway = NUAutoDiscoveredGateway(data=my_dict)
        """

        super(NUAutoDiscoveredGateway, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._gateway_id = None
        self._peer = None
        self._personality = None
        self._description = None
        self._entity_scope = None
        self._controllers = None
        self._vtep = None
        self._external_id = None
        self._system_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_id", remote_name="gatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer", remote_name="peer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=True, is_unique=False, choices=[u'DC7X50', u'HARDWARE_VTEP', u'NSG', u'OTHER', u'VRSG', u'VSA', u'VSG'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="controllers", remote_name="controllers", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vtep", remote_name="vtep", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="system_id", remote_name="systemID", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.wan_services = NUWANServicesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ports = NUPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_ports = NUNSPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Gateway

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Gateway

                
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
    def gateway_id(self):
        """ Get gateway_id value.

            Notes:
                The Gateway associated with this  Auto Discovered Gateway  . This is a read only attribute

                
                This attribute is named `gatewayID` in VSD API.
                
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, value):
        """ Set gateway_id value.

            Notes:
                The Gateway associated with this  Auto Discovered Gateway  . This is a read only attribute

                
                This attribute is named `gatewayID` in VSD API.
                
        """
        self._gateway_id = value

    
    @property
    def peer(self):
        """ Get peer value.

            Notes:
                The System ID of the peer gateway associated with this Gateway instance when it is discovered by the network manager (VSD) as being redundant.

                
        """
        return self._peer

    @peer.setter
    def peer(self, value):
        """ Set peer value.

            Notes:
                The System ID of the peer gateway associated with this Gateway instance when it is discovered by the network manager (VSD) as being redundant.

                
        """
        self._peer = value

    
    @property
    def personality(self):
        """ Get personality value.

            Notes:
                Personality of the Gateway - VSG,VRSG,NONE,OTHER, cannot be changed after creation.

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                Personality of the Gateway - VSG,VRSG,NONE,OTHER, cannot be changed after creation.

                
        """
        self._personality = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the Gateway

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the Gateway

                
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
    def controllers(self):
        """ Get controllers value.

            Notes:
                Controllers to which this gateway instance is associated with.

                
        """
        return self._controllers

    @controllers.setter
    def controllers(self, value):
        """ Set controllers value.

            Notes:
                Controllers to which this gateway instance is associated with.

                
        """
        self._controllers = value

    
    @property
    def vtep(self):
        """ Get vtep value.

            Notes:
                Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.

                
        """
        return self._vtep

    @vtep.setter
    def vtep(self, value):
        """ Set vtep value.

            Notes:
                Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.

                
        """
        self._vtep = value

    
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
    def system_id(self):
        """ Get system_id value.

            Notes:
                Identifier of the Gateway

                
                This attribute is named `systemID` in VSD API.
                
        """
        return self._system_id

    @system_id.setter
    def system_id(self, value):
        """ Set system_id value.

            Notes:
                Identifier of the Gateway

                
                This attribute is named `systemID` in VSD API.
                
        """
        self._system_id = value

    

    