.. _nuvnfcatalog:

nuvnfcatalog
===========================================

.. class:: nuvnfcatalog.NUVNFCatalog(bambou.nurest_object.NUMetaRESTObject,):

Represents VNF Catalog


Attributes
----------


- ``name`` (**Mandatory**): Name of the VNF catalog

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the VNF Catalog

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvnfdescriptor.NUVNFDescriptor<nuvnfdescriptor>`                                                                                                          ``vnf_descriptors`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

