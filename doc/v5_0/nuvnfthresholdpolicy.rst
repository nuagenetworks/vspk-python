.. _nuvnfthresholdpolicy:

nuvnfthresholdpolicy
===========================================

.. class:: nuvnfthresholdpolicy.NUVNFThresholdPolicy(bambou.nurest_object.NUMetaRESTObject,):

Represents thresholds for resources consumed by VNF instance running on NS Gateway and action to be taken when resource utilization crosses configured thresholds.


Attributes
----------


- ``cpu_threshold``: Threshold for CPU usage

- ``name`` (**Mandatory**): Name of VNF agent policy

- ``action``: Action to be taken on threshold crossover

- ``memory_threshold``: Threshold for memory usage

- ``description``: Description of VNF agent policy

- ``min_occurrence``: Minimum number of threshold crossover occurrence during monitoring interval before taking specified action

- ``monit_interval``: Monitoring interval (minutes) for threshold crossover occurrences to be considered

- ``storage_threshold``: Threshold for storage usage






Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

