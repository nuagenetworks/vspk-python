.. _nuvmresync:

nuvmresync
===========================================

.. class:: nuvmresync.NUVMResync(bambou.nurest_object.NUMetaRESTObject,):

Provide information about the state of a VM resync request.


Attributes
----------


- ``last_request_timestamp``: Time of the last timestamp received

- ``last_time_resync_initiated``: Time that the resync was initiated

- ``last_updated_by``: ID of the user who last updated the object.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``status``: Status of the resync

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


- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvm.NUVM<nuvm>`

