.. _nutestrun:

nutestrun
===========================================

.. class:: nutestrun.NUTestRun(bambou.nurest_object.NUMetaRESTObject,):

A Test Run object represents the execution of a specific Test as part of a Test Suite Run.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``command``: The command, with its arguments, that is to be executed as part of the Test Run.

- ``command_exit_code``: The exit code returned to the OS from the executed test command. Field modified on VSD by the NSG.

- ``command_output``: The output of the test command that was executed. Updated on VSD by the NSG.

- ``command_output_summary``: A brief summary of the command output received by the NSG.  Only the beginning and the end of the output is displayed.

- ``operation_status``: The status of the test operation request as received by the NSG Agent. This field is set by the NSG.

- ``associated_test_id``: The ID of the Test instance to which this Test Run is bound.

- ``associated_test_suite_run_id``: Test Run instances are part of a Test Suite Run.  This is the ID of the Test Suite Run object to which this Test Run belongs.

- ``start_date_time``: The start date and time of the test in milliseconds since Epoch.

- ``stop_date_time``: The stop date and time of the test in milliseconds since Epoch.

- ``duration``: The duration of execution of the Test in milliseconds.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nutestsuiterun.NUTestSuiteRun<nutestsuiterun>`

