.. _nuqos:

nuqos
===========================================

.. class:: nuqos.NUQOS(bambou.nurest_object.NUMetaRESTObject,):

The object manipulates the QoS parameters attached to a domain, zone, or subnet.


Attributes
----------


- ``fip_committed_burst_size``: Committed burst size setting in kilo-bytes (kilo-octets) for FIP Shaper.

- ``fip_committed_information_rate``: Committed information rate setting in Mb/s for FIP Shaper.

- ``fip_peak_burst_size``: Peak burst size setting in kilo-bytes (kilo-octets) for FIP rate limiting.

- ``fip_peak_information_rate``: Peak rate setting for FIP rate limiting in Mb/s;

- ``fip_rate_limiting_active``: Flag the indicates whether FIP rate limiting is enabled or disabled

- ``bum_committed_burst_size``: Committed burst size setting in kilo-bytes (kilo-octets) for BUM Shaper.

- ``bum_committed_information_rate``: Committed information rate setting in Mb/s for BUM Shaper.

- ``bum_peak_burst_size``: Peak burst size setting in kilo-bytes (kilo-octets) for Broadcast/Multicast rate limiting (BUM).

- ``bum_peak_information_rate``: Peak rate setting in Mb/s for Broadcast/Multicast rate limiting 

- ``bum_rate_limiting_active``: Flag the indicates whether Broadcast/Multicast rate limiting is enabled or disabled

- ``name`` (**Mandatory**): A unique name of the QoS object

- ``last_updated_by``: ID of the user who last updated the object.

- ``rate_limiting_active``: Identifies if rate limiting must be implemented

- ``active``: If enabled, it means that this ACL or QOS entry is active

- ``peak``: Peak Information Rate :  Peak bandwidth that is allowed from each VM in Mb/s; only whole values allowed and 'INFINITY' if rate limiting is disabled.

- ``service_class``: Class of service to be used. Service classes in order of priority are A(1), B(2), C(3), D(4), E(5), F(6), G(7) and H(8) Possible values are NONE, A, B, C, D, E, F, G, H, .

- ``description``: A description of the QoS object

- ``rewrite_forwarding_class``: Specifies if the rewrite flag is set for the QoS policy / template

- ``egress_fip_committed_burst_size``: Committed burst size setting in kilo-bytes (kilo-octets) for FIP Shaper on the Egress.

- ``egress_fip_committed_information_rate``: Committed information rate setting in Mb/s for FIP Shaper on the egress side.

- ``egress_fip_peak_burst_size``: Peak burst size setting in kilo-bytes (kilo-octets) for Egress FIP rate limiting.

- ``egress_fip_peak_information_rate``: Peak rate setting for FIP rate limiting on egress in Mb/s

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``committed_burst_size``: Committed Burst Size :  Burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values are supported.

- ``committed_information_rate``: Committed Information Rate :  Committed bandwidth that is allowed from each VM in Mb/s; only whole values supported.

- ``trusted_forwarding_class``: Specifies if the trusted flag is set for the QoS policy / template

- ``assoc_qos_id``: ID of object associated with this QoS object

- ``associated_dscp_forwarding_class_table_id``: ID of the DSCP->Forwarding Class used by this Qos Policy

- ``associated_dscp_forwarding_class_table_name``: Name of the DSCP->Forwarding Class used by this Qos Policy

- ``burst``: Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values allowed and 'INFINITY' if rate limiting is disabled.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nucontainer.NUContainer<nucontainer>`                                                                                                                      ``containers`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuzonetemplate.NUZoneTemplate<nuzonetemplate>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nupolicydecision.NUPolicyDecision<nupolicydecision>`

