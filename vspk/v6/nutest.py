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




from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUTest(NURESTObject):
    """ Represents a Test in the VSD

        Notes:
            A Test defines a command to run inside a diagnositc container on an NSG. It represents a command with arguments that will be executed within the diagnostic container as part of a Test Suite run
    """

    __rest_name__ = "test"
    __resource_name__ = "tests"

    
    ## Constants
    
    CONST_ASSOCIATED_TEST_DEFINITION_TYPE_ICMP_ECHO_TEST_DEFINITION = "ICMP_ECHO_TEST_DEFINITION"
    
    CONST_ASSOCIATED_TEST_DEFINITION_TYPE_TEST_DEFINITION = "TEST_DEFINITION"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Test instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> test = NUTest(id=u'xxxx-xxx-xxx-xxx', name=u'Test')
                >>> test = NUTest(data=my_dict)
        """

        super(NUTest, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._last_updated_date = None
        self._description = None
        self._destination = None
        self._timeout = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._command = None
        self._order = None
        self._creation_date = None
        self._associated_test_definition_id = None
        self._associated_test_definition_type = None
        self._associated_test_suite_id = None
        self._owner = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="destination", remote_name="destination", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="timeout", remote_name="timeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="command", remote_name="command", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="order", remote_name="order", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_test_definition_id", remote_name="associatedTestDefinitionID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="associated_test_definition_type", remote_name="associatedTestDefinitionType", attribute_type=str, is_required=True, is_unique=False, choices=[u'ICMP_ECHO_TEST_DEFINITION', u'TEST_DEFINITION'])
        self.expose_attribute(local_name="associated_test_suite_id", remote_name="associatedTestSuiteID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name of the Test Definition instance bound to this Test object.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name of the Test Definition instance bound to this Test object.

                
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
    def last_updated_date(self):
        """ Get last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, value):
        """ Set last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        self._last_updated_date = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A brief description of the Test Definition referred to by this Test object.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A brief description of the Test Definition referred to by this Test object.

                
        """
        self._description = value

    
    @property
    def destination(self):
        """ Get destination value.

            Notes:
                Destination to be used in conjunction with this Test. Could be an IPv4 address or FQDN

                
        """
        return self._destination

    @destination.setter
    def destination(self, value):
        """ Set destination value.

            Notes:
                Destination to be used in conjunction with this Test. Could be an IPv4 address or FQDN

                
        """
        self._destination = value

    
    @property
    def timeout(self):
        """ Get timeout value.

            Notes:
                The timeout value set for the Test Definition instance, in seconds, at which point the system will consider the test as failed.

                
        """
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        """ Set timeout value.

            Notes:
                The timeout value set for the Test Definition instance, in seconds, at which point the system will consider the test as failed.

                
        """
        self._timeout = value

    
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
    def command(self):
        """ Get command value.

            Notes:
                The command line with arguments as extracted from the Test Definition instance bound to this Test instance.

                
        """
        return self._command

    @command.setter
    def command(self, value):
        """ Set command value.

            Notes:
                The command line with arguments as extracted from the Test Definition instance bound to this Test instance.

                
        """
        self._command = value

    
    @property
    def order(self):
        """ Get order value.

            Notes:
                Test order used to run tests. Lower order tests will run before higher order ones.

                
        """
        return self._order

    @order.setter
    def order(self, value):
        """ Set order value.

            Notes:
                Test order used to run tests. Lower order tests will run before higher order ones.

                
        """
        self._order = value

    
    @property
    def creation_date(self):
        """ Get creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """ Set creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        self._creation_date = value

    
    @property
    def associated_test_definition_id(self):
        """ Get associated_test_definition_id value.

            Notes:
                The associated Test Definition instance used as an information base for the Test object.

                
                This attribute is named `associatedTestDefinitionID` in VSD API.
                
        """
        return self._associated_test_definition_id

    @associated_test_definition_id.setter
    def associated_test_definition_id(self, value):
        """ Set associated_test_definition_id value.

            Notes:
                The associated Test Definition instance used as an information base for the Test object.

                
                This attribute is named `associatedTestDefinitionID` in VSD API.
                
        """
        self._associated_test_definition_id = value

    
    @property
    def associated_test_definition_type(self):
        """ Get associated_test_definition_type value.

            Notes:
                The type of associated Test Definition instance.

                
                This attribute is named `associatedTestDefinitionType` in VSD API.
                
        """
        return self._associated_test_definition_type

    @associated_test_definition_type.setter
    def associated_test_definition_type(self, value):
        """ Set associated_test_definition_type value.

            Notes:
                The type of associated Test Definition instance.

                
                This attribute is named `associatedTestDefinitionType` in VSD API.
                
        """
        self._associated_test_definition_type = value

    
    @property
    def associated_test_suite_id(self):
        """ Get associated_test_suite_id value.

            Notes:
                The ID of the Test Suite this Test instance is part of.

                
                This attribute is named `associatedTestSuiteID` in VSD API.
                
        """
        return self._associated_test_suite_id

    @associated_test_suite_id.setter
    def associated_test_suite_id(self, value):
        """ Set associated_test_suite_id value.

            Notes:
                The ID of the Test Suite this Test instance is part of.

                
                This attribute is named `associatedTestSuiteID` in VSD API.
                
        """
        self._associated_test_suite_id = value

    
    @property
    def owner(self):
        """ Get owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """ Set owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        self._owner = value

    
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

    

    