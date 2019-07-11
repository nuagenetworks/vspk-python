.. _numonitorscope:

numonitorscope
===========================================

.. class:: numonitorscope.NUMonitorscope(bambou.nurest_object.NUMetaRESTObject,):

Monitoring Scope bound Performance monitors to either ALL or a sub-set of NSGs. Scope is defined by selecting NSGs that should execute Performance Monitors. 


Attributes
----------


- ``name`` (**Mandatory**): Name for the given scope

- ``last_updated_by``: ID of the user who last updated the object.

- ``read_only``: Determines whether this entity is read only. Read only objects cannot be modified or deleted.

- ``destination_nsgs``: List of destination NSGs to which the probe needs to run

- ``allow_all_destination_nsgs``: When set true, allows all destination NSGs

- ``allow_all_source_nsgs``: When set true, allows all Source NSGs

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``source_nsgs``: List of source NSGs from which the probe needs to be started.

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


- :ref:`nuapplication.NUApplication<nuapplication>`

- :ref:`nunetworkperformancemeasurement.NUNetworkPerformanceMeasurement<nunetworkperformancemeasurement>`

