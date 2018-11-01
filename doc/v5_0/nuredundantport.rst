.. _nuredundantport:

nuredundantport
===========================================

.. class:: nuredundantport.NURedundantPort(bambou.nurest_object.NUMetaRESTObject,):

Represents a Port under a particular gateway object or redundant group object.


Attributes
----------


- ``vlan_range`` (**Mandatory**): VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

- ``mtu``: Port MTU (Maximum Transmission Unit) :  The size in octets of the largest protocol data unit (PDU) that the layer can pass on.  The default value is normally 1500 octets for Ethernet v2 and can go up to 9198 for Jumbo Frames.

- ``name`` (**Mandatory**): Name of the Redundant Port

- ``last_updated_by``: ID of the user who last updated the object.

- ``permitted_action``: The permitted action to USE/EXTEND this Redundant Port.

- ``description``: A description of the Redundant Port instance.

- ``physical_name`` (**Mandatory**): Identifier of the Redundant Port.  The name should be corresponding to the Physical Name of the ports belonging to this redundant instance.

- ``infrastructure_profile_id``: The ID of the infrastructure port profile this instance is associated with.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port_peer1_id``: Port ID of the port acting as master component of the redundant port instance.

- ``port_peer2_id``: Port ID of the port acting as slave component of the redundant port instance.

- ``port_type`` (**Mandatory**): Type of the Redundant Port.

- ``speed``: Port Speed in Mb/s :  Supported Ethernet speeds are 10 (10Base-T), 100 (Fast-ethernet 100Base-TX), 1000 (Gigabit Ethernet 1000Base-T), 10 000 (10 Gigabit Ethernet 10GBase-X), and Auto-Negotiate.

- ``use_untagged_heartbeat_vlan``: A flag to indicate if for this redundant port an untagged heartbeat VLAN is to be used. If this is not set then will use the heartbeat VLAN set by the NS redundant group

- ``use_user_mnemonic``: Determines whether to use user mnemonic of the Port

- ``user_mnemonic``: User mnemonic of the Redundant Port.

- ``associated_egress_qos_policy_id``: ID of the Egress QoS Policy associated with this Redundant Port.

- ``status``: Status of the redundant port.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuvlan.NUVLAN<nuvlan>`                                                                                                                                     ``vlans`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nunsport.NUNSPort<nunsport>`                                                                                                                               ``ns_ports`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

