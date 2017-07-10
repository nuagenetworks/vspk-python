.. _nuapplicationperformancemanagement:

nuapplicationperformancemanagement
===========================================

.. class:: nuapplicationperformancemanagement.NUApplicationperformancemanagement(bambou.nurest_object.NUMetaRESTObject,):

Application Group is a container for group of applications 


Attributes
----------


- ``name`` (**Mandatory**): name of the application group

- ``read_only``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``description``: Description of Application Group

- ``associated_performance_monitor_id``: associated Probe ID




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuapplicationbinding.NUApplicationBinding<nuapplicationbinding>`                                                                                           ``application_bindings`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuperformancemonitor.NUPerformanceMonitor<nuperformancemonitor>`

