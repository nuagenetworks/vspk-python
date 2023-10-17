.. _nuvnfthresholdpolicy:

nuvnfthresholdpolicy
===========================================

.. class:: nuvnfthresholdpolicy.NUVNFThresholdPolicy(bambou.nurest_object.NUMetaRESTObject,):

VNF Threshold Policy represents thresholds for resources consumed by VNF instance running on NS Gateway and action to be taken when resource utilization crosses configured thresholds.


Attributes
----------


- ``cpu_threshold``: Threshold for CPU usage

- ``name`` (**Mandatory**): Name of VNF agent policy

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``action``: Action to be taken on threshold crossover

- ``memory_threshold``: Threshold for memory usage

- ``description``: Description of VNF agent policy

- ``min_occurrence``: Minimum number of threshold crossover occurrence during monitoring interval before taking specified action

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``monit_interval``: Monitoring interval (minutes) for threshold crossover occurrences to be considered

- ``creation_date``: Time stamp when this object was created.

- ``assoc_entity_type``: Type of the entity to which the Metadata is associated to.

- ``storage_threshold``: Threshold for storage usage

- ``owner``: Identifies the user that has created this object.

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


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuvnf.NUVNF<nuvnf>`

