.. _nuremotevrsinfo:

nuremotevrsinfo
===========================================

.. class:: nuremotevrsinfo.NURemoteVrsInfo(bambou.nurest_object.NUMetaRESTObject,):

Represents a VRS present in a remote DC across WAN. SRIC populates this object. This is used for NFIX(Network Function Interconnect).


Attributes
----------


- ``label_stack``: Label stack associated with the VRS

- ``last_updated_by``: ID of the user who last updated the object.

- ``next_hop``: Next hop DCGW associated with the VRS

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``color``: The color encoded with a traffic engineering constraint such as minimum latency, hops, maximum bandwidth, etc. This is used for NFIX(Network Function Interconnect).

- ``vrs_ip``: IP of the VRS/Hypervisor

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


- :ref:`nume.NUMe<nume>`

