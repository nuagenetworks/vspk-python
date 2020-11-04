.. _nuconnectionendpoint:

nuconnectionendpoint
===========================================

.. class:: nuconnectionendpoint.NUConnectionendpoint(bambou.nurest_object.NUMetaRESTObject,):

SSH (Secure Shell) is used to provide secure remote console access to NSGs deployed in branch locations. For additional security, you may restrict SSH access from specific host(s) by providing a list of source IP addresses.


Attributes
----------


- ``ip_address``: IP Address of the end point.

- ``ip_type``: IPv4 or IPv6.

- ``ipv6_address``: IPv6 address of the end point.

- ``name`` (**Mandatory**): Name of the connection endpoint.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A description of the connection endpoint.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``end_point_type``: Indicates if this endpoint is the source/destination of a network connection.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

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


- :ref:`nuinfrastructureaccessprofile.NUInfrastructureAccessProfile<nuinfrastructureaccessprofile>`

