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

- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

