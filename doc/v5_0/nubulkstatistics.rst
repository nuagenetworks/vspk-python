.. _nubulkstatistics:

nubulkstatistics
===========================================

.. class:: nubulkstatistics.NUBulkStatistics(bambou.nurest_object.NUMetaRESTObject,):

Retrieves the statistics for a particular Entity and its immediate child entity.


Attributes
----------


- ``data``: Map<TCAMetric, Long> TCAMetric is an Enum. Possible values are packets_in, bytes_in, packets_in_dropped, packets_in_errors, packets_out, bytes_out, packets_out_dropped, packeMaprs, packets_dropped_rate_limit

- ``version``: Version of this Sequence number.

- ``end_time``: End time for the statistics to be retrieved

- ``start_time``: Start time for the statistics to be retrieved

- ``number_of_data_points``: Number of data points between start time and end time




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

