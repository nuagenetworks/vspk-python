.. _nuvm:

nuvm
===========================================

.. class:: nuvm.NUVM(bambou.nurest_object.NUMetaRESTObject,):

Read only API that can retrieve the VMs associated with a domain, zone or subnet for mediation created VM's for REST created  VM's you need to set the additional proxy user header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example : Alcatel Lucent@bob), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header.


Attributes
----------


- ``l2_domain_ids``: Array of IDs of the l2 domain that the VM is connected to

- ``vrsid``: Id of the VRS that this VM is attached to.

- ``uuid`` (**Mandatory**): UUID of the VM

- ``name`` (**Mandatory**): Name of the VM

- ``last_updated_by``: ID of the user who last updated the object.

- ``reason_type``: Reason of the event associated with the VM.

- ``delete_expiry``: reflects the  VM Deletion expiry timer in secs , deleteMode needs to be non-null value for deleteExpiry to be taken in to effect. CMS created VM's will always have deleteMode set to TIMER

- ``delete_mode``: reflects the mode of VM Deletion -  TIMER  Possible values are TIMER, .

- ``resync_info``: Information of the status of the resync operation of a VM

- ``site_identifier``: This property specifies the site the VM belongs to, for Geo-redundancy.

- ``interfaces``: List of VM interfaces associated with the VM

- ``enterprise_id``: ID of the enterprise that this VM belongs to

- ``enterprise_name``: Name of the enterprise that this VM belongs to

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_ids``: Array of IDs of the domain that the VM is connected to

- ``zone_ids``: Array of IDs of the zone that this VM is attached to

- ``orchestration_id``: Orchestration ID

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

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nutier.NUTier<nutier>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

