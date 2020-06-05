.. _nuenterprisepermission:

nuenterprisepermission
===========================================

.. class:: nuenterprisepermission.NUEnterprisePermission(bambou.nurest_object.NUMetaRESTObject,):

Represents Enterprise Permission for a CSP entity.


Attributes
----------


- ``name``: Name of the  Permission

- ``last_updated_by``: ID of the user who last updated the object.

- ``permitted_action`` (**Mandatory**): The permitted action.

- ``permitted_entity_description``: Description for the permittedEntity

- ``permitted_entity_id``: The enterprise permitted to use/extend  this Gateway

- ``permitted_entity_name``: Name of the entity for which we have given permission.

- ``permitted_entity_type``: Type of the entity for which we have given permission.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nugatewayredundantport.NUGatewayRedundantPort<nugatewayredundantport>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuredundantport.NURedundantPort<nuredundantport>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nuwanservice.NUWANService<nuwanservice>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nuethernetsegmentgroup.NUEthernetSegmentGroup<nuethernetsegmentgroup>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`nuethernetsegmentgwgroup.NUEthernetSegmentGWGroup<nuethernetsegmentgwgroup>`

- :ref:`nunsport.NUNSPort<nunsport>`

