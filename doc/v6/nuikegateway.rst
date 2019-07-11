.. _nuikegateway:

nuikegateway
===========================================

.. class:: nuikegateway.NUIKEGateway(bambou.nurest_object.NUMetaRESTObject,):

Represents an IKE Gateway


Attributes
----------


- ``ike_version``: The IKE Version

- ``ik_ev1_mode``: Mode for IKEv1

- ``ip_address``: IP Address of the IKEv2 Gateway

- ``name``: Name of the IKEv2 Gateway

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the IKEv2 Gateway

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``configuration_status``: Status of configuration on third-party cloud instance

- ``associated_cloud_id``: ID of the associated third-party cloud instance

- ``associated_cloud_type``: Type of associated third-party cloud instance, ex. AZURECLOUD

- ``associated_enterprise_id``: The ID of the associated Enterprise

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuikegatewayconfig.NUIKEGatewayConfig<nuikegatewayconfig>`                                                                                                 ``ike_gateway_configs`` 
:ref:`nuikesubnet.NUIKESubnet<nuikesubnet>`                                                                                                                      ``ike_subnets`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

