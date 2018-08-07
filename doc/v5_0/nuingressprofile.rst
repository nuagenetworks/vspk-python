.. _nuingressprofile:

nuingressprofile
===========================================

.. class:: nuingressprofile.NUIngressProfile(bambou.nurest_object.NUMetaRESTObject,):

An Ingress Profile represents an aggregation of IP, MAC and ingress QoS profiles that are applied on a VPort instance.


Attributes
----------


- ``name``: A customer friendly name for the Ingress Profile entity.

- ``description``: A customer friendly description of the Ingress Profile entity.

- ``associated_ip_filter_profile_id``: UUID of the associated IP Filter Profile entity.

- ``associated_ip_filter_profile_name``: Name of the associated IP Filter Profile entity.

- ``associated_ipv6_filter_profile_id``: UUID of the associated IPv6 Filter Profile entity.

- ``associated_ipv6_filter_profile_name``: Name of the associated IPv6 Filter Profile entity.

- ``associated_mac_filter_profile_id``: UUID of the associated MAC Filter Profile entity.

- ``associated_mac_filter_profile_name``: Name of the associated MAC Filter Profile entity.

- ``associated_sap_ingress_qo_s_profile_id``: UUID of the associated SAP Ingress QoS Profile entity.

- ``associated_sap_ingress_qo_s_profile_name``: Name of the associated SAP Ingress QoS Profile entity.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nugateway.NUGateway<nugateway>`

