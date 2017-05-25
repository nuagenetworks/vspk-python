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


class NURoutingPolicy(NURESTObject):
    """ Represents a RoutingPolicy in the VSD

        Notes:
            None
    """

    __rest_name__ = "routingpolicy"
    __resource_name__ = "routingpolicies"

    
    ## Constants
    
    CONST_DEFAULT_ACTION_ACCEPT = "ACCEPT"
    
    CONST_DEFAULT_ACTION_REJECT = "REJECT"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a RoutingPolicy instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> routingpolicy = NURoutingPolicy(id=u'xxxx-xxx-xxx-xxx', name=u'RoutingPolicy')
                >>> routingpolicy = NURoutingPolicy(data=my_dict)
        """

        super(NURoutingPolicy, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._default_action = None
        self._description = None
        self._entity_scope = None
        self._policy_definition = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="default_action", remote_name="defaultAction", attribute_type=str, is_required=True, is_unique=False, choices=[u'ACCEPT', u'REJECT'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="policy_definition", remote_name="policyDefinition", attribute_type=str, is_required=False, is_unique=False)
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
                policy name, unique within an enterprise

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                policy name, unique within an enterprise

                
        """
        self._name = value

    
    @property
    def default_action(self):
        """ Get default_action value.

            Notes:
                accept/reject

                
                This attribute is named `defaultAction` in VSD API.
                
        """
        return self._default_action

    @default_action.setter
    def default_action(self, value):
        """ Set default_action value.

            Notes:
                accept/reject

                
                This attribute is named `defaultAction` in VSD API.
                
        """
        self._default_action = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                None

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                None

                
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
    def policy_definition(self):
        """ Get policy_definition value.

            Notes:
                String blob

                
                This attribute is named `policyDefinition` in VSD API.
                
        """
        return self._policy_definition

    @policy_definition.setter
    def policy_definition(self, value):
        """ Set policy_definition value.

            Notes:
                String blob

                
                This attribute is named `policyDefinition` in VSD API.
                
        """
        self._policy_definition = value

    
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

    

    