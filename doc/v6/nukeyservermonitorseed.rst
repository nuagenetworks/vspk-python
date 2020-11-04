.. _nukeyservermonitorseed:

nukeyservermonitorseed
===========================================

.. class:: nukeyservermonitorseed.NUKeyServerMonitorSeed(bambou.nurest_object.NUMetaRESTObject,):

Represents a Keyserver Monitor Seed Snapshot.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``seed_traffic_authentication_algorithm``: Seed traffic Authentication Algorithm.

- ``seed_traffic_encryption_algorithm``: Seed traffic Encryption Algorithm.

- ``seed_traffic_encryption_key_lifetime``: Seed Traffic Encryption Key Lifetime in Seconds

- ``seed_type``: Indicates if this is a Standard (or) a Disaster Recovery seed.

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
:ref:`nukeyservermonitorencryptedseed.NUKeyServerMonitorEncryptedSeed<nukeyservermonitorencryptedseed>`                                                          ``key_server_monitor_encrypted_seeds`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`

