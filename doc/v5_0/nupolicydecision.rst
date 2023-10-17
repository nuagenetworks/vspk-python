.. _nupolicydecision:

nupolicydecision
===========================================

.. class:: nupolicydecision.NUPolicyDecision(bambou.nurest_object.NUMetaRESTObject,):

This object is a read only object that provides the policy decisions for a particular VM interface.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``egress_acls``: List of actual Egress ACLs that will be applied on the interface of this VM

- ``egress_qos``: Egress QoS primitive that was selected

- ``fip_acls``: List of actual Egress ACLs that will be applied on the interface of this VM

- ``ingress_acls``: List of actual Ingress ACLs that will be applied on the interface of this VM

- ``ingress_adv_fwd``: List of actual Ingress Redirect ACLs that will be applied on the interface of this VM

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``qos``: QoS primitive that was selected based on inheritance policies

- ``stats``: Stats primitive that was selected based on inheritance policies

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

