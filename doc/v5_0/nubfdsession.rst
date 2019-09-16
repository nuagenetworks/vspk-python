.. _nubfdsession:

nubfdsession
===========================================

.. class:: nubfdsession.NUBFDSession(bambou.nurest_object.NUMetaRESTObject,):

Represents the Bidirectional Forwarding Detection session that can be configured on an uplink/BR connection.


Attributes
----------


- ``bfd_destination_ip``: Destination IP Address used for Bidirectional Forwarding Detection.

- ``bfd_destination_ip_type``: Destination IP Type of Bidirectional Forwarding Detection

- ``bfd_destination_ipv6``: Destination IPv6 Address used for Bidirectional Forwarding Detection. Required if BFD Destination IP Type is IPV6

- ``bfd_multiplier``: Multiplier used for Bidirectional Forwarding Detection Timer.

- ``bfd_timer``: Timer for Bidirectional Forwarding Detection in milliseconds.

- ``last_updated_by``: ID of the user who last updated the object.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``multi_hop_enabled``: Boolean flag to indicate whether the BFD Session has single hop or multi hop capability.

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


- :ref:`nuuplinkconnection.NUUplinkConnection<nuuplinkconnection>`

- :ref:`nubrconnection.NUBRConnection<nubrconnection>`

