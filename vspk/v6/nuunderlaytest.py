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



from bambou import NURESTObject


class NUUnderlayTest(NURESTObject):
    """ Represents a UnderlayTest in the VSD

        Notes:
            Underlay Test is a wrapper object for a Test Suite Run from the built in Underlay Tests Test Suite.
    """

    __rest_name__ = "underlaytest"
    __resource_name__ = "underlaytests"

    
    ## Constants
    
    CONST_UNDERLAY_TEST_TYPE_PRE_BOOTSTRAP = "PRE_BOOTSTRAP"
    
    CONST_UNDERLAY_TEST_TYPE_ON_DEMAND = "ON_DEMAND"
    
    CONST_TEST_RESULT_NOT_APPLICABLE = "NOT_APPLICABLE"
    
    CONST_TEST_RESULT_FAIL = "FAIL"
    
    CONST_TEST_RESULT_PASS = "PASS"
    
    CONST_TEST_RESULT_DEGRADED = "DEGRADED"
    
    CONST_UNDERLAY_TEST_TYPE_BIRTH_CERTIFICATE = "BIRTH_CERTIFICATE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a UnderlayTest instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> underlaytest = NUUnderlayTest(id=u'xxxx-xxx-xxx-xxx', name=u'UnderlayTest')
                >>> underlaytest = NUUnderlayTest(data=my_dict)
        """

        super(NUUnderlayTest, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._test_result = None
        self._underlay_test_server = None
        self._underlay_test_type = None
        self._create_only = None
        self._associated_data_path_id = None
        self._associated_ns_gateway_id = None
        self._associated_ns_gateway_name = None
        self._associated_system_id = None
        self._associated_test_suite_run_id = None
        self._associated_uplink_connection_id = None
        self._associated_uplink_interface = None
        self._start_date_time = None
        self._stop_date_time = None
        self._run_bandwidth_test = None
        self._run_connectivity_test = None
        self._run_mtu_discovery_test = None
        self._duration = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="test_result", remote_name="testResult", attribute_type=str, is_required=False, is_unique=False, choices=[u'DEGRADED', u'FAIL', u'NOT_APPLICABLE', u'PASS'])
        self.expose_attribute(local_name="underlay_test_server", remote_name="underlayTestServer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="underlay_test_type", remote_name="underlayTestType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BIRTH_CERTIFICATE', u'ON_DEMAND', u'PRE_BOOTSTRAP'])
        self.expose_attribute(local_name="create_only", remote_name="createOnly", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_data_path_id", remote_name="associatedDataPathID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ns_gateway_id", remote_name="associatedNSGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ns_gateway_name", remote_name="associatedNSGatewayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_system_id", remote_name="associatedSystemID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_test_suite_run_id", remote_name="associatedTestSuiteRunID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_uplink_connection_id", remote_name="associatedUplinkConnectionID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_uplink_interface", remote_name="associatedUplinkInterface", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="start_date_time", remote_name="startDateTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stop_date_time", remote_name="stopDateTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="run_bandwidth_test", remote_name="runBandwidthTest", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="run_connectivity_test", remote_name="runConnectivityTest", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="run_mtu_discovery_test", remote_name="runMTUDiscoveryTest", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="duration", remote_name="duration", attribute_type=int, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name of the test

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name of the test

                
        """
        self._name = value

    
    @property
    def test_result(self):
        """ Get test_result value.

            Notes:
                The result of the test

                
                This attribute is named `testResult` in VSD API.
                
        """
        return self._test_result

    @test_result.setter
    def test_result(self, value):
        """ Set test_result value.

            Notes:
                The result of the test

                
                This attribute is named `testResult` in VSD API.
                
        """
        self._test_result = value

    
    @property
    def underlay_test_server(self):
        """ Get underlay_test_server value.

            Notes:
                The Underlay Test Server this test was executed against

                
                This attribute is named `underlayTestServer` in VSD API.
                
        """
        return self._underlay_test_server

    @underlay_test_server.setter
    def underlay_test_server(self, value):
        """ Set underlay_test_server value.

            Notes:
                The Underlay Test Server this test was executed against

                
                This attribute is named `underlayTestServer` in VSD API.
                
        """
        self._underlay_test_server = value

    
    @property
    def underlay_test_type(self):
        """ Get underlay_test_type value.

            Notes:
                Type of Test

                
                This attribute is named `underlayTestType` in VSD API.
                
        """
        return self._underlay_test_type

    @underlay_test_type.setter
    def underlay_test_type(self, value):
        """ Set underlay_test_type value.

            Notes:
                Type of Test

                
                This attribute is named `underlayTestType` in VSD API.
                
        """
        self._underlay_test_type = value

    
    @property
    def create_only(self):
        """ Get create_only value.

            Notes:
                Create the test only, do not trigger the command. Used for loading existing results

                
                This attribute is named `createOnly` in VSD API.
                
        """
        return self._create_only

    @create_only.setter
    def create_only(self, value):
        """ Set create_only value.

            Notes:
                Create the test only, do not trigger the command. Used for loading existing results

                
                This attribute is named `createOnly` in VSD API.
                
        """
        self._create_only = value

    
    @property
    def associated_data_path_id(self):
        """ Get associated_data_path_id value.

            Notes:
                The associated data path ID

                
                This attribute is named `associatedDataPathID` in VSD API.
                
        """
        return self._associated_data_path_id

    @associated_data_path_id.setter
    def associated_data_path_id(self, value):
        """ Set associated_data_path_id value.

            Notes:
                The associated data path ID

                
                This attribute is named `associatedDataPathID` in VSD API.
                
        """
        self._associated_data_path_id = value

    
    @property
    def associated_ns_gateway_id(self):
        """ Get associated_ns_gateway_id value.

            Notes:
                The ID of the associated NSGateway

                
                This attribute is named `associatedNSGatewayID` in VSD API.
                
        """
        return self._associated_ns_gateway_id

    @associated_ns_gateway_id.setter
    def associated_ns_gateway_id(self, value):
        """ Set associated_ns_gateway_id value.

            Notes:
                The ID of the associated NSGateway

                
                This attribute is named `associatedNSGatewayID` in VSD API.
                
        """
        self._associated_ns_gateway_id = value

    
    @property
    def associated_ns_gateway_name(self):
        """ Get associated_ns_gateway_name value.

            Notes:
                The name of the associated NSGateway

                
                This attribute is named `associatedNSGatewayName` in VSD API.
                
        """
        return self._associated_ns_gateway_name

    @associated_ns_gateway_name.setter
    def associated_ns_gateway_name(self, value):
        """ Set associated_ns_gateway_name value.

            Notes:
                The name of the associated NSGateway

                
                This attribute is named `associatedNSGatewayName` in VSD API.
                
        """
        self._associated_ns_gateway_name = value

    
    @property
    def associated_system_id(self):
        """ Get associated_system_id value.

            Notes:
                The associated System ID

                
                This attribute is named `associatedSystemID` in VSD API.
                
        """
        return self._associated_system_id

    @associated_system_id.setter
    def associated_system_id(self, value):
        """ Set associated_system_id value.

            Notes:
                The associated System ID

                
                This attribute is named `associatedSystemID` in VSD API.
                
        """
        self._associated_system_id = value

    
    @property
    def associated_test_suite_run_id(self):
        """ Get associated_test_suite_run_id value.

            Notes:
                The ID of the associated Test Suite Run

                
                This attribute is named `associatedTestSuiteRunID` in VSD API.
                
        """
        return self._associated_test_suite_run_id

    @associated_test_suite_run_id.setter
    def associated_test_suite_run_id(self, value):
        """ Set associated_test_suite_run_id value.

            Notes:
                The ID of the associated Test Suite Run

                
                This attribute is named `associatedTestSuiteRunID` in VSD API.
                
        """
        self._associated_test_suite_run_id = value

    
    @property
    def associated_uplink_connection_id(self):
        """ Get associated_uplink_connection_id value.

            Notes:
                The uplink connection ID that this underlay test will be triggered on. This can be null in order to use any uplink

                
                This attribute is named `associatedUplinkConnectionID` in VSD API.
                
        """
        return self._associated_uplink_connection_id

    @associated_uplink_connection_id.setter
    def associated_uplink_connection_id(self, value):
        """ Set associated_uplink_connection_id value.

            Notes:
                The uplink connection ID that this underlay test will be triggered on. This can be null in order to use any uplink

                
                This attribute is named `associatedUplinkConnectionID` in VSD API.
                
        """
        self._associated_uplink_connection_id = value

    
    @property
    def associated_uplink_interface(self):
        """ Get associated_uplink_interface value.

            Notes:
                The interface name of the associated uplink in port.vlan format

                
                This attribute is named `associatedUplinkInterface` in VSD API.
                
        """
        return self._associated_uplink_interface

    @associated_uplink_interface.setter
    def associated_uplink_interface(self, value):
        """ Set associated_uplink_interface value.

            Notes:
                The interface name of the associated uplink in port.vlan format

                
                This attribute is named `associatedUplinkInterface` in VSD API.
                
        """
        self._associated_uplink_interface = value

    
    @property
    def start_date_time(self):
        """ Get start_date_time value.

            Notes:
                The start date time of the test

                
                This attribute is named `startDateTime` in VSD API.
                
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, value):
        """ Set start_date_time value.

            Notes:
                The start date time of the test

                
                This attribute is named `startDateTime` in VSD API.
                
        """
        self._start_date_time = value

    
    @property
    def stop_date_time(self):
        """ Get stop_date_time value.

            Notes:
                The stop date time of the test

                
                This attribute is named `stopDateTime` in VSD API.
                
        """
        return self._stop_date_time

    @stop_date_time.setter
    def stop_date_time(self, value):
        """ Set stop_date_time value.

            Notes:
                The stop date time of the test

                
                This attribute is named `stopDateTime` in VSD API.
                
        """
        self._stop_date_time = value

    
    @property
    def run_bandwidth_test(self):
        """ Get run_bandwidth_test value.

            Notes:
                Bandwidth test results enable verification of minimal requirements for NSG operations and is not indicative of the maximum throughput possible on an uplink.

                
                This attribute is named `runBandwidthTest` in VSD API.
                
        """
        return self._run_bandwidth_test

    @run_bandwidth_test.setter
    def run_bandwidth_test(self, value):
        """ Set run_bandwidth_test value.

            Notes:
                Bandwidth test results enable verification of minimal requirements for NSG operations and is not indicative of the maximum throughput possible on an uplink.

                
                This attribute is named `runBandwidthTest` in VSD API.
                
        """
        self._run_bandwidth_test = value

    
    @property
    def run_connectivity_test(self):
        """ Get run_connectivity_test value.

            Notes:
                Flag to run the connectivity test

                
                This attribute is named `runConnectivityTest` in VSD API.
                
        """
        return self._run_connectivity_test

    @run_connectivity_test.setter
    def run_connectivity_test(self, value):
        """ Set run_connectivity_test value.

            Notes:
                Flag to run the connectivity test

                
                This attribute is named `runConnectivityTest` in VSD API.
                
        """
        self._run_connectivity_test = value

    
    @property
    def run_mtu_discovery_test(self):
        """ Get run_mtu_discovery_test value.

            Notes:
                Flag to run the MTU Discovery test

                
                This attribute is named `runMTUDiscoveryTest` in VSD API.
                
        """
        return self._run_mtu_discovery_test

    @run_mtu_discovery_test.setter
    def run_mtu_discovery_test(self, value):
        """ Set run_mtu_discovery_test value.

            Notes:
                Flag to run the MTU Discovery test

                
                This attribute is named `runMTUDiscoveryTest` in VSD API.
                
        """
        self._run_mtu_discovery_test = value

    
    @property
    def duration(self):
        """ Get duration value.

            Notes:
                The test duration in seconds

                
        """
        return self._duration

    @duration.setter
    def duration(self, value):
        """ Set duration value.

            Notes:
                The test duration in seconds

                
        """
        self._duration = value

    

    