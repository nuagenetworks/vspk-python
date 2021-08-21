.. _nuingressqospolicy:

nuingressqospolicy
===========================================

.. class:: nuingressqospolicy.NUIngressQOSPolicy(bambou.nurest_object.NUMetaRESTObject,):

A Tunnel Shaper QoS Policy is a policy that groups rate-limiting profiles, traffic directionality and classifiers to govern the rate of traffic being sent or received by an end-host or application.


Attributes
----------


- ``name`` (**Mandatory**): A unique name of the QoS object

- ``parent_queue_associated_rate_limiter_id``: ID of the parent rate limiter associated with this Ingress QOS policy.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A description of the QoS object

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``assoc_egress_qos_id``: ID of object associated with this QoS object

- ``queue1_associated_rate_limiter_id``: ID of the queue1 rate limiter associated with this Ingress QOS policy.

- ``queue1_forwarding_classes``: Queue1 Forwarding Classes for this Ingress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

- ``queue2_associated_rate_limiter_id``: ID of the queue2 rate limiter associated with this Ingress QOS policy.

- ``queue2_forwarding_classes``: Queue2 Forwarding Classes for this Ingress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

- ``queue3_associated_rate_limiter_id``: ID of the queue3 rate limiter associated with this Ingress QOS policy.

- ``queue3_forwarding_classes``: Queue3 Forwarding Classes for this Ingress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

- ``queue4_associated_rate_limiter_id``: ID of the queue4 rate limiter associated with this Ingress QOS policy.

- ``queue4_forwarding_classes``: Queue4 Forwarding Classes for this Ingress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

- ``custom_spq_depth``: Custom Depth of the Strict Priority Queue (Queue1). Measured as 'Number of Packets'. A value of zero indicates it is 'not set'. Valid values are in range 32 to 512.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

