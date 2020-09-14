.. _nuvnfdescriptor:

nuvnfdescriptor
===========================================

.. class:: nuvnfdescriptor.NUVNFDescriptor(bambou.nurest_object.NUMetaRESTObject,):

The behavioral and deployment information of a VNF is defined in the VNF descriptor template. The template is based on the libvirt domain XML and is on-boarded in a VNF catalog. The resource requirements for CPU, memory and storage are defined in this screen and the rest of the template is inherited from the VNF Metadata object.


Attributes
----------


- ``cpu_count``: Number of CPUs to be allocated VNF instance when deployed

- ``name`` (**Mandatory**): Name of the VNF Descriptor

- ``memory_mb`` (**Mandatory**): Memory (in MB) to be allocated for VNF instance when deployed

- ``vendor``: The vendor generating this VNF Descriptor

- ``description``: A description of the VNF Descriptor

- ``metadata_id`` (**Mandatory**): Id of referenced Metadata Object

- ``visible``: Controls if descriptor visible in catalog to create new VNF

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_vnf_threshold_policy_id``: The Id of referenced VNF threshold policy

- ``storage_gb`` (**Mandatory**): Disk storage (in GB) to be allocated VNF instance when deployed

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Type of virtual network function




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvnfinterfacedescriptor.NUVNFInterfaceDescriptor<nuvnfinterfacedescriptor>`                                                                               ``vnf_interface_descriptors`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvnfcatalog.NUVNFCatalog<nuvnfcatalog>`

