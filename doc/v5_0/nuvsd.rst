.. _nuvsd:

nuvsd
===========================================

.. class:: nuvsd.NUVSD(bambou.nurest_object.NUMetaRESTObject,):

System Monitoring details for VSD.


Attributes
----------


- ``url``: An optional web url for management.

- ``name``: Identifies the entity with a name.

- ``management_ip``: An optional management IP to log into this component.

- ``last_state_change``: Last state change timestamp (in millis).

- ``last_updated_by``: ID of the user who last updated the object.

- ``address``: An optional IP to access this component.

- ``peak_cpuusage``: Peek CPU usage percentage.

- ``peak_memory_usage``: Peek memory usage percentage.

- ``peer_addresses``: A comma separated list of peer addresses, if it is in cluster mode.

- ``description``: Description of the entity.

- ``messages``: An array of degraded messages.

- ``disks``: Set of disk usage details.

- ``already_marked_for_unavailable``: Flag to indicate that it is already marked a unavailable.

- ``unavailable_timestamp``: The duration the controller is unavailable (in millis).

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location``: Identifies the entity to be associated with a location.

- ``mode``: Standalone or cluster mode.

- ``product_version``: Product version supported by this entity.

- ``status``: Computed status of the entity.

- ``current_cpuusage``: Current CPU usage percentage.

- ``current_memory_usage``: Current memory usage percentage.

- ``average_cpuusage``: Average CPU usage percentage.

- ``average_memory_usage``: Average memory usage percentage.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nuvsdcomponent.NUVSDComponent<nuvsdcomponent>`                                                                                                             ``vsd_components`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvsp.NUVSP<nuvsp>`

