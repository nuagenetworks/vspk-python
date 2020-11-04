.. _nuroutingpolicy:

nuroutingpolicy
===========================================

.. class:: nuroutingpolicy.NURoutingPolicy(bambou.nurest_object.NUMetaRESTObject,):

Pre-defined sets of attributes used in policy match conditions: prefix lists, entries, damping profiles, etc.


Attributes
----------


- ``name`` (**Mandatory**): policy name, unique within an enterprise

- ``default_action`` (**Mandatory**): accept/reject

- ``description``: None

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_definition``: String blob

- ``content_type``: Content type for routing policy provisioning for different mediation devices

- ``routing_protocol``: Routing protocol this policy definition is used for

- ``customer_id``: The customer ID given to parent enterprise. This is used by Netconf/Config manager.

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

- :ref:`nume.NUMe<nume>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

