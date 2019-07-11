.. _nupolicygroupcategory:

nupolicygroupcategory
===========================================

.. class:: nupolicygroupcategory.NUPolicyGroupCategory(bambou.nurest_object.NUMetaRESTObject,):

Policy Group Categories are used to group Policy Group tags of similar type (e.g., Application, App-Tier, Location etc.) to provide additional context for flow visualization and analytics


Attributes
----------


- ``name`` (**Mandatory**): Name of the Policy Group Cateogry

- ``last_updated_by``: ID of the user who last updated the object.

- ``default_category``: Boolean which identifies if this is a default policy group category.

- ``description``: Describes the Policy Group Category.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`                                                                                                                ``policy_groups`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

