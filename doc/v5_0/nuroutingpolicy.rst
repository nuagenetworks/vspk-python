.. _nuroutingpolicy:

nuroutingpolicy
===========================================

.. class:: nuroutingpolicy.NURoutingPolicy(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``name`` (**Mandatory**): policy name, unique within an enterprise

- ``default_action`` (**Mandatory**): accept/reject

- ``description``: None

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_definition``: String blob

- ``routing_protocol``: Routing protocol this policy definition is used for

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


- :ref:`nume.NUMe<nume>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

