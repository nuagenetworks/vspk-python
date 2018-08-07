.. _nubrconnection:

nubrconnection
===========================================

.. class:: nubrconnection.NUBRConnection(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``dns_address``: DNS Address for the vlan

- ``dns_address_v6``: DNS IPv6 Address

- ``gateway``: IP address of the gateway bound to the VLAN.

- ``gateway_v6``: IPv6 address of the gateway bound to the port.

- ``address``: Static IP address for the VLAN

- ``address_family``: IP address family of this BRConnection

- ``address_v6``: IPv6 address for static configuration.

- ``advertisement_criteria``: Advertisement Criteria for Traffic Flow

- ``netmask``: network mask

- ``inherited``: This flag will determine if the abstract connection is inherited from the instance template

- ``mode``: Connection mode: Static.

- ``uplink_id``: Internally generated ID in the range that idenitifies the uplink within the cotext of NSG




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nubfdsession.NUBFDSession<nubfdsession>`                                                                                                                   ``bfd_sessions`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`

