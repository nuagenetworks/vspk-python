.. _nuvnfinterface:

nuvnfinterface
===========================================

.. class:: nuvnfinterface.NUVNFInterface(bambou.nurest_object.NUMetaRESTObject,):

Represent VNF interface, This can not be created directly, it will be generated from VNF Interface Descriptor when VNF instance is created.


Attributes
----------


- ``mac``: MAC address of the  interface

- ``vnfuuid``: UUID of the associated VNF

- ``ip_address``: IP address of the  interface

- ``vport_id``: ID of the vport that the interface is attached to

- ``vport_name``: Name of the vport that the interface is attached to

- ``name``: Device name associated with this interface

- ``gateway``: Gateway of the subnet that the interface is connected to

- ``netmask``: Netmask of the subnet that the interface is attached to

- ``network_name``: Name of the network that the interface is attached to

- ``policy_decision_id``: The policy decision ID for this particular interface

- ``domain_id``: ID of the domain that the interface is attached to

- ``domain_name``: Name of the domain that the interface is attached to

- ``zone_id``: ID of the zone that the interface is attached to

- ``zone_name``: Name of the zone that the VM is attached to

- ``is_management_interface``: Indicates if this is a management interface

- ``attached_network_id``: ID of the Subnet that the interface is attached to

- ``attached_network_type``: network type that the interface is attached to






Parents
--------


- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuvnf.NUVNF<nuvnf>`

