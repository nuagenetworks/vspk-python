.. _nuvlan:

nuvlan
===========================================

.. class:: nuvlan.NUVLAN(bambou.nurest_object.NUMetaRESTObject,):

Represents VLAN object under a given Port object.


Attributes
----------


- ``value`` (**Mandatory**): value of VLAN

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway_id``: The Gateway associated with this  VLAN  . This is a read only attribute

- ``readonly``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``template_id``: The ID of the template that this Port was created from

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``description``: A description of the Port

- ``restricted``: Determines whether this entity can be used in associations with other properties.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``vport_id``: The Vport associated with this  VLAN  . This is a read only attribute

- ``use_user_mnemonic``: determines whether to use user mnemonic of the Port

- ``user_mnemonic``: user mnemonic of the Port

- ``associated_bgp_profile_id``: The ID of the associated BGP profile

- ``associated_egress_qos_policy_id``: ID of the Egress QOS Policy associated with this VLAN.

- ``associated_uplink_connection_id``: Associated uplink connection ID

- ``associated_vsc_profile_id``: The associated VSC profile for the uplink VLANS. This should be only be valid for the uplinks

- ``status``: Status of the VLAN.

- ``duc_vlan``: When set to true, this specifies that this VLAN instance serves as an underlay connection endpoint on an NSG-UBR gateway.

- ``external_id``: External object ID. Used for integration with third party systems




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
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`

- :ref:`nuredundantport.NURedundantPort<nuredundantport>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nunsport.NUNSPort<nunsport>`

