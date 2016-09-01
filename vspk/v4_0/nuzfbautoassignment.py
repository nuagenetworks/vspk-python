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


from bambou import NURESTObject


class NUZFBAutoAssignment(NURESTObject):
    """ Represents a ZFBAutoAssignment in the VSD

        Notes:
            ZFB Enterprise Auto Assignment 
    """

    __rest_name__ = "zfbautoassignment"
    __resource_name__ = "zfbautoassignments"

    
    ## Constants
    
    CONST_ZFB_MATCH_ATTRIBUTE_NSGATEWAY_ID = "NSGATEWAY_ID"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ZFB_MATCH_ATTRIBUTE_HOSTNAME = "HOSTNAME"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ZFB_MATCH_ATTRIBUTE_MAC_ADDRESS = "MAC_ADDRESS"
    
    CONST_ZFB_MATCH_ATTRIBUTE_IP_ADDRESS = "IP_ADDRESS"
    
    CONST_ZFB_MATCH_ATTRIBUTE_SERIAL_NUMBER = "SERIAL_NUMBER"
    
    

    def __init__(self, **kwargs):
        """ Initializes a ZFBAutoAssignment instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> zfbautoassignment = NUZFBAutoAssignment(id=u'xxxx-xxx-xxx-xxx', name=u'ZFBAutoAssignment')
                >>> zfbautoassignment = NUZFBAutoAssignment(data=my_dict)
        """

        super(NUZFBAutoAssignment, self).__init__()

        # Read/Write Attributes
        
        self._zfb_match_attribute = None
        self._zfb_match_attribute_values = None
        self._name = None
        self._last_updated_by = None
        self._description = None
        self._entity_scope = None
        self._priority = None
        self._associated_enterprise_id = None
        self._associated_enterprise_name = None
        self._external_id = None
        
        self.expose_attribute(local_name="zfb_match_attribute", remote_name="ZFBMatchAttribute", attribute_type=str, is_required=False, is_unique=False, choices=[u'HOSTNAME', u'IP_ADDRESS', u'MAC_ADDRESS', u'NSGATEWAY_ID', u'SERIAL_NUMBER'])
        self.expose_attribute(local_name="zfb_match_attribute_values", remote_name="ZFBMatchAttributeValues", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="associated_enterprise_id", remote_name="associatedEnterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_enterprise_name", remote_name="associatedEnterpriseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def zfb_match_attribute(self):
        """ Get zfb_match_attribute value.

            Notes:
                Attribute to auto match on

                
                This attribute is named `ZFBMatchAttribute` in VSD API.
                
        """
        return self._zfb_match_attribute

    @zfb_match_attribute.setter
    def zfb_match_attribute(self, value):
        """ Set zfb_match_attribute value.

            Notes:
                Attribute to auto match on

                
                This attribute is named `ZFBMatchAttribute` in VSD API.
                
        """
        self._zfb_match_attribute = value

    
    @property
    def zfb_match_attribute_values(self):
        """ Get zfb_match_attribute_values value.

            Notes:
                Array of values to match on

                
                This attribute is named `ZFBMatchAttributeValues` in VSD API.
                
        """
        return self._zfb_match_attribute_values

    @zfb_match_attribute_values.setter
    def zfb_match_attribute_values(self, value):
        """ Set zfb_match_attribute_values value.

            Notes:
                Array of values to match on

                
                This attribute is named `ZFBMatchAttributeValues` in VSD API.
                
        """
        self._zfb_match_attribute_values = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the ZFB auto assignment criteria.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the ZFB auto assignment criteria.

                
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
    def description(self):
        """ Get description value.

            Notes:
                Description of the ZFB auto assignment criteria.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the ZFB auto assignment criteria.

                
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
    def priority(self):
        """ Get priority value.

            Notes:
                Priority of the Auto Assignment

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                Priority of the Auto Assignment

                
        """
        self._priority = value

    
    @property
    def associated_enterprise_id(self):
        """ Get associated_enterprise_id value.

            Notes:
                Associated Enterprise ID

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        return self._associated_enterprise_id

    @associated_enterprise_id.setter
    def associated_enterprise_id(self, value):
        """ Set associated_enterprise_id value.

            Notes:
                Associated Enterprise ID

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        self._associated_enterprise_id = value

    
    @property
    def associated_enterprise_name(self):
        """ Get associated_enterprise_name value.

            Notes:
                The name of the associated Enterprise

                
                This attribute is named `associatedEnterpriseName` in VSD API.
                
        """
        return self._associated_enterprise_name

    @associated_enterprise_name.setter
    def associated_enterprise_name(self, value):
        """ Set associated_enterprise_name value.

            Notes:
                The name of the associated Enterprise

                
                This attribute is named `associatedEnterpriseName` in VSD API.
                
        """
        self._associated_enterprise_name = value

    
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

    

    