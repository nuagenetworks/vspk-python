.. _nustatisticspolicy:

nustatisticspolicy
===========================================

.. class:: nustatisticspolicy.NUStatisticsPolicy(bambou.nurest_object.NUMetaRESTObject,):

Defines the frequency of statistics collection associated with an object.


Attributes
----------


- ``name`` (**Mandatory**): Name of statistics policy

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``data_collection_frequency`` (**Mandatory**): How frequent to collect statistics in seconds

- ``description``: A description of the statistics policy

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

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


- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuaddressmap.NUAddressMap<nuaddressmap>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

