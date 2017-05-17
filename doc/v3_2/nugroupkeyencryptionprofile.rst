.. _nugroupkeyencryptionprofile:

nugroupkeyencryptionprofile
===========================================

.. class:: nugroupkeyencryptionprofile.NUGroupKeyEncryptionProfile(bambou.nurest_object.NUMetaRESTObject,):

Represents a Group Key Profile


Attributes
----------


- ``sek_generation_interval``: Group Key SEK Generation Interval in Seconds. Min=1, Max=86400

- ``sek_lifetime``: Group Key SEK Lifetime in Seconds. Min=1, Max=86400

- ``sek_payload_encryption_algorithm``: Group Key SEK Payload Encryption Algorithm.

- ``sek_payload_encryption_bc_algorithm``: Group Key Sek Payload Encryption BC Algorithm (read only)

- ``sek_payload_encryption_key_length``: Group Key Sek Payload Encryption Key Length (read only)

- ``sek_payload_signing_algorithm``: Group Key SEK Payload Signature Algorithm.

- ``name``: Name of the Encryption Profile

- ``last_updated_by``: ID of the user who last updated the object.

- ``seed_generation_interval``: Group Key SEED Generation Interval in Seconds.

- ``seed_lifetime``: Group Key SEED Lifetime in Seconds. Min=1, Max=86400

- ``seed_payload_authentication_algorithm``: Group Key SEK Payload Signature Algorithm.

- ``seed_payload_authentication_bc_algorithm``: Group Key Seed Payload Authentication Algorithm (read only)

- ``seed_payload_authentication_key_length``: Group Key Seed Payload Authentication Key Length  (read only)

- ``seed_payload_encryption_algorithm``: Group Key SEED Payload Encryption Algorithm.

- ``seed_payload_encryption_bc_algorithm``: Group Key Seed Payload Encryption Algorithm (read only)

- ``seed_payload_encryption_key_length``: Group Key Seed Payload Encryption Key Length (read only)

- ``seed_payload_signing_algorithm``: Group Key Seed Payload Signature Algorithm.

- ``description``: A description of the Profile instance created.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``traffic_authentication_algorithm``: Group Key traffic Authentication Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .

- ``traffic_encryption_algorithm``: Group Key traffic Encryption Algorithm. Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, TRIPLE_DES_CBC, .

- ``traffic_encryption_key_lifetime``: Group Key Traffic Encryption Key Lifetime in Seconds. Min=1, Max=86400

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

