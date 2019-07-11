.. _nulteinformation:

nulteinformation
===========================================

.. class:: nulteinformation.NULTEInformation(bambou.nurest_object.NUMetaRESTObject,):

Contains information about the LTE dongle plugged in USB port on NSG. This would have information like - Modem Manufacturer, Model Number, Subscriber Number, Operator etc. This information could vary from vendor to vendor.


Attributes
----------


- ``lte_connection_info``: This attribute holds all the information about the LTE dongle plugged in to NSG. This is in JSON format and has information like - Modem Manufacturer, Model Number, Subscriber Number,  Operator etc.

- ``last_updated_by``: ID of the user who last updated the object.

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


- :ref:`nunsport.NUNSPort<nunsport>`

