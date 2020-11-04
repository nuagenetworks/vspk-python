.. _nudomainkindsummary:

nudomainkindsummary
===========================================

.. class:: nudomainkindsummary.NUDomainKindSummary(bambou.nurest_object.NUMetaRESTObject,):

Represents a readonly domain summary object - various attributes of this object are gathered from Domain, Zones, SubNetwork, NSGInfo objects


Attributes
----------


- ``major_alarms_count``: Total count of alarms at MAJOR severity

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``gateway_count``: Total count of gateways in this domain

- ``mesh_group_count``: Total count of mesh groups in this domain

- ``minor_alarms_count``: Total count of alarms with MINOR severity

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``info_alarms_count``: Total count of alarms with INFO severity

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_kind_description``: A description string of the domain that is provided by the user

- ``domain_kind_name``: The name of the domain. Valid characters are  alphabets, numbers, space and hyphen( - ).

- ``zone_count``: Total count of zones in this domain

- ``traffic_volume``: Traffic volume within the domain in GB indicating whether the network is running ZERO, light, medium or heavy traffic based on last 24 hours traffic stats

- ``creation_date``: Time stamp when this object was created.

- ``critical_alarms_count``: Total count of alarms with CRITICAL severity

- ``nsg_count``: Total count of nsg in this domain

- ``sub_network_count``: Total count of sub networks in this domain

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


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

