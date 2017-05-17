.. _nunatmapentry:

nunatmapentry
===========================================

.. class:: nunatmapentry.NUNATMapEntry(bambou.nurest_object.NUMetaRESTObject,):

Defines a MAP between the private ip and public ip.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``private_ip`` (**Mandatory**): Private IP address of the interface

- ``associated_patnat_pool_id``: Indicates which PATNATPool this entry belongs to

- ``public_ip`` (**Mandatory**): Public IP address of the interface

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


- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

