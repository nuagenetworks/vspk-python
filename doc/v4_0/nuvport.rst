.. _nuvport:

nuvport
===========================================

.. class:: nuvport.NUVPort(bambou.nurest_object.NUMetaRESTObject,):

VPorts are a new level in the domain hierarchy, intended to provide more granular configuration than at subnet, and also support a split workflow, where the vPort is configured and associated with a VM port (or gateway port) before the port exists.


Attributes
----------


- ``vlanid``: associated Vlan of this vport - applicable for type host/bridge

- ``dpi``: determines whether or not Deep packet inspection is enabled

- ``name`` (**Mandatory**): Name of the vport. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``has_attached_interfaces``: Indicates that this vport has attached interfaces

- ``last_updated_by``: ID of the user who last updated the object.

- ``active``: Indicates if this vport is up or down

- ``address_spoofing`` (**Mandatory**): Indicates if address spoofing is ENABLED/DISABLED/INHERITED for this vport.

- ``description``: Description for this vport

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_id``: ID the Domain associated with the VPort

- ``zone_id``: ID the Zone associated with the VPort

- ``operational_state``: Operational State of the VPort. Possible values are INIT, UP, DOWN.

- ``associated_floating_ip_id``: Id of Floating IP address associated to this vport

- ``associated_multicast_channel_map_id``: The ID of the receive Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

- ``associated_send_multicast_channel_map_id``: The ID of the send Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

- ``multi_nic_vport_id``: ID of the Multi NIC VPort associated with the VPort

- ``multicast``: Indicates multicast policy on Vport.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): Type of vport. Possible values are VM, HOST, BRIDGE, CONTAINER.

- ``system_type``: Indicates what system it is.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nutca.NUTCA<nutca>`                                                                                                                                        ``tcas`` 
:ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`                                                                                              ``redirection_targets`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuaggregatemetadata.NUAggregateMetadata<nuaggregatemetadata>`                                                                                              ``aggregate_metadatas`` 
:ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`                                                                                                                ``bgp_neighbors`` 
:ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`                                                                                                                   ``dhcp_options`` 
:ref:`nuvirtualip.NUVirtualIP<nuvirtualip>`                                                                                                                      ``virtual_ips`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nuvminterface.NUVMInterface<nuvminterface>`                                                                                                                ``vm_interfaces`` 
:ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`                                                                                                                ``policy_groups`` 
:ref:`nucontainer.NUContainer<nucontainer>`                                                                                                                      ``containers`` 
:ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`                                                                                           ``container_interfaces`` 
:ref:`nuportmapping.NUPortMapping<nuportmapping>`                                                                                                                ``port_mappings`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nuhostinterface.NUHostInterface<nuhostinterface>`                                                                                                          ``host_interfaces`` 
:ref:`nuvportmirror.NUVPortMirror<nuvportmirror>`                                                                                                                ``vport_mirrors`` 
:ref:`nuapplicationperformancemanagement.NUApplicationperformancemanagement<nuapplicationperformancemanagement>`                                                 ``applicationperformancemanagements`` 
:ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`                                                                                                    ``bridge_interfaces`` 
:ref:`nuvrs.NUVRS<nuvrs>`                                                                                                                                        ``vrss`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`                                                                                                 ``statistics_policies`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nutier.NUTier<nutier>`

- :ref:`numultinicvport.NUMultiNICVPort<numultinicvport>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nufloatingip.NUFloatingIp<nufloatingip>`

