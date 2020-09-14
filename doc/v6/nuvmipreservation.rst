.. _nuvmipreservation:

nuvmipreservation
===========================================

.. class:: nuvmipreservation.NUVMIPReservation(bambou.nurest_object.NUMetaRESTObject,):

VM IP Reservation under Subnet/L2Domain.


Attributes
----------


- ``ip_type``: Specify if the VM IP Reservation is of type IPv6, IPv4 or DualStack. If not specified, it is derived from the Subnet/L2Domain

- ``ipv4_address``: IPv4 Address associated with this VM IP Reservation.

- ``ipv6_address``: IPv6 Address associated with this VM IP Reservation.

- ``ipv6_allocation_pools``: Collection of IPv6 address ranges to consider for reservation.

- ``last_updated_by``: ID of the user who last updated the object.

- ``allocation_pools``: Collection of IPv4 address ranges to consider for reservation.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``state``: This indicates the state of this VM IP Reservation. Possible values are 'ASSIGNED', 'ASSIGNED_DELETE_PENDING', 'UNASSIGNED'.

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


- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

