.. _nusaasapplicationgroup:

nusaasapplicationgroup
===========================================

.. class:: nusaasapplicationgroup.NUSaaSApplicationGroup(bambou.nurest_object.NUMetaRESTObject,):

Collection of SaaS Application Types.


Attributes
----------


- ``name`` (**Mandatory**): Name of the SaaS Breakout Group.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the SaaS Breakout Group.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nusaasapplicationtype.NUSaaSApplicationType<nusaasapplicationtype>`                                                                                        ``saa_s_application_types`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

