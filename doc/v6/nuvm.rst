.. _nuvm:

nuvm
===========================================

.. class:: nuvm.NUVM(bambou.nurest_object.NUMetaRESTObject,):

API that can retrieve the VMs associated with a domain, zone or subnet for mediation created VM's for REST created  VM's you need to set the additional proxy user header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example : Nokia@bob), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header.


Attributes
----------


- ``l2_domain_ids``: Array of IDs of the l2 domain that the VM is connected to

- ``vrsid``: Id of the VRS that this VM is attached to.

- ``uuid`` (**Mandatory**): UUID of the VM

- ``name`` (**Mandatory**): Name of the VM

- ``last_updated_by``: ID of the user who last updated the object.

- ``reason_type``: Reason of the event associated with the VM.

- ``delete_expiry``: Reflects the VM Deletion expiry timer in seconds, deleteMode needs to be non-null value for deleteExpiry to be taken in to effect. CMS created VMs will always have deleteMode set to TIMER.

- ``delete_mode``: Reflects the mode of VM Deletion.

- ``resync_info``: Information of the status of the resync operation of a VM

- ``site_identifier``: This property specifies the site the VM belongs to, for Geo-redundancy.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``interfaces``: List of VM interfaces associated with the VM

- ``enterprise_id``: ID of the enterprise that this VM belongs to

- ``enterprise_name``: Name of the enterprise that this VM belongs to

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_ids``: Array of IDs of the domain that the VM is connected to

- ``compute_provisioned``: computeProvisioned

- ``zone_ids``: Array of IDs of the zone that this VM is attached to

- ``orchestration_id``: Orchestration ID

- ``vrs_raw_version``: Release version of VRS, which is used to determine the feature capabilties of VRS.

- ``vrs_version``: Interpreted version of VRS, which is used to determine the feature capabilities of VRS.

- ``user_id``: ID of the user that created this VM

- ``user_name``: Username of the user that created this VM

- ``status``: Status of the VM.

- ``subnet_ids``: Array of IDs of the subnets that the VM is connected to

- ``external_id``: External object ID. Used for integration with third party systems

- ``hypervisor_ip``: IP address of the hypervisor that this VM is currently running in




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuvmresync.NUVMResync<nuvmresync>`                                                                                                                         ``vm_resyncs`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvminterface.NUVMInterface<nuvminterface>`                                                                                                                ``vm_interfaces`` 
:ref:`nuvrs.NUVRS<nuvrs>`                                                                                                                                        ``vrss`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuqos.NUQOS<nuqos>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

