.. _nukeyservermonitorencryptedseed:

nukeyservermonitorencryptedseed
===========================================

.. class:: nukeyservermonitorencryptedseed.NUKeyServerMonitorEncryptedSeed(bambou.nurest_object.NUMetaRESTObject,):

Represents a Keyserver Monitor Encrypted Seed Snapshot.


Attributes
----------


- ``sek_creation_time``: SEK Creation Time

- ``last_updated_by``: ID of the user who last updated the object.

- ``key_server_certificate_serial_number``: KeyServer Certificate Serial Number

- ``enterprise_secured_data_id``: Enterprise Secured ID record this monitor represents

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_key_server_monitor_sek_creation_time``: The creation time of the associated KeyServer Monitor Seed ID

- ``associated_key_server_monitor_sekid``: The ID of the associated KeyServer Monitor SEK ID

- ``associated_key_server_monitor_seed_creation_time``: The creation time of the associated KeyServer Monitor Seed ID

- ``associated_key_server_monitor_seed_id``: The ID of the associated KeyServer Monitor Seed ID

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


- :ref:`nukeyservermonitorseed.NUKeyServerMonitorSeed<nukeyservermonitorseed>`

- :ref:`nukeyservermonitor.NUKeyServerMonitor<nukeyservermonitor>`

