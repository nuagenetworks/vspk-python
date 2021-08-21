.. _nunsgatewaysummary:

nunsgatewaysummary
===========================================

.. class:: nunsgatewaysummary.NUNSGatewaySummary(bambou.nurest_object.NUMetaRESTObject,):

Summary information such as alarm counts, location, version, boostrap status for Network Services Gateway


Attributes
----------


- ``nsg_version``: The NSG Version (software) as reported during bootstrapping or following an upgrade.

- ``major_alarms_count``: Total number of alarms with MAJOR severity

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``gateway_id``: The ID of the NSG from which the infomation was collected.

- ``gateway_name``: The name of the gateway

- ``gateway_type``: Details on the type of gateway for which the summary is given.  For NSGs, the value would be NSGateway.

- ``latitude``: The latitude of the location of the NSG

- ``address``: Formatted address including property number, street name, suite or office number of the NSG

- ``redundant_group_id``: The ID of the Redundant Group which has this gateway

- ``redundant_group_name``: The Name of the Redundant Group which has this gateway

- ``personality``: Personality of the corresponding Network Services Gateway

- ``description``: A description of the NSG

- ``timezone_id``: Time zone in which the Gateway is located.  This can be in the form of a UTC/GMT offset, continent/city location, or country/region.  The available time zones can be found in /usr/share/zoneinfo on a Linux machine or retrieved with TimeZone.getAvailableIDs() in Java.  Refer to the IANA (Internet Assigned Numbers Authority) for a list of time zones.  URL :  http://www.iana.org/time-zones  Default value is UTC (translating to Etc/Zulu)

- ``minor_alarms_count``: Total number of alarms with MINOR severity

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``info_alarms_count``: Total number of alarms with INFO severity

- ``enterprise_id``: The enterprise associated with this NSG

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``locality``: Locality/City/County of the NSG

- ``longitude``: The longitude of the location of the NSG

- ``bootstrap_status``: Bootstrap status of the NSG

- ``country``: Country in which the NSG is located

- ``creation_date``: Time stamp when this object was created.

- ``critical_alarms_count``: Total number of alarms with CRITICAL severity

- ``state``: State/Province/Region

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``system_id``: Identifier of the gateway




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

