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

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

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


- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

