.. _nuzfbrequest:

nuzfbrequest
===========================================

.. class:: nuzfbrequest.NUZFBRequest(bambou.nurest_object.NUMetaRESTObject,):

Pending requests reflect Network Services Gateways that have initiated request for bootstrapping. Requests can be assigned or matched to continue the bootstrapping process


Attributes
----------


- ``mac_address``: MAC Address fo the NSG Port1 interface

- ``zfb_approval_status``: the status of the request

- ``zfb_bootstrap_enabled``: whether the NSG should bootstrap, or just simulate bootstrap. Set from System Config

- ``zfb_info``: The Base64 encoded JSON string of ZFB Attributes

- ``zfb_request_retry_timer``: ZFB Request retry timer on the gateway. Set on VSD's System Config panel.

- ``sku``: The part number of the gateway being bootstrapped through ZFB.

- ``ip_address``: IP Address of the gateway being bootstrapped using ZFB.

- ``cpu_type``: Processor Type

- ``nsg_version``: The Nuage NSG Version

- ``uuid``: Redhat UUID

- ``family``: Gateway Type

- ``last_connected_time``: The time in which the last GET was made from the gateway.

- ``last_updated_by``: ID of the user who last updated the object.

- ``registration_url``: Registration URL to be used for a gateway to be bootstrapped using ZFB.

- ``serial_number``: The gateway's Serial Number.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``hostname``: Hostname of the gateway bootstrapped using ZFB.

- ``associated_enterprise_id``: the ID of the associated enteprise

- ``associated_enterprise_name``: Name of the associated enterprise

- ``associated_entity_type``: Associated Entity Type: NSGATEWAY or GATEWAY

- ``associated_gateway_id``: ID of the assigned Gateway

- ``associated_gateway_name``: Name of the associated Gateway

- ``associated_ns_gateway_id``: ID of the assigned NSG

- ``associated_ns_gateway_name``: Name of the associated NSG

- ``status_string``: Extra status info

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

