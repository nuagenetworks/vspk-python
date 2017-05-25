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


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUPermission(NURESTObject):
    """ Represents a Permission in the VSD

        Notes:
            Represents  Permitted action on an  entity for a group.
    """

    __rest_name__ = "permission"
    __resource_name__ = "permissions"

    
    ## Constants
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Permission instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> permission = NUPermission(id=u'xxxx-xxx-xxx-xxx', name=u'Permission')
                >>> permission = NUPermission(data=my_dict)
        """

        super(NUPermission, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._permitted_action = None
        self._permitted_entity_description = None
        self._permitted_entity_id = None
        self._permitted_entity_name = None
        self._permitted_entity_type = None
        self._entity_scope = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=True, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="permitted_entity_description", remote_name="permittedEntityDescription", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_entity_id", remote_name="permittedEntityID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="permitted_entity_name", remote_name="permittedEntityName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_entity_type", remote_name="permittedEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the  Permission

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the  Permission

                
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
    def permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND/READ/INSTANTIATE  an entity.

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    @permitted_action.setter
    def permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND/READ/INSTANTIATE  an entity.

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    
    @property
    def permitted_entity_description(self):
        """ Get permitted_entity_description value.

            Notes:
                Description for the permittedEntity

                
                This attribute is named `permittedEntityDescription` in VSD API.
                
        """
        return self._permitted_entity_description

    @permitted_entity_description.setter
    def permitted_entity_description(self, value):
        """ Set permitted_entity_description value.

            Notes:
                Description for the permittedEntity

                
                This attribute is named `permittedEntityDescription` in VSD API.
                
        """
        self._permitted_entity_description = value

    
    @property
    def permitted_entity_id(self):
        """ Get permitted_entity_id value.

            Notes:
                The  entity ID for which this permission action is associated against.

                
                This attribute is named `permittedEntityID` in VSD API.
                
        """
        return self._permitted_entity_id

    @permitted_entity_id.setter
    def permitted_entity_id(self, value):
        """ Set permitted_entity_id value.

            Notes:
                The  entity ID for which this permission action is associated against.

                
                This attribute is named `permittedEntityID` in VSD API.
                
        """
        self._permitted_entity_id = value

    
    @property
    def permitted_entity_name(self):
        """ Get permitted_entity_name value.

            Notes:
                Name of the entity for which we have given permission.

                
                This attribute is named `permittedEntityName` in VSD API.
                
        """
        return self._permitted_entity_name

    @permitted_entity_name.setter
    def permitted_entity_name(self, value):
        """ Set permitted_entity_name value.

            Notes:
                Name of the entity for which we have given permission.

                
                This attribute is named `permittedEntityName` in VSD API.
                
        """
        self._permitted_entity_name = value

    
    @property
    def permitted_entity_type(self):
        """ Get permitted_entity_type value.

            Notes:
                Type of the entity for which we have given permission.

                
                This attribute is named `permittedEntityType` in VSD API.
                
        """
        return self._permitted_entity_type

    @permitted_entity_type.setter
    def permitted_entity_type(self, value):
        """ Set permitted_entity_type value.

            Notes:
                Type of the entity for which we have given permission.

                
                This attribute is named `permittedEntityType` in VSD API.
                
        """
        self._permitted_entity_type = value

    
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

    

    