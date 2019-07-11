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




from .fetchers import NUTestRunsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUTestSuiteRun(NURESTObject):
    """ Represents a TestSuiteRun in the VSD

        Notes:
            A Test Suite Run represents the execution of a given Test Suite within a diagnostic container on an NSG. It groups together multiple Test Runs.
    """

    __rest_name__ = "testsuiterun"
    __resource_name__ = "testsuiteruns"

    
    ## Constants
    
    CONST_OPERATION_STATUS_STARTED = "STARTED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_OPERATION_STATUS_UNKNOWN = "UNKNOWN"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_OPERATION_STATUS_COMPLETED = "COMPLETED"
    
    CONST_OPERATION_STATUS_CONTAINER_IP_FAILURE = "CONTAINER_IP_FAILURE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a TestSuiteRun instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> testsuiterun = NUTestSuiteRun(id=u'xxxx-xxx-xxx-xxx', name=u'TestSuiteRun')
                >>> testsuiterun = NUTestSuiteRun(data=my_dict)
        """

        super(NUTestSuiteRun, self).__init__()

        # Read/Write Attributes
        
        self._vport_name = None
        self._ns_gateway_name = None
        self._last_updated_by = None
        self._datapath_id = None
        self._destination = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._domain_name = None
        self._zone_name = None
        self._operation_status = None
        self._associated_entity_type = None
        self._associated_test_suite_id = None
        self._associated_test_suite_name = None
        self._subnet_name = None
        self._external_id = None
        
        self.expose_attribute(local_name="vport_name", remote_name="VPortName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ns_gateway_name", remote_name="NSGatewayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="datapath_id", remote_name="datapathID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="destination", remote_name="destination", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="domain_name", remote_name="domainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zone_name", remote_name="zoneName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="operation_status", remote_name="operationStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'COMPLETED', u'CONTAINER_IP_FAILURE', u'STARTED', u'UNKNOWN'])
        self.expose_attribute(local_name="associated_entity_type", remote_name="associatedEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_test_suite_id", remote_name="associatedTestSuiteID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="associated_test_suite_name", remote_name="associatedTestSuiteName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="subnet_name", remote_name="subnetName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.test_runs = NUTestRunsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vport_name(self):
        """ Get vport_name value.

            Notes:
                The name of the vPort against which the Test Suite is to be executed.

                
                This attribute is named `VPortName` in VSD API.
                
        """
        return self._vport_name

    @vport_name.setter
    def vport_name(self, value):
        """ Set vport_name value.

            Notes:
                The name of the vPort against which the Test Suite is to be executed.

                
                This attribute is named `VPortName` in VSD API.
                
        """
        self._vport_name = value

    
    @property
    def ns_gateway_name(self):
        """ Get ns_gateway_name value.

            Notes:
                The name of the NSG against which the Test Suite will be executed.

                
                This attribute is named `NSGatewayName` in VSD API.
                
        """
        return self._ns_gateway_name

    @ns_gateway_name.setter
    def ns_gateway_name(self, value):
        """ Set ns_gateway_name value.

            Notes:
                The name of the NSG against which the Test Suite will be executed.

                
                This attribute is named `NSGatewayName` in VSD API.
                
        """
        self._ns_gateway_name = value

    
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
    def datapath_id(self):
        """ Get datapath_id value.

            Notes:
                The datapath ID (System ID) of the NSG instance against which the tests are to be executed.

                
                This attribute is named `datapathID` in VSD API.
                
        """
        return self._datapath_id

    @datapath_id.setter
    def datapath_id(self, value):
        """ Set datapath_id value.

            Notes:
                The datapath ID (System ID) of the NSG instance against which the tests are to be executed.

                
                This attribute is named `datapathID` in VSD API.
                
        """
        self._datapath_id = value

    
    @property
    def destination(self):
        """ Get destination value.

            Notes:
                Destination to be used in conjunction with tests part of the Test Suite. Could be an IPv4 address or FQDN.

                
        """
        return self._destination

    @destination.setter
    def destination(self, value):
        """ Set destination value.

            Notes:
                Destination to be used in conjunction with tests part of the Test Suite. Could be an IPv4 address or FQDN.

                
        """
        self._destination = value

    
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
    def domain_name(self):
        """ Get domain_name value.

            Notes:
                The name of the Domain within which the source vPort being tested resides.

                
                This attribute is named `domainName` in VSD API.
                
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        """ Set domain_name value.

            Notes:
                The name of the Domain within which the source vPort being tested resides.

                
                This attribute is named `domainName` in VSD API.
                
        """
        self._domain_name = value

    
    @property
    def zone_name(self):
        """ Get zone_name value.

            Notes:
                The name of the Zone within which the source vPort being tested resides.

                
                This attribute is named `zoneName` in VSD API.
                
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value):
        """ Set zone_name value.

            Notes:
                The name of the Zone within which the source vPort being tested resides.

                
                This attribute is named `zoneName` in VSD API.
                
        """
        self._zone_name = value

    
    @property
    def operation_status(self):
        """ Get operation_status value.

            Notes:
                The status of the test operation request as received by the NSG Agent. This field is set by the NSG.

                
                This attribute is named `operationStatus` in VSD API.
                
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, value):
        """ Set operation_status value.

            Notes:
                The status of the test operation request as received by the NSG Agent. This field is set by the NSG.

                
                This attribute is named `operationStatus` in VSD API.
                
        """
        self._operation_status = value

    
    @property
    def associated_entity_type(self):
        """ Get associated_entity_type value.

            Notes:
                Type of the entity that is hosting the Test Suite Run.  This can be a vPort or an NSG.

                
                This attribute is named `associatedEntityType` in VSD API.
                
        """
        return self._associated_entity_type

    @associated_entity_type.setter
    def associated_entity_type(self, value):
        """ Set associated_entity_type value.

            Notes:
                Type of the entity that is hosting the Test Suite Run.  This can be a vPort or an NSG.

                
                This attribute is named `associatedEntityType` in VSD API.
                
        """
        self._associated_entity_type = value

    
    @property
    def associated_test_suite_id(self):
        """ Get associated_test_suite_id value.

            Notes:
                The ID of the Test Suite from which this instance of the Test Suite Run was created.

                
                This attribute is named `associatedTestSuiteID` in VSD API.
                
        """
        return self._associated_test_suite_id

    @associated_test_suite_id.setter
    def associated_test_suite_id(self, value):
        """ Set associated_test_suite_id value.

            Notes:
                The ID of the Test Suite from which this instance of the Test Suite Run was created.

                
                This attribute is named `associatedTestSuiteID` in VSD API.
                
        """
        self._associated_test_suite_id = value

    
    @property
    def associated_test_suite_name(self):
        """ Get associated_test_suite_name value.

            Notes:
                The name of the Test Suite instance from which this Test Suite Run was created.

                
                This attribute is named `associatedTestSuiteName` in VSD API.
                
        """
        return self._associated_test_suite_name

    @associated_test_suite_name.setter
    def associated_test_suite_name(self, value):
        """ Set associated_test_suite_name value.

            Notes:
                The name of the Test Suite instance from which this Test Suite Run was created.

                
                This attribute is named `associatedTestSuiteName` in VSD API.
                
        """
        self._associated_test_suite_name = value

    
    @property
    def subnet_name(self):
        """ Get subnet_name value.

            Notes:
                The name of the Subnet within which the source vPort being tested resides.

                
                This attribute is named `subnetName` in VSD API.
                
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, value):
        """ Set subnet_name value.

            Notes:
                The name of the Subnet within which the source vPort being tested resides.

                
                This attribute is named `subnetName` in VSD API.
                
        """
        self._subnet_name = value

    
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

    

    