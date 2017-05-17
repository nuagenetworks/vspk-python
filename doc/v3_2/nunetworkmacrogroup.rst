.. _nunetworkmacrogroup:

nunetworkmacrogroup
===========================================

.. class:: nunetworkmacrogroup.NUNetworkMacroGroup(bambou.nurest_object.NUMetaRESTObject,):

Administrators of an enterprise can define macros that are set of IP addresses that identify enterprise networks. These macros can be used in the ACL definitions by network designers and other users to identify access restrictions towards specific enterprise networks.


Attributes
----------


- ``name`` (**Mandatory**): Name of the macro group

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the macro group

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

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


- :ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

