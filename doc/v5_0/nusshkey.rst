.. _nusshkey:

nusshkey
===========================================

.. class:: nusshkey.NUSSHKey(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``name`` (**Mandatory**): Name of the SSH Key.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description of the SSH Key.

- ``key_type``: Type of SSH Key defined. Only RSA supported for now.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``public_key``: Public Key of a SSH Key Pair.

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


- :ref:`nuinfrastructureaccessprofile.NUInfrastructureAccessProfile<nuinfrastructureaccessprofile>`

