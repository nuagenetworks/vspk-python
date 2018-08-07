.. _nugatewaytemplate:

nugatewaytemplate
===========================================

.. class:: nugatewaytemplate.NUGatewayTemplate(bambou.nurest_object.NUMetaRESTObject,):

A gateway is your point of exit to an external network. It can be a physical or a virtual device. Gateways are templatable. You can attach gateway's VLANs to any existing host or bridge VPorts.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Gateway

- ``last_updated_by``: ID of the user who last updated the object.

- ``personality`` (**Mandatory**): Personality of the Gateway, cannot be changed after creation.

- ``description``: A description of the Gateway

- ``infrastructure_profile_id``: The ID of the associated Infrastructure Gateway Profile tied to this instance of a Gateway Template.

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

