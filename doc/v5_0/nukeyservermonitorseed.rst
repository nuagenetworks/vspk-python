.. _nukeyservermonitorseed:

nukeyservermonitorseed
===========================================

.. class:: nukeyservermonitorseed.NUKeyServerMonitorSeed(bambou.nurest_object.NUMetaRESTObject,):

Represents a Keyserver Monitor Seed Snapshot.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``seed_traffic_authentication_algorithm``: Seed traffic Authentication Algorithm.

- ``seed_traffic_encryption_algorithm``: Seed traffic Encryption Algorithm.

- ``seed_traffic_encryption_key_lifetime``: Seed Traffic Encryption Key Lifetime in Seconds

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
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`

