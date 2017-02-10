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

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

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

