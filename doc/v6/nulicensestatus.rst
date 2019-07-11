.. _nulicensestatus:

nulicensestatus
===========================================

.. class:: nulicensestatus.NULicenseStatus(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``accumulate_licenses_enabled``: Whether the various VRS license flavours be merged in one pool

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``total_licensed_avrsgs_count``: Indicates total AVRSG count for all the licenses in the system

- ``total_licensed_avrss_count``: Indicates total AVRS count for all the licenses in the system

- ``total_licensed_gateways_count``:  Indicates total VRS+VRSG+VRSB licenses licensed in the system

- ``total_licensed_nics_count``: Indicates total NIC count for all the licenses in the system

- ``total_licensed_nsgs_count``: Indicates total NSG count for all the licenses in the system

- ``total_licensed_used_avrsgs_count``: Indicates total used AVRSG count for all the licenses in the system

- ``total_licensed_used_avrss_count``: Indicates total used AVRS count for all the licenses in the system

- ``total_licensed_used_nics_count``: Indicates total used NIC count for all the licenses in the system

- ``total_licensed_used_nsgs_count``: Indicates total used NSG count for all the licenses in the system

- ``total_licensed_used_vdfgs_count``: Indicates total used VDFG count for all the licenses in the system.

- ``total_licensed_used_vdfs_count``: Indicates total used VDF count for all the licenses in the system.

- ``total_licensed_used_vms_count``: Indicates total used VM count for all the licenses in the system

- ``total_licensed_used_vrsgs_count``: Indicates total used VRSG count for all the licenses in the system

- ``total_licensed_used_vrss_count``: Indicates total used VRS count for all the licenses in the system

- ``total_licensed_vdfgs_count``: Indicates total VDFG count for all the licenses in the system

- ``total_licensed_vdfs_count``: Indicates total VDF count for all the licenses in the system

- ``total_licensed_vms_count``: Indicates total VM count for all the licenses in the system

- ``total_licensed_vrsgs_count``: Indicates total VRSG count for all the licenses in the system

- ``total_licensed_vrss_count``: Indicates total VRS count for all the licenses in the system

- ``total_used_gateways_count``: Indicates total VRS+VRSG+VRSB+VDF+VDFG licenses used in the system

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

