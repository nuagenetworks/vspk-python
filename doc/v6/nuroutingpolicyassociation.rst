.. _nuroutingpolicyassociation:

nuroutingpolicyassociation
===========================================

.. class:: nuroutingpolicyassociation.NURoutingPolicyAssociation(bambou.nurest_object.NUMetaRESTObject,):

Routing Policy Associattion object which will be associated with the Subent or Domain


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``netconf_gateway_ids`` (**Mandatory**): List of third-party Netconf Gateways on which Global Configuration will be deployed.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``ip_type`` (**Mandatory**): IP Type of the Routing Policy. Possible values are IPV4 or IPV6

- ``creation_date``: Time stamp when this object was created.

- ``associated_routing_policy_id`` (**Mandatory**): ID of the Associated Routing Policy.

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


- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nudomain.NUDomain<nudomain>`

