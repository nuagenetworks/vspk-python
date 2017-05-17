.. _nuaddressrange:

nuaddressrange
===========================================

.. class:: nuaddressrange.NUAddressRange(bambou.nurest_object.NUMetaRESTObject,):

This is the definition of a Address Range associated with a Network.


Attributes
----------


- ``dhcp_pool_type``: DHCPPoolType is an enum that indicates if the DHCP Pool is for HOST/BRIDGE.

- ``last_updated_by``: ID of the user who last updated the object.

- ``max_address`` (**Mandatory**): Higest address in the address range

- ``min_address`` (**Mandatory**): Lowest address in the address range

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`

- :ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

