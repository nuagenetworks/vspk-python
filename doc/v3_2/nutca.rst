.. _nutca:

nutca
===========================================

.. class:: nutca.NUTCA(bambou.nurest_object.NUMetaRESTObject,):

Provides the definition of the Threshold Control Alarms.


Attributes
----------


- ``url_end_point``: URL endpoint to post Alarm data to when TCA is triggered

- ``name`` (**Mandatory**): The name of the TCA

- ``last_updated_by``: ID of the user who last updated the object.

- ``scope`` (**Mandatory**): GLOBAL or LOCAL scope. Global refers to aggregate values across subnets, zones or domains. Local refers to traffic from/to individual VMs.

- ``period`` (**Mandatory**): The averaging period

- ``description``: Desription of the TCA

- ``metric`` (**Mandatory**): The metric associated with the TCA.

- ``threshold`` (**Mandatory**): The threshold that must be exceeded before an alarm is issued

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

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


- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nutier.NUTier<nutier>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nume.NUMe<nume>`

