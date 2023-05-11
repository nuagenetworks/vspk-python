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

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nuqos.NUQOS<nuqos>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nuvirtualip.NUVirtualIP<nuvirtualip>`

- :ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nutca.NUTCA<nutca>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nupermission.NUPermission<nupermission>`

- :ref:`nuipreservation.NUIPReservation<nuipreservation>`

- :ref:`nuredirectiontargettemplate.NURedirectionTargetTemplate<nuredirectiontargettemplate>`

- :ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`

- :ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`

- :ref:`nugroup.NUGroup<nugroup>`

- :ref:`nuwanservice.NUWANService<nuwanservice>`

- :ref:`nuvsp.NUVSP<nuvsp>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvsd.NUVSD<nuvsd>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nucontainer.NUContainer<nucontainer>`

- :ref:`numetadata.NUMetadata<numetadata>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nustaticroute.NUStaticRoute<nustaticroute>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nulicense.NULicense<nulicense>`

- :ref:`nupolicygrouptemplate.NUPolicyGroupTemplate<nupolicygrouptemplate>`

- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nudhcpv6option.NUDHCPv6Option<nudhcpv6option>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`numulticastrange.NUMultiCastRange<numulticastrange>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nussidconnection.NUSSIDConnection<nussidconnection>`

- :ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nuzonetemplate.NUZoneTemplate<nuzonetemplate>`

- :ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`

- :ref:`nupublicnetworkmacro.NUPublicNetworkMacro<nupublicnetworkmacro>`

- :ref:`nuaddressrange.NUAddressRange<nuaddressrange>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nuvm.NUVM<nuvm>`

- :ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nufloatingip.NUFloatingIp<nufloatingip>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`

- :ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

