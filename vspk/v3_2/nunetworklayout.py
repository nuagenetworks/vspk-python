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


class NUNetworkLayout(NURESTObject):
    """ Represents a NetworkLayout in the VSD

        Notes:
            This API defines the AS number that should be used in the data center as well as the IP address of the route reflector.
    """

    __rest_name__ = "networklayout"
    __resource_name__ = "networklayout"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_SERVICE_TYPE_SUBNET_ONLY = "SUBNET_ONLY"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_SERVICE_TYPE_ROUTER_SWITCH = "ROUTER_SWITCH"
    
    CONST_SERVICE_TYPE_ROUTER_ONLY = "ROUTER_ONLY"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NetworkLayout instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> networklayout = NUNetworkLayout(id=u'xxxx-xxx-xxx-xxx', name=u'NetworkLayout')
                >>> networklayout = NUNetworkLayout(data=my_dict)
        """

        super(NUNetworkLayout, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._service_type = None
        self._entity_scope = None
        self._route_reflector_ip = None
        self._autonomous_system_num = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="service_type", remote_name="serviceType", attribute_type=str, is_required=False, is_unique=False, choices=[u'ROUTER_ONLY', u'ROUTER_SWITCH', u'SUBNET_ONLY'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="route_reflector_ip", remote_name="routeReflectorIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="autonomous_system_num", remote_name="autonomousSystemNum", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
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
    def service_type(self):
        """ Get service_type value.

            Notes:
                Identifies whether L3 or L2 services are supported.

                
                This attribute is named `serviceType` in VSD API.
                
        """
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        """ Set service_type value.

            Notes:
                Identifies whether L3 or L2 services are supported.

                
                This attribute is named `serviceType` in VSD API.
                
        """
        self._service_type = value

    
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
    def route_reflector_ip(self):
        """ Get route_reflector_ip value.

            Notes:
                The IP address of the route reflector that can be used by the VSCs

                
                This attribute is named `routeReflectorIP` in VSD API.
                
        """
        return self._route_reflector_ip

    @route_reflector_ip.setter
    def route_reflector_ip(self, value):
        """ Set route_reflector_ip value.

            Notes:
                The IP address of the route reflector that can be used by the VSCs

                
                This attribute is named `routeReflectorIP` in VSD API.
                
        """
        self._route_reflector_ip = value

    
    @property
    def autonomous_system_num(self):
        """ Get autonomous_system_num value.

            Notes:
                The AS number associated with this data center

                
                This attribute is named `autonomousSystemNum` in VSD API.
                
        """
        return self._autonomous_system_num

    @autonomous_system_num.setter
    def autonomous_system_num(self, value):
        """ Set autonomous_system_num value.

            Notes:
                The AS number associated with this data center

                
                This attribute is named `autonomousSystemNum` in VSD API.
                
        """
        self._autonomous_system_num = value

    
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

    

    