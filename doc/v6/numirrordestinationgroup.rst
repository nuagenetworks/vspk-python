.. _numirrordestinationgroup:

numirrordestinationgroup
===========================================

.. class:: numirrordestinationgroup.NUMirrorDestinationGroup(bambou.nurest_object.NUMetaRESTObject,):

Mirror destination group is a collection of mirror destination objects.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Mirror Destination Group.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the Mirror Destination Group.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`numirrordestination.NUMirrorDestination<numirrordestination>`                                                                                              ``mirror_destinations`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuoverlaymirrordestination.NUOverlayMirrorDestination<nuoverlaymirrordestination>`                                                                         ``overlay_mirror_destinations`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

