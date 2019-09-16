.. _nutca:

nutca
===========================================

.. class:: nutca.NUTCA(bambou.nurest_object.NUMetaRESTObject,):

Provides the definition of the Threshold Control Alarms.


Attributes
----------


- ``url_end_point``: URL endpoint to post Alarm data to when TCA is triggered

- ``name`` (**Mandatory**): The name of the TCA

- ``target_policy_group_id``: Target policygroup when TCA is triggered

- ``last_updated_by``: ID of the user who last updated the object.

- ``action`` (**Mandatory**): Action to be taken when TCA is fired - Alert or PolicyGroupChange

- ``period`` (**Mandatory**): The averaging period

- ``description``: Description of the TCA

- ``metric`` (**Mandatory**): The metric associated with the TCA. The following enum values have been deprecated and will be removed in the next major release 6.0: ADDRESS_MAP_EGRESS_BYTE_CNT, ADDRESS_MAP_EGRESS_PKT_CNT, ADDRESS_MAP_INGRESS_BYTE_CNT, ADDRESS_MAP_INGRESS_PKT_CNT, CONNECTION_TYPE, EGRESS_BYTE_COUNT, EGRESS_PACKET_COUNT, INGRESS_BYTE_COUNT, INGRESS_PACKET_COUNT, Q0_BYTES, Q0_DROPPED, Q0_PKT_COUNT, Q10_BYTES, Q10_DROPPED, Q10_PKT_COUNT, Q1_BYTES, Q1_DROPPED, Q1_PKT_COUNT, Q2_BYTES, Q2_DROPPED, Q2_PKT_COUNT, Q3_BYTES, Q3_DROPPED, Q3_PKT_COUNT, Q4_BYTES, Q4_DROPPED, Q4_PKT_COUNT, RX_BYTES, RX_DROPPED, RX_ERRORS, RX_PKT_COUNT, TCP_SYN_EVENT_COUNT, TX_BYTES, TX_DROPPED, TX_ERRORS, TX_PKT_COUNT

- ``threshold`` (**Mandatory**): The threshold that must be exceeded before an alarm is issued

- ``throttle_time``: Throttle time in secs

- ``disable``: This flag is used to indicate whether the watch(TCA) is enabled/disabled

- ``display_status``: Explanation of the TCA status

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``count``: Count of the attempts by maintenanace thread to create/update watcher

- ``status``: This flag is used to indicate the status of TCA

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): Rolling average or sequence of samples over the averaging period.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

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

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

