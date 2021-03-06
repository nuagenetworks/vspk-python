.. _nupatch:

nupatch
===========================================

.. class:: nupatch.NUPatch(bambou.nurest_object.NUMetaRESTObject,):

This entity defines a patch installed somewhere (ie. NSG Patch)


Attributes
----------


- ``name``: The Patch name

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``patch_build_number``: The Patch build number (eg. 1)

- ``patch_summary``: The summary given for the Patch

- ``patch_tag``: The Patch Tag. This is a unique identifier including the name, version and release of the patch

- ``patch_version``: The Patch version (ie. 1.0.0)

- ``description``: The Patch description

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``supports_deletion``: Whether or not this Patch supports deletion. If a patch does not support deletion, the REST DELETE method will fail

- ``supports_network_acceleration``: Whether or not this patch supports Network Acceleration

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


- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

