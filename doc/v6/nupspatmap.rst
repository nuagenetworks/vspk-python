.. _nupspatmap:

nupspatmap
===========================================

.. class:: nupspatmap.NUPSPATMap(bambou.nurest_object.NUMetaRESTObject,):

Reserved provider SPAT IPs to be used to SPAT a collection of provider private IPs in customer domain.


Attributes
----------


- ``name`` (**Mandatory**): The name for this Bi-Directional mapping object

- ``family``: The IP type of this SPAT sources Pool, possible values are IPV4, IPV6 or DUALSTACK.

- ``last_updated_by``: ID of the user who last updated the object.

- ``reserved_spatips`` (**Mandatory**): Reserved provider SPAT IPs to be used to SPAT a collection of provider private IPs in customer domain.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_spat_sources_pool_id`` (**Mandatory**): The ID of the associated SPAT sources defined in the provider domain.

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


- :ref:`nupsnatpool.NUPSNATPool<nupsnatpool>`

