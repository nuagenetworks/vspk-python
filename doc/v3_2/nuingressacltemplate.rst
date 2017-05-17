.. _nuingressacltemplate:

nuingressacltemplate
===========================================

.. class:: nuingressacltemplate.NUIngressACLTemplate(bambou.nurest_object.NUMetaRESTObject,):

Defines the template for an Ingress ACL.


Attributes
----------


- ``name`` (**Mandatory**): The name of the entity

- ``last_updated_by``: ID of the user who last updated the object.

- ``active``: If enabled, it means that this ACL or QOS entry is active

- ``default_allow_ip``: If enabled a default ACL of Allow All is added as the last entry in the list of ACL entries

- ``default_allow_non_ip``: If enabled, non ip traffic will be dropped

- ``description``: A description of the entity

- ``allow_l2_address_spoof``: If enabled, it will disable the default anti-spoof ACL for this domain that essentially prevents any VM to send packets that do not originate from that particular VM

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_state``: 

- ``priority``: The priority of the ACL entry that determines the order of entries

- ``priority_type``: 

- ``assoc_acl_template_id``: ID of the ACL template associated with this ACL template

- ``associated_live_entity_id``: In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`                                                                            ``ingress_acl_entry_templates`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nume.NUMe<nume>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

