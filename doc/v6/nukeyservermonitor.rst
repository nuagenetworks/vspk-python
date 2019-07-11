.. _nukeyservermonitor:

nukeyservermonitor
===========================================

.. class:: nukeyservermonitor.NUKeyServerMonitor(bambou.nurest_object.NUMetaRESTObject,):

Represents a Keyserver Monitor Snapshot.


Attributes
----------


- ``last_update_time``: The time the latest SEK or Seed was created/removed (milliseconds since epoch)

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway_secured_data_record_count``: Total number of Gateway Secured Data records

- ``keyserver_monitor_encrypted_sek_count``: Total number of Keyserver Monitor Encrypted SEK records

- ``keyserver_monitor_encrypted_seed_count``: Total number of Keyserver Monitor Encrypted Seed records

- ``keyserver_monitor_sek_count``: Total number of Keyserver Monitor SEK records

- ``keyserver_monitor_seed_count``: Total number of Keyserver Monitor Seed records

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise_secured_data_record_count``: Total number of Enterprise Secured Data records

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nukeyservermonitorencryptedseed.NUKeyServerMonitorEncryptedSeed<nukeyservermonitorencryptedseed>`                                                          ``key_server_monitor_encrypted_seeds`` 
:ref:`nukeyservermonitorseed.NUKeyServerMonitorSeed<nukeyservermonitorseed>`                                                                                     ``key_server_monitor_seeds`` 
:ref:`nukeyservermonitorsek.NUKeyServerMonitorSEK<nukeyservermonitorsek>`                                                                                        ``key_server_monitor_seks`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

