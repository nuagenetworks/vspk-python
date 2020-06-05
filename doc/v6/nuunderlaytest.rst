.. _nuunderlaytest:

nuunderlaytest
===========================================

.. class:: nuunderlaytest.NUUnderlayTest(bambou.nurest_object.NUMetaRESTObject,):

Underlay Test is a wrapper object for a Test Suite Run from the built in Underlay Tests Test Suite


Attributes
----------


- ``name``: The name of the test

- ``test_result``: The result of the test

- ``underlay_test_server``: The Underlay Test Server this test was executed against

- ``underlay_test_type``: Type of Test

- ``create_only``: Create the test only, do not trigger the command. Used for loading existing results

- ``associated_data_path_id``: The associated data path ID

- ``associated_ns_gateway_id``: The ID of the associated NSGateway

- ``associated_ns_gateway_name``: The name of the associated NSGateway

- ``associated_test_suite_run_id``: The ID of the associated Test Suite Run

- ``start_date_time``: The start date time of the test

- ``stop_date_time``: The stop date time of the test

- ``run_bandwidth_test``: Flag to run the Bandwidth test

- ``run_connectivity_test``: Flag to run the connectivity test

- ``run_mtu_discovery_test``: Flag to run the MTU Discovery test

- ``duration``: The test duration in seconds






Parents
--------


- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

