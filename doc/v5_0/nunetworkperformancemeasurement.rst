.. _nunetworkperformancemeasurement:

nunetworkperformancemeasurement
===========================================

.. class:: nunetworkperformancemeasurement.NUNetworkPerformanceMeasurement(bambou.nurest_object.NUMetaRESTObject,):

Network Performance Measurement is a container for group of applications and monitor scopes


Attributes
----------


- ``npm_type``: Type of network performance measurement

- ``name`` (**Mandatory**): name of the network performance measurement

- ``last_updated_by``: ID of the user who last updated the object.

- ``read_only``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``description``: description of network performance measurement

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_performance_monitor_id``: associated Performance Monitor ID 

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nunetworkperformancebinding.NUNetworkPerformanceBinding<nunetworkperformancebinding>`                                                                      ``network_performance_bindings`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`numonitorscope.NUMonitorscope<numonitorscope>`                                                                                                             ``monitorscopes`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

