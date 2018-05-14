.. _nuapplicationbinding:

nuapplicationbinding
===========================================

.. class:: nuapplicationbinding.NUApplicationBinding(bambou.nurest_object.NUMetaRESTObject,):

None


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


- :ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`

- :ref:`nuapplication.NUApplication<nuapplication>`

