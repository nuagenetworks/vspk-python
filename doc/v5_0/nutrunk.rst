.. _nutrunk:

nutrunk
===========================================

.. class:: nutrunk.NUTrunk(bambou.nurest_object.NUMetaRESTObject,):

Trunk is an object that is an aggregator of sub-vports corresponding to segmentation-ids (vlans) in a trunk


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

