.. _nuesilmpolicy:

nuesilmpolicy
===========================================

.. class:: nuesilmpolicy.NUEsIlmPolicy(bambou.nurest_object.NUMetaRESTObject,):

An Elasticsearch Index Lifecycle Management Policy defines the phases and actions to manage the lifecycle of an ES index.


Attributes
----------


- ``name`` (**Mandatory**): A unique name of the EsIlmPolicy object

- ``warm_phase_enabled``: Enable WARM phase for the ES index

- ``warm_timer``: The number of hours after the rollover of the index until it moves to the warm phase.

- ``delete_phase_enabled``: Enable DELETE phase for the ES index

- ``delete_timer``: The number of hours after the rollover of the index until it gets deleted. This value has to be higher than the cold timer value.

- ``description``: Description of the Elasticsearch Index Lifecycle Management Policy.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``index_freeze`` (**Mandatory**): Mark the ES index as frozen when moving to the cold phase. This will freeze the index by calling the Freeze Index API.

- ``index_read_only``: Mark the ES index as readonly in the warm phase

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``cold_phase_enabled``: Enable COLD phase for the ES index.

- ``cold_timer``: The number of hours after the rollover of the index until it moves to the cold phase. This value has to be higher than the warm timer value.

- ``rollover_max_age``: The number of hours after which the index is rolled over in case it isn't rolled over based on size or number of documents.

- ``rollover_max_docs``: The number of documents after which the index is rolled over in case it isn't rolled over based on size or age.

- ``rollover_max_size``: The max size in GB after which the index is rolled over in case it isn't rolled over based on age or number of documents.

- ``force_merge_enabled``: Enable the Force Merge action for the ES index when moving to the warm phase.

- ``force_merge_max_num_segments``: Max number of segments for Force Merge

- ``es_ilm_policy_type``: The type of EsIlm Policy. 

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

