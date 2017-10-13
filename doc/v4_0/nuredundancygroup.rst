.. _nuredundancygroup:

nuredundancygroup
===========================================

.. class:: nuredundancygroup.NURedundancyGroup(bambou.nurest_object.NUMetaRESTObject,):

Represents Redundant Group formed by two Gateways.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Redundancy Group 

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway_peer1_autodiscovered_gateway_id``: The Auto Discovered Gateway configuration owner in this Redundant Group. 

- ``gateway_peer1_id``: The gateway configuration owner in this Redundant Group. when Redundant Group is deleted this gateway will recieve vport associations 

- ``gateway_peer1_name``: The gateway   configuration owner name in this Redundant Group

- ``gateway_peer2_autodiscovered_gateway_id``: The Auto Discovered Gateway  peer in this Redundant Group

- ``gateway_peer2_id``: The gateway peer in this Redundant Group. when Redundant Group is deleted this gateway will not recieve vport associations

- ``gateway_peer2_name``: The gateway peer name in this Redundant Group

- ``redundant_gateway_status``: The status of  Redundant Group, possible values are FAILED, SUCCESS Possible values are FAILED, SUCCESS, .

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

- ``personality``: derived personality of the Redundancy Group - VSG,VRSG,NSG,OTHER Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .

- ``description``:  Description of the Redundancy Group

- ``enterprise_id``: The enterprise associated with this Redundant Group. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``vtep``: Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nugateway.NUGateway<nugateway>`                                                                                                                            ``gateways`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`nuwanservice.NUWANService<nuwanservice>`                                                                                                                   ``wan_services`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nuport.NUPort<nuport>`                                                                                                                                     ``ports`` 
:ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`                                                                                                 ``vsg_redundant_ports`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

