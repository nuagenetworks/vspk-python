.. _nuvnfinterface:

nuvnfinterface
===========================================

.. class:: nuvnfinterface.NUVNFInterface(bambou.nurest_object.NUMetaRESTObject,):

Represent VNF interface, This can not be created directly, it will be generated from VNF Interface Descriptor when VNF instance is created.


Attributes
----------


- ``mac``: MAC address of the  interface

- ``vnfuuid``: UUID of the associated VNF

- ``ip_address``: IP address of the interface

- ``vport_id``: ID of the vport that the interface is attached to

- ``vport_name``: Name of the vport that the interface is attached to

- ``ipv6_address``: IPv6 address of the  interface

- ``ipv6_gateway``: IPV6 Gateway of the subnet that the VNF is connected to.

- ``name``: Device name associated with this interface

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway``: Gateway of the subnet that the interface is connected to

- ``netmask``: Netmask of the subnet that the interface is attached to

- ``network_name``: Name of the network that the interface is attached to

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_decision_id``: The policy decision ID for this particular interface

- ``domain_id``: ID of the domain that the interface is attached to

- ``domain_name``: Name of the domain that the interface is attached to

- ``zone_id``: ID of the zone that the interface is attached to

- ``zone_name``: Name of the zone that the VM is attached to

- ``attached_network_id``: ID of the Subnet that the interface is attached to

- ``attached_network_type``: network type that the interface is attached to

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Type of VNF interface




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuvnf.NUVNF<nuvnf>`

