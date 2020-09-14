.. _nutrunk:

nutrunk
===========================================

.. class:: nutrunk.NUTrunk(bambou.nurest_object.NUMetaRESTObject,):

A trunk is used to attach multiple vPorts to a single NIC on a VM. These sub-vPorts are separated by a segmentation identifier (currently the VLAN ID) so the attached VM can distinguish between traffic on the sub-vPorts.


Attributes
----------


- ``name`` (**Mandatory**): The name of the trunk

- ``last_updated_by``: ID of the user who last updated the object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_vport_id`` (**Mandatory**): the uuid of the parent vport (the trunkRole of the parent vport must be PARENT_PORT)

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

