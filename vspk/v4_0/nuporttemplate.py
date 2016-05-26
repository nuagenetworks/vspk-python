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


from .fetchers import NUVLANTemplatesFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUPortTemplate(NURESTObject):
    """ Represents a PortTemplate in the VSD

        Notes:
            Represents a Port Template object under a given gateway template object.
    """

    __rest_name__ = "porttemplate"
    __resource_name__ = "porttemplates"

    
    ## Constants
    
    CONST_PORT_TYPE_NETWORK = "NETWORK"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_PORT_TYPE_ACCESS = "ACCESS"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a PortTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> porttemplate = NUPortTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'PortTemplate')
                >>> porttemplate = NUPortTemplate(data=my_dict)
        """

        super(NUPortTemplate, self).__init__()

        # Read/Write Attributes
        
        self._vlan_range = None
        self._name = None
        self._last_updated_by = None
        self._description = None
        self._physical_name = None
        self._entity_scope = None
        self._port_type = None
        self._associated_egress_qos_policy_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="vlan_range", remote_name="VLANRange", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="physical_name", remote_name="physicalName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="port_type", remote_name="portType", attribute_type=str, is_required=True, is_unique=False, choices=[u'ACCESS', u'NETWORK'])
        self.expose_attribute(local_name="associated_egress_qos_policy_id", remote_name="associatedEgressQOSPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vlan_templates = NUVLANTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vlan_range(self):
        """ Get vlan_range value.

            Notes:
                VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        return self._vlan_range

    @vlan_range.setter
    def vlan_range(self, value):
        """ Set vlan_range value.

            Notes:
                VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        self._vlan_range = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Port

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Port

                
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
                A description of the Port

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the Port

                
        """
        self._description = value

    
    @property
    def physical_name(self):
        """ Get physical_name value.

            Notes:
                Identifier of the Port

                
                This attribute is named `physicalName` in VSD API.
                
        """
        return self._physical_name

    @physical_name.setter
    def physical_name(self, value):
        """ Set physical_name value.

            Notes:
                Identifier of the Port

                
                This attribute is named `physicalName` in VSD API.
                
        """
        self._physical_name = value

    
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
    def port_type(self):
        """ Get port_type value.

            Notes:
                Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .

                
                This attribute is named `portType` in VSD API.
                
        """
        return self._port_type

    @port_type.setter
    def port_type(self, value):
        """ Set port_type value.

            Notes:
                Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .

                
                This attribute is named `portType` in VSD API.
                
        """
        self._port_type = value

    
    @property
    def associated_egress_qos_policy_id(self):
        """ Get associated_egress_qos_policy_id value.

            Notes:
                ID of the Egress QOS Policy associated with this Vlan.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        return self._associated_egress_qos_policy_id

    @associated_egress_qos_policy_id.setter
    def associated_egress_qos_policy_id(self, value):
        """ Set associated_egress_qos_policy_id value.

            Notes:
                ID of the Egress QOS Policy associated with this Vlan.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        self._associated_egress_qos_policy_id = value

    
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
    