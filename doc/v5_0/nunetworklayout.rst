.. _nunetworklayout:

nunetworklayout
===========================================

.. class:: nunetworklayout.NUNetworkLayout(bambou.nurest_object.NUMetaRESTObject,):

This API defines the AS number that should be used in the data center as well as the IP address of the route reflector.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``service_type``: Identifies whether L3 or L2 services are supported.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``route_reflector_ip``: The IP address of the route reflector that can be used by the VSCs

- ``autonomous_system_num``: The AS number associated with this data center

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

