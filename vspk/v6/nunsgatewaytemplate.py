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


from .fetchers import NUNSPortTemplatesFetcher

from bambou import NURESTObject


class NUNSGatewayTemplate(NURESTObject):
    """ Represents a NSGatewayTemplate in the VSD

        Notes:
            Represents a Network Service Gateway Template.
    """

    __rest_name__ = "nsgatewaytemplate"
    __resource_name__ = "nsgatewaytemplates"

    
    ## Constants
    
    CONST_SSH_SERVICE_DISABLED = "DISABLED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_SSH_SERVICE_ENABLED = "ENABLED"
    
    CONST_INSTANCE_SSH_OVERRIDE_DISALLOWED = "DISALLOWED"
    
    CONST_INSTANCE_SSH_OVERRIDE_ALLOWED = "ALLOWED"
    
    CONST_PERSONALITY_NSG = "NSG"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_PERSONALITY_NSGDUC = "NSGDUC"
    
    CONST_PERSONALITY_NSGBR = "NSGBR"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NSGatewayTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsgatewaytemplate = NUNSGatewayTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'NSGatewayTemplate')
                >>> nsgatewaytemplate = NUNSGatewayTemplate(data=my_dict)
        """

        super(NUNSGatewayTemplate, self).__init__()

        # Read/Write Attributes
        
        self._ssh_service = None
        self._name = None
        self._last_updated_by = None
        self._personality = None
        self._description = None
        self._embedded_metadata = None
        self._infrastructure_access_profile_id = None
        self._infrastructure_profile_id = None
        self._instance_ssh_override = None
        self._enterprise_id = None
        self._entity_scope = None
        self._external_id = None
        
        self.expose_attribute(local_name="ssh_service", remote_name="SSHService", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=False, is_unique=False, choices=[u'NSG', u'NSGBR', u'NSGDUC'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="infrastructure_access_profile_id", remote_name="infrastructureAccessProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="infrastructure_profile_id", remote_name="infrastructureProfileID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="instance_ssh_override", remote_name="instanceSSHOverride", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALLOWED', u'DISALLOWED'])
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_port_templates = NUNSPortTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ssh_service(self):
        """ Get ssh_service value.

            Notes:
                Enable/Disable SSH Service on all the Gateway instances which inherit from this template.

                
                This attribute is named `SSHService` in VSD API.
                
        """
        return self._ssh_service

    @ssh_service.setter
    def ssh_service(self, value):
        """ Set ssh_service value.

            Notes:
                Enable/Disable SSH Service on all the Gateway instances which inherit from this template.

                
                This attribute is named `SSHService` in VSD API.
                
        """
        self._ssh_service = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Gateway template.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Gateway template.

                
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
    def personality(self):
        """ Get personality value.

            Notes:
                Personality of the Gateway template - NSG, NSGBR, cannot be changed after creation.

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                Personality of the Gateway template - NSG, NSGBR, cannot be changed after creation.

                
        """
        self._personality = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the Gateway template.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the Gateway template.

                
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
    def infrastructure_access_profile_id(self):
        """ Get infrastructure_access_profile_id value.

            Notes:
                The ID of the infrastructure access profile associated to this Gateway Template.

                
                This attribute is named `infrastructureAccessProfileID` in VSD API.
                
        """
        return self._infrastructure_access_profile_id

    @infrastructure_access_profile_id.setter
    def infrastructure_access_profile_id(self, value):
        """ Set infrastructure_access_profile_id value.

            Notes:
                The ID of the infrastructure access profile associated to this Gateway Template.

                
                This attribute is named `infrastructureAccessProfileID` in VSD API.
                
        """
        self._infrastructure_access_profile_id = value

    
    @property
    def infrastructure_profile_id(self):
        """ Get infrastructure_profile_id value.

            Notes:
                The ID of the infrastructure gateway profile this instance of a Gateway template is associated with.

                
                This attribute is named `infrastructureProfileID` in VSD API.
                
        """
        return self._infrastructure_profile_id

    @infrastructure_profile_id.setter
    def infrastructure_profile_id(self, value):
        """ Set infrastructure_profile_id value.

            Notes:
                The ID of the infrastructure gateway profile this instance of a Gateway template is associated with.

                
                This attribute is named `infrastructureProfileID` in VSD API.
                
        """
        self._infrastructure_profile_id = value

    
    @property
    def instance_ssh_override(self):
        """ Get instance_ssh_override value.

            Notes:
                Indicates if this template instance allows the gateway instance(s) which inherit from it to independently enable/disable SSH service.

                
                This attribute is named `instanceSSHOverride` in VSD API.
                
        """
        return self._instance_ssh_override

    @instance_ssh_override.setter
    def instance_ssh_override(self, value):
        """ Set instance_ssh_override value.

            Notes:
                Indicates if this template instance allows the gateway instance(s) which inherit from it to independently enable/disable SSH service.

                
                This attribute is named `instanceSSHOverride` in VSD API.
                
        """
        self._instance_ssh_override = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                The enterprise associated with this Gateway template. This is a read only attribute

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                The enterprise associated with this Gateway template. This is a read only attribute

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
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

    

    
    ## Custom methods
    def is_template(self):
        """ Verify that the object is a template
    
            Returns:
                (bool): True if the object is a template
        """
        return True
    
    def is_from_template(self):
        """ Verify if the object has been instantiated from a template
    
            Note:
                The object has to be fetched. Otherwise, it does not
                have information from its parent
    
            Returns:
                (bool): True if the object is a template
        """
        return False
    