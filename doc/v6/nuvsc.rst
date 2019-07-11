.. _nuvsc:

nuvsc
===========================================

.. class:: nuvsc.NUVSC(bambou.nurest_object.NUMetaRESTObject,):

System Monitoring details for VSC.


Attributes
----------


- ``name``: Identifies the entity with a name.

- ``management_ip``: The management IP of the VSC/HSC entity

- ``last_state_change``: Last state change timestamp (in millis).

- ``last_updated_by``: ID of the user who last updated the object.

- ``address``: The IP of the VRS entity

- ``addresses``: The Control IPv4 or IPv6 addresses of the VSC. Example: [10.10.18.10, 2001:10:10:18::10].

- ``peak_cpuusage``: Peek CPU usage percentage.

- ``peak_memory_usage``: Peek memory usage percentage.

- ``description``: Description of the entity.

- ``messages``: An array of degraded messages.

- ``disks``: Set of disk usage details.

- ``already_marked_for_unavailable``: Flag to indicate that it is already marked a unavailable.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``unavailable_timestamp``: The duration the controller is unavailable (in millis).

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location``: Identifies the entity to be associated with a location.

- ``product_version``: Product version supported by this entity.

- ``vsds``: A collection of VSD id(s) which are identified by this controller.

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
:ref:`nubgppeer.NUBGPPeer<nubgppeer>`                                                                                                                            ``bgp_peers`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`numonitoringport.NUMonitoringPort<numonitoringport>`                                                                                                       ``monitoring_ports`` 
:ref:`nucontrollervrslink.NUControllerVRSLink<nucontrollervrslink>`                                                                                              ``controller_vrs_links`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvsp.NUVSP<nuvsp>`

- :ref:`nucontrollervrslink.NUControllerVRSLink<nucontrollervrslink>`

- :ref:`nuvrs.NUVRS<nuvrs>`

