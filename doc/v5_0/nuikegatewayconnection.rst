.. _nuikegatewayconnection:

nuikegatewayconnection
===========================================

.. class:: nuikegatewayconnection.NUIKEGatewayConnection(bambou.nurest_object.NUMetaRESTObject,):

Represents an IKE Gateway Connection object


Attributes
----------


- ``nsg_identifier``: NSG Identifier. Null to take on the default 'uuid'

- ``nsg_identifier_type``: NSG Identifier Type. 

- ``nsg_role``: NSG role

- ``name``: Optional Name of the connection

- ``mark``: skbMark, used by vrs for the ike monitor feature

- ``last_updated_by``: ID of the user who last updated the object.

- ``sequence``: The sequence of the IKE Gateway Connection

- ``allow_any_subnet``: Allow any local subnets to be used

- ``unencrypted_psk``: Unencrypted PSK

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port_vlan_name``: The Name of the Port and Vlan the IKEv2 Connection is on

- ``priority``: Priority of the IKEv2 Gateway Connection

- ``associated_ike_authentication_id``: Associated Authentication ID

- ``associated_ike_authentication_type``: Associated Authentication Type

- ``associated_ike_encryption_profile_id``: The ID of the associated IKEEncryptionProfile

- ``associated_ike_gateway_profile_id``: The ID of the associated IKEGatewayProfile

- ``associated_vlanid``: The ID of the associated Vlan

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuperformancemonitor.NUPerformanceMonitor<nuperformancemonitor>`                                                                                           ``performance_monitors`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nusubnet.NUSubnet<nusubnet>`                                                                                                                               ``subnets`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

