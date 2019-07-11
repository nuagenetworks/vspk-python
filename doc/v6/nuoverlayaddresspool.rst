.. _nuoverlayaddresspool:

nuoverlayaddresspool
===========================================

.. class:: nuoverlayaddresspool.NUOverlayAddressPool(bambou.nurest_object.NUMetaRESTObject,):

The address pool the public IP of the PAT/NAT entries belong too.


Attributes
----------


- ``ip_type``: The IP Type of this Overlay Address Pool, possible values are IPV4, IPV6 or DUALSTACK.

- ``name``: Name for the PAT NAT pool

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: addresspool description

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``end_address_range``: The end address for the pool range.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_domain_id``: The ID of the associated l3-domain.

- ``start_address_range``: Start address for the pool range

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuoverlaypatnatentry.NUOverlayPATNATEntry<nuoverlaypatnatentry>`                                                                                           ``overlay_patnat_entries`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nulink.NULink<nulink>`

