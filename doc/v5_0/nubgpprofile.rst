.. _nubgpprofile:

nubgpprofile
===========================================

.. class:: nubgpprofile.NUBGPProfile(bambou.nurest_object.NUMetaRESTObject,):

Definitions for default import/export routing policies and dampening profiles


Attributes
----------


- ``name`` (**Mandatory**): Per enterprise unique name

- ``dampening_half_life``: The time in minutes to wait before decrementing dampening penalty.

- ``dampening_max_suppress``: The maximum duration in minutes that a route will be suppressed.

- ``dampening_name``: Name for the dampening profile. Unique per enterprise

- ``dampening_reuse``: This value is compared with penalty to determine route reusability, If the penalty is greater than the suppress limit, the route will be suppressed; if not, it will be reused.

- ``dampening_suppress``: Specifies the penalty that will be used if a route is suppressed.

- ``description``: The description of the BGP Profile

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_export_routing_policy_id``: export BGP policy ID

- ``associated_import_routing_policy_id``: import BGP policy ID

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


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

