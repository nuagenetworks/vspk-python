.. _nunsredundantgatewaygroup:

nunsredundantgatewaygroup
===========================================

.. class:: nunsredundantgatewaygroup.NUNSRedundantGatewayGroup(bambou.nurest_object.NUMetaRESTObject,):

Represents Redundant Group formed by two VNS Gateways.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Redundancy Group 

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway_peer1_autodiscovered_gateway_id``: The Auto Discovered Gateway configuration owner in this Redundant Group. 

- ``gateway_peer1_connected``: Indicates status of the authoritative gateway of this Redundancy Group.

- ``gateway_peer1_id`` (**Mandatory**): The gateway configuration owner in this Redundant Group. when Redundant Group is deleted this gateway will recieve vport associations 

- ``gateway_peer1_name``: The name of the authoritative gateway owning the configuration for the Redundant Group

- ``gateway_peer2_autodiscovered_gateway_id``: The Auto Discovered Gateway configuration for the secondary gateway in this Redundant Group.

- ``gateway_peer2_connected``: Indicates status of the secondary gateway of this Redundancy Group.

- ``gateway_peer2_id``: The gateway peer in this Redundant Group. when Redundant Group is deleted this gateway will not recieve vport associations

- ``gateway_peer2_name``: The secondary gateway peer name in this Redundant Group.

- ``heartbeat_interval``: Heartbeat interval in milliseconds to declare the neighbor as dead.

- ``heartbeat_vlanid``: Heartbeat VLAN used for BFD.

- ``redundancy_port_ids``: Collections resilient port IDs associated with this redundant group.

- ``redundant_gateway_status``: The status of the Redundant Group.

- ``permitted_action``: The permitted action to USE/EXTEND this Gateway.

- ``personality``: Derived personality of the Redundancy Group.

- ``description``: Description of the Redundancy Group

- ``enterprise_id``: The enterprise associated with this Redundant Group. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``consecutive_failures_count``: Consecutive failure count.  Supported value is 3.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nushuntlink.NUShuntLink<nushuntlink>`                                                                                                                      ``shunt_links`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nunsgateway.NUNSGateway<nunsgateway>`                                                                                                                      ``ns_gateways`` 
:ref:`nuredundantport.NURedundantPort<nuredundantport>`                                                                                                          ``redundant_ports`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

