.. _nuegressprofile:

nuegressprofile
===========================================

.. class:: nuegressprofile.NUEgressProfile(bambou.nurest_object.NUMetaRESTObject,):

An Egress Profile represents an aggregation of IP, MAC and egress QoS profiles that are applied on a VPort instance.


Attributes
----------


- ``name``: A customer friendly name for the Egress Profile entity.

- ``description``: A customer friendly description of the Egress Profile entity.

- ``associated_ip_filter_profile_id``: UUID of the associated IP Filter Profile entity.

- ``associated_ip_filter_profile_name``: Name of the associated IP Filter Profile entity.

- ``associated_ipv6_filter_profile_id``: UUID of the associated IPv6 Filter Profile entity.

- ``associated_ipv6_filter_profile_name``: Name of the associated IPv6 Filter Profile entity.

- ``associated_mac_filter_profile_id``: UUID of the associated MAC Filter Profile entity.

- ``associated_mac_filter_profile_name``: Name of the associated MAC Filter Profile entity.

- ``associated_sap_egress_qo_s_profile_id``: UUID of the associated SAP Egress QoS Profile entity.

- ``associated_sap_egress_qo_s_profile_name``: Name of the associated SAP Egress QoS Profile entity.




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

