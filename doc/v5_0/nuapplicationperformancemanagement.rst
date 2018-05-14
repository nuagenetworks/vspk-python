.. _nuapplicationperformancemanagement:

nuapplicationperformancemanagement
===========================================

.. class:: nuapplicationperformancemanagement.NUApplicationperformancemanagement(bambou.nurest_object.NUMetaRESTObject,):

Application Group is a container for group of applications 


Attributes
----------


- ``name`` (**Mandatory**): name of the application group

- ``last_updated_by``: ID of the user who last updated the object.

- ``read_only``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``description``: Description of Application Group

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_performance_monitor_id``: associated Probe ID

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuapplicationbinding.NUApplicationBinding<nuapplicationbinding>`                                                                                           ``application_bindings`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuperformancemonitor.NUPerformanceMonitor<nuperformancemonitor>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

