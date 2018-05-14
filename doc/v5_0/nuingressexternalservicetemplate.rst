.. _nuingressexternalservicetemplate:

nuingressexternalservicetemplate
===========================================

.. class:: nuingressexternalservicetemplate.NUIngressExternalServiceTemplate(bambou.nurest_object.NUMetaRESTObject,):

Defines the template for an Ingress External Service Acls.


Attributes
----------


- ``name``: The name of the entity

- ``active``: If enabled, it means that this ACL or QOS entry is active

- ``description``: A description of the entity

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_state``: None

- ``priority``: The priority of the ACL entry that determines the order of entries

- ``priority_type``: None

- ``associated_live_entity_id``: In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuingressexternalservicetemplateentry.NUIngressExternalServiceTemplateEntry<nuingressexternalservicetemplateentry>`                                        ``ingress_external_service_template_entries`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

