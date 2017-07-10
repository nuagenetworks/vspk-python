.. _numetadatatag:

numetadatatag
===========================================

.. class:: numetadatatag.NUMetadataTag(bambou.nurest_object.NUMetaRESTObject,):

Metadata tag associated to a metadata.


Attributes
----------


- ``name`` (**Mandatory**): name of the Metadata tag.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the Metadata tag.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_external_service_id``: ID of the entity to which the Metadata tag is  associated to

- ``auto_created``: set to true if it is the default metadata tag created as part of external service creation

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


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuexternalservice.NUExternalService<nuexternalservice>`

- :ref:`numetadata.NUMetadata<numetadata>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`

