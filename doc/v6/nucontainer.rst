.. _nucontainer:

nucontainer
===========================================

.. class:: nucontainer.NUContainer(bambou.nurest_object.NUMetaRESTObject,):

API that can retrieve the containers associated with a domain, zone or subnet for mediation created containers for REST created  containers you need to set the additional proxy user header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example : Nokia@bob), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header.


Attributes
----------


- ``l2_domain_ids``: Array of IDs of the l2 domain that the container is connected to

- ``vrsid``: Id of the VRS that this container is attached to.

- ``uuid`` (**Mandatory**): UUID of the container

- ``name`` (**Mandatory**): Name of the container

- ``last_updated_by``: ID of the user who last updated the object.

- ``reason_type``: Reason of the event associated with the container.

- ``delete_expiry``: reflects the  container Deletion expiry timer in secs , deleteMode needs to be non-null value for deleteExpiry to be taken in to effect. CMS created containers will always have deleteMode set to TIMER

- ``delete_mode``: reflects the mode of container Deletion -  TIMER  Possible values are TIMER, .

- ``resync_info``: Information of the status of the resync operation of a container

- ``site_identifier``: This property specifies the site the container belongs to, for Geo-redundancy.

- ``image_id``: Id of the container image

- ``image_name``: Name of the container image

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``interfaces``: List of container interfaces associated with the container

- ``enterprise_id``: ID of the enterprise that this container belongs to

- ``enterprise_name``: Name of the enterprise that this container belongs to

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_ids``: Array of IDs of the domain that the container is connected to

- ``compute_provisioned``: Compute Provisioned

- ``zone_ids``: Array of IDs of the zone that this container is attached to

- ``orchestration_id`` (**Mandatory**): Orchestration ID

- ``vrs_raw_version``: Release version of VRS, which is used to determine the feature capabilties of VRS.

- ``vrs_version``: Interpreted version of VRS, which is used to determine the feature capabilities of VRS.

- ``user_id``: ID of the user that created this container

- ``user_name``: Username of the user that created this container

- ``status``: Status of the container.

- ``subnet_ids``: Array of IDs of the subnets that the container is connected to

- ``external_id``: External object ID. Used for integration with third party systems

- ``hypervisor_ip``: IP address of the hypervisor that this container is currently running in




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`                                                                                           ``container_interfaces`` 
:ref:`nucontainerresync.NUContainerResync<nucontainerresync>`                                                                                                    ``container_resyncs`` 
:ref:`nuvrs.NUVRS<nuvrs>`                                                                                                                                        ``vrss`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuqos.NUQOS<nuqos>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nume.NUMe<nume>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

