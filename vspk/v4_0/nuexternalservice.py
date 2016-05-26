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


from .fetchers import NUMetadataTagsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUEndPointsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUExternalService(NURESTObject):
    """ Represents a ExternalService in the VSD

        Notes:
            Representation of External Service.
    """

    __rest_name__ = "externalservice"
    __resource_name__ = "externalservices"

    
    ## Constants
    
    CONST_SERVICE_TYPE_L2 = "L2"
    
    CONST_SERVICE_TYPE_L3 = "L3"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_STAGE_START = "START"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_DIRECTION_INGRESS = "INGRESS"
    
    

    def __init__(self, **kwargs):
        """ Initializes a ExternalService instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> externalservice = NUExternalService(id=u'xxxx-xxx-xxx-xxx', name=u'ExternalService')
                >>> externalservice = NUExternalService(data=my_dict)
        """

        super(NUExternalService, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._service_type = None
        self._description = None
        self._direction = None
        self._entity_scope = None
        self._stage = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="service_type", remote_name="serviceType", attribute_type=str, is_required=True, is_unique=False, choices=[u'L2', u'L3'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="direction", remote_name="direction", attribute_type=str, is_required=False, is_unique=False, choices=[u'INGRESS'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="stage", remote_name="stage", attribute_type=str, is_required=False, is_unique=False, choices=[u'START'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadata_tags = NUMetadataTagsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.end_points = NUEndPointsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                unique name of the External Service. 

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                unique name of the External Service. 

                
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
    def service_type(self):
        """ Get service_type value.

            Notes:
                Type of the service.

                
                This attribute is named `serviceType` in VSD API.
                
        """
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        """ Set service_type value.

            Notes:
                Type of the service.

                
                This attribute is named `serviceType` in VSD API.
                
        """
        self._service_type = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the External Service.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the External Service.

                
        """
        self._description = value

    
    @property
    def direction(self):
        """ Get direction value.

            Notes:
                Direction

                
        """
        return self._direction

    @direction.setter
    def direction(self, value):
        """ Set direction value.

            Notes:
                Direction

                
        """
        self._direction = value

    
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
    def stage(self):
        """ Get stage value.

            Notes:
                Stage -  START,END Possible values are START, .

                
        """
        return self._stage

    @stage.setter
    def stage(self, value):
        """ Set stage value.

            Notes:
                Stage -  START,END Possible values are START, .

                
        """
        self._stage = value

    
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

    

    