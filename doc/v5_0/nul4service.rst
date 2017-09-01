.. _nul4service:

nul4service
===========================================

.. class:: nul4service.NUL4Service(bambou.nurest_object.NUMetaRESTObject,):

L4 Service is a port range and protocol combination that can be used in ACLs


Attributes
----------


- ``name`` (**Mandatory**): Name of the service

- ``last_updated_by``: ID of the user who last updated the object.

- ``default_service``: Flag to identify default service

- ``description``: Description of the service

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``ports`` (**Mandatory**): Value should be either single port number or a port range like 1,2.. or 1 - 10

- ``protocol`` (**Mandatory**): Protocol number that must be matched

- ``external_id``: External object ID. Used for integration with third party systems






Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nul4servicegroup.NUL4ServiceGroup<nul4servicegroup>`

