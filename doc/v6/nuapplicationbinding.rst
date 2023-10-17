.. _nuapplicationbinding:

nuapplicationbinding
===========================================

.. class:: nuapplicationbinding.NUApplicationBinding(bambou.nurest_object.NUMetaRESTObject,):

Association of Applications in a priority order to an Application Performance Management Group. Priorities may be explicitly defined or auto-generated. Applications with higher priorities (lower numeric values) are evaluated first when classifying traffic.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``read_only``: Determines whether this entity is read only.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``priority``: Priority of the Application within an Application Group

- ``associated_application_id`` (**Mandatory**): Associated software application ID

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`

- :ref:`nuapplication.NUApplication<nuapplication>`

