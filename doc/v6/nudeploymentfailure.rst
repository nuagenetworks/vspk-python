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

- ``last_updated_date``: Time stamp when this object was last updated.

- ``affected_entity_id``: UUID of the entity on which deployment failed.

- ``affected_entity_type``: Managed object type corresponding to the entity on which deployment failed.

- ``diff_map``: Object difference in json format.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``error_condition``: A numerical code mapping to the deployment error condition.

- ``assoc_entity_id``: ID of the parent entity

- ``assoc_entity_type``: Type of parent entity.

- ``associated_domain_id``: ID of the associated Domain.

- ``associated_domain_type``: Type of the associated Domain

- ``associated_network_entity_id``: ID of associated Network entity.

- ``associated_network_entity_type``: Type of associated Network Entity. i.e Domain, Subnet, L2domain

- ``number_of_occurences``: A count of failed deployment attempts.

- ``event_type``: Event type corresponding to the deployment failure

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nustaticroute.NUStaticRoute<nustaticroute>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nuegressprofile.NUEgressProfile<nuegressprofile>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nunetconfglobalconfiguration.NUNetconfGlobalConfiguration<nunetconfglobalconfiguration>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuingressprofile.NUIngressProfile<nuingressprofile>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nubgpneighbor.NUBGPNeighbor<nubgpneighbor>`

- :ref:`nuethernetsegmentgwgroup.NUEthernetSegmentGWGroup<nuethernetsegmentgwgroup>`

