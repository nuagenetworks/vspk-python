.. _nuikepsk:

nuikepsk
===========================================

.. class:: nuikepsk.NUIKEPSK(bambou.nurest_object.NUMetaRESTObject,):

Shared secret used during the authentication phase of IKE protocol.


Attributes
----------


- ``name``: Name of the Encryption Profile

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the IKEv2 Authentication

- ``signature``: Base64 Encoded private key signature

- ``signing_certificate_serial_number``: Serial Number of the certificate needed to verify the encrypted data

- ``encrypted_psk``: Base64 Encoded Encrypted PSK

- ``encrypting_certificate_serial_number``: Serial Number of the certificate of the public key that encrypted this data

- ``unencrypted_psk``: Unencrypted PSK

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_enterprise_id``: The ID of the associated Enterprise

- ``auto_created``: Was this object autocreated from the connection

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


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

