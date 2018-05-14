.. _nuforwardingpathlist:

nuforwardingpathlist
===========================================

.. class:: nuforwardingpathlist.NUForwardingPathList(bambou.nurest_object.NUMetaRESTObject,):

Forwarding path list is l4 based policy to PAT / IKE to underlay.


Attributes
----------


- ``name`` (**Mandatory**): Name of the forwarding path list.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Describes the Forwarding Path List

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuforwardingpathlistentry.NUForwardingPathListEntry<nuforwardingpathlistentry>`                                                                            ``forwarding_path_list_entries`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

