.. _nuflowforwardingpolicy:

nuflowforwardingpolicy
===========================================

.. class:: nuflowforwardingpolicy.NUFlowForwardingPolicy(bambou.nurest_object.NUMetaRESTObject,):

The redirect policy on the flow.


Attributes
----------


- ``redirect_target_id``: The associated service id.

- ``destination_address_overwrite``: The destination address overwrite. Needs to be in CIDR format x.x.x.x/n

- ``flow_id``: The associated service id.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``source_address_overwrite``: The source address overwrite. Needs to be in CIDR format x.x.x.x/n

- ``associated_application_service_id``: The associated service id.

- ``associated_network_object_id``: The associated network object id.

- ``associated_network_object_type``: The associated network object type. Refer to API section for supported types.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: The redirect type.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuflow.NUFlow<nuflow>`

