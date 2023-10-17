.. _numulticastchannelmap:

numulticastchannelmap
===========================================

.. class:: numulticastchannelmap.NUMultiCastChannelMap(bambou.nurest_object.NUMetaRESTObject,):

Multicast channel maps define the available multicast groups that can be joined by VMs belonging to enterprises to which the maps have been assigned to. A map can contain one or more ranges defining the available channels. Ranges are non overlapping within a single map.


Attributes
----------


- ``name`` (**Mandatory**): Name of the current entity

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A description field provided by the user that identifies the MultiCast Channel Map

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
:ref:`numulticastrange.NUMultiCastRange<numulticastrange>`                                                                                                       ``multi_cast_ranges`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`numulticastlist.NUMultiCastList<numulticastlist>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

