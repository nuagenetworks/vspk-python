.. _nutestsuiterun:

nutestsuiterun
===========================================

.. class:: nutestsuiterun.NUTestSuiteRun(bambou.nurest_object.NUMetaRESTObject,):

A Test Suite Run represents the execution of a given Test Suite within a diagnostic container on an NSG. It groups together multiple Test Runs.


Attributes
----------


- ``vport_name``: The name of the vPort against which the Test Suite is to be executed.

- ``ns_gateway_name``: The name of the NSG against which the Test Suite will be executed.

- ``last_updated_by``: ID of the user who last updated the object.

- ``datapath_id``: The datapath ID (System ID) of the NSG instance against which the tests are to be executed.

- ``destination``: Destination to be used in conjunction with tests part of the Test Suite. Could be an IPv4 address or FQDN.

- ``birth_certificate``: Flag to mark this test as the Birth Certificate (i.e. it was run during activation)

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_name``: The name of the Domain within which the source vPort being tested resides.

- ``zone_name``: The name of the Zone within which the source vPort being tested resides.

- ``operation_status``: The status of the test operation request as received by the NSG Agent. This field is set by the NSG.

- ``associated_entity_type``: Type of the entity that is hosting the Test Suite Run.  This can be a vPort or an NSG.

- ``associated_test_suite_id`` (**Mandatory**): The ID of the Test Suite from which this instance of the Test Suite Run was created.

- ``associated_test_suite_name``: The name of the Test Suite instance from which this Test Suite Run was created.

- ``associated_underlay_test_id``: The associated underlay test (if applicable)

- ``subnet_name``: The name of the Subnet within which the source vPort being tested resides.

- ``external_id``: External object ID. Used for integration with third party systems




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

- :ref:`nutestsuite.NUTestSuite<nutestsuite>`

