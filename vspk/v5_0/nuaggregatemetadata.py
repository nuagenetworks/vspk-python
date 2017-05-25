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


class NUAggregateMetadata(NURESTObject):
    """ Represents a AggregateMetadata in the VSD

        Notes:
            Metadata associated to a entity
    """

    __rest_name__ = "aggregatemetadata"
    __resource_name__ = "aggregatemetadatas"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a AggregateMetadata instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> aggregatemetadata = NUAggregateMetadata(id=u'xxxx-xxx-xxx-xxx', name=u'AggregateMetadata')
                >>> aggregatemetadata = NUAggregateMetadata(data=my_dict)
        """

        super(NUAggregateMetadata, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._description = None
        self._metadata_tag_ids = None
        self._network_notification_disabled = None
        self._blob = None
        self._global_metadata = None
        self._entity_scope = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_tag_ids", remote_name="metadataTagIDs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_notification_disabled", remote_name="networkNotificationDisabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="blob", remote_name="blob", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="global_metadata", remote_name="global", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Metadata.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Metadata.

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the Metadata.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the Metadata.

                
        """
        self._description = value

    
    @property
    def metadata_tag_ids(self):
        """ Get metadata_tag_ids value.

            Notes:
                Metadata tag IDs associated with this metadata. You can filter metadata based on this attribute for example  X-Nuage-Filter: '2d6fb627-603b-421c-b63a-eb0a6d712761' IN metadataTagIDs 

                
                This attribute is named `metadataTagIDs` in VSD API.
                
        """
        return self._metadata_tag_ids

    @metadata_tag_ids.setter
    def metadata_tag_ids(self, value):
        """ Set metadata_tag_ids value.

            Notes:
                Metadata tag IDs associated with this metadata. You can filter metadata based on this attribute for example  X-Nuage-Filter: '2d6fb627-603b-421c-b63a-eb0a6d712761' IN metadataTagIDs 

                
                This attribute is named `metadataTagIDs` in VSD API.
                
        """
        self._metadata_tag_ids = value

    
    @property
    def network_notification_disabled(self):
        """ Get network_notification_disabled value.

            Notes:
                Specifies metadata changes need to be notified to controller,by default it is notified

                
                This attribute is named `networkNotificationDisabled` in VSD API.
                
        """
        return self._network_notification_disabled

    @network_notification_disabled.setter
    def network_notification_disabled(self, value):
        """ Set network_notification_disabled value.

            Notes:
                Specifies metadata changes need to be notified to controller,by default it is notified

                
                This attribute is named `networkNotificationDisabled` in VSD API.
                
        """
        self._network_notification_disabled = value

    
    @property
    def blob(self):
        """ Get blob value.

            Notes:
                Metadata that describes about the entity attached to it.

                
        """
        return self._blob

    @blob.setter
    def blob(self, value):
        """ Set blob value.

            Notes:
                Metadata that describes about the entity attached to it.

                
        """
        self._blob = value

    
    @property
    def global_metadata(self):
        """ Get global_metadata value.

            Notes:
                Specifies whether the metadata is global or local

                
                This attribute is named `global` in VSD API.
                
        """
        return self._global_metadata

    @global_metadata.setter
    def global_metadata(self, value):
        """ Set global_metadata value.

            Notes:
                Specifies whether the metadata is global or local

                
                This attribute is named `global` in VSD API.
                
        """
        self._global_metadata = value

    
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

    

    