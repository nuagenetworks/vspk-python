.. _nusubnettemplate:

nusubnettemplate
===========================================

.. class:: nusubnettemplate.NUSubnetTemplate(bambou.nurest_object.NUMetaRESTObject,):

As domain and zone objects, subnet objects are created in VSD as derived by templates. This object describes the subnet template.


Attributes
----------


- ``dpi``: determines whether or not Deep packet inspection is enabled

- ``ip_type``: IPv4 or DUALSTACK

- ``ipv6_gateway``: The IPv6 address of the gateway of this subnet

- ``ipv6address``: IPv6 address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

- ``name`` (**Mandatory**): Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway``: The IP address of the gateway of this subnet

- ``address`` (**Mandatory**): IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

- ``description``: A description field provided by the user that identifies the subnet

- ``netmask`` (**Mandatory**): Netmask of the subnet defined

- ``encryption``: Determines whether or not IPSEC is enabled. Possible values are INHERITED, ENABLED, DISABLED, .

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``split_subnet``: Need to add correct description

- ``proxy_arp``:  when set VRS will act as  ARP Proxy

- ``use_global_mac``: if this flag is enabled, the system configured globalMACAddress will be used as the gateway mac address

- ``associated_multicast_channel_map_id``: The ID of the Multi Cast Channel Map  this Subnet/Subnet Template is associated with. This has to be set when enableMultiCast is set to ENABLED

- ``multicast``: Indicates multicast policy on Subnet/Subnet Template.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuaddressrange.NUAddressRange<nuaddressrange>`                                                                                                             ``address_ranges`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nusubnet.NUSubnet<nusubnet>`                                                                                                                               ``subnets`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuzonetemplate.NUZoneTemplate<nuzonetemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

