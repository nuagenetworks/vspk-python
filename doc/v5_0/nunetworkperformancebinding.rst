.. _nunetworkperformancebinding:

nunetworkperformancebinding
===========================================

.. class:: nunetworkperformancebinding.NUNetworkPerformanceBinding(bambou.nurest_object.NUMetaRESTObject,):

Association of Network Performance Measurement policies enable the measurement of path SLA metrics between NSGs in the domain.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``read_only``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``priority``: Priority of the associated Network Performance Measurement

- ``associated_network_measurement_id``: Associated Network Performance Measurement UD

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


- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nunetworkperformancemeasurement.NUNetworkPerformanceMeasurement<nunetworkperformancemeasurement>`

