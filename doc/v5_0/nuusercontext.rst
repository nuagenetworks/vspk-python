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

- ``last_updated_by``: ID of the user who last updated the object.

- ``flow_collection_enabled``: Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires 'statisticsEnabled'.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``google_maps_api_key``: Google Maps API Key used to display maps on Nuage UI applications

- ``statistics_enabled``: This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

- ``stats_database_proxy``: The location of a public proxy to statistics database server in <FQDN>:<PORT> format.

- ``stats_tsdb_server_address``: IP address(es) of the elastic machine

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

