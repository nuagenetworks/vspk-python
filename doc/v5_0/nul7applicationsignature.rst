.. _nul7applicationsignature:

nul7applicationsignature
===========================================

.. class:: nul7applicationsignature.NUL7applicationsignature(bambou.nurest_object.NUMetaRESTObject,):

Layer 7 ApplicationType , these are auto created as part of VSD bringup


Attributes
----------


- ``name`` (**Mandatory**):  name of the L7 App

- ``category``: Category of this application

- ``readonly``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``reference``: URL address reference received from Procera for every signature.

- ``deprecated``: Determines whether this entity is deprecated. Deprecated L7 Application Signatures cannot be associated to an application.

- ``deprecated_version``: Determines the procera version when this entity was deprecated. Deprecated objects cannot be modified or deleted.

- ``description``: description for L7 App

- ``dictionary_version``: Version of the L7 Application Type

- ``signature_index``: Index number received from Procera for every L7 signature.

- ``risk``: Risk is determined on a scale of 1 to 5. It is received from Procera for every signature.

- ``plugin_name``: Plugin name received from Procera for every signature.

- ``software_flags``: Software flags received from Procera for every signature.

- ``productivity``: Productivity Index is scored relative to a work environment for every L7 signature on a scale of 1-5.

- ``guidstring``: GUID of the Application




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuapplication.NUApplication<nuapplication>`                                                                                                                ``applications`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

