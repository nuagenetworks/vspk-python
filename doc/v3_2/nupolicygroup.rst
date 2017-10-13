.. _nupolicygroup:

nupolicygroup
===========================================

.. class:: nupolicygroup.NUPolicyGroup(bambou.nurest_object.NUMetaRESTObject,):

PolicyGroup is group of policys on which a user can policies like ACL, QoS, etc.


Attributes
----------


- ``evpn_community_tag``: Assigned by VSD. An extended community or other similar BGP attribute to the specific EVPN / IP-VPN NLRI where the VM or network macro is being advertised.

- ``name`` (**Mandatory**): Name of the policy group

- ``last_updated_by``: ID of the user who last updated the object.

- ``template_id``: Determines which template ID this policy group belongs to.

- ``description``: Describes this policy group

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_group_id``: PG ID for the subnet. This is unique per domain and will be in the range 1-4095

- ``external``: Indicates whether this PG is internal to VSP or not.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): Type of policy group.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nume.NUMe<nume>`

