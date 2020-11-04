.. _nugnmiprofile:

nugnmiprofile
===========================================

.. class:: nugnmiprofile.NUGNMIProfile(bambou.nurest_object.NUMetaRESTObject,):

Represents configuration to access device using gNMI protocol


Attributes
----------


- ``name`` (**Mandatory**): Name of the GNMI Profile entity.

- ``password`` (**Mandatory**): The password used to establish GNMI sessions with the gateway instances using this GNMI Profile.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A detailed description of the GNMI Profile entity.

- ``key_alias``: Key alias name in keystore to connect device using TLS

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port``: GNMI session port

- ``creation_date``: Time stamp when this object was created.

- ``user_name`` (**Mandatory**): The user name used to establish GNMI sessions with the gateway instances using this GNMI Profile.

- ``assoc_entity_type``: Type of the entity to which the Profile belongs to.

- ``owner``: Identifies the user that has created this object.

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


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

