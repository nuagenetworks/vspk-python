.. _nuwanservice:

nuwanservice
===========================================

.. class:: nuwanservice.NUWANService(bambou.nurest_object.NUMetaRESTObject,):

Represents a WAN Service Object.


Attributes
----------


- ``wan_service_identifier`` (**Mandatory**): Identifier of the WAN Service

- ``irb_enabled``: Determines whether Integrated Routing and Bridging is enabled on the WAN Service

- ``name`` (**Mandatory**): Name of the WAN Service

- ``last_updated_by``: ID of the user who last updated the object.

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``service_policy``: Name of 7X50 Policy associated with the service

- ``service_type`` (**Mandatory**): Type of the service.

- ``description``: A description of the WAN Service

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``vn_id``: VNID of the BackHaul Subnet of L3Domain /L2Domain to which this WANService is associated

- ``enterprise_name``: The associated enterprise name.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_name``: The associated domain name.

- ``config_type``: Type of the CONFIG.

- ``orphan``: Indicates if this WAN Service is orphan or not.

- ``use_user_mnemonic``: Determines whether to use user mnemonic of the WAN Service

- ``user_mnemonic``: user mnemonic of the WAN Service

- ``associated_domain_id``: ID of the entity to which the WAN Service is attached to. This could be ID DOMAIN/L2DOMAIN

- ``associated_vpn_connect_id``: The associated vpn connect ID.

- ``tunnel_type``: Type of the tunnel.

- ``external_id``: External object ID. Used for integration with third party systems

- ``external_route_target``: Route target associated with the WAN. It is an optional parameterthat can be provided by the user




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nugateway.NUGateway<nugateway>`

