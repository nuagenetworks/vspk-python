.. _nunetconfprofile:

nunetconfprofile
===========================================

.. class:: nunetconfprofile.NUNetconfProfile(bambou.nurest_object.NUMetaRESTObject,):

Represents configuration to access device using Netconf protocol


Attributes
----------


- ``name`` (**Mandatory**): Name of the Netconf Profile entity.

- ``password`` (**Mandatory**): The password used to establish Netconf sessions with the gateway instances using this Netconf Profile.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A detailed description of the Netconf Profile entity.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port``: Netconf session port

- ``user_name`` (**Mandatory**): The user name used to establish Netconf sessions with the gateway instances using this Netconf Profile.

- ``assoc_entity_type``: Type of the entity to which the Profile belongs to.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

