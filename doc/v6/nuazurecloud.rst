.. _nuazurecloud:

nuazurecloud
===========================================

.. class:: nuazurecloud.NUAzureCloud(bambou.nurest_object.NUMetaRESTObject,):

Represents Azure Cloud account to configure IKE entities. 


Attributes
----------


- ``name`` (**Mandatory**): Name given to Azure Cloud instance

- ``last_updated_by``: ID of the user who last updated the object.

- ``tenant_id`` (**Mandatory**): The tenant Id of Azure Cloud account.

- ``client_id`` (**Mandatory**): The client Id of Azure Cloud account.

- ``client_secret`` (**Mandatory**): The client secret of Azure Cloud account.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_ike_encryption_profile_id``: Associated IKE Encryption Profile.

- ``associated_ikepskid`` (**Mandatory**): Associated IKE PSK

- ``subscription_id`` (**Mandatory**): The subscription Id of Azure Cloud account.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuikegatewayprofile.NUIKEGatewayProfile<nuikegatewayprofile>`                                                                                              ``ike_gateway_profiles`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

