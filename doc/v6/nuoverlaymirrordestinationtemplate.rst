.. _nuoverlaymirrordestinationtemplate:

nuoverlaymirrordestinationtemplate
===========================================

.. class:: nuoverlaymirrordestinationtemplate.NUOverlayMirrorDestinationTemplate(bambou.nurest_object.NUMetaRESTObject,):

Overlay mirror destinations are pointed to by advanced forwarding policies as the destination for redirected traffic. Targets can be of two types, L3 or virtual wire. For L3 targets a virtual IP should be provided as it allows the system to track among which of the end-points belonging to the overlay mirror destination is the active one. For this type of redirect the packet's destination MAC address is changed to match that of the Virtual IP. For virtual-wire redirection targets, the packets are untouched and forwarded directly to the end-point.


Attributes
----------


- ``name`` (**Mandatory**): Name of this overlay mirror destination template

- ``last_updated_by``: ID of the user who last updated the object.

- ``redundancy_enabled``: Allow/Disallow redundant appliances and VIP

- ``description``: Description of this overlay mirror destination template

- ``destination_type``: Determines the type of destination : redirection target or overlay mirror destination

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``end_point_type`` (**Mandatory**): VPortTagEndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a overlay mirror destination. Possible value is VIRTUAL_WIRE.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``trigger_type``: Trigger type, could be NONE/GARP - THIS IS READONLY

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


- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

