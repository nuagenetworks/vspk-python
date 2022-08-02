.. _nuscheduledtestsuite:

nuscheduledtestsuite
===========================================

.. class:: nuscheduledtestsuite.NUScheduledTestSuite(bambou.nurest_object.NUMetaRESTObject,):

A Scheduled Test Suite is grouping of a number of ICMP Echo Tests that can be run at the specified schedule, consecutively from a given source (NSGateway or VPort) toward a specified destination.


Attributes
----------


- ``name`` (**Mandatory**): Name of the scheduled test suite instance.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``schedule_interval``: This is the interval between all test runs in this suite and the next run of tests in this suite.

- ``schedule_interval_units``: The units for the specified interval. This can be minutes, hours or days.

- ``description``: Description for the scheduled test suite instance.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``end_date_time``: The date and time by which this suite will be terminated. If this is not specified the tests will continue to run at the specified frequency.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``start_date_time``: The date and time when this suite will start on the NSGateway.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuscheduledtestsuiterun.NUScheduledtestsuiterun<nuscheduledtestsuiterun>`                                                                                  ``scheduledtestsuiteruns`` 
:ref:`nutest.NUTest<nutest>`                                                                                                                                     ``tests`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

