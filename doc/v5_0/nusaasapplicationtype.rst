.. _nusaasapplicationtype:

nusaasapplicationtype
===========================================

.. class:: nusaasapplicationtype.NUSaaSApplicationType(bambou.nurest_object.NUMetaRESTObject,):

SaaS applications like office365 with the published list of IPs and/or URLs for creating firewall rules for IT admins.


Attributes
----------


- ``name`` (**Mandatory**): Name of the SaaS Application.

- ``last_updated_by``: ID of the user who last updated the object.

- ``read_only``: A flag to indicate if this SaaS Application Type was pre-defined by the system.

- ``description``: Description for the SaaS Application Type.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisenetwork.NUEnterpriseNetwork<nuenterprisenetwork>`                                                                                              ``enterprise_networks`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

- :ref:`nusaasapplicationgroup.NUSaaSApplicationGroup<nusaasapplicationgroup>`

