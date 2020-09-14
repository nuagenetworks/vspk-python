.. _nunsgroutingpolicybinding:

nunsgroutingpolicybinding
===========================================

.. class:: nunsgroutingpolicybinding.NUNSGRoutingPolicyBinding(bambou.nurest_object.NUMetaRESTObject,):

The NSG routing policy binding is used to assign routing policies to an NSG or group of NSGs as defined by the routing policy group. The local routing policies assigned to an NSG in a policy binding are preferred over global routing policies defined at the OSPF instance level.


Attributes
----------


- ``name`` (**Mandatory**): Name of the RoutingPolicyBinding is unique within the Domain

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description for this Routing Policy Binding Object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_export_routing_policy_id``: ID of the Export Routing Policy which is associated to the current NSGRoutingPolicyBinding object.

- ``associated_import_routing_policy_id``: ID of the Import Routing Policy which is associated to the current NSGRoutingPolicyBinding object.

- ``associated_policy_object_group_id`` (**Mandatory**): ID of the Policy Object Group which is associated to the current NSGRoutingPolicyBinding object.

- ``export_to_overlay``: Flag to determine whether the BGP and OSPF learnt routes will be exported to VSC or not. This flags also exists at the domain level. If this attribute is set to 'INHERITED' (the default), the behavior is whatever is set at the domain level. Otherwise, this attribute takes precedence over the domain level one.

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


- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nudomain.NUDomain<nudomain>`

