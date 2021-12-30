.. _nuscheduledtestsuite:

nuscheduledtestsuite
===========================================

.. class:: nuscheduledtestsuite.NUScheduledTestSuite(bambou.nurest_object.NUMetaRESTObject,):

A Scheduled Test Suite is grouping of a number of ICMP Echo Tests that can be run at the specified schedule, consecutively from a given source (NSGateway or VPort) toward a specified destination.


Attributes
----------


- ``name`` (**Mandatory**): Name of the scheduled test suite instance.

- ``schedule_interval``: This is the interval between all test runs in this suite and the next run of tests in this suite.

- ``schedule_interval_units``: The units for the specified interval. This can be minutes, hours or days.

- ``description``: Description for the scheduled test suite instance.

- ``end_date_time``: The date and time by which this suite will be terminated. If this is not specified the tests will continue to run at the specified frequency.

- ``start_date_time``: The date and time when this suite will start on the NSGateway.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuscheduledtestsuiterun.NUScheduledtestsuiterun<nuscheduledtestsuiterun>`                                                                                  ``scheduledtestsuiteruns`` 
:ref:`nutest.NUTest<nutest>`                                                                                                                                     ``tests`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

