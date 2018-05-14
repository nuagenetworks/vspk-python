.. _nuuplinkconnection:

nuuplinkconnection
===========================================

.. class:: nuuplinkconnection.NUUplinkConnection(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``pat_enabled``: Indicates whether PAT is enabled on the underlay for this uplink connection.

- ``dns_address``: DNS server address

- ``password``: PPPoE password.

- ``gateway``: IP address of the gateway bound to the port

- ``address``: IP address for static configuration

- ``advertisement_criteria``: Advertisement Criteria for Traffic Flow

- ``secondary_address``: Secondary IP Address (Control IP Address) for Loopback. 

- ``netmask``: Subnet mask

- ``vlan_id``: The tag of the uplink's parent VLAN

- ``underlay_enabled``: Indicated whether route to underlay is enabled on this uplink connection.

- ``inherited``: This flag will determine if the abstract connection is inherited from the instance template

- ``installer_managed``: Boolean flag to indicate that connection parameters will be configured by the installer onsite. Limited to ConnectionMode: PPPoE

- ``interface_connection_type``: The way the interface is connected via the NSG.  This value depends on if the interface internal or external to the NSG.

- ``mode``: Specify how to connect to the network. Possible values: Dynamic (DHCP), Static (static configuration is required), PPPoE (pppoe configuration required), LTE (LTE configuration required). Default: Dynamic

- ``role``: To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, 

- ``role_order``: Role order: Primary 1, Primary 2, Secondary 3. Note: Order will be calculated when all uplink connections fetched for gateway

- ``port_name``: Physical port name this uplink belongs to

- ``download_rate_limit``: Download rate limit for this uplink in Mbits/sec.

- ``uplink_id``: ID that unqiuely identifies the uplink.

- ``username``: PPPoE username

- ``assoc_underlay_id``: UUID of the underlay associated to the uplink.

- ``associated_bgp_neighbor_id``: UUID of BGP Neighbor associated to the Uplink which will be used for Bootstrap. This is mandatory if a secondaryAddress is defined.

- ``associated_underlay_name``: The display name of the Underlay instance associated with this uplink connection.

- ``auxiliary_link``: Make this uplink an auxiliary one that will only come up when all other uplinks are disconnected or can't perform their role.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nubfdsession.NUBFDSession<nubfdsession>`                                                                                                                   ``bfd_sessions`` 
:ref:`nuunderlay.NUUnderlay<nuunderlay>`                                                                                                                         ``underlays`` 
:ref:`nucustomproperty.NUCustomProperty<nucustomproperty>`                                                                                                       ``custom_properties`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`

