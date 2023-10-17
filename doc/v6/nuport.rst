.. _nuport:

nuport
===========================================

.. class:: nuport.NUPort(bambou.nurest_object.NUMetaRESTObject,):

A port represents specific connection point of a gateway. It can be used for internal networking, like an uplink connection or a management network. It can also be used for domain's access.


Attributes
----------


- ``vlan_range``: VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

- ``name`` (**Mandatory**): Name of the Port

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``native_vlan``: Native VLAN to carry untagged traffic on this port. Applicable for Access Ports on third-party Netconf Gateways only. Possible values are 1-3967.

- ``template_id``: The ID of the template that this Port was created from

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``description``: A description of the Port

- ``physical_name`` (**Mandatory**): Identifier of the Port

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port_type`` (**Mandatory**): Type of the Port. Possible values are ACCESS, NETWORK, MANAGEMENT.

- ``routed``: Indicates if this Port is a routed interface. Applicable for Access Ports on third-party Netconf Gateways only.

- ``operational_state``: Represents Operational State of the Port. Possible values are INIT, UP, DOWN.

- ``creation_date``: Time stamp when this object was created.

- ``is_resilient``: States if this port instance is resilient (redundant).  An example would be a Multi-Chassis LAG port.

- ``use_user_mnemonic``: determines whether to use user mnemonic of the Port

- ``user_mnemonic``: user mnemonic of the Port

- ``associated_egress_qos_policy_id``: ID of the Egress QOS Policy associated with this Vlan.

- ``associated_ethernet_segment_group_id``: ID of the Ethernet Segment Group to which this Port instance may be associated to.

- ``associated_ethernet_segment_id``: Identifier of the Ethernet Segment to which this Port is associated to.

- ``associated_ethernet_segment_vlan_range``: VLAN Range of the associated Ethernet Segment. Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

- ``associated_ethernet_segment_virtual``: Indicates if associated Ethernet Segment is virtual.

- ``associated_redundant_port_id``: ID of the redundant port to which this Port instance may be associated to.

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
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nugateway.NUGateway<nugateway>`

