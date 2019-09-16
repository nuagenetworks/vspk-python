.. _nuvlan:

nuvlan
===========================================

.. class:: nuvlan.NUVLAN(bambou.nurest_object.NUMetaRESTObject,):

VLANs are Virtual Local Area Networks. They allow to differentiate several traffic flows inside a single Port. A VLAN with a value set to 0 can be used to tell the system to not use any tagging.


Attributes
----------


- ``value`` (**Mandatory**): value of VLAN

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway_id``: The Gateway associated with this  VLAN. This is a read only attribute

- ``readonly``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``template_id``: The ID of the template that this Port was created from

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``description``: A description of the VLAN instance.

- ``restricted``: Determines whether this entity can be used in associations with other properties.

- ``shunt_vlan``: A flag to mark this instance of a VLAN as a candidate to be a termination point of a Shunt Link.  Only VLANs residing on a Network Port can have this attribute set to true.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``vport_id``: The Vport associated with this VLAN. This is a read only attribute

- ``is_uplink``: Indicates if the VLAN is used as an uplink.

- ``use_user_mnemonic``: Determines whether to use the defined mnemonic for this VLAN instance.

- ``user_mnemonic``: User mnemonic of the VLAN instance.

- ``associated_bgp_profile_id``: The ID of the associated BGP profile

- ``associated_connection_type``: Specifies the type of Connection (uplink, BR) associated to this VLAN instance.

- ``associated_egress_qos_policy_id``: ID of the Egress QOS Policy associated with this VLAN.

- ``associated_ingress_overlay_qo_s_policer_id``: ID of the Ingress Overlay QoS Policer associated with this VLAN.

- ``associated_ingress_qos_policy_id``: ID of the Ingress QoS Policy / Tunnel Shaper associated with this VLAN.

- ``associated_ingress_underlay_qo_s_policer_id``: ID of the Ingress Underlay QoS Policer associated with this VLAN.

- ``associated_uplink_connection_id``: Associated uplink connection ID

- ``associated_vsc_profile_id``: The associated VSC profile for the uplink VLANS. This should be only be valid for the uplinks

- ``status``: Status of the VLAN.

- ``duc_vlan``: When set to true, this specifies that this VLAN instance serves as an underlay connection endpoint on an NSG-UBR gateway.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: This type marks a VLAN for its utility.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`                                                                                                                   ``patnat_pools`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`                                                                                                                ``bgp_neighbors`` 
:ref:`nuikegatewayconnection.NUIKEGatewayConnection<nuikegatewayconnection>`                                                                                     ``ike_gateway_connections`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nuuplinkconnection.NUUplinkConnection<nuuplinkconnection>`                                                                                                 ``uplink_connections`` 
:ref:`nubrconnection.NUBRConnection<nubrconnection>`                                                                                                             ``br_connections`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nultestatistics.NULtestatistics<nultestatistics>`                                                                                                          ``ltestatistics`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nugatewayredundantport.NUGatewayRedundantPort<nugatewayredundantport>`

- :ref:`nuredundantport.NURedundantPort<nuredundantport>`

- :ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nunsport.NUNSPort<nunsport>`

