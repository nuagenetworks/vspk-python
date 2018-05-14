.. _nuzfbrequest:

nuzfbrequest
===========================================

.. class:: nuzfbrequest.NUZFBRequest(bambou.nurest_object.NUMetaRESTObject,):

A ZFB Request from an NSG


Attributes
----------


- ``mac_address``: MAC Address fo the NSG Port1 interface

- ``zfb_approval_status``: the status of the request

- ``zfb_bootstrap_enabled``: whether the NSG should bootstrap, or just simulate bootstrap. Set from System Config

- ``zfb_info``: The Base64 encoded JSON string of ZFB Attributes

- ``zfb_request_retry_timer``: ZFB Request retry timer on NSG. Set from System Config

- ``sku``: The part number of the NSG

- ``ip_address``: IP Address of the NSG

- ``cpu_type``: Processor Type

- ``nsg_version``: The Nuage NSG Version

- ``uuid``: Redhat UUID

- ``family``: NSG Type

- ``last_connected_time``: the time in which the last GET was made from the NSG

- ``last_updated_by``: ID of the user who last updated the object.

- ``serial_number``: The NSG's Serial Number

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``hostname``: hostname of the NSG

- ``associated_enterprise_id``: the ID of the associated enteprise

- ``associated_enterprise_name``: Name of the associated enterprise

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

