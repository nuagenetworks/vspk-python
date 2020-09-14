.. _nuospfarea:

nuospfarea
===========================================

.. class:: nuospfarea.NUOSPFArea(bambou.nurest_object.NUMetaRESTObject,):

OSPF relies on the concept of logical areas. The use of areas enables the hiding of topology information between areas whilst still providing reachability. Each router in the area shares the same routing tables, which simplifies the network topology and helps to optimize the route calculation algorithm. 


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``redistribute_external_enabled``: This flag will determine whether external routes will be redistributed into the area or not. This is enabled only for NSSA areas.

- ``default_metric``: Explicit route cost metric for the default route generated. For STUB areas, it defaults to 1. It is null for the other types of areas.

- ``default_originate_option``: Specifies whether an NSSA area generates a default route, and if it does, whether it is advertised as type 3 LSA or type 7 LSA. If the attribute is set to 'NONE', no default is generated.

- ``description``: Description of OSPFArea

- ``aggregate_area_range``: Routes (type 3 LSAs) that belong to networks listed here will be aggregated.

- ``aggregate_area_range_nssa``: Routes (type 7 LSAs) that belong to networks listed here will be aggregated.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``area_id`` (**Mandatory**): OSPF Area ID

- ``area_type``: Set the OSPF area type. The default value is 'NORMAL', which represents either a backbone area or a standard area. If the areaID is 0, this attribute must be set to 'NORMAL'.

- ``summaries_enabled``: This flag determines whether Summaries (Type 3 LSAs) will be redistributed into the area or not. Applicable only to NSSA and Stub area types. Disabling this will make the area a Totally Stub or Totally NSSA area.

- ``suppress_area_range``: Routes (type 3 LSAs) that belong to networks listed here will be suppressed.

- ``suppress_area_range_nssa``: Routes (type 7 LSAs) that belong to networks listed here will be suppressed.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuospfinterface.NUOSPFInterface<nuospfinterface>`                                                                                                          ``ospf_interfaces`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuospfinstance.NUOSPFInstance<nuospfinstance>`

