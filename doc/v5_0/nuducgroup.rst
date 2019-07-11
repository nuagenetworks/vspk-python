.. _nuducgroup:

nuducgroup
===========================================

.. class:: nuducgroup.NUDUCGroup(bambou.nurest_object.NUMetaRESTObject,):

A logical group of 1 or more NSGs of personality NSG-UBR, that are used to provide connectivity between NSGs in disjoint underlays.


Attributes
----------


- ``name``: Name given to the UBR Group.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the UBR Group.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_performance_monitor_id``: Identification of the Performance Monitoring Probe that is associated with this instance of a UBR Group.

- ``function``: The function of the group

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nunsgateway.NUNSGateway<nunsgateway>`                                                                                                                      ``ns_gateways`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

