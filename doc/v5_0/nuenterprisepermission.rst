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

- :ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nuport.NUPort<nuport>`

- :ref:`nuwanservice.NUWANService<nuwanservice>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

