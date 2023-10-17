.. _nuenterprisenetwork:

nuenterprisenetwork
===========================================

.. class:: nuenterprisenetwork.NUEnterpriseNetwork(bambou.nurest_object.NUMetaRESTObject,):

Network Macros are organization wide defined macros that can be used as a destination of a policy rule. For instance, you can create a network that represents your internal Intranet access, and use it as a destination of a policy rule to drop any packet that is coming from a particular port. Macros can now be created under SaaS Application Types. SaaS Application Types can then be associated to a SaaS Application Group which can be used as a destination of a policy rule.


Attributes
----------


- ``ip_type``: IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .

- ``ipv6_address``: IPv6 address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

- ``name`` (**Mandatory**): Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``address``: IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

- ``netmask``: Netmask of the subnet defined

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nunetworkmacrogroup.NUNetworkMacroGroup<nunetworkmacrogroup>`                                                                                              ``network_macro_groups`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nusaasapplicationtype.NUSaaSApplicationType<nusaasapplicationtype>`

- :ref:`nunetworkmacrogroup.NUNetworkMacroGroup<nunetworkmacrogroup>`

