.. _nuvminterface:

nuvminterface
===========================================

.. class:: nuvminterface.NUVMInterface(bambou.nurest_object.NUMetaRESTObject,):

API that can retrieve the VM interface associated with a domain, zone or subnet for mediation created VM's for REST created  VM interfaces you need to set the additional proxy header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example :bob@Nokia), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header.


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

- ``last_updated_date``: Time stamp when this object was last updated.

- ``gateway``: Gateway of the subnet that the VM is connected to

- ``netmask``: Netmask of the subnet that the VM is attached to

- ``network_name``: Name of the network that the VM is attached to

- ``tier_id``: ID of the tier that the interface is attached to.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_decision_id``: The policy decision ID for this particular  interface

- ``domain_id``: ID of the domain that the VM is attached to

- ``domain_name``: Name of the domain that the VM is attached to

- ``zone_id``: ID of the zone that the interface is attached to

- ``zone_name``: Name of the zone that the VM is attached to

- ``creation_date``: Time stamp when this object was created.

- ``attached_network_id``: ID of the l2 domain or Subnet that the VM is attached to

- ``attached_network_type``: l2 domain or Subnet that the interface is attached to

- ``multi_nic_vport_name``: Name of the Multi NIC VPort associated with this VM Interface

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nutca.NUTCA<nutca>`                                                                                                                                        ``tcas`` 
:ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`                                                                                              ``redirection_targets`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`                                                                                                                   ``dhcp_options`` 
:ref:`nudhcpv6option.NUDHCPv6Option<nudhcpv6option>`                                                                                                             ``dhcpv6_options`` 
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

- :ref:`nume.NUMe<nume>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuvm.NUVM<nuvm>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

