.. _nuwebcategory:

nuwebcategory
===========================================

.. class:: nuwebcategory.NUWebCategory(bambou.nurest_object.NUMetaRESTObject,):

This entity provides the definition of Web Category. It will be used in ACL definition to filter web traffic.


Attributes
----------


- ``name`` (**Mandatory**): A customer friendly name for this web category

- ``last_updated_by``: ID of the user who last updated the object.

- ``default_category``: Indicates if this is a system-defined web category

- ``description``: A customer friendly description for this web category

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): Type of the Web Category




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuwebdomainname.NUWebDomainName<nuwebdomainname>`                                                                                                          ``web_domain_names`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuwebdomainname.NUWebDomainName<nuwebdomainname>`

