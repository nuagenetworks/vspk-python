.. _nuvpnconnection:

nuvpnconnection
===========================================

.. class:: nuvpnconnection.NUVPNConnection(bambou.nurest_object.NUMetaRESTObject,):

This is the definition of a VPN Connect which holds the PE service assocaition with a DOMAIN.


Attributes
----------


- ``name`` (**Mandatory**): Name of the VPNConnect

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description of the VPNConnect

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_wan_service_id``: Assosciated WAN Service

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


- :ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

