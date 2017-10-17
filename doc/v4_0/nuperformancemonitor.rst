.. _nuperformancemonitor:

nuperformancemonitor
===========================================

.. class:: nuperformancemonitor.NUPerformanceMonitor(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``name`` (**Mandatory**): Name of the application group probe

- ``last_updated_by``: ID of the user who last updated the object.

- ``payload_size`` (**Mandatory**): Payload size

- ``read_only``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``service_class``: Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.

- ``description``: Description of application group probe

- ``interval`` (**Mandatory**): interval in seconds

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``number_of_packets`` (**Mandatory**): number of packets

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`                                                 ``applicationperformancemanagements`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

