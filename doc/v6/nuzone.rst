.. _nuzone:

nuzone
===========================================

.. class:: nuzone.NUZone(bambou.nurest_object.NUMetaRESTObject,):

The zone is a collection of subnets attached to a domain. The zone concept enables the definition of policies for collections of subnets.


Attributes
----------


- ``dpi``: determines whether or not Deep packet inspection is enabled

- ``ip_type``: IPv4 or IPv6

- ``ipv6_address``: IPv6 address range of the zone. This is an optional field that allows users to allocate an address range to a zone. The VSD will auto-assign IP ranges to subnets from this range if an IP range is not defined for a subnet.

- ``maintenance_mode``: Indicates if the Zone is accepting VM activation requests.

- ``name`` (**Mandatory**): Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``address``: IPv4 address range of the zone. This is an optional field that allows users to allocate an address range to a zone. The VSD will auto-assign IP ranges to subnets from this range if an IP range is not defined for a subnet.

- ``template_id``: The ID of the template that this zone was derived from

- ``description``: A description of the zone

- ``netmask``: Netmask of the subnet defined

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``encryption``: Determines whether or not IPSEC is enabled.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_group_id``: PG ID for the subnet. This is unique per domain and will be in the range 1-4095

- ``associated_multicast_channel_map_id``: The ID of the Multi Cast Channel Map  this zone/zone template is associated with. This has to be set when  enableMultiCast is set to ENABLED

- ``public_zone``: If a zone is marked as public, then it is lined to the public network associated with this data center

- ``multicast``: Indicates multicast policy on zone.

- ``number_of_hosts_in_subnets``: Number of hosts in each of the subnets that can be created under a zone and are auto-assigned IP addresses

- ``external_id``: External object ID. Used for integration with third party systems

- ``dynamic_ipv6_address``: Turn on or off dynamic allocation of IPV6 address




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nutca.NUTCA<nutca>`                                                                                                                                        ``tcas`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`                                                                                                                   ``dhcp_options`` 
:ref:`nudhcpv6option.NUDHCPv6Option<nudhcpv6option>`                                                                                                             ``dhcpv6_options`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nuvminterface.NUVMInterface<nuvminterface>`                                                                                                                ``vm_interfaces`` 
:ref:`nucontainer.NUContainer<nucontainer>`                                                                                                                      ``containers`` 
:ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`                                                                                           ``container_interfaces`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
:ref:`nugroup.NUGroup<nugroup>`                                                                                                                                  ``groups`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`                                                                                                 ``statistics_policies`` 
:ref:`nusubnet.NUSubnet<nusubnet>`                                                                                                                               ``subnets`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nume.NUMe<nume>`

- :ref:`nudomain.NUDomain<nudomain>`

