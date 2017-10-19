.. _nuperformancemonitor:

nuperformancemonitor
===========================================

.. class:: nuperformancemonitor.NUPerformanceMonitor(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``name`` (**Mandatory**): Name of the application group probe

- ``last_updated_by``: ID of the user who last updated the object.

- ``payload_size``: Payload size (This is a mandatory field if the networkProbeType = ONEWAY, and optional for probeType = HTTP,IPSEC_AND_VXLAN)

- ``read_only``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``service_class``: Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.

- ``description``: Description of application group probe

- ``destination_target_list``: List of targets for IKE performance monitor probes

- ``timeout``: number of milliseconds to wait until the probe is timed out

- ``interval`` (**Mandatory**): interval in seconds

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``down_threshold_count``: Number of times the probe is allowed to retry on successive timeouts

- ``probe_type``: Type to be assigned to this probe

- ``number_of_packets`` (**Mandatory**): number of packets

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`                                                 ``applicationperformancemanagements`` 
:ref:`nunsgateway.NUNSGateway<nunsgateway>`                                                                                                                      ``ns_gateways`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

