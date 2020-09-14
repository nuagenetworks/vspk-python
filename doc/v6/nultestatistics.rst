.. _nultestatistics:

nultestatistics
===========================================

.. class:: nultestatistics.NULtestatistics(bambou.nurest_object.NUMetaRESTObject,):

Retrieves statistical information for LTE uplinks.


Attributes
----------


- ``version``: Version of this Sequence number.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``end_time``: End time for the statistics to be retrieved

- ``start_time``: Start time for the statistics to be retrieved

- ``stats_data``: A list of statistical data returned for a selected LTE interface.  Information returned will contain the cellular signal strength and the current technology used (LTE, HSPA+, 3G, ...).




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


- :ref:`nuvlan.NUVLAN<nuvlan>`

