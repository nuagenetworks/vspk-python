.. _nugatewayredundantport:

nugatewayredundantport
===========================================

.. class:: nugatewayredundantport.NUGatewayRedundantPort(bambou.nurest_object.NUMetaRESTObject,):

Represents a redundant Port under a particular gateway object or redundant group object.


Attributes
----------


- ``vlan_range``: VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

- ``name`` (**Mandatory**): Name of the Port

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``native_vlan``: Default Native VLAN to carry untagged traffic on the redundant ports of this redundant gateway group. Applicable for third-party Netconf Gateways only. Possible values are 1-3967.

- ``permitted_action``: The permitted  action to USE/EXTEND  this port.

- ``description``: A description of the Port

- ``physical_name`` (**Mandatory**): Identifier of the Redundant Port. The name should be corresponding to the Physical Name of the ports belonging to this redundant instance.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port_peer1_id``: The master gateway peer port id.

- ``port_peer2_id``: The slave gateway peer port id.

- ``port_type`` (**Mandatory**): Type of the Port.

- ``creation_date``: Time stamp when this object was created.

- ``use_user_mnemonic``: determines whether to use user mnemonic of the Port

- ``user_mnemonic``: user mnemonic of the Port

- ``associated_egress_qos_policy_id``: UUID of the Egress QOS Policy associated with this Vlan.

- ``status``: Status of the port.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuvlan.NUVLAN<nuvlan>`                                                                                                                                     ``vlans`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

