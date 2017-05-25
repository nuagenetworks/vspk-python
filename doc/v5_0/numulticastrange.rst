.. _numulticastrange:

numulticastrange
===========================================

.. class:: numulticastrange.NUMultiCastRange(bambou.nurest_object.NUMetaRESTObject,):

This is the definition of a MultiCast Range associated with a MultiCast Channel Map.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``max_address`` (**Mandatory**): Highest address in the MultiCast range

- ``min_address`` (**Mandatory**): Lowest address in the MultiCast range

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`

