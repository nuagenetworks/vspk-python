.. _nustatistics:

nustatistics
===========================================

.. class:: nustatistics.NUStatistics(bambou.nurest_object.NUMetaRESTObject,):

Retrieves the statistics for a particular domain, zone, subnet, or VM.


Attributes
----------


- ``version``: Version of this Sequence number.

- ``end_time``: End time for the statistics to be retrieved

- ``start_time``: Start time for the statistics to be retrieved

- ``stats_data``: Map&lt;TCAMetric, Long[]&gt; TCAMetric is an Enum. Possible values are packets_in, bytes_in, packets_in_dropped, packets_in_errors, packets_out, bytes_out, packets_out_dropped, packets_out_errors, packets_dropped_rate_limit

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


- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nutier.NUTier<nutier>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuingressexternalservicetemplateentry.NUIngressExternalServiceTemplateEntry<nuingressexternalservicetemplateentry>`

- :ref:`nuaddressmap.NUAddressMap<nuaddressmap>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`

- :ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`

