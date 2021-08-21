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




from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUPermission(NURESTObject):
    """ Represents a Permission in the VSD

        Notes:
            User groups that are granted permissions for objects such as domains, zones, and subnets can see and manipulate everything within the object.
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
        self._last_updated_date = None
        self._permitted_action = None
        self._permitted_enterprise_description = None
        self._permitted_enterprise_id = None
        self._permitted_enterprise_name = None
        self._permitted_entity_id = None
        self._permitted_entity_name = None
        self._permitted_entity_type = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._creation_date = None
        self._associated_group_description = None
        self._associated_group_id = None
        self._associated_group_name = None
        self._associated_role_description = None
        self._associated_role_id = None
        self._associated_role_name = None
        self._owner = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="permitted_enterprise_description", remote_name="permittedEnterpriseDescription", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_enterprise_id", remote_name="permittedEnterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_enterprise_name", remote_name="permittedEnterpriseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_entity_id", remote_name="permittedEntityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_entity_name", remote_name="permittedEntityName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_entity_type", remote_name="permittedEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_group_description", remote_name="associatedGroupDescription", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_group_id", remote_name="associatedGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_group_name", remote_name="associatedGroupName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_role_description", remote_name="associatedRoleDescription", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_role_id", remote_name="associatedRoleID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_role_name", remote_name="associatedRoleName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
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
    def last_updated_date(self):
        """ Get last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, value):
        """ Set last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        self._last_updated_date = value

    
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
    def permitted_enterprise_description(self):
        """ Get permitted_enterprise_description value.

            Notes:
                Name of the permitted Enterprise

                
                This attribute is named `permittedEnterpriseDescription` in VSD API.
                
        """
        return self._permitted_enterprise_description

    @permitted_enterprise_description.setter
    def permitted_enterprise_description(self, value):
        """ Set permitted_enterprise_description value.

            Notes:
                Name of the permitted Enterprise

                
                This attribute is named `permittedEnterpriseDescription` in VSD API.
                
        """
        self._permitted_enterprise_description = value

    
    @property
    def permitted_enterprise_id(self):
        """ Get permitted_enterprise_id value.

            Notes:
                The enterprise permitted to use/extend  this Gateway

                
                This attribute is named `permittedEnterpriseID` in VSD API.
                
        """
        return self._permitted_enterprise_id

    @permitted_enterprise_id.setter
    def permitted_enterprise_id(self, value):
        """ Set permitted_enterprise_id value.

            Notes:
                The enterprise permitted to use/extend  this Gateway

                
                This attribute is named `permittedEnterpriseID` in VSD API.
                
        """
        self._permitted_enterprise_id = value

    
    @property
    def permitted_enterprise_name(self):
        """ Get permitted_enterprise_name value.

            Notes:
                Name of the associated Enterprise

                
                This attribute is named `permittedEnterpriseName` in VSD API.
                
        """
        return self._permitted_enterprise_name

    @permitted_enterprise_name.setter
    def permitted_enterprise_name(self, value):
        """ Set permitted_enterprise_name value.

            Notes:
                Name of the associated Enterprise

                
                This attribute is named `permittedEnterpriseName` in VSD API.
                
        """
        self._permitted_enterprise_name = value

    
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
    def creation_date(self):
        """ Get creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """ Set creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        self._creation_date = value

    
    @property
    def associated_group_description(self):
        """ Get associated_group_description value.

            Notes:
                Description of the Group

                
                This attribute is named `associatedGroupDescription` in VSD API.
                
        """
        return self._associated_group_description

    @associated_group_description.setter
    def associated_group_description(self, value):
        """ Set associated_group_description value.

            Notes:
                Description of the Group

                
                This attribute is named `associatedGroupDescription` in VSD API.
                
        """
        self._associated_group_description = value

    
    @property
    def associated_group_id(self):
        """ Get associated_group_id value.

            Notes:
                The Group ID associated with this permission.

                
                This attribute is named `associatedGroupID` in VSD API.
                
        """
        return self._associated_group_id

    @associated_group_id.setter
    def associated_group_id(self, value):
        """ Set associated_group_id value.

            Notes:
                The Group ID associated with this permission.

                
                This attribute is named `associatedGroupID` in VSD API.
                
        """
        self._associated_group_id = value

    
    @property
    def associated_group_name(self):
        """ Get associated_group_name value.

            Notes:
                Name of the group for which we have given permission.

                
                This attribute is named `associatedGroupName` in VSD API.
                
        """
        return self._associated_group_name

    @associated_group_name.setter
    def associated_group_name(self, value):
        """ Set associated_group_name value.

            Notes:
                Name of the group for which we have given permission.

                
                This attribute is named `associatedGroupName` in VSD API.
                
        """
        self._associated_group_name = value

    
    @property
    def associated_role_description(self):
        """ Get associated_role_description value.

            Notes:
                Description of the role asssociated with the permission

                
                This attribute is named `associatedRoleDescription` in VSD API.
                
        """
        return self._associated_role_description

    @associated_role_description.setter
    def associated_role_description(self, value):
        """ Set associated_role_description value.

            Notes:
                Description of the role asssociated with the permission

                
                This attribute is named `associatedRoleDescription` in VSD API.
                
        """
        self._associated_role_description = value

    
    @property
    def associated_role_id(self):
        """ Get associated_role_id value.

            Notes:
                ID of the associated Role

                
                This attribute is named `associatedRoleID` in VSD API.
                
        """
        return self._associated_role_id

    @associated_role_id.setter
    def associated_role_id(self, value):
        """ Set associated_role_id value.

            Notes:
                ID of the associated Role

                
                This attribute is named `associatedRoleID` in VSD API.
                
        """
        self._associated_role_id = value

    
    @property
    def associated_role_name(self):
        """ Get associated_role_name value.

            Notes:
                Associated Role Name

                
                This attribute is named `associatedRoleName` in VSD API.
                
        """
        return self._associated_role_name

    @associated_role_name.setter
    def associated_role_name(self, value):
        """ Set associated_role_name value.

            Notes:
                Associated Role Name

                
                This attribute is named `associatedRoleName` in VSD API.
                
        """
        self._associated_role_name = value

    
    @property
    def owner(self):
        """ Get owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """ Set owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        self._owner = value

    
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

    

    