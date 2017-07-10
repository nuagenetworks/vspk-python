.. _nuredundantport:

nuredundantport
===========================================

.. class:: nuredundantport.NURedundantPort(bambou.nurest_object.NUMetaRESTObject,):

Represents a Port under a particular gateway object or redundant group object.


Attributes
----------


- ``vlan_range`` (**Mandatory**): VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

- ``mtu``: Port MTU (Maximum Transmission Unit) :  The size in octets of the largest protocol data unit (PDU) that the layer can pass on.  The default value is normally 1500 octets for Ethernet v2 and can go up to 9198 for Jumbo Frames.

- ``name`` (**Mandatory**): Name of the Port

- ``last_updated_by``: ID of the user who last updated the object.

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``description``: A description of the Port

- ``physical_name`` (**Mandatory**): Identifier of the Port

- ``infrastructure_profile_id``: The ID of the infrastructure profile this instance is associated with.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port_peer1_id``: The master gateway peer port id.

- ``port_peer2_id``: The slave gateway peer port id.

- ``port_type`` (**Mandatory**): Type of the Port.

- ``speed``: Port Speed in Mb/s :  Supported Ethernet speeds are 10 (10Base-T), 100 (Fast-ethernet 100Base-TX), 1000 (Gigabit Ethernet 1000Base-T), 10 000 (10 Gigabit Ethernet 10GBase-X), and Auto-Negotiate.

- ``use_untagged_heartbeat_vlan``: A flag to indicate if for this redundant port an untagged heartbeat VLAN is to be used. If this is not set then will use the heartbeat VLAN set by the NS redundant group

- ``use_user_mnemonic``: determines whether to use user mnemonic of the Port

- ``user_mnemonic``: user mnemonic of the Port

- ``associated_egress_qos_policy_id``: ID of the Egress QOS Policy associated with this Vlan.

- ``status``: Status of the port.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuvlan.NUVLAN<nuvlan>`                                                                                                                                     ``vlans`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nunsport.NUNSPort<nunsport>`                                                                                                                               ``ns_ports`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

