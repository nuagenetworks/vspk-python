.. _nuaddressmap:

nuaddressmap
===========================================

.. class:: nuaddressmap.NUAddressMap(bambou.nurest_object.NUMetaRESTObject,):

Defines an address mapping between a private IP and a port with a public IP address and port.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``private_ip`` (**Mandatory**): Private IP address of the interface

- ``private_port``: None

- ``associated_patnat_pool_id``: Read Only - Indicates which PATNATPool this entry belongs to

- ``public_ip``: Public IP address of the interface

- ``public_port``: None

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Identifies the type of address mapping




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`                                                                                                 ``statistics_policies`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

