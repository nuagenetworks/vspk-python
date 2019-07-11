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


class NUPatch(NURESTObject):
    """ Represents a Patch in the VSD

        Notes:
            This entity defines a patch installed somewhere (ie. NSG Patch)
    """

    __rest_name__ = "patch"
    __resource_name__ = "patches"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Patch instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> patch = NUPatch(id=u'xxxx-xxx-xxx-xxx', name=u'Patch')
                >>> patch = NUPatch(data=my_dict)
        """

        super(NUPatch, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._patch_build_number = None
        self._patch_summary = None
        self._patch_tag = None
        self._patch_version = None
        self._description = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._supports_deletion = None
        self._supports_network_acceleration = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="patch_build_number", remote_name="patchBuildNumber", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="patch_summary", remote_name="patchSummary", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="patch_tag", remote_name="patchTag", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="patch_version", remote_name="patchVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="supports_deletion", remote_name="supportsDeletion", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="supports_network_acceleration", remote_name="supportsNetworkAcceleration", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The Patch name

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The Patch name

                
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
    def patch_build_number(self):
        """ Get patch_build_number value.

            Notes:
                The Patch build number (eg. 1)

                
                This attribute is named `patchBuildNumber` in VSD API.
                
        """
        return self._patch_build_number

    @patch_build_number.setter
    def patch_build_number(self, value):
        """ Set patch_build_number value.

            Notes:
                The Patch build number (eg. 1)

                
                This attribute is named `patchBuildNumber` in VSD API.
                
        """
        self._patch_build_number = value

    
    @property
    def patch_summary(self):
        """ Get patch_summary value.

            Notes:
                The summary given for the Patch

                
                This attribute is named `patchSummary` in VSD API.
                
        """
        return self._patch_summary

    @patch_summary.setter
    def patch_summary(self, value):
        """ Set patch_summary value.

            Notes:
                The summary given for the Patch

                
                This attribute is named `patchSummary` in VSD API.
                
        """
        self._patch_summary = value

    
    @property
    def patch_tag(self):
        """ Get patch_tag value.

            Notes:
                The Patch Tag. This is a unique identifier including the name, version and release of the patch

                
                This attribute is named `patchTag` in VSD API.
                
        """
        return self._patch_tag

    @patch_tag.setter
    def patch_tag(self, value):
        """ Set patch_tag value.

            Notes:
                The Patch Tag. This is a unique identifier including the name, version and release of the patch

                
                This attribute is named `patchTag` in VSD API.
                
        """
        self._patch_tag = value

    
    @property
    def patch_version(self):
        """ Get patch_version value.

            Notes:
                The Patch version (ie. 1.0.0)

                
                This attribute is named `patchVersion` in VSD API.
                
        """
        return self._patch_version

    @patch_version.setter
    def patch_version(self, value):
        """ Set patch_version value.

            Notes:
                The Patch version (ie. 1.0.0)

                
                This attribute is named `patchVersion` in VSD API.
                
        """
        self._patch_version = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                The Patch description

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                The Patch description

                
        """
        self._description = value

    
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
    def supports_deletion(self):
        """ Get supports_deletion value.

            Notes:
                Whether or not this Patch supports deletion. If a patch does not support deletion, the REST DELETE method will fail

                
                This attribute is named `supportsDeletion` in VSD API.
                
        """
        return self._supports_deletion

    @supports_deletion.setter
    def supports_deletion(self, value):
        """ Set supports_deletion value.

            Notes:
                Whether or not this Patch supports deletion. If a patch does not support deletion, the REST DELETE method will fail

                
                This attribute is named `supportsDeletion` in VSD API.
                
        """
        self._supports_deletion = value

    
    @property
    def supports_network_acceleration(self):
        """ Get supports_network_acceleration value.

            Notes:
                Whether or not this patch supports Network Acceleration

                
                This attribute is named `supportsNetworkAcceleration` in VSD API.
                
        """
        return self._supports_network_acceleration

    @supports_network_acceleration.setter
    def supports_network_acceleration(self, value):
        """ Set supports_network_acceleration value.

            Notes:
                Whether or not this patch supports Network Acceleration

                
                This attribute is named `supportsNetworkAcceleration` in VSD API.
                
        """
        self._supports_network_acceleration = value

    
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

    

    