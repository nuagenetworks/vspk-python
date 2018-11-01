.. _nudefaultgateway:

nudefaultgateway
===========================================

.. class:: nudefaultgateway.NUDefaultGateway(bambou.nurest_object.NUMetaRESTObject,):

This object represent default Gateway associated with Subnet


Attributes
----------


- ``name``: Name of the subnet gateway

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway_ip_address``: The IP address of this default gateway for parent subnet

- ``gateway_mac_address``: The MAC address of this default gateway for parent subnet

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

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


- :ref:`nusubnet.NUSubnet<nusubnet>`

