.. _nufirewallacl:

nufirewallacl
===========================================

.. class:: nufirewallacl.NUFirewallAcl(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``name``: The name of the entity

- ``active``: If enabled, it means that this ACL or QOS entry is active

- ``default_allow_ip``: If enabled a default ACL of Allow All is added as the last entry in thelist of ACL entries 

- ``default_allow_non_ip``: If enabled, non ip traffic will be dropped

- ``description``: A description of the entity

- ``rule_ids``: Firewall rules associated with this firewall acl.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nufirewallrule.NUFirewallRule<nufirewallrule>`                                                                                                             ``firewall_rules`` 
:ref:`nudomain.NUDomain<nudomain>`                                                                                                                               ``domains`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

