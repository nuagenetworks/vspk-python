.. _nusshkey:

nusshkey
===========================================

.. class:: nusshkey.NUSSHKey(bambou.nurest_object.NUMetaRESTObject,):

SSH (Secure Shell) is used to provide secure remote console access to NSGs deployed in branch locations. When key-based authentication is in use, the SSH keys represent the list of public keys that are authorized to open an SSH connection with the username set at the Access Profile level.


Attributes
----------


- ``name`` (**Mandatory**): Name of the SSH Key.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A description of the SSH Key.

- ``key_type``: Type of SSH Key defined. Only RSA supported for now.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``public_key`` (**Mandatory**): Public Key of a SSH Key Pair.

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


- :ref:`nuinfrastructureaccessprofile.NUInfrastructureAccessProfile<nuinfrastructureaccessprofile>`

