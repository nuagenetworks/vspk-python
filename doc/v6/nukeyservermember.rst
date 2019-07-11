.. _nukeyservermember:

nukeyservermember
===========================================

.. class:: nukeyservermember.NUKeyServerMember(bambou.nurest_object.NUMetaRESTObject,):

Represents a KeyServer


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``pem_encoded``: PEM Encoded Certificate

- ``certificate_serial_number``: Certificate serial number associated to the keyserver private key which it is currently signing with

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``fqdn``: FQDN of the keyserver member

- ``issuer_dn``: Issuer DN

- ``subject_dn``: Subject DN

- ``public_key``: Public Key

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


- :ref:`nume.NUMe<nume>`

