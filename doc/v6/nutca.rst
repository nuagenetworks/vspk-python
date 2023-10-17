.. _nutca:

nutca
===========================================

.. class:: nutca.NUTCA(bambou.nurest_object.NUMetaRESTObject,):

Provides the definition of the Threshold Control Alarms.


Attributes
----------


- ``url_end_point``: URL endpoint to post Alarm data to when TCA is triggered

- ``name`` (**Mandatory**): The name of the TCA

- ``target_entity_id``: ID of the target VSD entity used by the TCA action

- ``target_policy_group_id``: Target policygroup used by the TCA action

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``action`` (**Mandatory**): Action to be taken when TCA is fired - Alert or PolicyGroupChange

- ``period`` (**Mandatory**): The averaging period

- ``description``: Description of the TCA

- ``destination_port``: Destination Port Number. Valid range is 1-65535 for the metric DESTINATION_PORT_PROTOCOL_COUNT, 0 for rest of the metrics.

- ``metric`` (**Mandatory**): The metric associated with the TCA.

- ``threshold`` (**Mandatory**): The threshold that must be exceeded before an alarm is issued

- ``throttle_time``: Throttle time in seconds

- ``disable``: This flag is used to indicate whether the watch(TCA) is enabled/disabled

- ``display_status``: Explanation of the TCA status

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``count``: Count of the attempts by maintenanace thread to create/update watcher

- ``creation_date``: Time stamp when this object was created.

- ``trigger_interval``: The trigger interval of the ES watch corresponding to this TCA, in seconds

- ``protocol``: L4 service protocol - Possible values TCP, UDP for the metric DESTINATION_PORT_PROTOCOL_COUNT, NONE for rest of the metrics.

- ``status``: This flag is used to indicate the status of TCA

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): The aggregation type for the metric over the selected period - Sum, Average or Unique Count




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

