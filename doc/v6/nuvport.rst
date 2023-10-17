.. _nuvport:

nuvport
===========================================

.. class:: nuvport.NUVPort(bambou.nurest_object.NUMetaRESTObject,):

VPorts are a new level in the domain hierarchy, intended to provide more granular configuration than at subnet, and also support a split workflow, where the vPort is configured and associated with a VM port (or gateway port) before the port exists.


Attributes
----------


- ``fip_ignore_default_route``: Determines whether the default Overlay route will be ignored or not when a VM has FIP so that it takes Underlay route.

- ``vlan``: VLAN number of the associated VLAN of this vport - applicable for type host or bridge

- ``vlanid``: UUID of the associated VLAN of this vport - applicable for type host or bridge

- ``dpi``: determines whether or not deep packet inspection is enabled

- ``backhaul_subnet_vnid``: Backhaul subnet VNID of the L3Domain associated with the VPort. This is exposed for Netconf manager

- ``name`` (**Mandatory**): Name of the vport. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``has_attached_interfaces``: Indicates that this vport has attached interfaces

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``gateway_mac_move_role``: Role of the gateway vport when handling MAC move errors

- ``gateway_port_name``: Gateway portname eg: eth1 - applicable for type host/bridge

- ``access_restriction_enabled``: Enable Access Restriction

- ``active``: Indicates if this vport is up or down

- ``address_spoofing`` (**Mandatory**): Indicates if address spoofing is ENABLED/DISABLED/INHERITED for this vport.

- ``peer_operational_state``: Operational state of the peer vport in multichassis lag scenario

- ``segmentation_id``: The VLAN Number (1-4095), valid only if the trunkRole is SUB_PORT

- ``segmentation_type``: The type of segmentation that is used. This must be VLAN for vports with trunkRole set to SUB_PORT. This can not be specified for a parent vport (trunkRole = PARENT_PORT)

- ``service_id``: The service ID used by the VSCs to identify the subnet associated with this vport

- ``description``: Description for this vport

- ``flow_count``: Maximum number of data flows allowed for a VPort. If "Flow Limit Enabled" parameter is ENABLED/DISABLED/INHERITED, Flow Count parameter is configured/ignored/derived from parent domain respectively.

- ``flow_limit_enabled``: Indicates if flow limit is enabled or disabled or "Flow Count" attribute is derived from the parent Domain on this VPort . Possible values are ENABLED, DISABLED or INHERITED.

- ``flow_setup_rate``: Committed flow setup rate in pps for this VPort. If Flow Setup Rate Limit parameter is ENABLED/DISABLED/INHERITED, flow setup rate parameter is configured/ignored/derived from parent domain respectively.

- ``flow_setup_rate_limit_enabled``: Indicates if flow setup rate limit is enabled or disabled or derived from parent Domain. Possible values are ENABLED, DISABLED or INHERITED.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``color``: The color encoded with a traffic engineering constraint such as minimum latency, hops, maximum bandwidth, etc. This is used for NFIX(Network Function Interconnect). Color is applicable only when associated Domain's Tunnel Type is MPLSoUDP. Valid range is 1 - 4294967295. If 0 is provided, color will be derived from the associated Domain.

- ``domain_id``: ID the Domain associated with the VPort

- ``domain_name``: Name of the Domain associated with the VPort. This is exposed for Netconf manager 

- ``domain_service_label``: Service ID of Domain.

- ``domain_vlanid``: Backhaul vlan id the L3Domain associated with the VPort. This is exposed for Netconf manager

- ``zone_id``: ID the Zone associated with the VPort

- ``routed``: Indicates if this VPort is in routed mode. Applicable for Cisco 9K only.

- ``operational_state``: Operational State of the VPort. Possible values are INIT, UP, DOWN, DEGRADED

- ``creation_date``: Time stamp when this object was created.

- ``trunk_role``: Indicates the role of the vport in trunking operations

- ``es_group_vport_infos``: Array of the embedded resource VPortInfo for each gateway member of ethernet segment group

- ``assoc_entity_id``: UUID of the entity to which the vport is associated to. This could be UUID of a SUBNET or a L2DOMAIN

- ``associated_egress_profile_id``: UUID of the Egress Profile associated with this Vport entity.

- ``associated_floating_ip_id``: Id of Floating IP address associated to this VPort

- ``associated_gateway_id``: Associated gateway ID of VPort

- ``associated_gateway_personality``: Personality of the associated Gateway

- ``associated_gateway_type``: Associated gateway type of VPort.

- ``associated_ingress_profile_id``: UUID of the Ingress Profile associated with this Vport entity.

- ``associated_multicast_channel_map_id``: The ID of the receive Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

- ``associated_ssid``: The UUID of the SSID Connection tied to this instance of a vPort.

- ``associated_secondary_f_ip_id``: ID of Secondary Floating IP address associated to this vport.

- ``associated_send_multicast_channel_map_id``: The ID of the send Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

- ``associated_trunk_id``: The trunk uuid associated with another vport of trunkRole PARENT_PORT. Can be specified only if trunkRole of this vport is SUB_PORT.

- ``sub_type``: Sub type of vport - possible values are NONE/VNF

- ``subnet_vnid``: VNID of the associated subnet or L2domain with the VPort. This is exposed for Netconf manager

- ``multi_nic_vport_id``: ID of the Multi NIC VPort associated with the VPort

- ``multicast``: Indicates multicast policy on Vport.

- ``auto_created``: Indicates if vport was auto created by the system

- ``gw_eligible``: Indicates that this vport is eligible to be given in gateway vport config request. It becomes eligible when it has properly attached host or bridge interfaces.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): Type of vport. Possible values are VM, HOST, BRIDGE, CONTAINER.

- ``system_type``: Indicates what system it is.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nutca.NUTCA<nutca>`                                                                                                                                        ``tcas`` 
:ref:`nuscheduledtestsuiterun.NUScheduledtestsuiterun<nuscheduledtestsuiterun>`                                                                                  ``scheduledtestsuiteruns`` 
:ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`                                                                                              ``redirection_targets`` 
:ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`                                                                                              ``deployment_failures`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`nutestsuiterun.NUTestSuiteRun<nutestsuiterun>`                                                                                                             ``test_suite_runs`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuaggregatemetadata.NUAggregateMetadata<nuaggregatemetadata>`                                                                                              ``aggregate_metadatas`` 
:ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`                                                                                                                ``bgp_neighbors`` 
:ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`                                                                               ``egress_acl_entry_templates`` 
:ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`                                                                                                                   ``dhcp_options`` 
:ref:`nudhcpv6option.NUDHCPv6Option<nudhcpv6option>`                                                                                                             ``dhcpv6_options`` 
:ref:`nuvirtualip.NUVirtualIP<nuvirtualip>`                                                                                                                      ``virtual_ips`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nuvminterface.NUVMInterface<nuvminterface>`                                                                                                                ``vm_interfaces`` 
:ref:`nuvnfinterface.NUVNFInterface<nuvnfinterface>`                                                                                                             ``vnf_interfaces`` 
:ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`                                                                            ``ingress_acl_entry_templates`` 
:ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`                                                                   ``ingress_adv_fwd_entry_templates`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`                                                                                                                ``policy_groups`` 
:ref:`nucontainer.NUContainer<nucontainer>`                                                                                                                      ``containers`` 
:ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`                                                                                           ``container_interfaces`` 
:ref:`nuportmapping.NUPortMapping<nuportmapping>`                                                                                                                ``port_mappings`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nuhostinterface.NUHostInterface<nuhostinterface>`                                                                                                          ``host_interfaces`` 
:ref:`nuvportmirror.NUVPortMirror<nuvportmirror>`                                                                                                                ``vport_mirrors`` 
:ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`                                                                                                    ``bridge_interfaces`` 
:ref:`nuvrs.NUVRS<nuvrs>`                                                                                                                                        ``vrss`` 
:ref:`nutrunk.NUTrunk<nutrunk>`                                                                                                                                  ``trunks`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`                                                                                                 ``statistics_policies`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nuoverlaymirrordestination.NUOverlayMirrorDestination<nuoverlaymirrordestination>`

- :ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`

- :ref:`numultinicvport.NUMultiNICVPort<numultinicvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`

- :ref:`nutrunk.NUTrunk<nutrunk>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuegressprofile.NUEgressProfile<nuegressprofile>`

- :ref:`nufloatingip.NUFloatingIp<nufloatingip>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuingressprofile.NUIngressProfile<nuingressprofile>`

