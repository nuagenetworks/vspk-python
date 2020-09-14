.. _nuctranslationmap:

nuctranslationmap
===========================================

.. class:: nuctranslationmap.NUCTranslationMap(bambou.nurest_object.NUMetaRESTObject,):

1:1 mapping of customer private IPs in customer domain to customer alias (public) IPs in provider domain and N:1 mapping to customer alias SPAT IP in the provider domain.


Attributes
----------


- ``mapping_type``: NAT for 1:1 mapping or PAT for *:1 mappings.

- ``last_updated_by``: ID of the user who last updated the object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_domain_id``: Domain associated to this address mapping.

- ``customer_alias_ip`` (**Mandatory**): Customer public IP in the provider domain.

- ``customer_ip`` (**Mandatory**): Customer private IP in the customer domain.

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


- :ref:`nucsnatpool.NUCSNATPool<nucsnatpool>`

