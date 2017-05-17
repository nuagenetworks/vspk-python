.. _nuendpoint:

nuendpoint
===========================================

.. class:: nuendpoint.NUEndPoint(bambou.nurest_object.NUMetaRESTObject,):

Representation of End Point


Attributes
----------


- ``name``: unique name of the External Service. 

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the External Service.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuexternalservice.NUExternalService<nuexternalservice>`

