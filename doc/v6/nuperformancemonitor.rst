.. _nuperformancemonitor:

nuperformancemonitor
===========================================

.. class:: nuperformancemonitor.NUPerformanceMonitor(bambou.nurest_object.NUMetaRESTObject,):

To enable the network performance monitoring between NSGs in an NSG Group and NSG-UBRs in an NSG-UBR Group. 


Attributes
----------


- ``name`` (**Mandatory**): Name of the application group probe

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``payload_size``: Payload size (This is a mandatory field if the networkProbeType = ONEWAY, and optional for probeType = HTTP,IPSEC_AND_VXLAN)

- ``read_only``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``service_class``: Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.

- ``description``: Application Group Probe to be used between NSGs/NSG-UBRs OR between NSGs/non-NSG devices such as an IKE gateway in their respective groups

- ``interval`` (**Mandatory**): interval in seconds

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``hold_down_timer``: Probe Timeout in milliseconds

- ``creation_date``: Time stamp when this object was created.

- ``probe_type``: Type to be assigned to this probe

- ``number_of_packets`` (**Mandatory**): number of packets

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nutier.NUTier<nutier>`                                                                                                                                     ``tiers`` 
:ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`                                                 ``applicationperformancemanagements`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuikegatewayconnection.NUIKEGatewayConnection<nuikegatewayconnection>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

