.. _nuvnfdescriptor:

nuvnfdescriptor
===========================================

.. class:: nuvnfdescriptor.NUVNFDescriptor(bambou.nurest_object.NUMetaRESTObject,):

Represent Virtual Network Function Descriptor Object


Attributes
----------


- ``cpu_count``: Number of CPUs to be allocated VNF instance when deployed

- ``name`` (**Mandatory**): Name of the VNF Descriptor

- ``memory_mb`` (**Mandatory**): Memory (in MB) to be allocated for VNF instance when deployed

- ``vendor``: The vendor generating this VNF Descriptor

- ``description``: A description of the VNF Descriptor

- ``metadata_id`` (**Mandatory**): Id of referenced Metadata Object

- ``visible``: Controls if descriptor visible in catalog to create new VNF

- ``associated_vnf_threshold_policy_id``: The Id of referenced VNF threshold policy

- ``storage_gb`` (**Mandatory**): Disk storage (in GB) to be allocated VNF instance when deployed

- ``type``: Type of virtual network function




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuvnfinterfacedescriptor.NUVNFInterfaceDescriptor<nuvnfinterfacedescriptor>`                                                                               ``vnf_interface_descriptors`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvnfcatalog.NUVNFCatalog<nuvnfcatalog>`

