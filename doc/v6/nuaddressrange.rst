.. _nuaddressrange:

nuaddressrange
===========================================

.. class:: nuaddressrange.NUAddressRange(bambou.nurest_object.NUMetaRESTObject,):

Address ranges are used for dynamic IP address allocation within the subnet. Multiple address ranges may be used to support non-contiuous IP address ranges. VMs and hosts without static IP addresses assigned will receive an address within the available ranges. 


Attributes
----------


- ``dhcp_pool_type``: DHCPPoolType is an enum that indicates if the DHCP Pool is for HOST/BRIDGE/VRRP.

- ``ip_type``: Possible values are IPV4, IPV6.

- ``last_updated_by``: ID of the user who last updated the object.

- ``max_address`` (**Mandatory**): Highest address in the address range

- ``min_address`` (**Mandatory**): Lowest address in the address range

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

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

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

