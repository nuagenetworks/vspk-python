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


class NUDUCGroupBinding(NURESTObject):
    """ Represents a DUCGroupBinding in the VSD

        Notes:
            None
    """

    __rest_name__ = "ducgroupbinding"
    __resource_name__ = "ducgroupbindings"

    
    ## Constants
    
    CONST_ASSOCIATED_UBR_GROUP_FUNCTION_GATEWAY = "GATEWAY"
    
    CONST_ASSOCIATED_UBR_GROUP_FUNCTION_UBR = "UBR"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a DUCGroupBinding instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ducgroupbinding = NUDUCGroupBinding(id=u'xxxx-xxx-xxx-xxx', name=u'DUCGroupBinding')
                >>> ducgroupbinding = NUDUCGroupBinding(data=my_dict)
        """

        super(NUDUCGroupBinding, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._one_way_delay = None
        self._entity_scope = None
        self._priority = None
        self._associated_duc_group_id = None
        self._associated_ubr_group_function = None
        self._associated_ubr_group_name = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="one_way_delay", remote_name="oneWayDelay", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_duc_group_id", remote_name="associatedDUCGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ubr_group_function", remote_name="associatedUBRGroupFunction", attribute_type=str, is_required=False, is_unique=False, choices=[u'GATEWAY', u'UBR'])
        self.expose_attribute(local_name="associated_ubr_group_name", remote_name="associatedUBRGroupName", attribute_type=str, is_required=False, is_unique=False)
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
    def one_way_delay(self):
        """ Get one_way_delay value.

            Notes:
                SLA delay value in milliseconds that is tolerated between NSG instances and NSG-UBR (DUC) instances being bound through this binding instance.  If delay is to be ignored, then the value of -1 is to be entered.  Value 0 is not permitted.

                
                This attribute is named `oneWayDelay` in VSD API.
                
        """
        return self._one_way_delay

    @one_way_delay.setter
    def one_way_delay(self, value):
        """ Set one_way_delay value.

            Notes:
                SLA delay value in milliseconds that is tolerated between NSG instances and NSG-UBR (DUC) instances being bound through this binding instance.  If delay is to be ignored, then the value of -1 is to be entered.  Value 0 is not permitted.

                
                This attribute is named `oneWayDelay` in VSD API.
                
        """
        self._one_way_delay = value

    
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
    def priority(self):
        """ Get priority value.

            Notes:
                The priority for NSG Group to UBR Group relationship.

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                The priority for NSG Group to UBR Group relationship.

                
        """
        self._priority = value

    
    @property
    def associated_duc_group_id(self):
        """ Get associated_duc_group_id value.

            Notes:
                Identification of the UBR Group associated to this group binding instance.

                
                This attribute is named `associatedDUCGroupID` in VSD API.
                
        """
        return self._associated_duc_group_id

    @associated_duc_group_id.setter
    def associated_duc_group_id(self, value):
        """ Set associated_duc_group_id value.

            Notes:
                Identification of the UBR Group associated to this group binding instance.

                
                This attribute is named `associatedDUCGroupID` in VSD API.
                
        """
        self._associated_duc_group_id = value

    
    @property
    def associated_ubr_group_function(self):
        """ Get associated_ubr_group_function value.

            Notes:
                NSG Function supported by the associated UBR group.

                
                This attribute is named `associatedUBRGroupFunction` in VSD API.
                
        """
        return self._associated_ubr_group_function

    @associated_ubr_group_function.setter
    def associated_ubr_group_function(self, value):
        """ Set associated_ubr_group_function value.

            Notes:
                NSG Function supported by the associated UBR group.

                
                This attribute is named `associatedUBRGroupFunction` in VSD API.
                
        """
        self._associated_ubr_group_function = value

    
    @property
    def associated_ubr_group_name(self):
        """ Get associated_ubr_group_name value.

            Notes:
                Name of the associated UBR Group.

                
                This attribute is named `associatedUBRGroupName` in VSD API.
                
        """
        return self._associated_ubr_group_name

    @associated_ubr_group_name.setter
    def associated_ubr_group_name(self, value):
        """ Set associated_ubr_group_name value.

            Notes:
                Name of the associated UBR Group.

                
                This attribute is named `associatedUBRGroupName` in VSD API.
                
        """
        self._associated_ubr_group_name = value

    
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

    

    