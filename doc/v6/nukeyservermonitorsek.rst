.. _nukeyservermonitorsek:

nukeyservermonitorsek
===========================================

.. class:: nukeyservermonitorsek.NUKeyServerMonitorSEK(bambou.nurest_object.NUMetaRESTObject,):

Represents a Keyserver Monitor SEK Snapshot.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``seed_payload_authentication_algorithm``: SEK Payload Signature Algorithm Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA512, .

- ``seed_payload_encryption_algorithm``: SEK Payload Encryption Algorithm Possible values are AES_128_CBC, AES_256_CBC, TRIPLE_DES_CBC, .

- ``lifetime``: The lifetime of this entry (seconds)

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``creation_time``: The time this entry was created (milliseconds since epoch)

- ``start_time``: The time this entry  was activated (milliseconds since epoch)

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


- :ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`

