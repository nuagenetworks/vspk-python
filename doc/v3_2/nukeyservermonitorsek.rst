.. _nukeyservermonitorsek:

nukeyservermonitorsek
===========================================

.. class:: nukeyservermonitorsek.NUKeyServerMonitorSEK(bambou.nurest_object.NUMetaRESTObject,):

Represents a Keyserver Monitor SEK Snapshot


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``seed_payload_authentication_algorithm``: SEK Payload Signature Algorithm Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA512, .

- ``seed_payload_encryption_algorithm``: SEK Payload Encryption Algorithm Possible values are AES_128_CBC, AES_256_CBC, TRIPLE_DES_CBC, .

- ``lifetime``: The lifetime of this entry (seconds)

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_time``: The time this entry was created (milliseconds since epoch)

- ``start_time``: The time this entry  was activated (milliseconds since epoch)

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nukeyservermonitorencryptedseed.NUKeyServerMonitorEncryptedSeed<nukeyservermonitorencryptedseed>`                                                          ``key_server_monitor_encrypted_seeds`` 
:ref:`nukeyservermonitorencryptedsek.NUKeyServerMonitorEncryptedSEK<nukeyservermonitorencryptedsek>`                                                             ``key_server_monitor_encrypted_seks`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`

