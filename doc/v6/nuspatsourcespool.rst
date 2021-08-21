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

- ``last_updated_date``: Time stamp when this object was last updated.

- ``address_list`` (**Mandatory**): The collection of IP addresses that will SPATed in the customer domain.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

