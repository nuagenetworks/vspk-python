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

from bambou import NURESTObject


class NUScheduledtestsuiterun(NURESTObject):
    """ Represents a Scheduledtestsuiterun in the VSD

        Notes:
            A Scheduled Test Suite Run represents the execution of a given Scheduled Test Suite within a namespace on an NSG. It groups together multiple ICMP Echo Test Runs.
    """

    __rest_name__ = "scheduledtestsuiterun"
    __resource_name__ = "scheduledtestsuiteruns"

    
    ## Constants
    
    CONST_OPERATION_STATUS_RUNNING = "RUNNING"
    
    CONST_OPERATION_STATUS_STARTED = "STARTED"
    
    CONST_OPERATION_STATUS_UNKNOWN = "UNKNOWN"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Scheduledtestsuiterun instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> scheduledtestsuiterun = NUScheduledtestsuiterun(id=u'xxxx-xxx-xxx-xxx', name=u'Scheduledtestsuiterun')
                >>> scheduledtestsuiterun = NUScheduledtestsuiterun(data=my_dict)
        """

        super(NUScheduledtestsuiterun, self).__init__()

        # Read/Write Attributes
        
        self._vport_name = None
        self._ns_gateway_name = None
        self._mac_address = None
        self._datapath_id = None
        self._secondary_datapath_id = None
        self._secondary_ns_gateway_name = None
        self._secondary_system_id = None
        self._destination = None
        self._vlan_id = None
        self._domain_name = None
        self._zone_name = None
        self._source_ip = None
        self._operation_status = None
        self._vport_port_name = None
        self._vport_vlan_id = None
        self._associated_scheduled_test_suite_id = None
        self._associated_scheduled_test_suite_name = None
        self._subnet_name = None
        self._system_id = None
        
        self.expose_attribute(local_name="vport_name", remote_name="VPortName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ns_gateway_name", remote_name="NSGatewayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mac_address", remote_name="macAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="datapath_id", remote_name="datapathID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_datapath_id", remote_name="secondaryDatapathID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_ns_gateway_name", remote_name="secondaryNSGatewayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="secondary_system_id", remote_name="secondarySystemID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="destination", remote_name="destination", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vlan_id", remote_name="vlanID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="domain_name", remote_name="domainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zone_name", remote_name="zoneName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="source_ip", remote_name="sourceIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="operation_status", remote_name="operationStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'RUNNING', u'STARTED', u'UNKNOWN'])
        self.expose_attribute(local_name="vport_port_name", remote_name="vportPortName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vport_vlan_id", remote_name="vportVlanID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_scheduled_test_suite_id", remote_name="associatedScheduledTestSuiteID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="associated_scheduled_test_suite_name", remote_name="associatedScheduledTestSuiteName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="subnet_name", remote_name="subnetName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="system_id", remote_name="systemID", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.test_runs = NUTestRunsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vport_name(self):
        """ Get vport_name value.

            Notes:
                VPort name against which the test suite is executed.

                
                This attribute is named `VPortName` in VSD API.
                
        """
        return self._vport_name

    @vport_name.setter
    def vport_name(self, value):
        """ Set vport_name value.

            Notes:
                VPort name against which the test suite is executed.

                
                This attribute is named `VPortName` in VSD API.
                
        """
        self._vport_name = value

    
    @property
    def ns_gateway_name(self):
        """ Get ns_gateway_name value.

            Notes:
                Name of the NSG on which the suite will be executed.

                
                This attribute is named `NSGatewayName` in VSD API.
                
        """
        return self._ns_gateway_name

    @ns_gateway_name.setter
    def ns_gateway_name(self, value):
        """ Set ns_gateway_name value.

            Notes:
                Name of the NSG on which the suite will be executed.

                
                This attribute is named `NSGatewayName` in VSD API.
                
        """
        self._ns_gateway_name = value

    
    @property
    def mac_address(self):
        """ Get mac_address value.

            Notes:
                MAC address for the interface in the namespace on the NSG.

                
                This attribute is named `macAddress` in VSD API.
                
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        """ Set mac_address value.

            Notes:
                MAC address for the interface in the namespace on the NSG.

                
                This attribute is named `macAddress` in VSD API.
                
        """
        self._mac_address = value

    
    @property
    def datapath_id(self):
        """ Get datapath_id value.

            Notes:
                DatapathID of the NSG against which the tests are to be executed.

                
                This attribute is named `datapathID` in VSD API.
                
        """
        return self._datapath_id

    @datapath_id.setter
    def datapath_id(self, value):
        """ Set datapath_id value.

            Notes:
                DatapathID of the NSG against which the tests are to be executed.

                
                This attribute is named `datapathID` in VSD API.
                
        """
        self._datapath_id = value

    
    @property
    def secondary_datapath_id(self):
        """ Get secondary_datapath_id value.

            Notes:
                The datapath ID of the secondary gateway in the Redundant Group.

                
                This attribute is named `secondaryDatapathID` in VSD API.
                
        """
        return self._secondary_datapath_id

    @secondary_datapath_id.setter
    def secondary_datapath_id(self, value):
        """ Set secondary_datapath_id value.

            Notes:
                The datapath ID of the secondary gateway in the Redundant Group.

                
                This attribute is named `secondaryDatapathID` in VSD API.
                
        """
        self._secondary_datapath_id = value

    
    @property
    def secondary_ns_gateway_name(self):
        """ Get secondary_ns_gateway_name value.

            Notes:
                The NSGateway name of the secondary gateway in the Redundant Group.

                
                This attribute is named `secondaryNSGatewayName` in VSD API.
                
        """
        return self._secondary_ns_gateway_name

    @secondary_ns_gateway_name.setter
    def secondary_ns_gateway_name(self, value):
        """ Set secondary_ns_gateway_name value.

            Notes:
                The NSGateway name of the secondary gateway in the Redundant Group.

                
                This attribute is named `secondaryNSGatewayName` in VSD API.
                
        """
        self._secondary_ns_gateway_name = value

    
    @property
    def secondary_system_id(self):
        """ Get secondary_system_id value.

            Notes:
                The system ID of the secondary gateway in the Redundant Group.

                
                This attribute is named `secondarySystemID` in VSD API.
                
        """
        return self._secondary_system_id

    @secondary_system_id.setter
    def secondary_system_id(self, value):
        """ Set secondary_system_id value.

            Notes:
                The system ID of the secondary gateway in the Redundant Group.

                
                This attribute is named `secondarySystemID` in VSD API.
                
        """
        self._secondary_system_id = value

    
    @property
    def destination(self):
        """ Get destination value.

            Notes:
                Either an IPv4 address or FQDN to be used in conjunction with the ICMP echo test. If provided, this destination will override the destination at individual Test level.

                
        """
        return self._destination

    @destination.setter
    def destination(self, value):
        """ Set destination value.

            Notes:
                Either an IPv4 address or FQDN to be used in conjunction with the ICMP echo test. If provided, this destination will override the destination at individual Test level.

                
        """
        self._destination = value

    
    @property
    def vlan_id(self):
        """ Get vlan_id value.

            Notes:
                VLAN ID of the interface in the namespace on NSG.

                
                This attribute is named `vlanID` in VSD API.
                
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, value):
        """ Set vlan_id value.

            Notes:
                VLAN ID of the interface in the namespace on NSG.

                
                This attribute is named `vlanID` in VSD API.
                
        """
        self._vlan_id = value

    
    @property
    def domain_name(self):
        """ Get domain_name value.

            Notes:
                Domain name within which the source vPort being tested resides.

                
                This attribute is named `domainName` in VSD API.
                
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        """ Set domain_name value.

            Notes:
                Domain name within which the source vPort being tested resides.

                
                This attribute is named `domainName` in VSD API.
                
        """
        self._domain_name = value

    
    @property
    def zone_name(self):
        """ Get zone_name value.

            Notes:
                Zone name within which the source vPort being tested resides.

                
                This attribute is named `zoneName` in VSD API.
                
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value):
        """ Set zone_name value.

            Notes:
                Zone name within which the source vPort being tested resides.

                
                This attribute is named `zoneName` in VSD API.
                
        """
        self._zone_name = value

    
    @property
    def source_ip(self):
        """ Get source_ip value.

            Notes:
                The IP address that will be assigned to the interface in namespace on NSG and used by the ICMP Echo test as the source IP. This is an optional field, if not provided the interface in namespace is assigned an IP from the DHCP pool.

                
                This attribute is named `sourceIP` in VSD API.
                
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, value):
        """ Set source_ip value.

            Notes:
                The IP address that will be assigned to the interface in namespace on NSG and used by the ICMP Echo test as the source IP. This is an optional field, if not provided the interface in namespace is assigned an IP from the DHCP pool.

                
                This attribute is named `sourceIP` in VSD API.
                
        """
        self._source_ip = value

    
    @property
    def operation_status(self):
        """ Get operation_status value.

            Notes:
                The status of the test operation request received by the NSG agent.

                
                This attribute is named `operationStatus` in VSD API.
                
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, value):
        """ Set operation_status value.

            Notes:
                The status of the test operation request received by the NSG agent.

                
                This attribute is named `operationStatus` in VSD API.
                
        """
        self._operation_status = value

    
    @property
    def vport_port_name(self):
        """ Get vport_port_name value.

            Notes:
                The access port of the VPort against which the test suite is executed.

                
                This attribute is named `vportPortName` in VSD API.
                
        """
        return self._vport_port_name

    @vport_port_name.setter
    def vport_port_name(self, value):
        """ Set vport_port_name value.

            Notes:
                The access port of the VPort against which the test suite is executed.

                
                This attribute is named `vportPortName` in VSD API.
                
        """
        self._vport_port_name = value

    
    @property
    def vport_vlan_id(self):
        """ Get vport_vlan_id value.

            Notes:
                The VLAN ID of the VPort against which the test suite is executed.

                
                This attribute is named `vportVlanID` in VSD API.
                
        """
        return self._vport_vlan_id

    @vport_vlan_id.setter
    def vport_vlan_id(self, value):
        """ Set vport_vlan_id value.

            Notes:
                The VLAN ID of the VPort against which the test suite is executed.

                
                This attribute is named `vportVlanID` in VSD API.
                
        """
        self._vport_vlan_id = value

    
    @property
    def associated_scheduled_test_suite_id(self):
        """ Get associated_scheduled_test_suite_id value.

            Notes:
                The ID of the Scheduled Test Suite from which this instance of run was created.

                
                This attribute is named `associatedScheduledTestSuiteID` in VSD API.
                
        """
        return self._associated_scheduled_test_suite_id

    @associated_scheduled_test_suite_id.setter
    def associated_scheduled_test_suite_id(self, value):
        """ Set associated_scheduled_test_suite_id value.

            Notes:
                The ID of the Scheduled Test Suite from which this instance of run was created.

                
                This attribute is named `associatedScheduledTestSuiteID` in VSD API.
                
        """
        self._associated_scheduled_test_suite_id = value

    
    @property
    def associated_scheduled_test_suite_name(self):
        """ Get associated_scheduled_test_suite_name value.

            Notes:
                Name of the Scheduled Test Suite from which this run was created.

                
                This attribute is named `associatedScheduledTestSuiteName` in VSD API.
                
        """
        return self._associated_scheduled_test_suite_name

    @associated_scheduled_test_suite_name.setter
    def associated_scheduled_test_suite_name(self, value):
        """ Set associated_scheduled_test_suite_name value.

            Notes:
                Name of the Scheduled Test Suite from which this run was created.

                
                This attribute is named `associatedScheduledTestSuiteName` in VSD API.
                
        """
        self._associated_scheduled_test_suite_name = value

    
    @property
    def subnet_name(self):
        """ Get subnet_name value.

            Notes:
                Subnet name within which the source vPort being tested resides.

                
                This attribute is named `subnetName` in VSD API.
                
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, value):
        """ Set subnet_name value.

            Notes:
                Subnet name within which the source vPort being tested resides.

                
                This attribute is named `subnetName` in VSD API.
                
        """
        self._subnet_name = value

    
    @property
    def system_id(self):
        """ Get system_id value.

            Notes:
                System ID of the NSG against which the tests are to be executed.

                
                This attribute is named `systemID` in VSD API.
                
        """
        return self._system_id

    @system_id.setter
    def system_id(self, value):
        """ Set system_id value.

            Notes:
                System ID of the NSG against which the tests are to be executed.

                
                This attribute is named `systemID` in VSD API.
                
        """
        self._system_id = value

    

    