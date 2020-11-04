.. _nupsnatpool:

nupsnatpool
===========================================

.. class:: nupsnatpool.NUPSNATPool(bambou.nurest_object.NUMetaRESTObject,):

Provider alias IP range to map provider private IPs from provider domain to provider public IPs in the customer domain.


Attributes
----------


- ``ip_type``: The IP Type of this provider alias IP, possible values are IPV4, IPV6 or DUALSTACK.

- ``name`` (**Mandatory**): The Provider to Customer NAT Pool

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A description of the PATNATPool instance

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``end_address`` (**Mandatory**): The last IP address in the range.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``start_address`` (**Mandatory**): The first IP address in the range.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nupspatmap.NUPSPATMap<nupspatmap>`                                                                                                                         ``pspat_maps`` 
:ref:`nuptranslationmap.NUPTranslationMap<nuptranslationmap>`                                                                                                    ``p_translation_maps`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nulink.NULink<nulink>`

