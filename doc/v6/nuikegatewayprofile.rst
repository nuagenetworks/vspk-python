.. _nuikegatewayprofile:

nuikegatewayprofile
===========================================

.. class:: nuikegatewayprofile.NUIKEGatewayProfile(bambou.nurest_object.NUMetaRESTObject,):

Define attributes of the remote IKE gateway.


Attributes
----------


- ``ike_gateway_identifier``: IKE Gateway Identifier. Null to take on the default 'ipaddress'

- ``ike_gateway_identifier_type``: IKE Gateway Identifier Type.

- ``name``: Name of the IKEv2 Gateway Profile

- ``last_updated_by``: ID of the user who last updated the object.

- ``service_class``: Class of service to be used. Service classes in order of priority are A, B, C, D, E, F, G, and H.

- ``description``: Description of the IKEv2 Gateway Profile

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``anti_replay_check``: Allow any local subnets to be used

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``configuration_status``: Status of configuration on third-party cloud instance

- ``associated_cloud_id``: ID of the associated third-party cloud instance

- ``associated_cloud_type``: Type of associated third-party cloud instance, ex. AZURECLOUD

- ``associated_enterprise_id``: The ID of the associated Enterprise

- ``associated_ike_authentication_id``: Associated IKE Authentication ID

- ``associated_ike_authentication_type``: Associated IKE Authentication Type

- ``associated_ike_encryption_profile_id``: The ID of the associated IKE Encryption Profile

- ``associated_ike_gateway_id``: The IKE Gateway associated with this Profile

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuazurecloud.NUAzureCloud<nuazurecloud>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

