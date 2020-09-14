.. _nuoverlaypatnatentry:

nuoverlaypatnatentry
===========================================

.. class:: nuoverlaypatnatentry.NUOverlayPATNATEntry(bambou.nurest_object.NUMetaRESTObject,):

Create a static NAT 1:1 IP mapping between a Pool IP and a host IP in the branch domain, to provide access to the branch resource.


Attributes
----------


- ``nat_enabled``: This flag will determine whether the entry is NAT or PAT.

- ``last_updated_by``: ID of the user who last updated the object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``private_ip``: Private IP address for the interface

- ``associated_domain_id``: The ID of the associated l3-domain.

- ``associated_link_id``: The ID of the associated domain-link.

- ``public_ip``: Public IP address of the interface

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


- :ref:`nuoverlayaddresspool.NUOverlayAddressPool<nuoverlayaddresspool>`

