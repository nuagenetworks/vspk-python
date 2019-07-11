.. _nudestinationurl:

nudestinationurl
===========================================

.. class:: nudestinationurl.NUDestinationurl(bambou.nurest_object.NUMetaRESTObject,):

destination URL under tier


Attributes
----------


- ``url``: Uniform Resource Locator

- ``http_method``: HTTP probe method (GET/HEAD)

- ``packet_count``: packet count (part of rate along with probeInterval). Applicable only if this URL's parent is Tier1

- ``last_updated_by``: ID of the user who last updated the object.

- ``percentage_weight``: Weight of the URL in %. Applicable only when parent is Tier1

- ``timeout``: number of milliseconds to wait until the probe is timed out. Applicable only if this URL's parent is Tier1

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``down_threshold_count``: Successive Probe threshold. Applicable only if this URL's parent is Tier1

- ``probe_interval``: probe interval (part of rate along with packetCount). Applicable only if this URL's parent is Tier1

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


- :ref:`nutier.NUTier<nutier>`

