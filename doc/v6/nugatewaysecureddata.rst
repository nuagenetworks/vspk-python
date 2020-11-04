.. _nugatewaysecureddata:

nugatewaysecureddata
===========================================

.. class:: nugatewaysecureddata.NUGatewaySecuredData(bambou.nurest_object.NUMetaRESTObject,):

This object represents the secured data object under the gateway


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``data``: Encrypted data

- ``gateway_cert_serial_number``: Serial Number of the certificate of the public key that encrypted this data

- ``keyserver_cert_serial_number``: Serial Number of the certificate needed to verify the encrypted data

- ``signed_data``: Private key signed data.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``associated_enterprise_id``: Identification of the Enterprise instance to which the Gateway Secure Data is related.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nugatewaysecurity.NUGatewaySecurity<nugatewaysecurity>`

