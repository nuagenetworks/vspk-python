.. _nubgppeer:

nubgppeer
===========================================

.. class:: nubgppeer.NUBGPPeer(bambou.nurest_object.NUMetaRESTObject,):

Encapsulates the BGP peer information for system monitor entity.


Attributes
----------


- ``last_state_change``: Last state change timestamp.

- ``address``: IP of the BGP peer.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``status``: Current connection status of the BGP peer.

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


- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nuhsc.NUHSC<nuhsc>`

