.. _nuvnfinterfacedescriptor:

nuvnfinterfacedescriptor
===========================================

.. class:: nuvnfinterfacedescriptor.NUVNFInterfaceDescriptor(bambou.nurest_object.NUMetaRESTObject,):

The interfaces attached to the VNF descriptor. The interfaces are used for management and datapath traffic. Atleast one interface should be designated as a management interface


Attributes
----------


- ``name`` (**Mandatory**): Device name associated with this interface

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

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

