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

- ``last_updated_date``: Time stamp when this object was last updated.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``multi_hop_enabled``: Boolean flag to indicate whether the BFD Session has single hop or multi hop capability.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




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


- :ref:`nubrconnection.NUBRConnection<nubrconnection>`

- :ref:`nuuplinkconnection.NUUplinkConnection<nuuplinkconnection>`

