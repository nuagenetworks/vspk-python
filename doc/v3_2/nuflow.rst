.. _nuflow:

nuflow
===========================================

.. class:: nuflow.NUFlow(bambou.nurest_object.NUMetaRESTObject,):

Flow represents the traffic between two different application tiers.


Attributes
----------


- ``name`` (**Mandatory**): Name of the flow.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the flow.

- ``destination_tier_id``: Flow destination tier id.

- ``metadata``: Metadata field to store flow related data.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``origin_tier_id``: Flow origin tier id.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuflowforwardingpolicy.NUFlowForwardingPolicy<nuflowforwardingpolicy>`                                                                                     ``flow_forwarding_policies`` 
:ref:`nuflowsecuritypolicy.NUFlowSecurityPolicy<nuflowsecuritypolicy>`                                                                                           ``flow_security_policies`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuapp.NUApp<nuapp>`

