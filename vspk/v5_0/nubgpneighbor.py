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


class NUBGPNeighbor(NURESTObject):
    """ Represents a BGPNeighbor in the VSD

        Notes:
            None
    """

    __rest_name__ = "bgpneighbor"
    __resource_name__ = "bgpneighbors"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a BGPNeighbor instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> bgpneighbor = NUBGPNeighbor(id=u'xxxx-xxx-xxx-xxx', name=u'BGPNeighbor')
                >>> bgpneighbor = NUBGPNeighbor(data=my_dict)
        """

        super(NUBGPNeighbor, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._dampening_enabled = None
        self._peer_as = None
        self._peer_ip = None
        self._description = None
        self._session = None
        self._entity_scope = None
        self._associated_export_routing_policy_id = None
        self._associated_import_routing_policy_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dampening_enabled", remote_name="dampeningEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer_as", remote_name="peerAS", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="peer_ip", remote_name="peerIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="session", remote_name="session", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_export_routing_policy_id", remote_name="associatedExportRoutingPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_import_routing_policy_id", remote_name="associatedImportRoutingPolicyID", attribute_type=str, is_required=False, is_unique=False)
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
                Name of the peer

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the peer

                
        """
        self._name = value

    
    @property
    def dampening_enabled(self):
        """ Get dampening_enabled value.

            Notes:
                Enable/disable route flap damping.

                
                This attribute is named `dampeningEnabled` in VSD API.
                
        """
        return self._dampening_enabled

    @dampening_enabled.setter
    def dampening_enabled(self, value):
        """ Set dampening_enabled value.

            Notes:
                Enable/disable route flap damping.

                
                This attribute is named `dampeningEnabled` in VSD API.
                
        """
        self._dampening_enabled = value

    
    @property
    def peer_as(self):
        """ Get peer_as value.

            Notes:
                Local autonomous system to be used when establishing a session with the remote peer if it is different from the global BGP router autonomous system number.

                
                This attribute is named `peerAS` in VSD API.
                
        """
        return self._peer_as

    @peer_as.setter
    def peer_as(self, value):
        """ Set peer_as value.

            Notes:
                Local autonomous system to be used when establishing a session with the remote peer if it is different from the global BGP router autonomous system number.

                
                This attribute is named `peerAS` in VSD API.
                
        """
        self._peer_as = value

    
    @property
    def peer_ip(self):
        """ Get peer_ip value.

            Notes:
                IP Address of the neighbor. If the neighbor is attached to a host vPort this is optional or must be the same as the host's IP. For uplink or bridge vPort neighbors the IP address must be specified 

                
                This attribute is named `peerIP` in VSD API.
                
        """
        return self._peer_ip

    @peer_ip.setter
    def peer_ip(self, value):
        """ Set peer_ip value.

            Notes:
                IP Address of the neighbor. If the neighbor is attached to a host vPort this is optional or must be the same as the host's IP. For uplink or bridge vPort neighbors the IP address must be specified 

                
                This attribute is named `peerIP` in VSD API.
                
        """
        self._peer_ip = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Short description for this peer

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Short description for this peer

                
        """
        self._description = value

    
    @property
    def session(self):
        """ Get session value.

            Notes:
                neighbor session yang blob

                
        """
        return self._session

    @session.setter
    def session(self, value):
        """ Set session value.

            Notes:
                neighbor session yang blob

                
        """
        self._session = value

    
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
    def associated_export_routing_policy_id(self):
        """ Get associated_export_routing_policy_id value.

            Notes:
                export policy ID

                
                This attribute is named `associatedExportRoutingPolicyID` in VSD API.
                
        """
        return self._associated_export_routing_policy_id

    @associated_export_routing_policy_id.setter
    def associated_export_routing_policy_id(self, value):
        """ Set associated_export_routing_policy_id value.

            Notes:
                export policy ID

                
                This attribute is named `associatedExportRoutingPolicyID` in VSD API.
                
        """
        self._associated_export_routing_policy_id = value

    
    @property
    def associated_import_routing_policy_id(self):
        """ Get associated_import_routing_policy_id value.

            Notes:
                import routing policy ID

                
                This attribute is named `associatedImportRoutingPolicyID` in VSD API.
                
        """
        return self._associated_import_routing_policy_id

    @associated_import_routing_policy_id.setter
    def associated_import_routing_policy_id(self, value):
        """ Set associated_import_routing_policy_id value.

            Notes:
                import routing policy ID

                
                This attribute is named `associatedImportRoutingPolicyID` in VSD API.
                
        """
        self._associated_import_routing_policy_id = value

    
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

    

    