.. _nuexternalservice:

nuexternalservice
===========================================

.. class:: nuexternalservice.NUExternalService(bambou.nurest_object.NUMetaRESTObject,):

Representation of External Service.


Attributes
----------


- ``name`` (**Mandatory**): unique name of the External Service. 

- ``last_updated_by``: ID of the user who last updated the object.

- ``service_type`` (**Mandatory**): Type of the service.

- ``description``: Description of the External Service.

- ``direction``: Direction

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``stage``: Stage -  START,END Possible values are START, .

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`numetadatatag.NUMetadataTag<numetadatatag>`                                                                                                                ``metadata_tags`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuendpoint.NUEndPoint<nuendpoint>`                                                                                                                         ``end_points`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterpriseprofile.NUEnterpriseProfile<nuenterpriseprofile>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

