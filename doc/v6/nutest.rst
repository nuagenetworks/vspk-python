.. _nutest:

nutest
===========================================

.. class:: nutest.NUTest(bambou.nurest_object.NUMetaRESTObject,):

A Test defines a command to run inside a diagnositc container on an NSG. It represents a command with arguments that will be executed within the diagnostic container as part of a Test Suite run


Attributes
----------


- ``name``: The name of the Test Definition instance bound to this Test object.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A brief description of the Test Definition referred to by this Test object.

- ``destination``: Destination to be used in conjunction with this Test. Could be an IPv4 address or FQDN

- ``timeout``: The timeout value set for the Test Definition instance, in seconds, at which point the system will consider the test as failed.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``command``: The command line with arguments as extracted from the Test Definition instance bound to this Test instance.

- ``order``: Test order used to run tests. Lower order tests will run before higher order ones.

- ``associated_test_definition_id`` (**Mandatory**): The associated Test Definition instance used as an information base for the Test object.

- ``associated_test_suite_id``: The ID of the Test Suite this Test instance is part of.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nutestsuite.NUTestSuite<nutestsuite>`

