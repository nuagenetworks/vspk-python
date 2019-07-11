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


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`

- :ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

- :ref:`nuaddressmap.NUAddressMap<nuaddressmap>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nunsport.NUNSPort<nunsport>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

