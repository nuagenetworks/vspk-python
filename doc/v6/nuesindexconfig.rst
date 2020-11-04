.. _nuesindexconfig:

nuesindexconfig
===========================================

.. class:: nuesindexconfig.NUEsIndexConfig(bambou.nurest_object.NUMetaRESTObject,):

Elasticsearch Index configuration


Attributes
----------


- ``name`` (**Mandatory**): Name of the ES Index Config.

- ``description``: Description of the ES Index Config.

- ``ilm_status``: Index Life Management Status.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``index_pattern`` (**Mandatory**): The wildcard pattern for the specific ES index

- ``index_type`` (**Mandatory**): The enum value corresponding to an ES index.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_name``: The associated EsIlmPolicy name.

- ``rollover_alias`` (**Mandatory**): The rollover alias for the specific ES index.

- ``config_status``: Configuration status of ES Config.

- ``associated_es_ilm_policy_id``: The UUID of the associated EsIlmPolicy object with ES Index Config.

- ``num_shards`` (**Mandatory**): The number of primary shards for this index.

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


- :ref:`nume.NUMe<nume>`

