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


class NUDHCPOption(NURESTObject):
    """ Represents a DHCPOption in the VSD

        Notes:
            Allows the definition of one or more DHCP options that will be provided to all VMs that are associated with a given domain. DHCP options are provided as Type- Length-Value (TLV). There is no validation by VSD on whether these options are valid or not. It is up to the user to guarantee that the options make sense for their application.
    """

    __rest_name__ = "dhcpoption"
    __resource_name__ = "dhcpoptions"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a DHCPOption instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> dhcpoption = NUDHCPOption(id=u'xxxx-xxx-xxx-xxx', name=u'DHCPOption')
                >>> dhcpoption = NUDHCPOption(data=my_dict)
        """

        super(NUDHCPOption, self).__init__()

        # Read/Write Attributes
        
        self._value = None
        self._last_updated_by = None
        self._actual_type = None
        self._actual_values = None
        self._length = None
        self._entity_scope = None
        self._external_id = None
        self._type = None
        
        self.expose_attribute(local_name="value", remote_name="value", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="actual_type", remote_name="actualType", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="actual_values", remote_name="actualValues", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="length", remote_name="length", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=True, is_unique=False)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def value(self):
        """ Get value value.

            Notes:
                DHCP option value. Value should be a hexadecimal value(ie. Hex value 0xac40 would be passed as 'ac40')

                
        """
        return self._value

    @value.setter
    def value(self, value):
        """ Set value value.

            Notes:
                DHCP option value. Value should be a hexadecimal value(ie. Hex value 0xac40 would be passed as 'ac40')

                
        """
        self._value = value

    
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
    def actual_type(self):
        """ Get actual_type value.

            Notes:
                This will be used to send actual type instead of the hexadecimal. Note: If actualType is set, it will override the entry set in the type attribute

                
                This attribute is named `actualType` in VSD API.
                
        """
        return self._actual_type

    @actual_type.setter
    def actual_type(self, value):
        """ Set actual_type value.

            Notes:
                This will be used to send actual type instead of the hexadecimal. Note: If actualType is set, it will override the entry set in the type attribute

                
                This attribute is named `actualType` in VSD API.
                
        """
        self._actual_type = value

    
    @property
    def actual_values(self):
        """ Get actual_values value.

            Notes:
                This will be used to send actual values instead of the hexadecimal. Note: If actualValues are set, it will override entry set in the value attribute

                
                This attribute is named `actualValues` in VSD API.
                
        """
        return self._actual_values

    @actual_values.setter
    def actual_values(self, value):
        """ Set actual_values value.

            Notes:
                This will be used to send actual values instead of the hexadecimal. Note: If actualValues are set, it will override entry set in the value attribute

                
                This attribute is named `actualValues` in VSD API.
                
        """
        self._actual_values = value

    
    @property
    def length(self):
        """ Get length value.

            Notes:
                DHCP option length. Length should be a hexadecimal value(ie. Hex value 0x04 would be passed as '04')

                
        """
        return self._length

    @length.setter
    def length(self, value):
        """ Set length value.

            Notes:
                DHCP option length. Length should be a hexadecimal value(ie. Hex value 0x04 would be passed as '04')

                
        """
        self._length = value

    
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

    
    @property
    def type(self):
        """ Get type value.

            Notes:
                DHCP option type. Type should be a hexadecimal value(ie. Hex value 0x06 would be passed as '06')

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                DHCP option type. Type should be a hexadecimal value(ie. Hex value 0x06 would be passed as '06')

                
        """
        self._type = value

    

    