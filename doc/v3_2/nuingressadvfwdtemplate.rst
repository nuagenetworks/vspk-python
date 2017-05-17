.. _nuingressadvfwdtemplate:

nuingressadvfwdtemplate
===========================================

.. class:: nuingressadvfwdtemplate.NUIngressAdvFwdTemplate(bambou.nurest_object.NUMetaRESTObject,):

Defines the template for an Ingress Advanced Forwarding.


Attributes
----------


- ``name``: The name of the entity

- ``last_updated_by``: ID of the user who last updated the object.

- ``active``: If enabled, it means that this ACL or QOS entry is active

- ``description``: A description of the entity

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_state``: 

- ``priority``: The priority of the ACL entry that determines the order of entries

- ``priority_type``: 

- ``associated_live_entity_id``: In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`                                                                   ``ingress_adv_fwd_entry_templates`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

