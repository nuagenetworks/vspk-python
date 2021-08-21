.. _nustatisticspolicy:

nustatisticspolicy
===========================================

.. class:: nustatisticspolicy.NUStatisticsPolicy(bambou.nurest_object.NUMetaRESTObject,):

Defines the frequency of statistics collection associated with an object.


Attributes
----------


- ``name`` (**Mandatory**): Name of statistics policy

- ``last_updated_by``: ID of the user who last updated the object.

- ``data_collection_frequency`` (**Mandatory**): How frequent to collect statistics in seconds

- ``description``: A description of the statistics policy

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

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


- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuaddressmap.NUAddressMap<nuaddressmap>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

