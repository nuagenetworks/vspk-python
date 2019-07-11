.. _nuvportmirror:

nuvportmirror
===========================================

.. class:: nuvportmirror.NUVPortMirror(bambou.nurest_object.NUMetaRESTObject,):

VPort Mirror represents the relationship between a vport and a mirror destination.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``network_name``: Name of the network to which the vport belongs to

- ``mirror_destination_id``: Destination ID of the mirror destination object.

- ``mirror_destination_name``: Name of the mirror destination

- ``mirror_direction``: Describes what type of traffic needs to be mirrored.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterpise_name``: Enterprise to which the vport associated with the mirror destination belongs to.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_name``: Domain name of the vport associated with the mirror destination

- ``vport_id``: Id of the vport to which the mirror destination is associated with.

- ``vport_name``: Name of the vport to which the mirror destination is associated with.

- ``attached_network_type``: Type of the network attached - L2/L3

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


- :ref:`numirrordestination.NUMirrorDestination<numirrordestination>`

- :ref:`nuvport.NUVPort<nuvport>`

