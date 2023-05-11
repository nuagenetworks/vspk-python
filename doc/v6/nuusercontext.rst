.. _nuusercontext:

nuusercontext
===========================================

.. class:: nuusercontext.NUUserContext(bambou.nurest_object.NUMetaRESTObject,):

This defines a proxy class to expose some of the configuration parameters which are required by UI


Attributes
----------


- ``aar_flow_stats_interval``: Interval for AAR flow stats

- ``aar_probe_stats_interval``: Interval for AAR probe stats

- ``vss_feature_enabled``: Flag to indicate if VSS feature is enabled.

- ``vss_stats_interval``: Interval for VSS stats

- ``page_size``: Result size for queries

- ``maintenance_mode_enabled``: Indicates if this VSD is configured in maintenance mode. This is typically enabled during the VSD upgrade window and when enabled VSD supports only a subset of functionality.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``rbac_enabled``: Indicates wether the new RBAC feature is enabled

- ``denied_flow_collection_enabled``: When this option is selected, VSS will only store flows that are denied by security policy (implicit or explicit ACLs). This requires a valid VSS license and Flow Collection enabled.

- ``threat_intelligence_enabled``: Enables IP based threat intelligence. This requires Flow Collection to be enabled

- ``allow_enterprise_avatar_on_nsg``: When enabled, it allows Enterprise Avatar (image) to be populated on the NSGateway bootstrapping portal and blocked page notification.

- ``global_network_macro_groups_enabled``: Enables the global network macro groups feature.

- ``flow_collection_enabled``: Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires 'statisticsEnabled'.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enhanced_security_enabled``: Indicates if Enhanced Security is enabled for Routing Protocols.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``google_maps_api_key``: Google Maps API Key used to display maps on Nuage UI applications

- ``creation_date``: Time stamp when this object was created.

- ``statistics_enabled``: This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

- ``stats_database_proxy``: The location of a public proxy to statistics database server in <FQDN>:<PORT> format.

- ``stats_tsdb_server_address``: IP address(es) of the elastic machine

- ``owner``: Identifies the user that has created this object.

- ``explicit_acl_matching_enabled``: When this option is selected, VSS will only store allow/denied flows that matches explicit ingress/egress security ACL. This requires a valid VSS license and Flow Collection enabled.

- ``external_id``: External object ID. Used for integration with third party systems

- ``system_avatar_data``: URL to the avatar data configured at System Configuration. If the avatarType is URL then value of avatarData should be URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image.

- ``system_avatar_type``: The type of avatar data.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

