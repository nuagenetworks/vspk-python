.. _nugatewaysecurity:

nugatewaysecurity
===========================================

.. class:: nugatewaysecurity.NUGatewaySecurity(bambou.nurest_object.NUMetaRESTObject,):

This object represents the gateway security object


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway_id``: The gateway associated with this object. This is a read only attribute

- ``revision``: change revision number for the gateway security data

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_entity_type``: Object type of the associated entity.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nugatewaysecureddata.NUGatewaySecuredData<nugatewaysecureddata>`                                                                                           ``gateway_secured_datas`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

