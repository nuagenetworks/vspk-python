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


from .fetchers import NUApplicationsFetcher

from bambou import NURESTObject


class NUL7applicationsignature(NURESTObject):
    """ Represents a L7applicationsignature in the VSD

        Notes:
            Layer 7 ApplicationType , these are auto created as part of VSD bringup
    """

    __rest_name__ = "l7applicationsignature"
    __resource_name__ = "l7applicationsignatures"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a L7applicationsignature instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> l7applicationsignature = NUL7applicationsignature(id=u'xxxx-xxx-xxx-xxx', name=u'L7applicationsignature')
                >>> l7applicationsignature = NUL7applicationsignature(data=my_dict)
        """

        super(NUL7applicationsignature, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._category = None
        self._readonly = None
        self._reference = None
        self._deprecated = None
        self._deprecated_version = None
        self._description = None
        self._dictionary_version = None
        self._signature_index = None
        self._signature_version = None
        self._risk = None
        self._plugin_name = None
        self._entity_scope = None
        self._software_flags = None
        self._productivity = None
        self._guidstring = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="category", remote_name="category", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="readonly", remote_name="readonly", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="reference", remote_name="reference", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="deprecated", remote_name="deprecated", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="deprecated_version", remote_name="deprecatedVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dictionary_version", remote_name="dictionaryVersion", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="signature_index", remote_name="signatureIndex", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="signature_version", remote_name="signatureVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="risk", remote_name="risk", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="plugin_name", remote_name="pluginName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="software_flags", remote_name="softwareFlags", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="productivity", remote_name="productivity", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="guidstring", remote_name="guidstring", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.applications = NUApplicationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                 name of the L7 App

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                 name of the L7 App

                
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
    def category(self):
        """ Get category value.

            Notes:
                Category of this application

                
        """
        return self._category

    @category.setter
    def category(self, value):
        """ Set category value.

            Notes:
                Category of this application

                
        """
        self._category = value

    
    @property
    def readonly(self):
        """ Get readonly value.

            Notes:
                Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

                
        """
        return self._readonly

    @readonly.setter
    def readonly(self, value):
        """ Set readonly value.

            Notes:
                Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

                
        """
        self._readonly = value

    
    @property
    def reference(self):
        """ Get reference value.

            Notes:
                URL address reference received from Procera for every signature.

                
        """
        return self._reference

    @reference.setter
    def reference(self, value):
        """ Set reference value.

            Notes:
                URL address reference received from Procera for every signature.

                
        """
        self._reference = value

    
    @property
    def deprecated(self):
        """ Get deprecated value.

            Notes:
                Determines whether this entity is deprecated. Deprecated L7 Application Signatures cannot be associated to an application.

                
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, value):
        """ Set deprecated value.

            Notes:
                Determines whether this entity is deprecated. Deprecated L7 Application Signatures cannot be associated to an application.

                
        """
        self._deprecated = value

    
    @property
    def deprecated_version(self):
        """ Get deprecated_version value.

            Notes:
                Determines the procera version when this entity was deprecated. Deprecated objects cannot be modified or deleted.

                
                This attribute is named `deprecatedVersion` in VSD API.
                
        """
        return self._deprecated_version

    @deprecated_version.setter
    def deprecated_version(self, value):
        """ Set deprecated_version value.

            Notes:
                Determines the procera version when this entity was deprecated. Deprecated objects cannot be modified or deleted.

                
                This attribute is named `deprecatedVersion` in VSD API.
                
        """
        self._deprecated_version = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                description for L7 App

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                description for L7 App

                
        """
        self._description = value

    
    @property
    def dictionary_version(self):
        """ Get dictionary_version value.

            Notes:
                Version of the L7 Application Type

                
                This attribute is named `dictionaryVersion` in VSD API.
                
        """
        return self._dictionary_version

    @dictionary_version.setter
    def dictionary_version(self, value):
        """ Set dictionary_version value.

            Notes:
                Version of the L7 Application Type

                
                This attribute is named `dictionaryVersion` in VSD API.
                
        """
        self._dictionary_version = value

    
    @property
    def signature_index(self):
        """ Get signature_index value.

            Notes:
                Index number received from Procera for every L7 signature.

                
                This attribute is named `signatureIndex` in VSD API.
                
        """
        return self._signature_index

    @signature_index.setter
    def signature_index(self, value):
        """ Set signature_index value.

            Notes:
                Index number received from Procera for every L7 signature.

                
                This attribute is named `signatureIndex` in VSD API.
                
        """
        self._signature_index = value

    
    @property
    def signature_version(self):
        """ Get signature_version value.

            Notes:
                The AAR application version where this signature was last updated.

                
                This attribute is named `signatureVersion` in VSD API.
                
        """
        return self._signature_version

    @signature_version.setter
    def signature_version(self, value):
        """ Set signature_version value.

            Notes:
                The AAR application version where this signature was last updated.

                
                This attribute is named `signatureVersion` in VSD API.
                
        """
        self._signature_version = value

    
    @property
    def risk(self):
        """ Get risk value.

            Notes:
                Risk is determined on a scale of 1 to 5. It is received from Procera for every signature.

                
        """
        return self._risk

    @risk.setter
    def risk(self, value):
        """ Set risk value.

            Notes:
                Risk is determined on a scale of 1 to 5. It is received from Procera for every signature.

                
        """
        self._risk = value

    
    @property
    def plugin_name(self):
        """ Get plugin_name value.

            Notes:
                Plugin name received from Procera for every signature.

                
                This attribute is named `pluginName` in VSD API.
                
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, value):
        """ Set plugin_name value.

            Notes:
                Plugin name received from Procera for every signature.

                
                This attribute is named `pluginName` in VSD API.
                
        """
        self._plugin_name = value

    
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
    def software_flags(self):
        """ Get software_flags value.

            Notes:
                Software flags received from Procera for every signature.

                
                This attribute is named `softwareFlags` in VSD API.
                
        """
        return self._software_flags

    @software_flags.setter
    def software_flags(self, value):
        """ Set software_flags value.

            Notes:
                Software flags received from Procera for every signature.

                
                This attribute is named `softwareFlags` in VSD API.
                
        """
        self._software_flags = value

    
    @property
    def productivity(self):
        """ Get productivity value.

            Notes:
                Productivity Index is scored relative to a work environment for every L7 signature on a scale of 1-5.

                
        """
        return self._productivity

    @productivity.setter
    def productivity(self, value):
        """ Set productivity value.

            Notes:
                Productivity Index is scored relative to a work environment for every L7 signature on a scale of 1-5.

                
        """
        self._productivity = value

    
    @property
    def guidstring(self):
        """ Get guidstring value.

            Notes:
                GUID of the Application

                
        """
        return self._guidstring

    @guidstring.setter
    def guidstring(self, value):
        """ Set guidstring value.

            Notes:
                GUID of the Application

                
        """
        self._guidstring = value

    
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

    

    