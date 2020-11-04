.. _nuvirtualuplink:

nuvirtualuplink
===========================================

.. class:: nuvirtualuplink.NUVirtualUplink(bambou.nurest_object.NUMetaRESTObject,):

Virtual Uplinks are entities that represent on an NSG the properties that are set for corresponding control uplink instances that are residing on the NSG RG Peer when tied together by a Shunt Link.


Attributes
----------


- ``peer_endpoint``: The physical port and VLAN endpoint hosting the peer control uplink that this virtual uplink mirrors. This is derived from the peer NSG of the Shunt Link in a redundant gateway group.

- ``peer_gateway_id``: The UUID of the peer NSG in the redundant gateway group part of the Shunt Link.

- ``peer_gateway_name``: The name of the peer NSG in the redundant gateway group part of the Shunt Link.

- ``peer_gateway_system_id``: IP format of system generated identifier of the peer NSG.

- ``peer_port_id``: The UUID of the port hosting the peer control uplink that this virtual uplink mirrors. This is derived from the peer NSG of the Shunt Link on a redundant gateway group.

- ``peer_uplink_id``: ID that unqiuely identifies the uplink. This attribute represents the configuration on the remote uplink connection that this virtual uplink mirrors.

- ``peer_vlanid``: The UUID of the VLAN in the control uplink that this virtual uplink mirrors.This is derived from the peer NSG of the Shunt Link on a redundant gateway group.

- ``shunt_endpoint``: The physical port and VLAN endpoint hosting the shunt endpoint on this Gateway.

- ``shunt_port_id``: The UUID of the shunt port on the NSG hosting the Virtual Uplink.

- ``shunt_vlanid``: The UUID of the shunt VLAN on the NSG hosting the Virtual Uplink.

- ``virtual_uplink_datapath_id``: IP format of system generated identifier of an uplink on NSG.

- ``enable_nat_probes``: If enabled, probes will be sent to other NSGs and DTLS sessions for IPSEC and VXLAN will be set up to the VSCs. If disabled, no NAT probes are sent on that uplink and no DTLS sessions are set up to the VSCs.

- ``underlay_id``: Underlay Identifier of underlay associated with the uplink mirrored by this Virtual Uplink.

- ``underlay_nat``: Indicates whether PAT is enabled on the underlay for this uplink connection. Inherits the PATEnabled attribute from remote uplink connection.

- ``underlay_name``: Name of the underlay associated with the uplink mirrored by this Virtual Uplink.

- ``underlay_routing``: Indicates whether route to underlay is enabled on the uplink connection that this Virtual uplink mirrors.

- ``role``: To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, This attribute represents the configuration on the remote uplink connection that this virtual uplink mirrors.

- ``role_order``: Determines the order in which uplinks are configured on NSG. It also determines the priority for an Uplink for management traffic. This value will be auto-generated based on the order of creation of Virtual Uplink.

- ``traffic_through_ubr_only``: If enabled, cuts down the number of probes to just the number of provisioned UBRs. This attribute represents "             + "the configuration on the remote uplink connection that this virtual uplink mirrors.

- ``associated_egress_qo_s_policy_id``: ID of the Egress QoS Policy associated with remote VlLAN.

- ``associated_ingress_overlay_qo_s_policer_id``: ID of the Ingress Overlay QoS Policer associated with the remote VlLAN.

- ``associated_ingress_qo_s_policy_id``: ID of the Ingress QoS Policy / Tunnel Shaper associated with the remote VLAN.

- ``associated_ingress_underlay_qo_s_policer_id``: ID of the Ingress Underlay QoS Policer associated with the remote VLAN.

- ``associated_uplink_connection_id``: UUID of the uplink connection from the peer NSG that this virtual uplink mirrors.

- ``associated_vsc_profile_id``: The associated VSC profile of remote control uplink.

- ``aux_mode``: Type of redundancy offered by the Uplink that is mirrored by this Virtual uplink when marked as auxiliary.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuikegatewayconnection.NUIKEGatewayConnection<nuikegatewayconnection>`                                                                                     ``ike_gateway_connections`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nushuntlink.NUShuntLink<nushuntlink>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

