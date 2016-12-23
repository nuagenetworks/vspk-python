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

- ``mode``: Specify how to connect to the network. Possible values: Any, Dynamic (DHCP), Static (static configuration is required), PPPoE (pppoe configuration required). Default: Dynamic

- ``role``: To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, 

- ``uplink_id``: ID that unqiuely identifies the uplink. 

- ``username``: PPPoE username

- ``assoc_underlay_id``: UUID of the underlay associated to the uplink.

- ``associated_vsc_profile_id``: The ID of the infrastructure VSC profile this is associated with this instance of a vlan or vlan template.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuunderlay.NUUnderlay<nuunderlay>`                                                                                                                         ``underlays`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`

