.. _nutier:

nutier
===========================================

.. class:: nutier.NUTier(bambou.nurest_object.NUMetaRESTObject,):

When the customer creates an HTTP probe, VSD will automatically create Tier1 and Tier2 under it with default properties.


Attributes
----------


- ``packet_count``: packet count (part of rate along with probeInterval). Applicable to Tier2 type.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Descrtiption of the Tier

- ``tier_type`` (**Mandatory**): Tier type

- ``timeout``: number of milliseconds to wait until the probe is timed out. Applicable to Tier2 type.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``down_threshold_count``: Number of times the probe is allowed to retry on successive timeouts. Applicable only for TIER2

- ``probe_interval``: probe interval (part of rate along with packetCount). Applicable to Tier2 type.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nudestinationurl.NUDestinationurl<nudestinationurl>`                                                                                                       ``destinationurls`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuperformancemonitor.NUPerformanceMonitor<nuperformancemonitor>`

