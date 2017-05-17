.. _numultinicvport:

numultinicvport
===========================================

.. class:: numultinicvport.NUMultiNICVPort(bambou.nurest_object.NUMetaRESTObject,):

Encapsulates the Multi NIC VPort information for system monitoring entity.


Attributes
----------


- ``name``: Name for the Multi NIC VPort.

- ``last_updated_by``: ID of the user who last updated the object.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvrs.NUVRS<nuvrs>`

