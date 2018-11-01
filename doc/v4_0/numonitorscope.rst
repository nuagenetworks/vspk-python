.. _numonitorscope:

numonitorscope
===========================================

.. class:: numonitorscope.NUMonitorscope(bambou.nurest_object.NUMetaRESTObject,):

This class tries to define the scope of probe (the NSGs between which the probe needs) to run.


Attributes
----------


- ``name`` (**Mandatory**): Name for the given scope

- ``read_only``: Determines whether this entity is read only. Read only objects cannot be modified or deleted.

- ``destination_nsgs``: List of destination NSGs to which the probe needs to run

- ``allow_all_destination_nsgs``: When set true, allows all destination NSGs

- ``allow_all_source_nsgs``: When set true, allows all Source NSGs

- ``source_nsgs``: List of source NSGs from which the probe needs to be started.






Parents
--------


- :ref:`nuapplication.NUApplication<nuapplication>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nunetworkperformancemeasurement.NUNetworkPerformanceMeasurement<nunetworkperformancemeasurement>`

