.. _nuapplicationperformancemanagement:

nuapplicationperformancemanagement
===========================================

.. class:: nuapplicationperformancemanagement.NUApplicationperformancemanagement(bambou.nurest_object.NUMetaRESTObject,):

Application Group is a container for group of applications 


Attributes
----------


- ``name`` (**Mandatory**): name of the application group

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``read_only``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``description``: Description of Application Group

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``app_group_unique_id``: 2 byte Id to uniquely identify Application Group between OVS, nuage_dpi and perfd processes for proper functioning of AAR.

- ``creation_date``: Time stamp when this object was created.

- ``associated_performance_monitor_id``: associated Probe ID

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuapplicationbinding.NUApplicationBinding<nuapplicationbinding>`                                                                                           ``application_bindings`` 
:ref:`nuapplicationperformancemanagementbinding.NUApplicationperformancemanagementbinding<nuapplicationperformancemanagementbinding>`                            ``applicationperformancemanagementbindings`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuperformancemonitor.NUPerformanceMonitor<nuperformancemonitor>`

