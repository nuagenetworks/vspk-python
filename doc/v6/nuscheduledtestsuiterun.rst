.. _nuscheduledtestsuiterun:

nuscheduledtestsuiterun
===========================================

.. class:: nuscheduledtestsuiterun.NUScheduledtestsuiterun(bambou.nurest_object.NUMetaRESTObject,):

A Scheduled Test Suite Run represents the execution of a given Scheduled Test Suite within a namespace on an NSG. It groups together multiple ICMP Echo Test Runs.


Attributes
----------


- ``vport_name``: VPort name against which the test suite is executed.

- ``ns_gateway_name``: Name of the NSG on which the suite will be executed.

- ``mac_address``: MAC address for the interface in the namespace on the NSG.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``datapath_id``: DatapathID of the NSG against which the tests are to be executed.

- ``secondary_datapath_id``: The datapath ID of the secondary gateway in the Redundant Group.

- ``secondary_ns_gateway_name``: The NSGateway name of the secondary gateway in the Redundant Group.

- ``secondary_system_id``: The system ID of the secondary gateway in the Redundant Group.

- ``destination``: Either an IPv4 address or FQDN to be used in conjunction with the ICMP echo test. If provided, this destination will override the destination at individual Test level.

- ``vlan_id``: VLAN ID of the interface in the namespace on NSG.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_name``: Domain name within which the source vPort being tested resides.

- ``zone_name``: Zone name within which the source vPort being tested resides.

- ``source_ip``: The IP address that will be assigned to the interface in namespace on NSG and used by the ICMP Echo test as the source IP. This is an optional field, if not provided the interface in namespace is assigned an IP from the DHCP pool.

- ``operation_status``: The status of the test operation request received by the NSG agent.

- ``vport_port_name``: The access port of the VPort against which the test suite is executed.

- ``vport_vlan_id``: The VLAN ID of the VPort against which the test suite is executed.

- ``creation_date``: Time stamp when this object was created.

- ``associated_scheduled_test_suite_id`` (**Mandatory**): The ID of the Scheduled Test Suite from which this instance of run was created.

- ``associated_scheduled_test_suite_name``: Name of the Scheduled Test Suite from which this run was created.

- ``subnet_name``: Subnet name within which the source vPort being tested resides.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``system_id``: System ID of the NSG against which the tests are to be executed.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nutestrun.NUTestRun<nutestrun>`                                                                                                                            ``test_runs`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuscheduledtestsuite.NUScheduledTestSuite<nuscheduledtestsuite>`

