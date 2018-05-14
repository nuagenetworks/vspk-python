.. _nuvminterface:

nuvminterface
===========================================

.. class:: nuvminterface.NUVMInterface(bambou.nurest_object.NUMetaRESTObject,):

Read only API that can retrieve the VM interface associated with a domain, zone or subnet for mediation created VM's for REST created  VM interfaces you need to set the additional proxy header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example :bob@Alcatel Lucent), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header.


Attributes
----------


- ``mac``: MAC address of the  interface

- ``vmuuid``: UUID of the associated virtual machine

- ``ip_address``: IP address of the  interface

- ``vport_id``: ID of the vport that the interface is attached to

- ``vport_name``: Name of the vport that the VM is attached to

- ``ipv6_address``: IPv6 address of the  interface

- ``ipv6_gateway``: IPV6 Gateway of the subnet that the VM is connected to

- ``name``: Device name associated with this interface

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway``: Gateway of the subnet that the VM is connected to

- ``netmask``: Netmask of the subnet that the VM is attached to

- ``network_name``: Name of the network that the VM is attached to

- ``tier_id``: ID of the tier that the interface is attached to.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_decision_id``: The policy decision ID for this particular  interface

- ``domain_id``: ID of the domain that the VM is attached to

- ``domain_name``: Name of the domain that the VM is attached to

- ``zone_id``: ID of the zone that the interface is attached to

- ``zone_name``: Name of the zone that the VM is attached to

- ``associated_floating_ip_address``: Floating Ip Address of this network interface eg: 10.1.2.1

- ``attached_network_id``: ID of the l2 domain or Subnet that the VM is attached to

- ``attached_network_type``: l2 domain or Subnet that the interface is attached to

- ``multi_nic_vport_name``: Name of the Multi NIC VPort associated with this VM Interface

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nutca.NUTCA<nutca>`                                                                                                                                        ``tcas`` 
:ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`                                                                                              ``redirection_targets`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`                                                                                                                   ``dhcp_options`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nupolicydecision.NUPolicyDecision<nupolicydecision>`                                                                                                       ``policy_decisions`` 
:ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`                                                                                                                ``policy_groups`` 
:ref:`nustaticroute.NUStaticRoute<nustaticroute>`                                                                                                                ``static_routes`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`                                                                                        ``multi_cast_channel_maps`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuvm.NUVM<nuvm>`

