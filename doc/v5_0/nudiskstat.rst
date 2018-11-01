.. _nudiskstat:

nudiskstat
===========================================

.. class:: nudiskstat.NUDiskStat(bambou.nurest_object.NUMetaRESTObject,):

Encapsulates the disk usage metrics for system monitor entity.


Attributes
----------


- ``name``: Name of the disk.

- ``size``: Total disk space.

- ``unit``: Storage unit type (example: bytes, KB, MB, etc.,).

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``used``: Disk space used.

- ``available``: Available disk space.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================


