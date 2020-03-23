.. _nuptranslationmap:

nuptranslationmap
===========================================

.. class:: nuptranslationmap.NUPTranslationMap(bambou.nurest_object.NUMetaRESTObject,):

1:1 mappings of private IPs in provider domain to the provider  alias (public) IPs in customer domain and N:1 mappings of a collection of provider private IPs to a provider alias IP into the customer domain.


Attributes
----------


- ``spat_source_list``: The list of provider source IPs to be SPAT'd.

- ``mapping_type``: 1:1 NATmapping, or *:1 PAT mappings

- ``last_updated_by``: ID of the user who last updated the object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``provider_alias_ip`` (**Mandatory**): Provider public IP in Customer Domain

- ``provider_ip`` (**Mandatory**): Provider private IP in Provider Domain.

- ``associated_domain_id``: associated domain for this

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


- :ref:`nupsnatpool.NUPSNATPool<nupsnatpool>`

