.. _nunsgatewaytemplate:

nunsgatewaytemplate
===========================================

.. class:: nunsgatewaytemplate.NUNSGatewayTemplate(bambou.nurest_object.NUMetaRESTObject,):

Represents a Network Service Gateway Template.


Attributes
----------


- ``ssh_service``: Enable/Disable SSH Service on all the Gateway instances which inherit from this template.

- ``name`` (**Mandatory**): Name of the Gateway template.

- ``last_updated_by``: ID of the user who last updated the object.

- ``personality``: Personality of the Gateway template - NSG, NSGBR, cannot be changed after creation.

- ``description``: A description of the Gateway template.

- ``infrastructure_access_profile_id``: The ID of the infrastructure access profile associated to this Gateway Template.

- ``infrastructure_profile_id`` (**Mandatory**): The ID of the infrastructure gateway profile this instance of a Gateway template is associated with.

- ``instance_ssh_override``: Indicates if this template instance allows the gateway instance(s) which inherit from it to independently enable/disable SSH service.

- ``enterprise_id``: The enterprise associated with this Gateway template. This is a read only attribute

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

- :ref:`nuinfrastructureaccessprofile.NUInfrastructureAccessProfile<nuinfrastructureaccessprofile>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

