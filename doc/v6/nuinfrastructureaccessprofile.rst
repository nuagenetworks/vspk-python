.. _nuinfrastructureaccessprofile:

nuinfrastructureaccessprofile
===========================================

.. class:: nuinfrastructureaccessprofile.NUInfrastructureAccessProfile(bambou.nurest_object.NUMetaRESTObject,):

Infrastructure Access Profiles identify a set of NSG template level platform attributes specifically related to user and access control, inherited by gateways as they are instantiated.


Attributes
----------


- ``ssh_auth_mode``: Indicates the authentication method used during an SSH session.

- ``name`` (**Mandatory**): Name of the Infrastructure Access Profile

- ``password`` (**Mandatory**): Password of the default user associated to the access profile.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description of the Profile instance created.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise_id``: Enterprise/Organisation associated with this Profile instance.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``source_ip_filter``: Indicates if source based IP filtering is enabled for this access profile.

- ``user_name``: Default user name which is associated to the access profile.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuconnectionendpoint.NUConnectionendpoint<nuconnectionendpoint>`                                                                                           ``connectionendpoints`` 
:ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`                                                                                              ``ns_gateway_templates`` 
:ref:`nusshkey.NUSSHKey<nusshkey>`                                                                                                                               ``ssh_keys`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

