.. _nunetworklayout:

nunetworklayout
===========================================

.. class:: nunetworklayout.NUNetworkLayout(bambou.nurest_object.NUMetaRESTObject,):

This API defines the AS number that should be used in the data center as well as the IP address of the route reflector.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``service_type``: Identifies whether L3 or L2 services are supported.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``route_reflector_ip``: The IP address of the route reflector that can be used by the VSCs

- ``creation_date``: Time stamp when this object was created.

- ``autonomous_system_num``: The AS number associated with this data center

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




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


- :ref:`nume.NUMe<nume>`

