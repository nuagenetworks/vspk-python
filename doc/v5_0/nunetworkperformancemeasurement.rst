.. _nunetworkperformancemeasurement:

nunetworkperformancemeasurement
===========================================

.. class:: nunetworkperformancemeasurement.NUNetworkPerformanceMeasurement(bambou.nurest_object.NUMetaRESTObject,):

Network Performance Measurement is a container for group of applications and monitor scopes


Attributes
----------


- ``npm_type``: Type of network performance measurement

- ``name`` (**Mandatory**): name of the network performance measurement

- ``read_only``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``description``: description of network performance measurement

- ``associated_performance_monitor_id``: associated Performance Monitor ID 




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nunetworkperformancebinding.NUNetworkPerformanceBinding<nunetworkperformancebinding>`                                                                      ``network_performance_bindings`` 
:ref:`numonitorscope.NUMonitorscope<numonitorscope>`                                                                                                             ``monitorscopes`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

