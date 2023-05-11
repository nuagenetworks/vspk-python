.. _nudeploymentfailure:

nudeploymentfailure
===========================================

.. class:: nudeploymentfailure.NUDeploymentFailure(bambou.nurest_object.NUMetaRESTObject,):

A deployment failure represents a deployment operation initiated by the VSD that resulted in a failure.


Attributes
----------


- ``last_failure_reason``: A detailed description of the last deployment failure.

- ``last_known_error``: A string reporting the last reported deployment error condition.

- ``last_updated_by``: ID of the user who last updated the object.

- ``affected_entity_id``: UUID of the entity on which deployment failed.

- ``affected_entity_type``: Managed object type corresponding to the entity on which deployment failed.

- ``diff_map``: Object difference in json format.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``error_condition``: A numerical code mapping to the deployment error condition.

- ``assoc_entity_id``: ID of the parent entity

- ``assoc_entity_type``: Type of parent entity.

- ``associated_domain_id``: ID of the associated Domain.

- ``associated_domain_type``: Type of the associated Domain

- ``associated_network_entity_id``: ID of associated Network entity.

- ``associated_network_entity_type``: Type of associated Network Entity. i.e Domain, Subnet, L2domain

- ``number_of_occurences``: A count of failed deployment attempts.

- ``event_type``: Event type corresponding to the deployment failure

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


- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nustaticroute.NUStaticRoute<nustaticroute>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nuegressprofile.NUEgressProfile<nuegressprofile>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuingressprofile.NUIngressProfile<nuingressprofile>`

- :ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

