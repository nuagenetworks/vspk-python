.. _numulticastrange:

numulticastrange
===========================================

.. class:: numulticastrange.NUMultiCastRange(bambou.nurest_object.NUMetaRESTObject,):

A multicast channel range defines a set of multicast groups that will be allowed to be joined. They act as a set of "white-list" addresses that a VM will be allowed to join. A multicast channel map requires at least one range defined to be of use. Ranges within the same channel map must be non-overlapping between each other. Groups not covered by a range won't be joinable from the VMs.


Attributes
----------


- ``ip_type``: The ip type.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``max_address`` (**Mandatory**): Highest address in the MultiCast range

- ``min_address`` (**Mandatory**): Lowest address in the MultiCast range

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

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
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`numulticastchannelmap.NUMultiCastChannelMap<numulticastchannelmap>`

