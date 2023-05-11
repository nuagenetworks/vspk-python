.. _nul7applicationsignature:

nul7applicationsignature
===========================================

.. class:: nul7applicationsignature.NUL7applicationsignature(bambou.nurest_object.NUMetaRESTObject,):

Layer 7 ApplicationType , these are auto created as part of VSD bringup


Attributes
----------


- ``name`` (**Mandatory**):  name of the L7 App

- ``last_updated_by``: ID of the user who last updated the object.

- ``category``: Category of this application

- ``readonly``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``reference``: URL address reference received from Procera for every signature.

- ``deprecated``: Determines whether this entity is deprecated. Deprecated L7 Application Signatures cannot be associated to an application.

- ``deprecated_version``: Determines the procera version when this entity was deprecated. Deprecated objects cannot be modified or deleted.

- ``description``: description for L7 App

- ``dictionary_version``: Version of the L7 Application Type

- ``signature_index``: Index number received from Procera for every L7 signature.

- ``signature_version``: The AAR application version where this signature was last updated.

- ``risk``: Risk is determined on a scale of 1 to 5. It is received from Procera for every signature.

- ``plugin_name``: Plugin name received from Procera for every signature.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``software_flags``: Software flags received from Procera for every signature.

- ``productivity``: Productivity Index is scored relative to a work environment for every L7 signature on a scale of 1-5.

- ``guidstring``: GUID of the Application

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuapplication.NUApplication<nuapplication>`                                                                                                                ``applications`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

