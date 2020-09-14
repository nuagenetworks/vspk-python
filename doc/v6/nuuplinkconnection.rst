.. _nuuplinkconnection:

nuuplinkconnection
===========================================

.. class:: nuuplinkconnection.NUUplinkConnection(bambou.nurest_object.NUMetaRESTObject,):

Configuration of VNS Gateway uplinks


Attributes
----------


- ``pat_enabled``: Indicates whether PAT is enabled on the underlay for this uplink connection.

- ``dns_address``: DNS server address.

- ``dns_address_v6``: IPv6 DNS server address.

- ``password``: PPPoE password.

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway``: IP address of the gateway bound to the port

- ``gateway_v6``: IPv6 address of the gateway bound to the port.

- ``address``: IP address for static configuration

- ``address_family``: IP address family of this UplinkConnection

- ``address_v6``: IPv6 address for static configuration

- ``advertisement_criteria``: Advertisement Criteria for Traffic Flow

- ``secondary_address``: Secondary IP Address (Control IP Address) for Loopback. 

- ``netmask``: Subnet mask of the uplink connection if mode is set to Static.

- ``vlan``: VLAN Id of this uplink

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``underlay_enabled``: Indicated whether route to underlay is enabled on this uplink connection.

- ``underlay_id``: Underlay Identifier of underlay associated with this uplink.

- ``inherited``: This flag will determine if the abstract connection is inherited from the instance template

- ``installer_managed``: Boolean flag to indicate that connection parameters will be configured by the installer onsite. Limited to ConnectionMode: PPPoE

- ``interface_connection_type``: The way the interface is connected via the NSG.  This value depends on if the interface internal or external to the NSG.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``mode``: Specify how to connect to the network. Possible values: Dynamic (DHCP), Static (static configuration is required), PPPoE (pppoe configuration required), LTE (LTE configuration required). Default: Dynamic

- ``role``: To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, 

- ``role_order``: Determines the order in which uplinks are configured on NSG. It also determines the priority for an Uplink for management traffic. This value will be auto-generated when not provided by user.

- ``port_name``: Physical port name this uplink belongs to.

- ``download_rate_limit``: Download rate limit for this uplink in Mb/s.

- ``uplink_id``: ID that unqiuely identifies the uplink.

- ``primary_data_path_id``: System generated identifier of an uplink on NSG.

- ``username``: PPPoE username if uplink mode is set to PPPoE.

- ``assoc_underlay_id``: UUID of the underlay associated to the uplink.

- ``associated_bgp_neighbor_id``: UUID of BGP Neighbor associated to the Uplink which will be used for Bootstrap. This is mandatory if a secondaryAddress is defined.

- ``associated_underlay_name``: The display name of the Underlay instance associated with this uplink connection.

- ``aux_mode``: The type of redundancy this Uplink offers when marked as auxiliary link.

- ``auxiliary_link``: Make this uplink an auxiliary one that will only come up when all other uplinks are disconnected or can't perform their role.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nubfdsession.NUBFDSession<nubfdsession>`                                                                                                                   ``bfd_sessions`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nucustomproperty.NUCustomProperty<nucustomproperty>`                                                                                                       ``custom_properties`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`

