.. _nustatistics:

nustatistics
===========================================

.. class:: nustatistics.NUStatistics(bambou.nurest_object.NUMetaRESTObject,):

Retrieves the statistics for a particular domain, zone, subnet, or VM.


Attributes
----------


- ``version``: Version of this Sequence number.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

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


- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nuaddressmap.NUAddressMap<nuaddressmap>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`

- :ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`

