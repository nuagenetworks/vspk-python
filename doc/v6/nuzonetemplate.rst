.. _nuzonetemplate:

nuzonetemplate
===========================================

.. class:: nuzonetemplate.NUZoneTemplate(bambou.nurest_object.NUMetaRESTObject,):

As in domains and subnets, zones are derived from templates. This object provides the definition of the template.


Attributes
----------


- ``dpi``: determines whether or not Deep packet inspection is enabled

- ``ip_type``: IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .

- ``ipv6_address``: IPv6 address range of the zone. This is an optional field that allows users to allocate an address range to a zone. The VSD will auto-assign IP ranges to subnets from this range if an IP range is not defined for a subnet.

- ``name`` (**Mandatory**): Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``address``: IPv4 address range of the zone. This is an optional field that allows users to allocate an address range to a zone. The VSD will auto-assign IP ranges to subnets from this range if an IP range is not defined for a subnet.

- ``description``: A description of the Zone template

- ``netmask``: Netmask of the subnet defined

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``encryption``: Determines whether or not IPSEC is enabled.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``associated_multicast_channel_map_id``: The ID of the Multi Cast Channel Map  this zone/zone template is associated with. This has to be set when  enableMultiCast is set to ENABLED

- ``public_zone``: Identifies if the zone is a public zone, in which case any subnets associated with this zone are actually connected to the public subnet of the data center

- ``multicast``: Indicates multicast policy on zone template.

- ``number_of_hosts_in_subnets``: Number of hosts in the subnets where IP addresses are automatically assigned from the zone IP pool

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``dynamic_ipv6_address``: Turn on or off dynamic allocation of IPV6 address




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`                                                                                                       ``subnet_templates`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

