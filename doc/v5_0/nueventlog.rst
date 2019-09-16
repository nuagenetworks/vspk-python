.. _nueventlog:

nueventlog
===========================================

.. class:: nueventlog.NUEventLog(bambou.nurest_object.NUMetaRESTObject,):

The API retrieves the events related to a particular entity


Attributes
----------


- ``request_id``: Holds the unique ID generated for the REST request associated with this event.

- ``diff``: Holds the results of diff between two objects of same type.

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


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nuqos.NUQOS<nuqos>`

- :ref:`nuvirtualip.NUVirtualIP<nuvirtualip>`

- :ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nugroup.NUGroup<nugroup>`

- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`

- :ref:`nupermission.NUPermission<nupermission>`

- :ref:`nuipreservation.NUIPReservation<nuipreservation>`

- :ref:`nuredirectiontargettemplate.NURedirectionTargetTemplate<nuredirectiontargettemplate>`

- :ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`

- :ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`

- :ref:`nuvsp.NUVSP<nuvsp>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nucontainer.NUContainer<nucontainer>`

- :ref:`numetadata.NUMetadata<numetadata>`

- :ref:`nutca.NUTCA<nutca>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nustaticroute.NUStaticRoute<nustaticroute>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nulicense.NULicense<nulicense>`

- :ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`numulticastrange.NUMultiCastRange<numulticastrange>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nuwanservice.NUWANService<nuwanservice>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nussidconnection.NUSSIDConnection<nussidconnection>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nudhcpoption.NUDHCPOption<nudhcpoption>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nuzonetemplate.NUZoneTemplate<nuzonetemplate>`

- :ref:`nuvsd.NUVSD<nuvsd>`

- :ref:`nupublicnetworkmacro.NUPublicNetworkMacro<nupublicnetworkmacro>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nuaddressrange.NUAddressRange<nuaddressrange>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nuvm.NUVM<nuvm>`

- :ref:`nufloatingip.NUFloatingIp<nufloatingip>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`

- :ref:`nupolicygrouptemplate.NUPolicyGroupTemplate<nupolicygrouptemplate>`

- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

