.. _nukeyservermember:

nukeyservermember
===========================================

.. class:: nukeyservermember.NUKeyServerMember(bambou.nurest_object.NUMetaRESTObject,):

Represents a KeyServer


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``pem_encoded``: PEM Encoded Certificate

- ``certificate_serial_number``: Certificate serial number associated to the keyserver private key which it is currently signing with

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``fqdn``: FQDN of the keyserver member

- ``creation_date``: Time stamp when this object was created.

- ``issuer_dn``: Issuer DN

- ``subject_dn``: Subject DN

- ``public_key``: Public Key

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


- :ref:`nume.NUMe<nume>`

