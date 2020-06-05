.. _nupermission:

nupermission
===========================================

.. class:: nupermission.NUPermission(bambou.nurest_object.NUMetaRESTObject,):

User groups that are granted permissions for objects such as domains, zones, and subnets can see and manipulate everything within the object.


Attributes
----------


- ``name``: Name of the  Permission

- ``last_updated_by``: ID of the user who last updated the object.

- ``permitted_action``: The permitted  action to USE/EXTEND/READ/INSTANTIATE  an entity.

- ``permitted_enterprise_description``: Name of the permitted Enterprise

- ``permitted_enterprise_name``: Name of the associated Enterprise

- ``permitted_entity_id`` (**Mandatory**): The  entity ID for which this permission action is associated against.

- ``permitted_entity_name``: Name of the entity for which we have given permission.

- ``permitted_entity_type``: Type of the entity for which we have given permission.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_group_description``: Description of the Group

- ``associated_group_id``: The Group ID associated with this permission.

- ``associated_group_name``: Name of the group for which we have given permission.

- ``associated_role_description``: Description of the role asssociated with the permission

- ``associated_role_id``: ID of the associated Role

- ``associated_role_name``: Associated Role Name

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nugatewayredundantport.NUGatewayRedundantPort<nugatewayredundantport>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuredundantport.NURedundantPort<nuredundantport>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nuwanservice.NUWANService<nuwanservice>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nuethernetsegmentgroup.NUEthernetSegmentGroup<nuethernetsegmentgroup>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`nuethernetsegmentgwgroup.NUEthernetSegmentGWGroup<nuethernetsegmentgwgroup>`

- :ref:`nunsport.NUNSPort<nunsport>`

