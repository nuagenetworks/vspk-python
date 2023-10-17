.. _nufloatingip:

nufloatingip
===========================================

.. class:: nufloatingip.NUFloatingIp(bambou.nurest_object.NUMetaRESTObject,):

Floating IP that is associated to a Domain. This floating IP could be used in the VM interface for NAT functionality.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``access_control``: If access control is enabled this FIP is part of the Internet PG.

- ``address``: Floating IP address assigned to the Domain

- ``egress_rate_limiter_id``: ID of the Egress Rate Limiter for this FloatingIP.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``ingress_rate_limiter_id``: ID of the Ingress Rate Limiter for this FloatingIP.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``is_secondary_fip``: Flag to indicate if this FIP is created from secondary FIP domain.

- ``assigned``: True if this floating IP is assigned to a network interface else the value is false

- ``assigned_to_object_type``: The object type to which this floating ip is assigned. Eg. vport or virtualip

- ``associated_shared_network_resource_id`` (**Mandatory**): Id of the shared network resource subnet which was used to get this floating IP address

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

