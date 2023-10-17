.. _nusharednetworkresource:

nusharednetworkresource
===========================================

.. class:: nusharednetworkresource.NUSharedNetworkResource(bambou.nurest_object.NUMetaRESTObject,):

This defines shared infrastructure resources that are created by user with CSPROOT role. These resources can be used by all the enterprises in the data center for various purposes. Examples of  shared resources are public subnet, floating subnet, public L2 domain.


Attributes
----------


- ``ecmp_count``: Domain specific Equal-cost multi-path routing count, ECMPCount = 1 means no ECMP

- ``dhcp_managed``: true if DHCP is enabled else it is false. This value is always true for network resource of type PUBLIC or FLOATING.

- ``back_haul_route_distinguisher``: Backhaul route distinguisher of the shared resource. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

- ``back_haul_route_target``: Backhaul route target of the shared resource. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

- ``back_haul_vnid``: Backhaul virtual network ID of the shared resource

- ``name`` (**Mandatory**): Name of the shared resource. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway``: Gatemask configured on the shared resource

- ``gateway_mac_address``: MAC address for a public subnet or managed l2 domain

- ``access_restriction_enabled``: Boolean indicates that this shared network resource is avaiable to everyone by default or not

- ``address`` (**Mandatory**): Address configured on the shared resource

- ``permitted_action_type``: Permitted action on this shared network resource

- ``description``: Description of the shared resource

- ``netmask`` (**Mandatory**): Netmask configured on the shared resource

- ``shared_resource_parent_id``: Parent ID of the floating IP subnet to which this FIP subnet must be attached. If empty it will be created in a new domain.

- ``vn_id``: Virtual network ID of the shared resource

- ``underlay``: Indicates whether this shared subnet is in underlay or not.

- ``enterprise_id``: Enterprise that this subnet belongs to

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_route_distinguisher``: Route distinguisher configured on the shared resource. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

- ``domain_route_target``: Route target configured on the shared resource. Supported formats are: [2-byte ASN]:[4-byte value] or [4-byte ASN]:[2-byte value]

- ``uplink_gw_vlan_attachment_id``: VLAN ID to which this vport must be attached

- ``uplink_interface_ip``: IP address of the host interface

- ``uplink_interface_mac``: MAC address of the host interface

- ``uplink_vport_name``: Name of the uplink vport

- ``use_global_mac``: if this flag is enabled, the system configured globalMACAddress will be used as the gateway mac address

- ``associated_pat_mapper_id``: The ID of the PatMapper entity to which this pool is associated to.

- ``subnet_route_distinguisher``: Route distinguisher configured on the shared resource subnetwork

- ``subnet_route_target``: Route target configured on the shared resource subnetwork

- ``external_id``: External object ID. Used for integration with third party systems

- ``dynamic_pat_allocation_enabled``: Indicates if PAT Mapping is enabled for the SharedNetworkResource or not

- ``type`` (**Mandatory**): Type of the shared resource.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupatipentry.NUPATIPEntry<nupatipentry>`                                                                                                                   ``patip_entries`` 
:ref:`nuaddressrange.NUAddressRange<nuaddressrange>`                                                                                                             ``address_ranges`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`                                                                                                                   ``dhcp_options`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nuvpnconnection.NUVPNConnection<nuvpnconnection>`                                                                                                          ``vpn_connections`` 
:ref:`nustaticroute.NUStaticRoute<nustaticroute>`                                                                                                                ``static_routes`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

- :ref:`nupatmapper.NUPATMapper<nupatmapper>`

