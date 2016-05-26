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


class NUVPortMirror(NURESTObject):
    """ Represents a VPortMirror in the VSD

        Notes:
            VPort Mirror represents the relationship between a vport and a mirror destination.
    """

    __rest_name__ = "vportmirror"
    __resource_name__ = "vportmirrors"

    
    ## Constants
    
    CONST_MIRROR_DIRECTION_BOTH = "BOTH"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_MIRROR_DIRECTION_INGRESS = "INGRESS"
    
    CONST_MIRROR_DIRECTION_EGRESS = "EGRESS"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VPortMirror instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vportmirror = NUVPortMirror(id=u'xxxx-xxx-xxx-xxx', name=u'VPortMirror')
                >>> vportmirror = NUVPortMirror(data=my_dict)
        """

        super(NUVPortMirror, self).__init__()

        # Read/Write Attributes
        
        self._vport_name = None
        self._last_updated_by = None
        self._network_name = None
        self._mirror_destination_id = None
        self._mirror_destination_name = None
        self._mirror_direction = None
        self._enterpise_name = None
        self._entity_scope = None
        self._domain_name = None
        self._vport_id = None
        self._attached_network_type = None
        self._external_id = None
        
        self.expose_attribute(local_name="vport_name", remote_name="VPortName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_name", remote_name="networkName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mirror_destination_id", remote_name="mirrorDestinationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mirror_destination_name", remote_name="mirrorDestinationName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mirror_direction", remote_name="mirrorDirection", attribute_type=str, is_required=False, is_unique=False, choices=[u'BOTH', u'EGRESS', u'INGRESS'])
        self.expose_attribute(local_name="enterpise_name", remote_name="enterpiseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="domain_name", remote_name="domainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vport_id", remote_name="vportId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="attached_network_type", remote_name="attachedNetworkType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vport_name(self):
        """ Get vport_name value.

            Notes:
                Name of the vport to which the mirror destination is associated with.

                
                This attribute is named `VPortName` in VSD API.
                
        """
        return self._vport_name

    @vport_name.setter
    def vport_name(self, value):
        """ Set vport_name value.

            Notes:
                Name of the vport to which the mirror destination is associated with.

                
                This attribute is named `VPortName` in VSD API.
                
        """
        self._vport_name = value

    
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
    def network_name(self):
        """ Get network_name value.

            Notes:
                Name of the network to which the vport belongs to

                
                This attribute is named `networkName` in VSD API.
                
        """
        return self._network_name

    @network_name.setter
    def network_name(self, value):
        """ Set network_name value.

            Notes:
                Name of the network to which the vport belongs to

                
                This attribute is named `networkName` in VSD API.
                
        """
        self._network_name = value

    
    @property
    def mirror_destination_id(self):
        """ Get mirror_destination_id value.

            Notes:
                Destination ID of the mirror destination object.

                
                This attribute is named `mirrorDestinationID` in VSD API.
                
        """
        return self._mirror_destination_id

    @mirror_destination_id.setter
    def mirror_destination_id(self, value):
        """ Set mirror_destination_id value.

            Notes:
                Destination ID of the mirror destination object.

                
                This attribute is named `mirrorDestinationID` in VSD API.
                
        """
        self._mirror_destination_id = value

    
    @property
    def mirror_destination_name(self):
        """ Get mirror_destination_name value.

            Notes:
                Name of the mirror destination

                
                This attribute is named `mirrorDestinationName` in VSD API.
                
        """
        return self._mirror_destination_name

    @mirror_destination_name.setter
    def mirror_destination_name(self, value):
        """ Set mirror_destination_name value.

            Notes:
                Name of the mirror destination

                
                This attribute is named `mirrorDestinationName` in VSD API.
                
        """
        self._mirror_destination_name = value

    
    @property
    def mirror_direction(self):
        """ Get mirror_direction value.

            Notes:
                Describes what type of traffic needs to be mirrored.

                
                This attribute is named `mirrorDirection` in VSD API.
                
        """
        return self._mirror_direction

    @mirror_direction.setter
    def mirror_direction(self, value):
        """ Set mirror_direction value.

            Notes:
                Describes what type of traffic needs to be mirrored.

                
                This attribute is named `mirrorDirection` in VSD API.
                
        """
        self._mirror_direction = value

    
    @property
    def enterpise_name(self):
        """ Get enterpise_name value.

            Notes:
                Enterprise to which the vport associated with the mirror destination belongs to.

                
                This attribute is named `enterpiseName` in VSD API.
                
        """
        return self._enterpise_name

    @enterpise_name.setter
    def enterpise_name(self, value):
        """ Set enterpise_name value.

            Notes:
                Enterprise to which the vport associated with the mirror destination belongs to.

                
                This attribute is named `enterpiseName` in VSD API.
                
        """
        self._enterpise_name = value

    
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
    def domain_name(self):
        """ Get domain_name value.

            Notes:
                Domain name of the vport associated with the mirror destination

                
                This attribute is named `domainName` in VSD API.
                
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        """ Set domain_name value.

            Notes:
                Domain name of the vport associated with the mirror destination

                
                This attribute is named `domainName` in VSD API.
                
        """
        self._domain_name = value

    
    @property
    def vport_id(self):
        """ Get vport_id value.

            Notes:
                Id of the vport to which the mirror destination is associated with.

                
                This attribute is named `vportId` in VSD API.
                
        """
        return self._vport_id

    @vport_id.setter
    def vport_id(self, value):
        """ Set vport_id value.

            Notes:
                Id of the vport to which the mirror destination is associated with.

                
                This attribute is named `vportId` in VSD API.
                
        """
        self._vport_id = value

    
    @property
    def attached_network_type(self):
        """ Get attached_network_type value.

            Notes:
                Type of the network attached - L2/L3

                
                This attribute is named `attachedNetworkType` in VSD API.
                
        """
        return self._attached_network_type

    @attached_network_type.setter
    def attached_network_type(self, value):
        """ Set attached_network_type value.

            Notes:
                Type of the network attached - L2/L3

                
                This attribute is named `attachedNetworkType` in VSD API.
                
        """
        self._attached_network_type = value

    
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

    

    