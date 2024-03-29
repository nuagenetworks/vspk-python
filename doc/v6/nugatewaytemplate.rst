.. _nugatewaytemplate:

nugatewaytemplate
===========================================

.. class:: nugatewaytemplate.NUGatewayTemplate(bambou.nurest_object.NUMetaRESTObject,):

A gateway is your point of exit to an external network. It can be a physical or a virtual device. Gateways are templatable. You can attach gateway's VLANs to any existing host or bridge VPorts.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Gateway

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``native_vlan``: Default Native VLAN to carry untagged traffic on the ports of the gateways using this template. Applicable for third-party Netconf Gateways only. Possible values are 1-3967.

- ``personality`` (**Mandatory**): Personality of the Gateway, cannot be changed after creation.

- ``description``: A description of the Gateway

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``infrastructure_profile_id``: The ID of the associated Infrastructure Gateway Profile tied to this instance of a Gateway Template.

- ``enterprise_id``: The enterprise associated with this Gateway. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuporttemplate.NUPortTemplate<nuporttemplate>`                                                                                                             ``port_templates`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

