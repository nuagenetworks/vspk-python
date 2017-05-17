.. _nupatnatpool:

nupatnatpool
===========================================

.. class:: nupatnatpool.NUPATNATPool(bambou.nurest_object.NUMetaRESTObject,):

Represents a PAT NAT Pool object.


Attributes
----------


- ``name`` (**Mandatory**): Name of the PATNATPool

- ``last_updated_by``: ID of the user who last updated the object.

- ``address_range`` (**Mandatory**): Pool of IP Address that is available for use ex : 130.12.0.0/16

- ``default_patip``: Default PAT IP Address, must belong to the pool above

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``description``: A description of the PATNATPool

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_gateway_id``: Default PAT IP Address, must belong to the pool above

- ``associated_gateway_type``: 

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nunatmapentry.NUNATMapEntry<nunatmapentry>`                                                                                                                ``nat_map_entries`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nume.NUMe<nume>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

