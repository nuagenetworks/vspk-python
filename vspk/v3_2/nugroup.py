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


from .fetchers import NUUsersFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUGroup(NURESTObject):
    """ Represents a Group in the VSD

        Notes:
            Identifies a group within an enterprise
    """

    __rest_name__ = "group"
    __resource_name__ = "groups"

    
    ## Constants
    
    CONST_MANAGEMENT_MODE_CMS = "CMS"
    
    CONST_ROLE_CMS = "CMS"
    
    CONST_ROLE_UNKNOWN = "UNKNOWN"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ROLE_ORGNETWORKDESIGNER = "ORGNETWORKDESIGNER"
    
    CONST_ROLE_CSPOPERATOR = "CSPOPERATOR"
    
    CONST_ROLE_USER = "USER"
    
    CONST_ROLE_ORGAPPDESIGNER = "ORGAPPDESIGNER"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ROLE_JMS = "JMS"
    
    CONST_ROLE_ORGUSER = "ORGUSER"
    
    CONST_ROLE_CSPROOT = "CSPROOT"
    
    CONST_ROLE_SYSTEM = "SYSTEM"
    
    CONST_ROLE_ORGADMIN = "ORGADMIN"
    
    CONST_MANAGEMENT_MODE_DEFAULT = "DEFAULT"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Group instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> group = NUGroup(id=u'xxxx-xxx-xxx-xxx', name=u'Group')
                >>> group = NUGroup(data=my_dict)
        """

        super(NUGroup, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._management_mode = None
        self._last_updated_by = None
        self._account_restrictions = None
        self._description = None
        self._restriction_date = None
        self._entity_scope = None
        self._role = None
        self._private = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="management_mode", remote_name="managementMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'CMS', u'DEFAULT'])
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="account_restrictions", remote_name="accountRestrictions", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="restriction_date", remote_name="restrictionDate", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="role", remote_name="role", attribute_type=str, is_required=False, is_unique=False, choices=[u'CMS', u'CSPOPERATOR', u'CSPROOT', u'JMS', u'ORGADMIN', u'ORGAPPDESIGNER', u'ORGNETWORKDESIGNER', u'ORGUSER', u'SYSTEM', u'UNKNOWN', u'USER'])
        self.expose_attribute(local_name="private", remote_name="private", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.users = NUUsersFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                A unique name of the group

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                A unique name of the group

                
        """
        self._name = value

    
    @property
    def management_mode(self):
        """ Get management_mode value.

            Notes:
                Management mode of the user object - allows for override of external authorization and syncup

                
                This attribute is named `managementMode` in VSD API.
                
        """
        return self._management_mode

    @management_mode.setter
    def management_mode(self, value):
        """ Set management_mode value.

            Notes:
                Management mode of the user object - allows for override of external authorization and syncup

                
                This attribute is named `managementMode` in VSD API.
                
        """
        self._management_mode = value

    
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
    def account_restrictions(self):
        """ Get account_restrictions value.

            Notes:
                Determines whether group is disabled or not.

                
                This attribute is named `accountRestrictions` in VSD API.
                
        """
        return self._account_restrictions

    @account_restrictions.setter
    def account_restrictions(self, value):
        """ Set account_restrictions value.

            Notes:
                Determines whether group is disabled or not.

                
                This attribute is named `accountRestrictions` in VSD API.
                
        """
        self._account_restrictions = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the group

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the group

                
        """
        self._description = value

    
    @property
    def restriction_date(self):
        """ Get restriction_date value.

            Notes:
                When the group was disabled.

                
                This attribute is named `restrictionDate` in VSD API.
                
        """
        return self._restriction_date

    @restriction_date.setter
    def restriction_date(self, value):
        """ Set restriction_date value.

            Notes:
                When the group was disabled.

                
                This attribute is named `restrictionDate` in VSD API.
                
        """
        self._restriction_date = value

    
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
    def role(self):
        """ Get role value.

            Notes:
                The role associated with this group.

                
        """
        return self._role

    @role.setter
    def role(self, value):
        """ Set role value.

            Notes:
                The role associated with this group.

                
        """
        self._role = value

    
    @property
    def private(self):
        """ Get private value.

            Notes:
                A private group is visible only by the owner of the group. Public groups are visible by all users in the enterprise

                
        """
        return self._private

    @private.setter
    def private(self, value):
        """ Set private value.

            Notes:
                A private group is visible only by the owner of the group. Public groups are visible by all users in the enterprise

                
        """
        self._private = value

    
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

    

    