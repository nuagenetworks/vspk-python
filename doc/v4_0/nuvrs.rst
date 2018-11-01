.. _nuvrs:

nuvrs
===========================================

.. class:: nuvrs.NUVRS(bambou.nurest_object.NUMetaRESTObject,):

System Monitoring details for VRS connected to VSC or HSC


Attributes
----------


- ``jsonrpc_connection_state``: The current JSON RPC connection status.

- ``name``: Identifies the entity with a name.

- ``management_ip``: The management IP of the VRS entity

- ``parent_ids``: Holds VRS controllers ids

- ``last_event_name``: The last event name from the hypervisor.

- ``last_event_object``: The last event object (including metadata) from the hypervisor.

- ``last_event_timestamp``: The last event timestamp from the hypervisor.

- ``last_state_change``: Last state change timestamp (in millis).

- ``last_updated_by``: ID of the user who last updated the object.

- ``db_synced``: Flag to indicate if the ovs database is synced between the NSG pair part of a redundant group

- ``address``: The IP of the VRS entity

- ``peak_cpuusage``: Peek CPU usage percentage.

- ``peak_memory_usage``: Peek memory usage percentage.

- ``peer``: The redundant peer id for the current VRS.

- ``personality``: VRS personality.

- ``description``: Description of the entity.

- ``messages``: An array of degraded messages.

- ``revert_behavior_enabled``: Flag to indicate if the revert behavior took place or not.

- ``revert_completed``: Flag indicates whether revert was completed successfully.

- ``revert_count``: Indicates the number of retries for the revert to take place.

- ``revert_failed_count``: This value indicates the number of failed attempts for the revert to happen successfully.

- ``licensed_state``: Licensed state.

- ``disks``: Set of disk usage details.

- ``cluster_node_role``: Indicate that the controller associated is primary, secondary or unknown.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location``: Identifies the entity to be associated with a location.

- ``role``: Flag to indicate that VRS-G redundancy state (active/standby/standalone).  Only applicable for gateways.

- ``uptime``: How long the VRS was up.

- ``primary_vsc_connection_lost``: Flag indicates whether the connection with the primary is lost, which will help trigger alarms.

- ``product_version``: Product version supported by this entity.

- ``is_resilient``: Flag to indicate that the VRS is part of a redundant group.

- ``vsc_config_state``: Indicates the configured state of the VSC.

- ``vsc_current_state``: Indicates the current state of the VSC, which may or maybe not be same as the configured state.

- ``status``: Computed status of the entity.

- ``multi_nic_vport_enabled``: VRS is in Multi-NIC VPORT Mode

- ``number_of_bridge_interfaces``: Number of bridge interfaces defined in this VRS.

- ``number_of_containers``: Number of containers defined in this VRS.

- ``number_of_host_interfaces``: Number of host interfaces defined in this VRS.

- ``number_of_virtual_machines``: Number of VMs defined in this VRS.

- ``current_cpuusage``: Current CPU usage percentage.

- ``current_memory_usage``: Current memory usage percentage.

- ``average_cpuusage``: Average CPU usage percentage.

- ``average_memory_usage``: Average memory usage percentage.

- ``external_id``: External object ID. Used for integration with third party systems

- ``dynamic``: Flag to indicate it is dynamically configured or not.

- ``hypervisor_connection_state``: The VRS connection state with the hypervisor.

- ``hypervisor_identifier``: The hypervisor IP (or name) associated with the VRS.

- ``hypervisor_name``: The hypervisor name associated with the VRS.

- ``hypervisor_type``: The hypervisor type associated with the VRS.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`numonitoringport.NUMonitoringPort<numonitoringport>`                                                                                                       ``monitoring_ports`` 
:ref:`nucontainer.NUContainer<nucontainer>`                                                                                                                      ``containers`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
:ref:`nuhsc.NUHSC<nuhsc>`                                                                                                                                        ``hscs`` 
:ref:`nuvsc.NUVSC<nuvsc>`                                                                                                                                        ``vscs`` 
:ref:`numultinicvport.NUMultiNICVPort<numultinicvport>`                                                                                                          ``multi_nic_vports`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nucontainer.NUContainer<nucontainer>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nuvm.NUVM<nuvm>`

