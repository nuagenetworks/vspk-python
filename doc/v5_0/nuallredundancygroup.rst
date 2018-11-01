.. _nuallredundancygroup:

nuallredundancygroup
===========================================

.. class:: nuallredundancygroup.NUAllRedundancyGroup(bambou.nurest_object.NUMetaRESTObject,):

A read only API to get all redundancy gateway objects in the VSD environment. Use the ID field to then actually manage the redundancy gateway using the redundancy gateway API entity.


Attributes
----------


- ``name``: Name of the Redundancy Group 

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway_peer1_autodiscovered_gateway_id``: The Auto Discovered Gateway configuration owner in this Redundant Group. 

- ``gateway_peer1_connected``: Indicates status of the authoritative  gateway of this Redundancy Group.

- ``gateway_peer1_id``: The gateway configuration owner in this Redundant Group. when Redundant Group is deleted this gateway will recieve vport associations 

- ``gateway_peer1_name``: The gateway   configuration owner name in this Redundant Group

- ``gateway_peer2_autodiscovered_gateway_id``: The Auto Discovered Gateway  peer in this Redundant Group

- ``gateway_peer2_connected``: Indicates status of the secondary gateway of this Redundancy Group.

- ``gateway_peer2_name``: The gateway peer name in this Redundant Group

- ``redundant_gateway_status``: The status of  Redundant Group, possible values are FAILED, SUCCESS Possible values are FAILED, SUCCESS, .

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

- ``personality``: derived personality of the Redundancy Group - VSG,VRSG,NSG,OTHER Possible values are VSG, VSA, VRSG, VDFG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .

- ``description``:  Description of the Redundancy Group

- ``enterprise_id``: The enterprise associated with this Redundant Group. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``vtep``: Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

