.. _nueventlog:

nueventlog
===========================================

.. class:: nueventlog.NUEventLog(bambou.nurest_object.NUMetaRESTObject,):

The API retrieves the events related to a particular entity


Attributes
----------


- ``request_id``: Holds the unique ID generated for the REST request associated with this event.

- ``diff``: Holds the results of diff between two objects of same type.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise``: The enterprise name of the user who triggered this event.

- ``entities``: List of entities associated with the event.

- ``entity_id``: The entity id associated with this event.

- ``entity_parent_id``: The entity parent id associated with this event. It can be null.

- ``entity_parent_type``: Event parent entity type.  Generally reported against enterprise.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``entity_type``: The entity type of this event. It may be Domain, VirtualMachine, etc.,

- ``user``: The authenticated user who triggered this event.

- ``event_received_time``: The time that event was received.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: The event type (CREATE, UPDATE or DELETE).




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nulicense.NULicense<nulicense>`

- :ref:`nupublicnetworkmacro.NUPublicNetworkMacro<nupublicnetworkmacro>`

- :ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`

- :ref:`numulticastrange.NUMultiCastRange<numulticastrange>`

- :ref:`nuipreservation.NUIPReservation<nuipreservation>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nuredirectiontargettemplate.NURedirectionTargetTemplate<nuredirectiontargettemplate>`

- :ref:`nucontainer.NUContainer<nucontainer>`

- :ref:`nufloatingip.NUFloatingIp<nufloatingip>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nuvsp.NUVSP<nuvsp>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nupolicygrouptemplate.NUPolicyGroupTemplate<nupolicygrouptemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nuvirtualip.NUVirtualIP<nuvirtualip>`

- :ref:`nustaticroute.NUStaticRoute<nustaticroute>`

- :ref:`nussidconnection.NUSSIDConnection<nussidconnection>`

- :ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`

- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nupermission.NUPermission<nupermission>`

- :ref:`nuqos.NUQOS<nuqos>`

- :ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`

- :ref:`nudhcpv6option.NUDHCPv6Option<nudhcpv6option>`

- :ref:`numetadata.NUMetadata<numetadata>`

- :ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nutca.NUTCA<nutca>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`

- :ref:`nuvm.NUVM<nuvm>`

- :ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`

- :ref:`nugroup.NUGroup<nugroup>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuwanservice.NUWANService<nuwanservice>`

- :ref:`nuvsd.NUVSD<nuvsd>`

- :ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`

- :ref:`nuaddressrange.NUAddressRange<nuaddressrange>`

- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nuzonetemplate.NUZoneTemplate<nuzonetemplate>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

