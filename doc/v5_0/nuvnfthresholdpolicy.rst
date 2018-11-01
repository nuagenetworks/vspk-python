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

- ``action``: Action to be taken on threshold crossover

- ``memory_threshold``: Threshold for memory usage

- ``description``: Description of VNF agent policy

- ``min_occurrence``: Minimum number of threshold crossover occurrence during monitoring interval before taking specified action

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``monit_interval``: Monitoring interval (minutes) for threshold crossover occurrences to be considered

- ``assoc_entity_type``: Type of the entity to which the Metadata is associated to.

- ``storage_threshold``: Threshold for storage usage

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

- :ref:`nuvnf.NUVNF<nuvnf>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

