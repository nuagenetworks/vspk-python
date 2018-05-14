.. _nuforwardingpathlistentry:

nuforwardingpathlistentry
===========================================

.. class:: nuforwardingpathlistentry.NUForwardingPathListEntry(bambou.nurest_object.NUMetaRESTObject,):

Forwarding path list entry to be associated with forwarding path list for l4 based policy to PAT / IKE to underlay.


Attributes
----------


- ``fc_override``: Value of the Service Class to be overridden in the packet when the match conditions are satisfied.

- ``last_updated_by``: ID of the user who last updated the object.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``forwarding_action`` (**Mandatory**): Type of forwarding action associated with this entry.

- ``uplink_preference``: Type of forwarding uplink preference associated with this entry. In case of forwardingAction "IKE", uplinkPreference must not be set.

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


- :ref:`nuforwardingpathlist.NUForwardingPathList<nuforwardingpathlist>`

