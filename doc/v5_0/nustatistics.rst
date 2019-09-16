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

- ``stats_data``: Contains the requested statistics data. Possible values are PACKETS_IN, BYTES_IN, PACKETS_IN_DROPPED, PACKETS_IN_ERRORS, PACKETS_OUT, BYTES_OUT, PACKETS_OUT_DROPPED, PACKETS_OUT_ERRORS, PACKETS_DROPPED_RATE_LIMIT, DISKS, MEMORY, CPU

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


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuaddressmap.NUAddressMap<nuaddressmap>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`

- :ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nunsport.NUNSPort<nunsport>`

