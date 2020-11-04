.. _nuegressqospolicy:

nuegressqospolicy
===========================================

.. class:: nuegressqospolicy.NUEgressQOSPolicy(bambou.nurest_object.NUMetaRESTObject,):

An Egress QoS Policy is a policy that groups rate-limiting profiles, traffic directionality and classifiers to govern the rate of traffic being sent or received by an end-host or application.


Attributes
----------


- ``name`` (**Mandatory**): A unique name of the QoS object

- ``parent_queue_associated_rate_limiter_id`` (**Mandatory**): ID of the parent rate limiter associated with this Egress QoS policy.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``default_service_class``: The Default Service Class for this Egress QoS Policy. The queue that contains the default service class will be treated as the default queue.

- ``description``: A description of the QoS object

- ``network_ctrl_queue_associated_rate_limiter_id``: Rate limiter ID associated to the Network Control Queue for this Egress QoS Policy. 

- ``mgmt_queue_associated_rate_limiter_id``: Rate Limiter ID associated to the Management Queue for this Egress QoS Policy. 

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``assoc_egress_qos_id``: ID of object associated with this QoS object

- ``associated_cos_remarking_policy_table_id``: ID of the associated CoS Remarking Policy table. 

- ``associated_dscp_remarking_policy_table_id``: ID of the DSCP Remarking Policy Table associated with this Egress QoS policy.

- ``queue1_associated_rate_limiter_id``: ID of the queue1 rate limiter associated with this Egress QoS policy.

- ``queue1_forwarding_classes``: Queue1 Forwarding Classes for this Egress QoS Policy Possible values are NONE, A, B, C, D, E, F, G, H.

- ``queue2_associated_rate_limiter_id``: ID of the queue2 rate limiter associated with this Egress QoS policy.

- ``queue2_forwarding_classes``: Queue2 Forwarding Classes for this Egress QoS Policy Possible values are NONE, A, B, C, D, E, F, G, H.

- ``queue3_associated_rate_limiter_id``: ID of the queue3 rate limiter associated with this Egress QoS policy.

- ``queue3_forwarding_classes`` (**Mandatory**): Queue3 Forwarding Classes for this Egress QoS Policy Possible values are NONE, A, B, C, D, E, F, G, H.

- ``queue4_associated_rate_limiter_id``: ID of the queue4 rate limiter associated with this Egress QoS policy.

- ``queue4_forwarding_classes``: Queue4 Forwarding Classes for this Egress QoS Policy Possible values are NONE, A, B, C, D, E, F, G, H.

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


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

