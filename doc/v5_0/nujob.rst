.. _nujob:

nujob
===========================================

.. class:: nujob.NUJob(bambou.nurest_object.NUMetaRESTObject,):

Represents JOB entity. The job API accepts a command and parameters and executes the job and returns the results. Jobs API are typically used for long running tasks.


Attributes
----------


- ``parameters``: Additional arguments required for the specific command. Differs based on types of command.

- ``last_updated_by``: ID of the user who last updated the object.

- ``result``: Results from the execution of the job

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``command`` (**Mandatory**): Name of the command.

- ``progress``: Indicates the progress of the job as a faction. eg : 0.5 means 50% done.

- ``assoc_entity_type``: Entity with which this job is associated Refer to API section for supported types.

- ``status``: Current status of the job. Possible values are RUNNING, FAILED, SUCCESS, .

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


- :ref:`nuvsd.NUVSD<nuvsd>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nuzfbrequest.NUZFBRequest<nuzfbrequest>`

- :ref:`nuvcentercluster.NUVCenterCluster<nuvcentercluster>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nuvcenter.NUVCenter<nuvcenter>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nume.NUMe<nume>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nuvsc.NUVSC<nuvsc>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

- :ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`

- :ref:`nuvnf.NUVNF<nuvnf>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`

- :ref:`nuvcenterhypervisor.NUVCenterHypervisor<nuvcenterhypervisor>`

