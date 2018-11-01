.. _nucsnatpool:

nucsnatpool
===========================================

.. class:: nucsnatpool.NUCSNATPool(bambou.nurest_object.NUMetaRESTObject,):

Customer Alias IP range to be used in provider domain. This pool is used to map customer private IPs from customer domain to customer public IPs in provider domain.


Attributes
----------


- ``ip_type``: The IP type of this CSNAT Pool, possible values are IPV4, IPV6 or DUALSTACK.

- ``name`` (**Mandatory**): The Customer to Provider NAT Pool

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description of the PATNATPool instance

- ``end_address`` (**Mandatory**): The last IP address in the range.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``start_address`` (**Mandatory**): The first IP in the range.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuctranslationmap.NUCTranslationMap<nuctranslationmap>`                                                                                                    ``c_translation_maps`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nulink.NULink<nulink>`

