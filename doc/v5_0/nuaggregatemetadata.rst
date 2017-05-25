.. _nuaggregatemetadata:

nuaggregatemetadata
===========================================

.. class:: nuaggregatemetadata.NUAggregateMetadata(bambou.nurest_object.NUMetaRESTObject,):

Metadata associated to a entity


Attributes
----------


- ``name``: Name of the Metadata.

- ``description``: Description of the Metadata.

- ``metadata_tag_ids``: Metadata tag IDs associated with this metadata. You can filter metadata based on this attribute for example  X-Nuage-Filter: '2d6fb627-603b-421c-b63a-eb0a6d712761' IN metadataTagIDs 

- ``network_notification_disabled``: Specifies metadata changes need to be notified to controller,by default it is notified

- ``blob`` (**Mandatory**): Metadata that describes about the entity attached to it.

- ``global_metadata``: Specifies whether the metadata is global or local

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems






Parents
--------


- :ref:`nuvport.NUVPort<nuvport>`

