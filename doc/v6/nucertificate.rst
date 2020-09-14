.. _nucertificate:

nucertificate
===========================================

.. class:: nucertificate.NUCertificate(bambou.nurest_object.NUMetaRESTObject,):

This object represents a X509 Certificate Request


Attributes
----------


- ``pem_encoded``: The PEM encoded certificate.

- ``serial_number``: The serial number of this certificate.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``issuer_dn``: The distinguished name of the authority that issued this certificate.

- ``subject_dn``: The distinguished name of this certificate's end entity.

- ``public_key``: The public key contained in this certificate.

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


- :ref:`nume.NUMe<nume>`

