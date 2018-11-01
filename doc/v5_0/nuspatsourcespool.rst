.. _nuspatsourcespool:

nuspatsourcespool
===========================================

.. class:: nuspatsourcespool.NUSPATSourcesPool(bambou.nurest_object.NUMetaRESTObject,):

The list of source IPs from the provider domain to be SPATed.


Attributes
----------


- ``name``: The name for this address pool

- ``family``: The IP address family. Supported IPV4 for the time being.

- ``last_updated_by``: ID of the user who last updated the object.

- ``address_list``: The collection of IP addresses that will SPATed in the customer domain.

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


- :ref:`nudomain.NUDomain<nudomain>`

