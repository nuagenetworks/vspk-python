.. _nuikesubnet:

nuikesubnet
===========================================

.. class:: nuikesubnet.NUIKESubnet(bambou.nurest_object.NUMetaRESTObject,):

Represents an IKE Subnet (remote side)


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``prefix``: The subnet prefix (eg: 10.0.0.0/24)

- ``associated_ike_gateway_id``: The ID of the associated IKEGateway

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


- :ref:`nuikegateway.NUIKEGateway<nuikegateway>`

