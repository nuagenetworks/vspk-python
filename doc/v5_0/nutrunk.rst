.. _nutrunk:

nutrunk
===========================================

.. class:: nutrunk.NUTrunk(bambou.nurest_object.NUMetaRESTObject,):

A trunk is used to attach multiple vPorts to a single NIC on a VM. These sub-vPorts are separated by a segmentation identifier (currently the VLAN ID) so the attached VM can distinguish between traffic on the sub-vPorts.


Attributes
----------


- ``name`` (**Mandatory**): The name of the trunk

- ``associated_vport_id`` (**Mandatory**): the uuid of the parent vport (the trunkRole of the parent vport must be PARENT_PORT)




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

