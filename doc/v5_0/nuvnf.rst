.. _nuvnf:

nuvnf
===========================================

.. class:: nuvnf.NUVNF(bambou.nurest_object.NUMetaRESTObject,):

Instantiation of a VNF on a specified Network Services Gateway that has the resources to manage a VNF.


Attributes
----------


- ``vnf_descriptor_id``: The ID of VNF Descriptor from which VNF to be created. This is required on creation and can be removed on moidification of VNF instance.

- ``vnf_descriptor_name``: The Name of VNF Descriptor from which this VNF instance is created.

- ``cpu_count``: Number of CPUs to be allocated for this VNF instance

- ``nsg_name``: The NSG name where VNF is deployed

- ``nsg_system_id``: The NSG system id where VNF is deployed

- ``ns_gateway_id`` (**Mandatory**): The NSG instance id where VNF is deployed

- ``name`` (**Mandatory**): Name of the VNF

- ``task_state``: Current state of operation/task

- ``last_known_error``: Last error reported

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_user_action``: Last action perform by user

- ``memory_mb``: Memory (in MB) to be allocated for this VNF instance.

- ``vendor``: The vendor for VNF

- ``description``: Description of the VNF Instance

- ``allowed_actions``: Action allowed to  performed on VNF based on current status and taskState

- ``enterprise_id``: ID of the enterprise that this VNF belongs to

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``is_attached_to_descriptor``: This specifies if VNF instance is using VNF descriptor or it is decoupled from it

- ``associated_vnf_metadata_id``: VNF metadata associated to VNF instance. 

- ``associated_vnf_threshold_policy_id``: VNF threshold policy associated to VNF instance

- ``status``: State/Status of the VNF

- ``storage_gb``: Disk storage (in GB) to be allocated for deployed VNF instance

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Type of virtual network function




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvnfinterface.NUVNFInterface<nuvnfinterface>`                                                                                                             ``vnf_interfaces`` 
:ref:`nuvnfmetadata.NUVNFMetadata<nuvnfmetadata>`                                                                                                                ``vnf_metadatas`` 
:ref:`nuvnfthresholdpolicy.NUVNFThresholdPolicy<nuvnfthresholdpolicy>`                                                                                           ``vnf_threshold_policies`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

