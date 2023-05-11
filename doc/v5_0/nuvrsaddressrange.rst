.. _nuvrsaddressrange:

nuvrsaddressrange
===========================================

.. class:: nuvrsaddressrange.NUVRSAddressRange(bambou.nurest_object.NUMetaRESTObject,):

This is the definition of a Address Range associated with a VRS.


Attributes
----------


- ``ip_type``: The ip type of the address range, possible values are IPV4, IPV6 and DUALSTACK.

- ``last_updated_by``: ID of the user who last updated the object.

- ``max_address`` (**Mandatory**): Higest address in the address range

- ``min_address`` (**Mandatory**): Lowest address in the address range

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

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


- :ref:`nuvcentervrsconfig.NUVCenterVRSConfig<nuvcentervrsconfig>`

- :ref:`nuvcentercluster.NUVCenterCluster<nuvcentercluster>`

- :ref:`nuvcenterdatacenter.NUVCenterDataCenter<nuvcenterdatacenter>`

- :ref:`nuvcenter.NUVCenter<nuvcenter>`

- :ref:`nuvcenterhypervisor.NUVCenterHypervisor<nuvcenterhypervisor>`

