.. _nuwebcategory:

nuwebcategory
===========================================

.. class:: nuwebcategory.NUWebCategory(bambou.nurest_object.NUMetaRESTObject,):

This entity provides the definition of Web Category. It will be used in ACL definition to filter web traffic.


Attributes
----------


- ``name`` (**Mandatory**): A customer friendly name for this web category

- ``last_updated_by``: ID of the user who last updated the object.

- ``web_category_identifier``: The unique identifier of a web category to be used by NSG

- ``default_category``: Indicates if this is a system-defined web category

- ``description``: A customer friendly description for this web category

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): Type of the Web Category




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuwebdomainname.NUWebDomainName<nuwebdomainname>`                                                                                                          ``web_domain_names`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuwebdomainname.NUWebDomainName<nuwebdomainname>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

