.. _nuenterprisesecureddata:

nuenterprisesecureddata
===========================================

.. class:: nuenterprisesecureddata.NUEnterpriseSecuredData(bambou.nurest_object.NUMetaRESTObject,):

This object represents the secured data object under the enterprise


Attributes
----------


- ``hash``: authentication hash

- ``last_updated_by``: ID of the user who last updated the object.

- ``data``: encrypted data

- ``seed_type``: seed type

- ``sek_id``: Seed Encryption Key id that encrypted this data

- ``keyserver_cert_serial_number``: Serial Number of the certificate needed to verify the encrypted data

- ``signed_hash``: private key signed hash

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

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


- :ref:`nuenterprisesecurity.NUEnterpriseSecurity<nuenterprisesecurity>`

