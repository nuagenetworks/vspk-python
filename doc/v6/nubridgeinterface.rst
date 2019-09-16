.. _nubridgeinterface:

nubridgeinterface
===========================================

.. class:: nubridgeinterface.NUBridgeInterface(bambou.nurest_object.NUMetaRESTObject,):

Provides information for each bridge interface.


Attributes
----------


- ``vport_id``: ID of the vport that the interface is attached to

- ``vport_name``: Name of the vport that the VM is attached to

- ``ipv6_gateway``: IPV6 Gateway of the subnet that the Bridge is connected to

- ``name``: Device name associated with this interface

- ``last_updated_by``: ID of the user who last updated the object.

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

- ``zone_name``: Name of the zone that the VM is attached to.

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
:ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`                                                                                              ``deployment_failures`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`                                                                                                                   ``dhcp_options`` 
:ref:`nudhcpv6option.NUDHCPv6Option<nudhcpv6option>`                                                                                                             ``dhcpv6_options`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nupolicydecision.NUPolicyDecision<nupolicydecision>`                                                                                                       ``policy_decisions`` 
:ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`                                                                                                                ``policy_groups`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

