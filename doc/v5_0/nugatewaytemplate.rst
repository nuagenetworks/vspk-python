.. _nugatewaytemplate:

nugatewaytemplate
===========================================

.. class:: nugatewaytemplate.NUGatewayTemplate(bambou.nurest_object.NUMetaRESTObject,):

Represents Gateway Template object.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Gateway

- ``last_updated_by``: ID of the user who last updated the object.

- ``personality`` (**Mandatory**): Personality of the Gateway, cannot be changed after creation.

- ``description``: A description of the Gateway

- ``enterprise_id``: The enterprise associated with this Gateway. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuporttemplate.NUPortTemplate<nuporttemplate>`                                                                                                             ``port_templates`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

