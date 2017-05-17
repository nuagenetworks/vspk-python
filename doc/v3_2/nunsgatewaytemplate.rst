.. _nunsgatewaytemplate:

nunsgatewaytemplate
===========================================

.. class:: nunsgatewaytemplate.NUNSGatewayTemplate(bambou.nurest_object.NUMetaRESTObject,):

Represents a Network Service Gateway Template.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Gateway

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description of the Gateway

- ``infrastructure_profile_id`` (**Mandatory**): The ID of the infrastructure gateway profile this instance of a Gateway is associated with.

- ``enterprise_id``: The enterprise associated with this Gateway. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nunsporttemplate.NUNSPortTemplate<nunsporttemplate>`                                                                                                       ``ns_port_templates`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

