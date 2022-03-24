.. _nunetconfglobalconfiguration:

nunetconfglobalconfiguration
===========================================

.. class:: nunetconfglobalconfiguration.NUNetconfGlobalConfiguration(bambou.nurest_object.NUMetaRESTObject,):

This Entity defines Global Configurations such as Prefix-list, Mac-list etc., to be configured on a Third-party Gateway (Netconf - VTEP).


Attributes
----------


- ``name`` (**Mandatory**): The unique name of the Global Configuration.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A description of the GlobalConfiguration.

- ``netconf_gateway_ids``: List of third-party Netconf Gateways on which Global Configuration will be deployed.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``config_definition`` (**Mandatory**): Global configurations like prefix lists, community, mac-list etc.. to be configured on a Netconf Gateway.

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`                                                                                              ``deployment_failures`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

