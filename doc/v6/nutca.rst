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

- ``metric`` (**Mandatory**): The metric associated with the TCA.

- ``threshold`` (**Mandatory**): The threshold that must be exceeded before an alarm is issued

- ``throttle_time``: Throttle time in secs

- ``disable``: This flag is used to indicate whether the watch(TCA) is enabled/disabled

- ``display_status``: Explanation of the TCA status

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

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

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

