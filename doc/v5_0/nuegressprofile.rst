.. _nuegressprofile:

nuegressprofile
===========================================

.. class:: nuegressprofile.NUEgressProfile(bambou.nurest_object.NUMetaRESTObject,):

An Egress Profile represents an aggregation of IP, MAC and egress QoS profiles that are applied on a VPort instance.


Attributes
----------


- ``name``: A customer friendly name for the Egress Profile entity.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A customer friendly description of the Egress Profile entity.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``assoc_entity_type``: Type of parent entity

- ``associated_ip_filter_profile_id``: UUID of the associated IP Filter Profile entity.

- ``associated_ip_filter_profile_name``: Name of the associated IP Filter Profile entity.

- ``associated_ipv6_filter_profile_id``: UUID of the associated IPv6 Filter Profile entity.

- ``associated_ipv6_filter_profile_name``: Name of the associated IPv6 Filter Profile entity.

- ``associated_mac_filter_profile_id``: UUID of the associated MAC Filter Profile entity.

- ``associated_mac_filter_profile_name``: Name of the associated MAC Filter Profile entity.

- ``associated_sap_egress_qo_s_profile_id``: UUID of the associated SAP Egress QoS Profile entity.

- ``associated_sap_egress_qo_s_profile_name``: Name of the associated SAP Egress QoS Profile entity.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`                                                                                              ``deployment_failures`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nugateway.NUGateway<nugateway>`

