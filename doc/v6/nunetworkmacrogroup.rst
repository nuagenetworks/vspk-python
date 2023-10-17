.. _nunetworkmacrogroup:

nunetworkmacrogroup
===========================================

.. class:: nunetworkmacrogroup.NUNetworkMacroGroup(bambou.nurest_object.NUMetaRESTObject,):

Network Macro Groups are a collection of existing Network Macros. These groups can be used in Security Policies in order to create rules that matches multiple Network Macros.


Attributes
----------


- ``macro_group_type``: Macro Group Type.

- ``name`` (**Mandatory**): Name of the macro group

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: Description of the macro group

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``is_saa_s_type``: Determines whether this entity is specific to SaaS Breakout Feature.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`                                                                                              ``enterprise_networks`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`

- :ref:`nume.NUMe<nume>`

- :ref:`nudomain.NUDomain<nudomain>`

