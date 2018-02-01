.. _nustaticroute:

nustaticroute
===========================================

.. class:: nustaticroute.NUStaticRoute(bambou.nurest_object.NUMetaRESTObject,):

Static routes allow end users to define how traffic is routed through the dVRS in addition to the routes learned by VSC through VM activation. By using static routes, end users can define for example that all traffic with a destination address towards a specific subnet must be forwarded to a specific VM attached in the dVRS and this VM could be a firewall


Attributes
----------


- ``bfd_enabled``: Enable or disable Bidirectional Forwarding Detection for this static route

- ``ip_type``: IPv4 or IPv6

- ``ipv6_address``: IPv6 address of the route

- ``last_updated_by``: ID of the user who last updated the object.

- ``address`` (**Mandatory**): IP address of the route

- ``netmask`` (**Mandatory**): Netmask associated with the route

- ``next_hop_ip`` (**Mandatory**): IP address of the next hop. This must be a VM attached to the dVRS

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``route_distinguisher``: Route distinguisher associated with the nexthop. System generates this identifier automatically

- ``associated_subnet_id``: UUID of Do Not Advertise Subnet

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Type flag for static-route provisioning for exit-domain (break-to-underlay) prefixes.




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


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nume.NUMe<nume>`

