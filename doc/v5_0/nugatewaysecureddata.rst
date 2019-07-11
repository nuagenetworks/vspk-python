.. _nugatewaysecureddata:

nugatewaysecureddata
===========================================

.. class:: nugatewaysecureddata.NUGatewaySecuredData(bambou.nurest_object.NUMetaRESTObject,):

This object represents the secured data object under the gateway


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``data``: Encrypted data

- ``gateway_cert_serial_number``: Serial Number of the certificate of the public key that encrypted this data

- ``keyserver_cert_serial_number``: Serial Number of the certificate needed to verify the encrypted data

- ``signed_data``: Private key signed data.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_enterprise_id``: Identification of the Enterprise instance to which the Gateway Secure Data is related.

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


- :ref:`nugatewaysecurity.NUGatewaySecurity<nugatewaysecurity>`

