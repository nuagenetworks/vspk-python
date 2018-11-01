.. _nuvnfinterfacedescriptor:

nuvnfinterfacedescriptor
===========================================

.. class:: nuvnfinterfacedescriptor.NUVNFInterfaceDescriptor(bambou.nurest_object.NUMetaRESTObject,):

Represent VNF interface descriptor


Attributes
----------


- ``name`` (**Mandatory**): Device name associated with this interface

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Type of VNF interface




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvnfdescriptor.NUVNFDescriptor<nuvnfdescriptor>`

