.. _nufirewallacl:

nufirewallacl
===========================================

.. class:: nufirewallacl.NUFirewallAcl(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``name``: The name of the entity

- ``last_updated_by``: ID of the user who last updated the object.

- ``active``: If enabled, it means that this ACL or QOS entry is active

- ``default_allow_ip``: If enabled a default ACL of Allow All is added as the last entry in thelist of ACL entries 

- ``default_allow_non_ip``: If enabled, non ip traffic will be dropped

- ``description``: A description of the entity

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``rule_ids``: Firewall rules associated with this firewall acl.

- ``auto_generate_priority``: If enabled, entries priority will be randomly generated between allowed range.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nufirewallrule.NUFirewallRule<nufirewallrule>`                                                                                                             ``firewall_rules`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nudomain.NUDomain<nudomain>`                                                                                                                               ``domains`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nudomain.NUDomain<nudomain>`

