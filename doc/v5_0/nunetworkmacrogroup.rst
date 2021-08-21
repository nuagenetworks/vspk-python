.. _nunetworkmacrogroup:

nunetworkmacrogroup
===========================================

.. class:: nunetworkmacrogroup.NUNetworkMacroGroup(bambou.nurest_object.NUMetaRESTObject,):

Network Macro Groups are a collection of existing Network Macros. These groups can be used in Security Policies in order to create rules that matches multiple Network Macros.


Attributes
----------


- ``name`` (**Mandatory**): Name of the macro group

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the macro group

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``is_saa_s_type``: Determines whether this entity is specific to SaaS Breakout Feature.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`                                                                                              ``enterprise_networks`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`

