.. _numulticastchannelmap:

numulticastchannelmap
===========================================

.. class:: numulticastchannelmap.NUMultiCastChannelMap(bambou.nurest_object.NUMetaRESTObject,):

This is the definition of a MultiCast Channel Map.


Attributes
----------


- ``name`` (**Mandatory**): Name of the current entity

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description field provided by the user that identifies the MultiCast Channel Map

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`numulticastrange.NUMultiCastRange<numulticastrange>`                                                                                                       ``multi_cast_ranges`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`numulticastlist.NUMultiCastList<numulticastlist>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nume.NUMe<nume>`

