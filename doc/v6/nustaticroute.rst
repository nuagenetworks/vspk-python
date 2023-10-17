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

- ``last_updated_date``: Time stamp when this object was last updated.

- ``address``: IP address of the route

- ``netmask``: Netmask associated with the route

- ``next_hop_ip``: IP address of the next hop. This must be a VM attached to the dVRS

- ``black_hole_enabled``: Indicates if this is a black hole static route. Applicable only when the static route type is 'NETCONF'.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``route_distinguisher``: Route distinguisher associated with the nexthop. System generates this identifier automatically

- ``creation_date``: Time stamp when this object was created.

- ``associated_fip_domain_id``: ID of the associated Secondary FIP Domain. Valid for static route of type FIP.

- ``associated_gateway_ids``: List of associated gateway IDs for static route, returned as a JSON list of strings

- ``associated_subnet_id``: UUID of Do Not Advertise Subnet

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Type flag for static-route provisioning for exit-domain (break-to-underlay) prefixes.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`                                                                                              ``deployment_failures`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

