.. _nuegressprofile:

nuegressprofile
===========================================

.. class:: nuegressprofile.NUEgressProfile(bambou.nurest_object.NUMetaRESTObject,):

An Egress Profile represents an aggregation of IP, MAC and egress QoS profiles that are applied on a VPort instance.


Attributes
----------


- ``name`` (**Mandatory**): A customer friendly name for the Egress Profile entity.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A customer friendly description of the Egress Profile entity.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``assoc_entity_type``: Type of parent entity

- ``associated_ip_filter_profile_id``: UUID of the associated IP Filter Profile entity.

- ``associated_ip_filter_profile_name``: Name of the associated IP Filter Profile entity.

- ``associated_ipv6_filter_profile_id``: UUID of the associated IPv6 Filter Profile entity.

- ``associated_ipv6_filter_profile_name``: Name of the associated IPv6 Filter Profile entity.

- ``associated_mac_filter_profile_id``: UUID of the associated MAC Filter Profile entity.

- ``associated_mac_filter_profile_name``: Name of the associated MAC Filter Profile entity.

- ``associated_sap_egress_qo_s_profile_id``: UUID of the associated SAP Egress QoS Profile entity.

- ``associated_sap_egress_qo_s_profile_name``: Name of the associated SAP Egress QoS Profile entity.

- ``customer_id``: The customer ID given to parent enterprise. This is used by Netconf/Config manager.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`                                                                                              ``deployment_failures`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nuethernetsegmentgwgroup.NUEthernetSegmentGWGroup<nuethernetsegmentgwgroup>`

