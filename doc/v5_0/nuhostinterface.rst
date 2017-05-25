.. _nuhostinterface:

nuhostinterface
===========================================

.. class:: nuhostinterface.NUHostInterface(bambou.nurest_object.NUMetaRESTObject,):

Provides information for each host interface.


Attributes
----------


- ``mac``: MAC address of the  interface, cannot be modified after creation.

- ``ip_address``: IP address of the  interface

- ``vport_id``: ID of the vport that the interface is attached to

- ``vport_name``: Name of the vport that the VM is attached to

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
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nustaticroute.NUStaticRoute<nustaticroute>`                                                                                                                ``static_routes`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`                                                                                        ``multi_cast_channel_maps`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nume.NUMe<nume>`

