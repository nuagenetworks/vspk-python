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


class NULTEInformation(NURESTObject):
    """ Represents a LTEInformation in the VSD

        Notes:
            Contains information about the LTE dongle plugged in USB port on NSG. This would have information like - Modem Manufacturer, Model Number, Subscriber Number, Operator etc. This information could vary from vendor to vendor.
    """

    __rest_name__ = "lteinformation"
    __resource_name__ = "lteinformations"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a LTEInformation instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> lteinformation = NULTEInformation(id=u'xxxx-xxx-xxx-xxx', name=u'LTEInformation')
                >>> lteinformation = NULTEInformation(data=my_dict)
        """

        super(NULTEInformation, self).__init__()

        # Read/Write Attributes
        
        self._lte_connection_info = None
        self._last_updated_by = None
        self._entity_scope = None
        self._external_id = None
        
        self.expose_attribute(local_name="lte_connection_info", remote_name="LTEConnectionInfo", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def lte_connection_info(self):
        """ Get lte_connection_info value.

            Notes:
                This attribute holds all the information about the LTE dongle plugged in to NSG. This is in JSON format and has information like - Modem Manufacturer, Model Number, Subscriber Number,  Operator etc.

                
                This attribute is named `LTEConnectionInfo` in VSD API.
                
        """
        return self._lte_connection_info

    @lte_connection_info.setter
    def lte_connection_info(self, value):
        """ Set lte_connection_info value.

            Notes:
                This attribute holds all the information about the LTE dongle plugged in to NSG. This is in JSON format and has information like - Modem Manufacturer, Model Number, Subscriber Number,  Operator etc.

                
                This attribute is named `LTEConnectionInfo` in VSD API.
                
        """
        self._lte_connection_info = value

    
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

    

    