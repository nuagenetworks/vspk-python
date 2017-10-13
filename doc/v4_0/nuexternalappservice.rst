.. _nuexternalappservice:

nuexternalappservice
===========================================

.. class:: nuexternalappservice.NUExternalAppService(bambou.nurest_object.NUMetaRESTObject,):

Represents an External Service in the Application Designer.


Attributes
----------


- ``name`` (**Mandatory**): Name of the flow.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the flow.

- ``destination_nat_address``: Destination NAT Address

- ``destination_nat_enabled``: Boolean flag to indicate whether source NAT is enabled

- ``destination_nat_mask``: netmask of the Destination NAT

- ``metadata``: metadata

- ``egress_type``: Egress type.

- ``virtual_ip``: Virtual IP Address

- ``virtual_ip_required``: Boolean flag to indicate whether we require a VIP

- ``ingress_type``: Ingress type.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``source_nat_address``: Source NAT Address

- ``source_nat_enabled``: Boolean flag to indicate whether source NAT is enabled

- ``associated_service_egress_group_id``: ID of service port group identifying the output ports

- ``associated_service_egress_redirect_id``: the redirect target ID that identifies the output ports

- ``associated_service_ingress_group_id``: ID of service port group identifying the input ports

- ``associated_service_ingress_redirect_id``: the redirect target ID that identifies the input ports

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nume.NUMe<nume>`

