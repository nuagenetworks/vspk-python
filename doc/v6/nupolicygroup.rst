.. _nupolicygroup:

nupolicygroup
===========================================

.. class:: nupolicygroup.NUPolicyGroup(bambou.nurest_object.NUMetaRESTObject,):

Policy groups are collections of VPorts that are used as building blocks for security policies encompassing multiple end-points. One or more vports can be added to a policy group using this interface.


Attributes
----------


- ``evpn_community_tag``: Assigned by VSD. An extended community or other similar BGP attribute to the specific EVPN / IP-VPN NLRI where the VM or network macro is being advertised.

- ``name`` (**Mandatory**): Name of the policy group

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``template_id``: Determines which template ID this policy group belongs to.

- ``description``: Describes this policy group

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``entity_state``: Intermediate State of L2 Domain.

- ``policy_group_id``: PG ID for the subnet. This is unique per domain and will be in the range 1-4095

- ``creation_date``: Time stamp when this object was created.

- ``assoc_policy_group_category_id``: UUID of the associated Policy Group Category for contextual filtering of policy groups.

- ``assoc_policy_group_category_name``: Name of the Policy Group Category used for contextual filtering of policy groups.

- ``owner``: Identifies the user that has created this object.

- ``external``: Indicates whether this PG is internal to VSP or not.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): Type of policy group.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nupolicygroupcategory.NUPolicyGroupCategory<nupolicygroupcategory>`                                                                                        ``policy_group_categories`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nume.NUMe<nume>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nupolicygroupcategory.NUPolicyGroupCategory<nupolicygroupcategory>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

