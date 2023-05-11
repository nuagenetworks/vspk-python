.. _nuapplicationbinding:

nuapplicationbinding
===========================================

.. class:: nuapplicationbinding.NUApplicationBinding(bambou.nurest_object.NUMetaRESTObject,):

Association of Applications in a priority order to an Application Performance Management Group. Priorities may be explicitly defined or auto-generated. Applications with higher priorities (lower numeric values) are evaluated first when classifying traffic.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``read_only``: Determines whether this entity is read only.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``priority``: Priority of the Application within an Application Group

- ``associated_application_id`` (**Mandatory**): Associated software application ID

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

- :ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`

