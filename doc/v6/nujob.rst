.. _nujob:

nujob
===========================================

.. class:: nujob.NUJob(bambou.nurest_object.NUMetaRESTObject,):

Represents JOB entity. The job API accepts a command and parameters and executes the job and returns the results. Jobs API are typically used for long running tasks.


Attributes
----------


- ``parameters``: Additional arguments required for the specific command. Differs based on types of command.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``result``: Results from the execution of the job

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``command`` (**Mandatory**): Name of the command.

- ``creation_date``: Time stamp when this object was created.

- ``progress``: Indicates the progress of the job as a faction. eg : 0.5 means 50% done.

- ``assoc_entity_type``: Entity with which this job is associated Refer to API section for supported types.

- ``status``: Current status of the job. Possible values are RUNNING, FAILED, SUCCESS, .

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


- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuazurecloud.NUAzureCloud<nuazurecloud>`

- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nuikegatewayconnection.NUIKEGatewayConnection<nuikegatewayconnection>`

- :ref:`nume.NUMe<nume>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`

- :ref:`nuzfbrequest.NUZFBRequest<nuzfbrequest>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nuvcentercluster.NUVCenterCluster<nuvcentercluster>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nuvcenter.NUVCenter<nuvcenter>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nuvsd.NUVSD<nuvsd>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`nuvnf.NUVNF<nuvnf>`

- :ref:`nuethernetsegmentgwgroup.NUEthernetSegmentGWGroup<nuethernetsegmentgwgroup>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

- :ref:`nuvcenterhypervisor.NUVCenterHypervisor<nuvcenterhypervisor>`

