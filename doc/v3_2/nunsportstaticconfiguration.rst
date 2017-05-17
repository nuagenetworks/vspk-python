.. _nunsportstaticconfiguration:

nunsportstaticconfiguration
===========================================

.. class:: nunsportstaticconfiguration.NUNSPortStaticConfiguration(bambou.nurest_object.NUMetaRESTObject,):

Represents a network port static configuration in the context of an Network Services Gateway.


Attributes
----------


- ``dns_address``: DNS Address for Network NSPort.

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway``: IP address of the gateway bound to the Network NSPort.

- ``address``: IP address of the Network NSPort.

- ``netmask``: IP address netmask of the Network NSPort.

- ``enabled``: Boolean value that states if the NSG Port static configuration needs to be applied.

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


- :ref:`nume.NUMe<nume>`

- :ref:`nunsport.NUNSPort<nunsport>`

