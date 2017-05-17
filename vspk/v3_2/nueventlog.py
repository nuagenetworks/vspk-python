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


class NUEventLog(NURESTObject):
    """ Represents a EventLog in the VSD

        Notes:
            The API retrieves the events related to a particular entity
    """

    __rest_name__ = "eventlog"
    __resource_name__ = "eventlogs"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a EventLog instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> eventlog = NUEventLog(id=u'xxxx-xxx-xxx-xxx', name=u'EventLog')
                >>> eventlog = NUEventLog(data=my_dict)
        """

        super(NUEventLog, self).__init__()

        # Read/Write Attributes
        
        self._diff = None
        self._enterprise = None
        self._entities = None
        self._entity_id = None
        self._entity_parent_id = None
        self._entity_parent_type = None
        self._entity_scope = None
        self._entity_type = None
        self._user = None
        self._event_received_time = None
        self._external_id = None
        self._type = None
        
        self.expose_attribute(local_name="diff", remote_name="diff", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise", remote_name="enterprise", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entities", remote_name="entities", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_id", remote_name="entityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_parent_id", remote_name="entityParentID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_parent_type", remote_name="entityParentType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="entity_type", remote_name="entityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="user", remote_name="user", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="event_received_time", remote_name="eventReceivedTime", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def diff(self):
        """ Get diff value.

            Notes:
                Holds the results of diff between two objects of same type.

                
        """
        return self._diff

    @diff.setter
    def diff(self, value):
        """ Set diff value.

            Notes:
                Holds the results of diff between two objects of same type.

                
        """
        self._diff = value

    
    @property
    def enterprise(self):
        """ Get enterprise value.

            Notes:
                The enterprise name of the user who triggered this event.

                
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, value):
        """ Set enterprise value.

            Notes:
                The enterprise name of the user who triggered this event.

                
        """
        self._enterprise = value

    
    @property
    def entities(self):
        """ Get entities value.

            Notes:
                List of entities associated with the event.

                
        """
        return self._entities

    @entities.setter
    def entities(self, value):
        """ Set entities value.

            Notes:
                List of entities associated with the event.

                
        """
        self._entities = value

    
    @property
    def entity_id(self):
        """ Get entity_id value.

            Notes:
                The entity id associated with this event.

                
                This attribute is named `entityID` in VSD API.
                
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        """ Set entity_id value.

            Notes:
                The entity id associated with this event.

                
                This attribute is named `entityID` in VSD API.
                
        """
        self._entity_id = value

    
    @property
    def entity_parent_id(self):
        """ Get entity_parent_id value.

            Notes:
                The entity parent id associated with this event. It can be null.

                
                This attribute is named `entityParentID` in VSD API.
                
        """
        return self._entity_parent_id

    @entity_parent_id.setter
    def entity_parent_id(self, value):
        """ Set entity_parent_id value.

            Notes:
                The entity parent id associated with this event. It can be null.

                
                This attribute is named `entityParentID` in VSD API.
                
        """
        self._entity_parent_id = value

    
    @property
    def entity_parent_type(self):
        """ Get entity_parent_type value.

            Notes:
                Event parent entity type.  Generally reported against enterprise.

                
                This attribute is named `entityParentType` in VSD API.
                
        """
        return self._entity_parent_type

    @entity_parent_type.setter
    def entity_parent_type(self, value):
        """ Set entity_parent_type value.

            Notes:
                Event parent entity type.  Generally reported against enterprise.

                
                This attribute is named `entityParentType` in VSD API.
                
        """
        self._entity_parent_type = value

    
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
    def entity_type(self):
        """ Get entity_type value.

            Notes:
                The entity type of this event. It may be Domain, VirtualMachine, etc.,

                
                This attribute is named `entityType` in VSD API.
                
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        """ Set entity_type value.

            Notes:
                The entity type of this event. It may be Domain, VirtualMachine, etc.,

                
                This attribute is named `entityType` in VSD API.
                
        """
        self._entity_type = value

    
    @property
    def user(self):
        """ Get user value.

            Notes:
                The authenticated user who triggered this event.

                
        """
        return self._user

    @user.setter
    def user(self, value):
        """ Set user value.

            Notes:
                The authenticated user who triggered this event.

                
        """
        self._user = value

    
    @property
    def event_received_time(self):
        """ Get event_received_time value.

            Notes:
                The time that event was received.

                
                This attribute is named `eventReceivedTime` in VSD API.
                
        """
        return self._event_received_time

    @event_received_time.setter
    def event_received_time(self, value):
        """ Set event_received_time value.

            Notes:
                The time that event was received.

                
                This attribute is named `eventReceivedTime` in VSD API.
                
        """
        self._event_received_time = value

    
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
    def type(self):
        """ Get type value.

            Notes:
                The event type (CREATE, UPDATE or DELETE).

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                The event type (CREATE, UPDATE or DELETE).

                
        """
        self._type = value

    

    