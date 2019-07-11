.. _nutestsuite:

nutestsuite
===========================================

.. class:: nutestsuite.NUTestSuite(bambou.nurest_object.NUMetaRESTObject,):

A Test Suite is grouping a number of diagnostic Tests that can be run consecutively from a given source (NSGateway or VPort) toward a specified destination.


Attributes
----------


- ``name`` (**Mandatory**): The name given by the operator to the Test Suite.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: An operator given description of the Test Suite.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise_id``: The ID of the Enterprise to which this Test Suite belongs to.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nutest.NUTest<nutest>`                                                                                                                                     ``tests`` 
:ref:`nutestsuiterun.NUTestSuiteRun<nutestsuiterun>`                                                                                                             ``test_suite_runs`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

