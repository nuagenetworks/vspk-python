.. _nuikecertificate:

nuikecertificate
===========================================

.. class:: nuikecertificate.NUIKECertificate(bambou.nurest_object.NUMetaRESTObject,):

Represents an IKE Trusted Certificate


Attributes
----------


- ``pem_encoded``: PEM Encoded Certificate

- ``name``: Name of the Encryption Profile

- ``last_updated_by``: ID of the user who last updated the object.

- ``serial_number``: Serial Number of the Certificate - Read Only Attribute

- ``description``: Description of the IKEv2 Authentication

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``not_after``: Date this Certificate is valid to - Read Only Attribute

- ``not_before``: Date this Certificate is valid from - Read Only Attribute

- ``associated_enterprise_id``: The ID of the associated Enterprise

- ``issuer_dn``: Issuer Distinguished Name of the Certificate - Read Only Attribute

- ``subject_dn``: Subject Distinguished Name of the Certificate - Read Only Attribute

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


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

