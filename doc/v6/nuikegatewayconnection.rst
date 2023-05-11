.. _nuikegatewayconnection:

nuikegatewayconnection
===========================================

.. class:: nuikegatewayconnection.NUIKEGatewayConnection(bambou.nurest_object.NUMetaRESTObject,):

Set the attributes like NSG role, authentication method etc for establishing IKE security association with remote gateway.


Attributes
----------


- ``nsg_identifier``: NSG Identifier. Null to take on the default 'uuid'

- ``nsg_identifier_type``: NSG Identifier Type. 

- ``nsg_role``: NSG role

- ``name``: Optional Name of the connection

- ``mark``: skbMark, used by vrs for the ike monitor feature

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``sequence``: The sequence of the IKE Gateway Connection

- ``mirrored_connection``: Indicates if the IKEGatewayConnection is mirroring an equivalent one on Shunt VLAN or not.

- ``allow_any_subnet``: Allow any local subnets to be used

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``unencrypted_psk``: Unencrypted PSK

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``configuration_status``: Status of configuration on third-party cloud instance

- ``port_vlan_name``: The Name of the Port and Vlan the IKEv2 Connection is on

- ``creation_date``: Time stamp when this object was created.

- ``priority``: Priority of the IKEv2 Gateway Connection

- ``associated_cloud_id``: ID of the associated third-party cloud instance

- ``associated_cloud_type``: Type of associated third-party cloud instance, ex. AZURECLOUD

- ``associated_ike_authentication_id``: Associated Authentication ID

- ``associated_ike_authentication_type``: Associated Authentication Type

- ``associated_ike_encryption_profile_id``: The ID of the associated IKEEncryptionProfile

- ``associated_ike_gateway_profile_id``: The ID of the associated IKEGatewayProfile

- ``associated_vlanid``: The ID of the associated Vlan

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuperformancemonitor.NUPerformanceMonitor<nuperformancemonitor>`                                                                                           ``performance_monitors`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nusubnet.NUSubnet<nusubnet>`                                                                                                                               ``subnets`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvirtualuplink.NUVirtualUplink<nuvirtualuplink>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

