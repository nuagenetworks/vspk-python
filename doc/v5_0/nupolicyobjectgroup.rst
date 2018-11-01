.. _nupolicyobjectgroup:

nupolicyobjectgroup
===========================================

.. class:: nupolicyobjectgroup.NUPolicyObjectGroup(bambou.nurest_object.NUMetaRESTObject,):

Policy Object Groups are a collection of existing Network Services Gateways. These groups can be used in routing policies for domain links.


Attributes
----------


- ``name``: Name of the Policy Object Group

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the Policy Object Group

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Type of the Policy Object Group




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nunsgateway.NUNSGateway<nunsgateway>`                                                                                                                      ``ns_gateways`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

