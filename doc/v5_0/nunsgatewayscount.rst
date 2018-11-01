.. _nunsgatewayscount:

nunsgatewayscount
===========================================

.. class:: nunsgatewayscount.NUNSGatewaysCount(bambou.nurest_object.NUMetaRESTObject,):

NSGateway count is a summary object per enterprise which contains the counts of inactive and NSGs by alarm severity. This object is used in Application Aware Routing (AAR) visualization


Attributes
----------


- ``active_nsg_count``: Number of Network Service Gateways in an enterprise whose bootstrap status is ACTIVE

- ``alarmed_nsg_count``: An embedded object containing three attributes: critical, major, healthy - number of NSGs with CRITICAL alarm severity, manumber of NSGs with MAJOR alarm severity, number of NSGs that have no CRITICAL or MAJOR alarms

- ``inactive_nsg_count``: Number of Network Service Gateways in an enterprise whose bootstrap status is not ACTIVE

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


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

