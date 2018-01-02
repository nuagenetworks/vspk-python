.. _nunsgroutingpolicybinding:

nunsgroutingpolicybinding
===========================================

.. class:: nunsgroutingpolicybinding.NUNSGRoutingPolicyBinding(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``name`` (**Mandatory**): Name of the RoutingPolicyBinding is unique within the Domain

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description for this Routing Policy Binding Object.

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

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

