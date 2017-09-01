.. _nuvnf:

nuvnf
===========================================

.. class:: nuvnf.NUVNF(bambou.nurest_object.NUMetaRESTObject,):

Represent a VNF instance


Attributes
----------


- ``vnf_descriptor_id`` (**Mandatory**): The ID of VNF Descriptor from which VNF to be created.

- ``vnf_descriptor_name``: The Name of VNF Descriptor from which this VNF instance is created.

- ``cpu_count``: Number of CPUs to be allocated for this VNF instance

- ``nsg_name``: The NSG name where VNF is deployed

- ``nsg_system_id``: The NSG system id where VNF is deployed

- ``ns_gateway_id`` (**Mandatory**): The NSG instance id where VNF is deployed

- ``name`` (**Mandatory**): Name of the VNF

- ``task_state``: Current state of operation/task

- ``last_known_error``: Last error reported

- ``memory_mb``: Memory (in MB) to be allocated for this VNF instance.

- ``vendor``: The vendor for VNF

- ``description``: Description of the VNF Instance

- ``metadata_id``: Id of referenced metadata object

- ``allowed_actions``: Action allowed to  performed on VNF based on current status and taskState

- ``enterprise_id``: ID of the enterprise that this VNF belongs to

- ``is_attached_to_descriptor``: This specifies if VNF instance is using VNF descriptor or it is decoupled from it

- ``associated_vnf_metadata_id``: VNF metadata associated to VNF instance. 

- ``status``: State/Status of the VNF

- ``storage_gb``: Disk storage (in GB) to be allocated for deployed VNF instance




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuvnfinterface.NUVNFInterface<nuvnfinterface>`                                                                                                             ``vnf_interfaces`` 
:ref:`nuvnfmetadata.NUVNFMetadata<nuvnfmetadata>`                                                                                                                ``vnf_metadatas`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

