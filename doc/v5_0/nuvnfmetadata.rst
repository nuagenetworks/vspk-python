.. _nuvnfmetadata:

nuvnfmetadata
===========================================

.. class:: nuvnfmetadata.NUVNFMetadata(bambou.nurest_object.NUMetaRESTObject,):

The VNF deployment properties that includes the location of the image, bootstrap config and rest of the libvirt domain XML template defined as text file.


Attributes
----------


- ``name`` (**Mandatory**): Name of the VNF Metadata  

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the VNF Metadata

- ``blob`` (**Mandatory**): The Metadata blob 

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``assoc_entity_type``: Type of the entity to which the Metadata is associated to.

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

- :ref:`nuvnf.NUVNF<nuvnf>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

