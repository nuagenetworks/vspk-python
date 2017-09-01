.. _nuusercontext:

nuusercontext
===========================================

.. class:: nuusercontext.NUUserContext(bambou.nurest_object.NUMetaRESTObject,):

This defines a proxy class to expose some of the configuration parameters which are required by UI


Attributes
----------


- ``aar_flow_stats_interval``: Interval for AAR flow stats

- ``aar_probe_stats_interval``: Interval for AAR probe stats

- ``vss_stats_interval``: Interval for VSS stats

- ``flow_collection_enabled``: Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires "statisticsEnabled".

- ``statistics_enabled``: This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

- ``stats_tsdb_server_address``: ip address(es) of the elastic machine





