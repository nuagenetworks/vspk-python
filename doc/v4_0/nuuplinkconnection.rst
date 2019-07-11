.. _nuuplinkconnection:

nuuplinkconnection
===========================================

.. class:: nuuplinkconnection.NUUplinkConnection(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``dns_address``: DNS server address

- ``password``: PPPoE password.

- ``gateway``: IP address of the gateway bound to the port

- ``address``: IP address for static configuration

- ``advertisement_criteria``: Advertisement Criteria for Traffic Flow

- ``netmask``: Subnet mask

- ``interface_connection_type``: The way the interface is connected via the NSG.  This value depends on if the interface internal or external to the NSG.

- ``mode``: Specify how to connect to the network. Possible values: Any, Dynamic (DHCP), Static (static configuration is required), PPPoE (pppoe configuration required), LTE (LTE configuration required). Default: Dynamic

- ``role``: To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, 

- ``uplink_id``: ID that unqiuely identifies the uplink.

- ``username``: PPPoE username

- ``assoc_underlay_id``: UUID of the underlay associated to the uplink.

- ``associated_underlay_name``: The display name of the Underlay instance associated with this uplink connection.

- ``auxiliary_link``: Make this uplink an auxiliary one that will only come up when all other uplinks are disconnected or can't perform their role.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nubfdsession.NUBFDSession<nubfdsession>`                                                                                                                   ``bfd_sessions`` 
:ref:`nuunderlay.NUUnderlay<nuunderlay>`                                                                                                                         ``underlays`` 
:ref:`nucustomproperty.NUCustomProperty<nucustomproperty>`                                                                                                       ``custom_properties`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`

