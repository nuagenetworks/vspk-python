.. _nuapp:

nuapp
===========================================

.. class:: nuapp.NUApp(bambou.nurest_object.NUMetaRESTObject,):

Represents a real life application like a vendor website, or a social network.


Attributes
----------


- ``name`` (**Mandatory**): Name of the application.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the application.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``assoc_egress_acl_template_id``: The ID of the ACL template that this application is pointing to.

- ``assoc_ingress_acl_template_id``: The ID of the ACL template that this application is pointing to

- ``associated_domain_id`` (**Mandatory**): Domain id where the application is running.

- ``associated_domain_type`` (**Mandatory**): Type of domain (DOMAIN, L2DOMAIN). Refer to API section for supported types.

- ``associated_network_object_id``: ID of the network object that this App is associated with.

- ``associated_network_object_type``: Type of network object this App is associated with (ENTERPRISE, DOMAIN) Refer to API section for supported types.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nutier.NUTier<nutier>`                                                                                                                                     ``tiers`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuflow.NUFlow<nuflow>`                                                                                                                                     ``flows`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

