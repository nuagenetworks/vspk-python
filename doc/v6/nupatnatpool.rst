.. _nupatnatpool:

nupatnatpool
===========================================

.. class:: nupatnatpool.NUPATNATPool(bambou.nurest_object.NUMetaRESTObject,):

Address Translation Pools are a range of externally routable IP addresses. User or application traffic is translated prior to being forwarded across the network.


Attributes
----------


- ``ip_type``: The IP type of this Address Translation Pool. This can be DUALSTACK, IPV4 or IPV6

- ``name`` (**Mandatory**): Name of the PATNATPool

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``address_range``: Default PAT IP Address, must belong to the pool above

- ``default_patip``: Default PAT IP Address, must belong to the pool above

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``description``: A description of the PATNATPool

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``end_address_range``: Ending IP Address for the pool of available addresses for use

- ``end_source_address``: Ending Source IP Address for the pool. (Dynamic Source NAT)

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``use_uplink_ip``: Specifying if the IP address of the uplink will be used as the public IP for a defined PAT/NAT pool.

- ``associated_gateway_id``: UUID of the NSG instance this Pool is assocated with. This attribute may be auto-populated when the pool is assigned to a Network VLAN instance.

- ``associated_gateway_type``: None

- ``associated_subnet_id``: ID of the Subnet for which the information will be used to populate Source Address Range (Dynamic Source NAT).

- ``associated_vlan_id``: ID of the network port VLAN on which the pool is associated.

- ``start_address_range``: Starting IP Address for the pool of available addresses for use

- ``start_source_address``: Starting Source IP Address for the pool. (Dynamic Source NAT)

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``dynamic_source_enabled``: Set to True if the address translation pool at the address translation pool definition level




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nunatmapentry.NUNATMapEntry<nunatmapentry>`                                                                                                                ``nat_map_entries`` 
:ref:`nuaddressmap.NUAddressMap<nuaddressmap>`                                                                                                                   ``address_maps`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`                                                                                                 ``statistics_policies`` 
:ref:`nubulkstatistics.NUBulkStatistics<nubulkstatistics>`                                                                                                       ``bulk_statistics`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

