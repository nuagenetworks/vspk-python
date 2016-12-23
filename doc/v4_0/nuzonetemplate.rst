.. _nuzonetemplate:

nuzonetemplate
===========================================

.. class:: nuzonetemplate.NUZoneTemplate(bambou.nurest_object.NUMetaRESTObject,):

As in domains and subnets, zones are derived from templates. This object provides the definition of the template.


Attributes
----------


- ``dpi``: determines whether or not Deep packet inspection is enabled

- ``ip_type``: IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .

- ``name`` (**Mandatory**): Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``address``: IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

- ``description``: A description of the Zone template

- ``netmask``: Netmask of the subnet defined

- ``encryption``: Determines whether or not IPSEC is enabled.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_multicast_channel_map_id``: The ID of the Multi Cast Channel Map  this zone/zone template is associated with. This has to be set when  enableMultiCast is set to ENABLED

- ``public_zone``: Identifies if the zone is a public zone, in which case any subnets associated with this zone are actually connected to the public subnet of the data center

- ``multicast``: Indicates multicast policy on zone template.

- ``number_of_hosts_in_subnets``: Number of hosts in the subnets where IP addresses are automatically assigned from the zone IP pool

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`                                                                                                       ``subnet_templates`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

