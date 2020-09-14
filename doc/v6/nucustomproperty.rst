.. _nucustomproperty:

nucustomproperty
===========================================

.. class:: nucustomproperty.NUCustomProperty(bambou.nurest_object.NUMetaRESTObject,):

Developed in the context of the Uplink Connection on the NSG, this API could be used for other types of objects. It is used as a collection of name-value (or key-value) pairs for custom attributes that could be used to enrich existing class instances.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``attribute_name``: The name of the custom attribute (key) used to enrich the object the customProperty instance is attached to.

- ``attribute_value``: The value assigned to the custom attribute (key) of that customProperty instance.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuuplinkconnection.NUUplinkConnection<nuuplinkconnection>`

