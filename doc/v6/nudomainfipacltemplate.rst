.. _nudomainfipacltemplate:

nudomainfipacltemplate
===========================================

.. class:: nudomainfipacltemplate.NUDomainFIPAclTemplate(bambou.nurest_object.NUMetaRESTObject,):

Defines the template for an Domain Floating IP ACL


Attributes
----------


- ``name``: The name of the entity

- ``last_updated_by``: ID of the user who last updated the object.

- ``active``: If enabled, it means that this ACL or QOS entry is active

- ``default_allow_ip``: If enabled a default ACL of Allow All is added as the last entry in the list of ACL entries

- ``default_allow_non_ip``: If enabled, non ip traffic will be dropped

- ``description``: A description of the entity

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``entries``: List of Egress Domain ACL entries associated with this ACL

- ``policy_state``: State of the policy

- ``priority``: The priority of the ACL entry that determines the order of entries

- ``priority_type``: None

- ``associated_live_entity_id``: ID of the associated live entity

- ``auto_generate_priority``: If enabled, entries priority will be randomly generated between allowed range.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nudomainfipacltemplateentry.NUDomainFIPAclTemplateEntry<nudomainfipacltemplateentry>`                                                                      ``domain_fip_acl_template_entries`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nume.NUMe<nume>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

